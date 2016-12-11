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
    scope = {'line': input_file.readline().strip()}
    def inner(n):
        if len(scope['line']) > n:
            ret_line, scope['line'] = splitter(scope['line'], n)
            return ret_line
        else:
            remainder = scope['line']
            new_line = input_file.readline().strip()
            if new_line:
                scope['line'] = new_line
                import pdb; pdb.set_trace()
                rest = inner(n - len(remainder))
                return remainder + rest if rest else ''
            else:
                return remainder
    return inner


def decoder(input_file):
    pass


def run(input_file):
    return gen_length(decoder(input_file))


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    input_file = open(input_path, 'r')

    ret = run(input_file)

    print ret
