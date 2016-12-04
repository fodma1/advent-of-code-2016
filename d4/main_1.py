from collections import Counter, namedtuple
import string
import os
from operator import attrgetter
import re

Bin = namedtuple('Bin', 'letter occurrences')

class Entry(object):
    line_matcher = re.compile(r'(?P<encoded>[a-z\-]+)-(?P<id>\d+)\[(?P<checksum>[a-z]+)\]')
    
    def __init__(self, text, id, checksum):
        self.text = text
        self.sector_id = id
        self.checksum = checksum

    @classmethod
    def from_line(cls, line):
        parts = cls.line_matcher.match(line)
        return Entry(
            text=parts.group('encoded'),
            id=int(parts.group('id')),
            checksum=parts.group('checksum')
        )

    @property
    def valid(self):
        return self._calculate_checksum() == self.checksum

    def _calculate_checksum(self):
        counter = Counter([c for c in self.text if c in string.ascii_lowercase])
        bins = [Bin(k, v) for k, v in counter.items()]
        bins.sort(key=attrgetter('letter'))
        bins.sort(key=attrgetter('occurrences'), reverse=True)
        bins = bins[:5]
        return ''.join([b.letter for b in bins])


def run(raw_data):
    return sum([e.sector_id for e in [Entry.from_line(l) for l in raw_data] if e.valid])


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    input_file = open(input_path, 'r')
    raw_data = [l.strip() for l in input_file.readlines() if l.strip()]

    ret = run(raw_data)

    print ret