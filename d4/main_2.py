from collections import Counter, namedtuple
from functools import partial
import string
import os
from operator import attrgetter
import re

Bin = namedtuple('Bin', 'letter occurrences')

def rotate(charset, shift, letter):
    return charset[(charset.find(letter) + shift) % len(charset)]

class Entry(object):
    line_matcher = re.compile(r'(?P<encoded>[a-z\-]+)-(?P<sector_id>\d+)\[(?P<checksum>[a-z]+)\]')
    
    def __init__(self, text, sector_id, checksum):
        self.text = text
        self.sector_id = sector_id
        self.checksum = checksum

    @classmethod
    def from_line(cls, line):
        parts = cls.line_matcher.match(line)
        return Entry(
            text=parts.group('encoded'),
            sector_id=int(parts.group('sector_id')),
            checksum=parts.group('checksum')
        )

    @property
    def deciphered(self):
        rotator = partial(
            rotate,
            charset=string.ascii_lowercase,
            shift=self.sector_id
        )
        return ''.join([rotator(letter=c) if c != '-' else '-' for c in self.text])


def run(raw_data):
    entries = [Entry.from_line(l) for l in raw_data]
    return [e.sector_id for e in entries if e.deciphered == 'northpole-object-storage'].pop(0)


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    input_file = open(input_path, 'r')
    raw_data = [l.strip() for l in input_file.readlines() if l.strip()]

    ret = run(raw_data)

    print ret
