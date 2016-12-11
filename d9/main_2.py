import os
import re


def gen_length(gen):
    length = 0
    for part in gen:
        length += len(part)
    return length


def splitter(line, n):
    return line[:n], line[n:]

class Streamer(object):

    def __init__(self, input_file):
        self.file = input_file
        self.line = None
        self._buffer_line()

    def _buffer_line(self):
        self.line = self.file.readline().strip()

    def _read(self, n):
        if len(self.line) > n:
            ret_line, self.line = splitter(self.line, n)
            return ret_line
        else:
            remainder = self.line
            self._buffer_line()
            if not self.line:
                return remainder
            rest = inner(n - len(remainder))
            return remainder + rest

    def read(self, n):
        next_part = self._read(n)
        if not next_part:
            raise StopIteration
        return next_part

    def feed_text(self, text):
        import pdb; pdb.set_trace()
        self.line = text + self.line


def decoder(input_file):
    gen = Streamer(input_file)
    while True:
        try:
            next_char = gen.read(1)
        except StopIteration:
            break
        if next_char != '(':
            yield next_char
        else:
            expression = next_char
            while True:
                next_char = gen.read(1)
                expression += next_char
                if next_char == ')':
                    break
            match = re.match(r'\((?P<length>\d+)x(?P<times>\d+)\)', expression)
            length = int(match.group('length'))
            times = int(match.group('times'))
            gen.feed_text(gen.read(length) * times)

def run(input_file):
    return gen_length(decoder(input_file))


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    input_file = open(input_path, 'r')

    ret = run(input_file)
    # Expect 74532
    print ret
