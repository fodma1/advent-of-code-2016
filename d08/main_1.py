import numpy as np
import os
import re

class Screen(object):
    rect_matcher = re.compile(r'rect (?P<width>\d+)x(?P<height>\d+)')
    rotate_matcher = re.compile(r'rotate (?P<direction>\w*) [xy]=(?P<number>\d+) by (?P<amount>\d+)')

    def __init__(self, width, height):
        self.matrix = np.zeros((height, width))

    def rect(self, width, height):
        width, height = int(width), int(height)
        self.matrix[:height, :width] = 1
    rect.matcher = rect_matcher

    def rotate(self, direction, number, amount):
        number, amount = int(number), int(amount)
        if direction == 'column':
            self.matrix[:, number] = np.roll(self.matrix[:, number], amount)
        elif direction == 'row':
            self.matrix[number, :] = np.roll(self.matrix[number, :], amount)
        else:
            msg = "Direction {} not understood".format(direction)
            raise ValueError(msg)
    rotate.matcher = rotate_matcher


    def apply(self, line):
        for func in [self.rect, self.rotate]:
            match = func.matcher.match(line)
            if match:
                func(**(match.groupdict()))
                break
        else:
            msg = "line '{}' did not match any definitions".format(line)
            raise ValueError(msg)

    @property
    def pixels_on(self):
        return self.matrix[self.matrix==1]

def run(raw_data):
    screen = Screen(50, 6)
    for line in raw_data:
        screen.apply(line)
    return len(screen.pixels_on)


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    input_file = open(input_path, 'r')
    raw_data = [l.strip() for l in input_file.readlines() if l.strip()]

    ret = run(raw_data)

    print ret
