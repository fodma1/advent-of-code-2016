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
    code = [None for _ in range(8)]
    gen = generate_hash(data)
    while not all([c is not None for c in code]):
        next_item = next(gen)
        index, value = next_item[5], next_item[6]
        try:
            index = int(index)
            if code[index] is None:
                code[index] = value
        except (ValueError, IndexError):
            pass

    return ''.join(code)

if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    input_file = open(input_path, 'r')
    raw_data = [l.strip() for l in input_file.readlines() if l.strip()]

    ret = run(raw_data)

    print ret