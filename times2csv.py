import csv
import codecs
import sys

from robot.api import ExecutionResult


class Times(object):

    def __init__(self, writer):
        self.writer = writer

    def process_suites(self, suites):
        self.process_items('SUITE', suites)
        for kws in zip(*(s.keywords for s in suites)):
            self.process_keywords(kws)
        for children in zip(*(s.suites for s in suites)):
            self.process_suites(children)
        for tests in zip(*(s.tests for s in suites)):
            self.process_tests(tests)

    def process_tests(self, tests):
        self.process_items('TEST', tests)
        for kws in zip(*(t.keywords for t in tests)):
            self.process_keywords(kws)

    def process_keywords(self, keywords, level=1):
        self.process_items('%s KW %s' % ('_' * (level-1), level), keywords)
        for kws in zip(*(k.keywords for k in keywords)):
            self.process_keywords(kws, level+1)

    def process_items(self, item_type, items):
        name = items[0].name.encode('UTF-8')
        #assert all(item.name == name for item in items)
        self.writer.writerow([item_type, name] + [item.elapsedtime for item in items])


def main(paths, outpath='times2csv.csv'):
    with open(outpath, 'wb') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['TYPE', 'NAME'] + paths)
        suites = [ExecutionResult(p).suite for p in paths]
        times = Times(writer)
        times.process_suites(suites)

main(sys.argv[1:])
