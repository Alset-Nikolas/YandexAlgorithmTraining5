import copy


def get_step_to_move_min_distinct_sheep(cords_shep: list, y_: int, x_opt: int):
	get_d = lambda c1, c2: abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
	min_d = None
	x_ans, y_ans = None, None
	for yi, xi in cords_shep:
		d = get_d((yi, xi), (y_, x_opt))
		if min_d is None or d < min_d:
			min_d = d
			x_ans, y_ans = xi, yi
	cords_shep.remove(
		(y_ans, x_ans)
	)
	return min_d, [y_ans, x_ans]


def get_min_steps_by_opt_clm(N: int, cords: list[list[int]], j_opt: int):
	steps_n = 0
	cords_shep = list((y - 1, x - 1) for y, x in cords)
	for i in range(N):
		yx, xi = cords_shep[i]
		steps_n += abs(yx - i) + abs(xi - j_opt)
	return steps_n


def find_optim_j(N, cords):
	cords.sort()
	if len(cords) % 2 == 1:
		return cords[len(cords)//2][1] - 1
	return (cords[len(cords)//2 - 1][1] + cords[len(cords)//2][1])//2 - 1


def generate_table(N: int, cords: list[list[int]]) -> list[list[int]]:
	table = [[0] * N for x in range(N)]
	for yi, xi in cords:
		table[yi - 1][xi - 1] = 1
	return table


def solution(N: int, cords: list[list[int]]) -> int:
	if N == 0:
		return 0
	j_opt = find_optim_j(N, cords)
	res_opt = None
	for j_opt in range(N):
		res = get_min_steps_by_opt_clm(
			N,  copy.deepcopy(cords), j_opt
		)
		if res_opt is None or res < res_opt:
			res_opt = res
	return res_opt


def run_tests():
	return
	test1 = solution(3, [[1, 2], [3, 3], [1, 1]])
	assert test1 == 3, test1

	test2 = solution(5, [
		[1, 5],
		[2, 4],
		[3, 3],
		[4, 2],
		[5, 1],
	])
	assert test2 == 6, test2


if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	N = int(input())
	table = []
	for i in range(N):
		table.append(list(map(int, input().split())))
	res = solution(N, table)
	print(res)
