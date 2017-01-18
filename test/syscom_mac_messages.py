from robot.libraries.BuiltIn import BuiltIn

class syscom_mac_messages(object):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.syscom = BuiltIn().get_library_instance('syscom_rammbock')

    def SPduMuxDataCombReq(self, name):
        self.syscom.new_struct('SPduMuxDataCombReq', name)
        self.syscom.u16('ueIndex')
        self.syscom.u16('macId')
        self.syscom.i32('txPower')
        self.syscom.u8('cfi')
        self.syscom.u8('spatialMode')
        self.syscom.u8('numOfLayers')
        self.syscom.u8('paddingNumOfLayers')
        self.syscom.u32('codebookIndex')
        self.syscom.u32('nIr')
        BuiltIn().run_keyword('SPdschResources', 'resources')
        self.syscom.u8('mimoIndicator')
        self.syscom.u8('servingCellIndex')
        self.syscom.u8('reqType')
        self.syscom.u8('paddingReqType')
        self.syscom.u32('lnCellIdServCell')
        self.syscom.u32('enbIdServCell')
        self.syscom.u32('tbFlags')
        self.syscom.array('2', 'SDlSchPduMuxCwAttributes', 'cwAttributes')
        self.syscom.u32('hasCriPayload')
        self.syscom.array('6', 'u8', 'criPayload')
        self.syscom.u16('paddingCriPayload')
        self.syscom.u32('subFrameNumberSubstitute')

    def STddPduMuxDataCombReq_temp(self, name):
        self.syscom.new_struct('STddPduMuxDataCombReq_temp', name)
        self.syscom.u16('ueIndex')
        self.syscom.u16('macId')
        self.syscom.i32('txPower')
        self.syscom.u8('cfi')
        self.syscom.u8('spatialMode')
        self.syscom.u8('numOfLayers')
        self.syscom.u8('paddingNumOfLayers')
        self.syscom.u32('codebookIndex')
        self.syscom.u32('nIr')
        BuiltIn().run_keyword('SPdschResources', 'resources')
        self.syscom.u8('mimoIndicator')
        self.syscom.u8('servingCellIndex')
        self.syscom.u8('reqType')
        self.syscom.u8('paddingReqType')
        self.syscom.u32('lnCellIdServCell')
        self.syscom.u32('enbIdServCell')
        self.syscom.u32('tbFlags')
        self.syscom.array('2', 'SDlSchPduMuxCwAttributes', 'cwAttributes')
        self.syscom.u32('hasDlBfTbFormat')
        BuiltIn().run_keyword('SDlBfTbFormat', 'dlBfTbFormat')
        self.syscom.end_struct()
