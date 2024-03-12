def get_min_time(L, x1, v1, x2, v2) -> int:
	'''
	:param L: Длина окружности
	:param x1: Расстояние до точки 1
	:param v1: Скорость первого бегуна
	:param x2: Расстояние до точки 2
	:param v2: Скорость второго бегуна
	:return:
	'''

	def get_min_time_coincided():
		if v1 - v2 == 0:
			return -1
		f = lambda n: ((x1 - x2) + n * L) / (v2 - v1)
		vars = list(filter(lambda x: x != -1 and x >= 0, list(f(x) for x in range(-10000, 10000))))
		if vars:
			return min(vars)
		return -1

	def get_min_time_opposite():
		'''

		:param n:
		:return:
		'''
		if v1 + v2 == 0:
			return -1
		f = lambda n :(-(x1 + x2) + n * L) / (v1 + v2)
		vars = list(filter(lambda x: x != -1 and x >= 0, list(f(x) for x in range(-10000, 10000))))
		if vars:
			return min(vars)
		return -1

	if x1 == x2:
		return 0
	res_1 = get_min_time_coincided()
	res_2 = get_min_time_opposite()
	if res_1 == -1:
		return res_2
	if res_2 == -1:
		return res_1
	return min(res_1, res_2)


def run_tests():
	pass


if __name__ == '__main__':
	is_debug = False
	if is_debug:
		run_tests()
	L, x1, v1, x2, v2 = list(map(int, input().split()))
	res = get_min_time(L, x1, v1, x2, v2)
	if res == -1:
		print('NO')
	else:
		print('YES')
		print(res)
