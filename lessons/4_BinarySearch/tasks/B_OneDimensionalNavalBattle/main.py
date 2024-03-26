def check_valid_game(n, ki):
	n -= ki
	ki -= 1
	m = 2
	while ki > 0:
		n -= (ki + 1) * m
		if n < 0:
			return False
		ki -= 1
		m += 1
	return n >= 0


def bin_search_last_true(n):
	l = 0
	r = n
	ans = -1
	while l <= r:
		m = (l + r) // 2
		if check_valid_game(n=n,ki=m):
			l = m+ 1
			ans = m
		else:
			r = m - 1
	return ans


def solution(n: int) -> int:
	return bin_search_last_true(n)


def run_tests():
	test1 = solution(7)
	assert test1 == 2, test1


if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	table = []
	N = int(input())
	k_max = solution(N)
	print(k_max)
