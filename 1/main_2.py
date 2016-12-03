from collections import namedtuple, defaultdict
import os

Coordinate = namedtuple('Coordinate', 'direction steps')

def signed_range(stop):
	sign = 1 if stop > 0 else -1 if stop < 0 else 0
	for x in range(1, abs(stop) + 1):
		yield sign * x

def run(raw_data):
	coordinates = raw_data.split(', ')
	coordinates = [Coordinate(c[0], int(c[1:])) for c in coordinates]
	direction = 1
	vertical = 0
	horizontal = 0
	places = defaultdict(lambda : defaultdict(int))
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
			h_diff = sign * coordinate.steps
			
			for h_it in signed_range(h_diff):
				part_coords_h = horizontal + h_it
				places[part_coords_h][vertical] += 1
				# print places
				if places[part_coords_h][vertical] > 1:
					return abs(part_coords_h) + abs(vertical)
			
			horizontal += h_diff
		else:
			v_diff = sign * coordinate.steps

			for v_it in signed_range(v_diff):
				part_coords_v = vertical + v_it
				places[horizontal][part_coords_v] += 1
				# print places
				if places[horizontal][part_coords_v] > 1:
					return abs(horizontal) + abs(part_coords_v)

			vertical += v_diff


if __name__ == '__main__':
	input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
	input_file = open(input_path, 'r')
	raw_data = ''.join(input_file.readlines()).strip()

	ret = run(raw_data)

	print ret
