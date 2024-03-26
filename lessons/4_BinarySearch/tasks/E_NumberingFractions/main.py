def cals_sum_steps_to_change_number_top(number_top):
	'[0, 0, 1, 5, 6, 14, 15, 27, 28, 44, 45, 65, 66]'
	n1 = number_top // 2
	if number_top > 2:
		an = number_top - (2 - number_top % 2)
		n2 = (2 + an) * (an // 2) // 2
	else:
		n2 = 0
	return n1 + 2 * n2


def find_start_diagonal(n: int):
	l = 0
	r = 10 ** 18 + 1
	ans = -1
	while l <= r:
		m = (l + r) // 2

		if cals_sum_steps_to_change_number_top(m) > n:
			r = m - 1
		else:
			ans = m
			l = m + 1
	return ans


def solution(n: int) -> (int, int):
	n -= 1
	start_diag = find_start_diagonal(n)
	n -= cals_sum_steps_to_change_number_top(start_diag)
	if n == 0:
		return (start_diag, 1)
	if n > start_diag - 1:
		n -= start_diag - 1
		return (n, start_diag + 1 - n + 1)
	return (start_diag - n, n+1)


if __name__ == '__main__':
	n = int(input())
	res1, res2 = solution(n)
	print('{}/{}'.format(res1, res2))
