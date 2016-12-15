from collections import Counter
import os


def run(raw_data):
    return ''.join([Counter(charset).most_common(1)[0][0] for charset in zip(*raw_data)])


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    input_file = open(input_path, 'r')
    raw_data = [l.strip() for l in input_file.readlines() if l.strip()]

    ret = run(raw_data)

    print ret
