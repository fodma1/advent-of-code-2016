import os

class Coordinate(object):
    keypad = (
    (None, None, '1' , None, None,),
    (None, '2' , '3' , '4' , None,),
    ('5' , '6' , '7' , '8' , '9' ,),
    (None, 'A' , 'B' , 'C' , None,),
    (None, None, 'D' , None, None,),
    )

    keypad_height = 4
    keypad_width = 4

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
    coord = Coordinate(2, 0)
    for line in raw_data:
        for c in line:
            if c not in 'UDRL':
                raise ValueError('{} not in UDRL'.format(c))

            new_coord = getattr(coord, c)()
            if new_coord.value() is not None:
                coord = new_coord
        values.append(coord.value())
    return ''.join(values)

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