import os

class Coordinate(object):
    keypad = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    )

    keypad_height = 2
    keypad_width = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def _move(self, x, y):
        x = min(x, self.keypad_height)
        x = max(x, 0)

        y = min(y, self.keypad_width)
        y = max(y, 0)
        return Coordinate(x, y)

    def U(self):
        return self._move(self.x - 1, self.y)

    def D(self):
        return self._move(self.x + 1, self.y)

    def R(self):
        return self._move(self.x, self.y + 1)

    def L(self):
        return self._move(self.x, self.y - 1)

    def value(self):
        return self.keypad[self.x][self.y]


def run(raw_data):
    values = []
    coord = Coordinate(1, 1)
    for line in raw_data:
        for c in line:
            if c not in 'UDRL':
                raise ValueError('{} not in UDRL'.format(c))

            coord = getattr(coord, c)()
        #     print '######', coord.value()
        # print '###', coord.value()    
        values.append(coord.value())
    return ''.join([str(v) for v in values])

if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    input_file = open(input_path, 'r')
    raw_data = [l.strip() for l in input_file.readlines() if l.strip()]

    ret = run(raw_data)
    # v = ['ULL',
    # 'RRDDD',
    # 'LURDL',
    # 'UUUUD',]
    # ret = run(v)

    print ret