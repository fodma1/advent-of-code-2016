import hashlib
import os


def generate_hash(prefix):
    i = 0
    while True:
        m = hashlib.md5()
        m.update('{prefix}{postfix}'.format(prefix=prefix, postfix=i))
        op = m.hexdigest()
        if op[:5] == '00000':
            yield op
        i += 1

def query_n_times(n, generator, *args, **kwargs):
    for _, gen in zip(range(n), generator(*args, **kwargs)):
        yield gen

def run(raw_data):
    data = raw_data[0]
    return ''.join([h[5] for h in query_n_times(8, generate_hash, data)])


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    input_file = open(input_path, 'r')
    raw_data = [l.strip() for l in input_file.readlines() if l.strip()]

    ret = run(raw_data)

    print ret