import os
import re

matcher = re.compile(r'^(?P<pre>[A-Z]*)\((?P<length>\d+)x(?P<times>\d+)\)(?P<rest>[A-Z\(\)0-9x]*)')

def splitter(line, n):
    return line[:n], line[n:]

def gen_length(line):
    match = matcher.match(line)
    if match:
        pre = match.group('pre')
        length = int(match.group('length'))
        times = int(match.group('times'))
        rest = match.group('rest')
        to_repreat, rest= splitter(rest, length)
        return len(pre) + gen_length(to_repreat) * times + gen_length(rest)
    else:
        return len(line)


def run(data):
    return gen_length(data)


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    input_file = open(input_path, 'r')
    raw_data = ''.join([l.strip() 
        for l in input_file.readlines() if l.strip()])

    ret = run(raw_data)
    #  expect 11558231665
    print ret
