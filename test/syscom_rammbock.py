import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'rammbock', 'src'))
from Rammbock.rammbock import Rammbock
from Rammbock.templates.containers import MessageTemplate
from Rammbock.binary_tools import to_bin
from robot.libraries.BuiltIn import BuiltIn
from contextlib import contextmanager
from robot.api import logger
import pickle
import os.path
from Rammbock.networking import _NetworkNode


def gorilla_patch_decode(original_function):
    def decode(self, data, parent=None, name=None, little_endian=False):
        little_endian = parent.flags.int & 0x04
        return original_function(self, data, parent=parent,
                                 name=name, little_endian=little_endian)
    return decode


def gorilla_patch_encode(original_function):
    def encode(self, message_params, header_params, little_endian=False):
        little_endian = is_little_endian(self, header_params)
        return original_function(self, message_params, header_params, little_endian=little_endian)

    def is_little_endian(self, header_params):
        return ord(to_bin(get_flags(header_params, self.header_parameters))[-1]) & 0x04
    return encode


def get_flags(encoding, header):
    return encoding.get('flags', header.get('flags', None)) or '0x00'


def gorilla_patch_check_message_lengths():
    def check_message_lengths(self, msg, data):
        if ((len(msg) + 3) & 0xFFFC) < len(data):
            logger.warn('Receiving %s. Message too long. Expected %s but got %s.' % (self.name, len(msg), len(data)))
    return check_message_lengths


def gorilla_patch_get_message():
    def get_message(self, message_template, timeout=None, header_filter=None, latest=None):
        if not self._protocol:
            raise AssertionError('Can not receive messages without protocol. Initialize network node with "protocol=<protocl name>"')
        if self.protocol_name != message_template._protocol.name:
            raise AssertionError('Template protocol does not match network node protocol %s!=%s' % (self.protocol_name, message_template._protocol.name))
        return self._get_from_stream(message_template, self._message_stream, timeout=timeout, header_filter=header_filter, latest=latest)
    return get_message


class syscom_rammbock(Rammbock):

    BIG_ENDIAN = 0
    LITTLE_ENDIAN = 4

    MessageTemplate.decode = gorilla_patch_decode(MessageTemplate.decode)
    MessageTemplate.encode = gorilla_patch_encode(MessageTemplate.encode)
    MessageTemplate.check_message_lengths = gorilla_patch_check_message_lengths()
    _NetworkNode.get_message = gorilla_patch_get_message()

    def new_msg(self, name='', msgId='', sic='', flags='0x0000'):
        test_tool_sic = BuiltIn().replace_variables('${TEST TOOL SIC}')
        self.new_message(name, 'Syscom', 'header:msgId:%s' % msgId, 'header:ownSic:%s' % test_tool_sic, 'header:sic:%s' % sic, 'header:flags:%s' % flags)

    @contextmanager
    def _debuglevel(self):
        orig_level = BuiltIn().set_log_level('DEBUG')
        try:
            yield
        finally:
            BuiltIn().set_log_level(orig_level)

    def send_udp(self, *params):
        self.client_sends_message('name=SyscomUdpClient', *params)

    def receive_udp(self, *params):
        return self.client_receives_message('name=SyscomUdpClient', 'header_filter=msgId', 'header:ownSic:', 'header:sic:', 'header:flags:', *params)

    def send_tcp(self, *params):
        self.client_sends_message('name=SyscomTcpClient', *params)

    def receive_tcp(self, *params):
        return self.client_receives_message('name=SyscomTcpClient', 'header_filter=msgId', 'header:ownSic:', 'header:sic:', 'header:flags:', *params)

    def i16(self, name, value=None, align=None):
        self.uint(2, name, value, align)

    def i32(self, name, value=None, align=None):
        self.uint(4, name, value, align)

    def real32(self, name, value=None, align=None):
        self.uint(4, name, value, align)

    def save_all_templates_to_file(self, filename):
        templates = self._message_templates
        with open(filename, 'wb') as output:
                pickle.dump(templates, output, pickle.HIGHEST_PROTOCOL)

    def are_message_templates_in_file(self, filename):
        return os.path.exists(filename)

    def load_message_templates_from_file(self, filename):
        with open(filename, 'rb') as input:
            read_from_file = pickle.load(input)
        self._message_templates = read_from_file

    def receive_udp_with_endianess(self, endianess, *params):
        msg = self.receive_udp(*params)
        self.mask_and_verify_endianness(msg, endianess)
        return msg

    def mask_and_verify_endianness(self, msg, expected_endianess):
        endianess_map = {'BIG_ENDIAN': self.BIG_ENDIAN, 'LITTLE_ENDIAN': self.LITTLE_ENDIAN}
        if expected_endianess not in endianess_map:
            raise Exception('Unknown endianess: %s' % expected_endianess)
        actual_value = msg._header.flags.int & int(BuiltIn().get_variable_value('${ENDIAN FLAG}'))
        if actual_value != endianess_map[expected_endianess]:
            error_text = 'Expected message with endiannes flag: %s, but got %s\n' % (endianess_map[expected_endianess], actual_value)
            error_text += '%s\n %s' % (str(msg), repr(msg._header))
            raise AssertionError(error_text)

    def arrayU8(self, size, name, *parameters):
        """Define a new u8 values array of given `size`.

        `name` if the name of this array element.

        Examples:
        | ArrayU8 | 8 | myU8Array |
        """
        self._new_list(size, name)
        self.u8(name, *parameters)
        self._end_list()

    def save_message_to_file(self, message, filename):
        with open(filename, 'wb') as output:
                pickle.dump(message, output)