def create_vector(cords: list[int]):
	x1, y1, x2, y2 = cords
	x_start, y_start = x1, y1
	x_end, y_end = x2, y2
	if y_start > y_end or y_start == y_end and x_start > x_end:
		x_start, y_start = x2, y2
		x_end, y_end = x1, y1
	x_move, y_move = x_end - x_start, y_end - y_start
	return (x_start, y_start), (x_move, y_move)


def create_vectors_direction(figure_: list[list[int]]):
	vectors_direction = dict()
	for cords in figure_:
		(x_start, y_start), (x_move, y_move) = create_vector(cords)
		if (x_move, y_move) not in vectors_direction:
			vectors_direction[(x_move, y_move)] = []
		vectors_direction[(x_move, y_move)].append((x_start, y_start))
	return vectors_direction

def solution(n: int, figure_A: list[list[int]], figure_B: list[list[int]]) -> int:
	vectors_direction_A = create_vectors_direction(figure_A)
	vectors_direction_B = create_vectors_direction(figure_B)

	diff = dict()
	max_ = 0
	for k, items_A in vectors_direction_B.items():
		if not k in vectors_direction_A:
			continue
		for (x1, y1) in items_A:
			for (x2, y2) in vectors_direction_A[k]:
				dx, dy = x2- x1, y2-y1
				if (dx, dy) not in diff:
					diff[(dx, dy)] = 0
				diff[(dx, dy)] += 1
				if max_ < diff[(dx, dy)]:
					max_ = diff[(dx, dy)]
	return n - max_




def run_tests():
	test1 = solution(
		n=5,
		figure_A=[[0, 0, 1, 2], [1, 0, 0, 2], [2, 0, 2, 2], [4, 0, 3, 2], [4, 0, 5, 2]],
		figure_B=[[9, -1, 10, 1], [10, 1, 9, 3], [8, 1, 10, 1], [8, 1, 9, -1], [8, 1, 9, 3]],
	)
	assert test1 == 3, test1

	test2 = solution(
		n=1,
		figure_A=[[3, 4, 7, 9]],
		figure_B=[[-1, 3, 3, 8]],
	)
	assert test2 == 0, test2

	test3 = solution(
		n=1,
		figure_A=[[-4, 5, 2, -3]],
		figure_B=[[-12, 4, -2, 4]],
	)
	assert test3 == 1, test3


if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	n = int(input())
	figure_A = []
	for i in range(n):
		figure_A.append(list(map(int, input().split())))
	figure_B = []
	for i in range(n):
		figure_B.append(list(map(int, input().split())))
	n = solution(n, figure_A, figure_B)
	print(n)

