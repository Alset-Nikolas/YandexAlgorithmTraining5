def solution(mass: list[int]):
	maxL = 0
	n_maxL = 0
	sum_ = 0
	for x in mass:
		sum_ += x
		if x > maxL:
			maxL = x
			n_maxL = 0
		if maxL == x:
			n_maxL += 1
	if n_maxL == 1:
		delta = sum_ - maxL
		if delta < maxL:
			return maxL - delta
	return sum_


def run_tests():
	assert solution(mass=[1, 5, 2, 1]) == 1, solution(mass=[1, 5, 2, 1])
	assert solution(mass=[5, 12, 4, 3]) == 24, solution(mass=[5, 12, 4, 3])


if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	N = int(input())
	mass = list(map(int, input().split()))
	result = solution(mass)
	print(result)
