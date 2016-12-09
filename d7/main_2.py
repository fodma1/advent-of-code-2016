from collections import Counter
from functools import partial
from itertools import groupby, ifilter
from operator import itemgetter
import os
import re

matcher = re.compile(
    r'(?=(?P<first_letter>[a-z])(?P<second_letter>[a-z])(?P=first_letter))'
)

def stream_chars(line):
    is_brackets = False
    char_to_look_for = '['
    for char in line:
        if char != char_to_look_for:
            yield is_brackets, char
        else:
            is_brackets = not is_brackets
            char_to_look_for = ']' if is_brackets else '['

def block_chars(gen):
    try:
        current_state, first_char = next(gen)
    except StopIteration:
        return
    block = first_char
    for state, char in gen:
        if state == current_state:
            block += char
        else:
            yield current_state, block
            block = ''
            current_state = state
    yield current_state, block

def block_chars_2(gen):
    for state, tuples in groupby(gen, itemgetter(0)):
        yield state, ''.join([c[1] for c in tuples])

# def get_bracked_substr(line):
#     is_brackets = False
#     line = line[:]
#     # import pdb; pdb.set_trace()
#     while line:
#         next_index = line.find(']' if is_brackets else '[')
#         if next_index > -1:
#             yield is_brackets, line[:next_index]
#             line = line[next_index + 1:]
#             is_brackets = not is_brackets
#         else:
#             yield is_brackets, line

def palindrome_gen(line):
    for f, s in matcher.findall(line):
        if f != s:
            yield f, s


def valid(line):
    blocked_chars = block_chars_2(stream_chars(line))
    blocked_chars = sorted(blocked_chars, key=itemgetter(0))

    streams = {}
    for k, g in groupby(blocked_chars, itemgetter(0)):
        streams[k] = map(itemgetter(1), g)

    no_block_streams = streams[False]
    block_streams = streams[True]

    no_block_palindromes = ({(f, s) for line in no_block_streams
        for f, s in palindrome_gen(line)})
    block_palindromes = ({(s, f) for line in block_streams
        for f, s in palindrome_gen(line)})

    return len(no_block_palindromes & block_palindromes) > 0



def run(raw_data):
    return len([1 for line in raw_data if valid(line)])

if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    input_file = open(input_path, 'r')
    raw_data = [l.strip() for l in input_file.readlines() if l.strip()]

    ret = run(raw_data)

    print ret