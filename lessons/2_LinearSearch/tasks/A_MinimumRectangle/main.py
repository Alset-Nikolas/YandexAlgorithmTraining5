def solution(cords: list[list[int]]) -> list[int]:
	x0, y0 = cords[0]
	xmin, xmax = x0, x0
	ymin, ymax = y0, y0
	for x, y in cords:
		if x < xmin:
			xmin = x
		if x > xmax:
			xmax = x
		if y < ymin:
			ymin = y
		if y > ymax:
			ymax = y
	return [xmin, ymin, xmax, ymax]


def run_tests():
	assert solution([[1, 3], [3, 1], [3, 5], [6, 3]]) == [1, 1, 6, 5]


if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()

	N = int(input())
	cords = []
	for _ in range(N):
		xi, yi = list(map(int, input().split()))
		cords.append([xi, yi])
	result = solution(cords)
	print(' '.join(str(x) for x in result))
