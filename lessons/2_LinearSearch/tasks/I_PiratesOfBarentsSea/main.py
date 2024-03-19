import copy



def get_min_steps_by_opt_clm(N: int, cords: list[list[int]], j_opt: int):
	steps_n = 0
	cords_shep = list((y - 1, x - 1) for y, x in cords)
	for i in range(N):
		yx, xi = cords_shep[i]
		steps_n += abs(yx - i) + abs(xi - j_opt)
	return steps_n



def solution(N: int, cords: list[list[int]]) -> int:
	if N == 0:
		return 0
	res_opt = None
	for j_opt in range(N):
		res = get_min_steps_by_opt_clm(
			N,  copy.deepcopy(cords), j_opt
		)
		if res_opt is None or res < res_opt:
			res_opt = res
	return res_opt


def run_tests():
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
