import copy

def solution_TL(N: int, M: int, table: list[list[int]]) -> list[int]:
	items = []
	for i in range(N):
		for j in range(M):
			list_ = table[i][:] + [table[l][j] for l in range(N)]
			list_.remove(table[i][j])
			list_.sort(reverse=True, )
			items.append(
				[list_, i, j]
			)
	items.sort(reverse=True, key=lambda x: x[0])
	result, i_max, j_max = items[0]
	return [i_max + 1, j_max + 1]

def check_var(N: int, M: int, table: list[list[int]], i_max: int, j_max:int, is_line: bool, info: dict):
	if is_line:
		for j in range(M):
			x = table[i_max][j]
			info[x] -= 1
			if info[x] == 0:
				info.pop(x)
			table[i_max][j] = None

	else:
		for i in range(N):
			x = table[i][j_max]
			info[x] -= 1
			if info[x] == 0:
				info.pop(x)
			table[i][j_max] = None
	key_max = max(info.keys())
	is_end = False
	for i in range(N):
		for j in range(M):
			x = table[i][j]
			if x == key_max:
				if is_line:
					ans =  [i_max, j]
				else:
					ans =  [i, j_max]
				is_end = True
			if is_end:
				break
		if is_end:
			break
	i_ans, j_ans = ans
	if is_line:
		for i in range(N):
			x = table[i][j_ans]
			if x is not None:
				info[x] -= 1
				if info[x] == 0:
					info.pop(x)
				table[i][j_ans] = None

	else:
		for j in range(M):
			x = table[i_ans][j]
			if x is not None:
				info[x] -= 1
				if info[x] == 0:
					info.pop(x)
				table[i_ans][j] = None
	return  max(info.keys()), [i_ans, j_ans]


def solution(N: int, M: int, table: list[list[int]]) -> list[int]:
	info = dict()
	max_el = table[0][0]
	i_max, j_max = 0, 0
	for i in range(N):
		for j in range(M):
			x = table[i][j]
			if x not in info:
				info[x] = 0
			info[x] += 1
			if x > max_el:
				max_el = x
				i_max, j_max = i, j
	var1, [i1, j1] = check_var(N, M, copy.deepcopy(table), i_max, j_max, is_line=True, info=info.copy())
	var2, [i2, j2] = check_var(N, M, copy.deepcopy(table), i_max, j_max, is_line=False, info=info.copy())
	if var1 > var2:
		return [i2+1, j2+1]
	return [i1+1, j1+1]


def run_tests():
	test1 = solution(2, 2,
	                 [[1, 2], [3, 4]]
	                 )
	assert test1 == [2, 2], test1

	test2 = solution(3, 4,
	                 [
		                 [1, 3, 5, 7, ],
		                 [9, 11, 2, 4],
		                 [6, 8, 10, 12]
	                 ],
	                 )
	assert test2 == [3, 2], test2


if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	N, M = list(map(int, input().split()))
	table = []
	for i in range(N):
		numbers = list(map(int, input().split()))
		table.append(numbers)
	res = solution(N, M, table)
	print(*res)
