

def profitable_startup(n: int, k: int, d: int) -> str:
	'''

	:param n: Изначальная прибыль
	:param k: Кол-во людей
	:param d: Кол-дней
	:return: -1 или число
	'''
	if k == 0:
		return -1
	if d <= 0:
		if n % k == 0:
			return str(n)
		return '-1'
	for i in range(10):
		node_x = n * 10 + i
		if node_x % k == 0:
			return str(node_x) + '0'*max(d-1, 0)
	return '-1'


def run_tests():
	test_1 = [21, 108, 1]
	assert profitable_startup(*test_1) == '216', profitable_startup(*test_1)
	test_2 = [5, 12, 4]
	assert profitable_startup(*test_2) == '-1', profitable_startup(*test_2)


if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	n,k,d=list(map(int, input().split()))
	res = profitable_startup(n, k, d)
	print(res)