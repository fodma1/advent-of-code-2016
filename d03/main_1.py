import collections
import os

def get_head(array):
    return array[0], array[1:]

def rotate(array):
    dequeue = collections.deque(array)
    for _ in range(len(array)):
        dequeue.rotate(1)
        yield list(dequeue)
    return


def line_transoform(line):
    return [int(e) for e in line.split()]

def valid(entry):
    decomposition = [get_head(e) for e in rotate(entry)]
    return all([head < sum(rest) for head, rest in decomposition])

def run(raw_data):
    data = [line_transoform(l) for l in raw_data]
    return len([1 for p in data if valid(p)])

if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    input_file = open(input_path, 'r')
    raw_data = [l.strip() for l in input_file.readlines() if l.strip()]

    ret = run(raw_data)

    print ret