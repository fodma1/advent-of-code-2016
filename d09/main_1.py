import os
import re


def gen_length(gen):
    length = 0
    for part in gen:
        length += len(part)
    return length


def splitter(line, n):
    return line[:n], line[n:]


def streamer(input_file):
    # It's the best way to accomplish clojure behaviour
    scope = {'line': input_file.readline().strip()}
    def inner(n):
        if len(scope['line']) > n:
            ret_line, scope['line'] = splitter(scope['line'], n)
            return ret_line
        else:
            remainder = scope['line']
            scope['line'] = input_file.readline().strip()
            if not scope['line']:
                return remainder
            rest = inner(n - len(remainder))
            return remainder + rest
    return inner

def stream_guard(gen):
    def inner(n):
        next_part = gen(n)
        if not next_part:
            raise StopIteration
        return next_part
    return inner

def decoder(input_file):
    gen = stream_guard(streamer(input_file))
    while True:
        try:
            next_char = gen(1)
        except StopIteration:
            break
        if next_char != '(':
            yield next_char
        else:
            expression = next_char
            while True:
                next_char = gen(1)
                expression += next_char
                if next_char == ')':
                    break
            match = re.match(r'\((?P<length>\d+)x(?P<times>\d+)\)', expression)
            length = int(match.group('length'))
            times = int(match.group('times'))
            yield gen(length) * times


def run(input_file):
    return gen_length(decoder(input_file))


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    input_file = open(input_path, 'r')

    ret = run(input_file)
    # Expect 74532
    print ret
