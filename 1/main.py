from collections import namedtuple
import os

Coordinate = namedtuple('Coordinate', 'direction steps')

def run(raw_data):
	coordinates = raw_data.split(', ')
	coordinates = [Coordinate(c[0], int(c[1:])) for c in coordinates]
	direction = 1
	vertical = 0
	horizontal = 0
	for coordinate in coordinates:
		if coordinate.direction == 'R':
			turn = 1
		else:
			turn = -1

		direction = (4 + direction + turn) % 4

		if direction < 2:
			sign = -1
		else:
			sign = 1

		if direction % 2 == 0:
			horizontal += sign * coordinate.steps
		else:
			vertical += sign * coordinate.steps

	return abs(horizontal) + abs(vertical)


if __name__ == '__main__':
	input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
	input_file = open(input_path, 'r')
	raw_data = ''.join(input_file.readlines()).strip()

	ret = run(raw_data)

	print ret