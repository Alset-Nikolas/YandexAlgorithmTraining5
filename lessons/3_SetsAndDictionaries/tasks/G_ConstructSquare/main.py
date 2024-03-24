def get_res_ij(all_points, c1, c2):
	res = 0
	result = []
	if c1 not in all_points:
		res += 1
		result.append(c1)

	if c2 not in all_points:
		res += 1
		result.append(c2)
	return res, result

def var1_circle(all_points, x1, y1, x2, y2):
	x11 = x1 + (y2 - y1)
	y11 = y1 - (x2 - x1)

	x22 = x2 + (y2 - y1)
	y22 = y2 - (x2 - x1)

	return  get_res_ij(all_points, c1=(x11, y11), c2=(x22, y22))

def var2_circle(all_points, x1, y1, x2, y2):
	x11 = x1 - (y2 - y1)
	y11 = y1 + (x2 - x1)

	x22 = x2 - (y2 - y1)
	y22 = y2 + (x2 - x1)

	return  get_res_ij(all_points, c1=(x11, y11), c2=(x22, y22))


def var3_circle(all_points, x1, y1, x2, y2):
	is_correct_int = lambda x: (x // 2) * 2 == x
	if x1 < x2:
		xl, yl = x1, y1
		xr, yr = x2, y2
	else:
		xl, yl = x2, y2
		xr, yr = x1, y1
	if yr > yl:
		x11_2 = (x1 + x2) - abs(y2 - y1)
		y11_2 = (y1 + y2) + abs(x2 - x1)

		x22_2 = ((x1 + x2) + abs(y2 - y1))
		y22_2 = (y1 + y2) - abs(x2 - x1)
	else:
		x11_2 = (x1 + x2) - abs(y2 - y1)
		y11_2 = (y1 + y2) - abs(x2 - x1)

		x22_2 = ((x1 + x2) + abs(y2 - y1))
		y22_2 = (y1 + y2) + abs(x2 - x1)
	if all(is_correct_int(x) for x in [x11_2, y11_2, x22_2, y22_2]):
		return get_res_ij(all_points, c1=(x11_2 // 2, y11_2 // 2), c2=(x22_2 // 2, y22_2 // 2))
	return  None, None

def solution(n, table) -> list:
	if n == 1:
		(x,y) = table[0]
		return [3, {
			(x+1, y),
			(x, y-1),
			(x+1, y+1),
		}]
	all_points = set(tuple(x) for x in table)
	res = 4
	result = []
	ans_1 = None
	ans_2 = None
	for i, (x1, y1) in enumerate(table[:-1]):
		for j, (x2, y2) in enumerate(table[i+1:]):

			res_ij, result_ij = var1_circle(all_points, x1, y1, x2, y2)
			if res_ij < res:
				ans_1 = (x1, y1)
				ans_2 = (x2, y2)
				res = res_ij
				result = result_ij

			res_ij, result_ij = var2_circle(all_points, x1, y1, x2, y2)
			if res_ij < res:
				ans_1 = (x1, y1)
				ans_2 = (x2, y2)
				res = res_ij
				result = result_ij

			res_ij, result_ij = var3_circle(all_points, x1, y1, x2, y2)
			if res_ij is not None and res_ij < res:
				ans_1 = (x1, y1)
				ans_2 = (x2, y2)
				res = res_ij
				result = result_ij

			if res == 0:
				return  [res, set(result)]
	return [res, set(result)]



def run_tests():
	return
	test1 = solution(
		2,
		[
			[0, 1],
			[1, 0]
		],
	)
	assert test1 == [
		2,
		{
			(1, 2),
			(2, 1),

		},
	], test1

	test2 = solution(
		3,
		[
			[0, 2],
			[2, 0],
			[2, 2],
		],
	)
	assert test2 == [
		1,
		{
			(0, 0),
		}
	], test2

	test3 = solution(
		4,
		[
			[-1, 1],
			[1, 1],
			[-1, -1],
			[1, -1]
		],
	)
	assert test3 == [
		0,
		set()
	], test3


if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	n = int(input())
	table = []
	for i in range(n):
		table.append(tuple(map(int, input().split())))

	n, res = solution(n, table)
	print(n)
	for line in res:
		print(*line)
