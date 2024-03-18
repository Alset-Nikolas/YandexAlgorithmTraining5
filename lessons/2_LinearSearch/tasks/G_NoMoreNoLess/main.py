from typing import Union


def solution(numbers: list[int]) -> list[Union[int, list[int]]]:
	if not numbers:
		return [0, []]
	result = []
	ni = 1
	n_max = numbers[0]
	for x in numbers[1:]:
		if ni == n_max:
			result.append(ni)
			ni = 1
			n_max = x
		else:
			if x <= ni:
				result.append(ni)
				ni = 1
				n_max = x
			else:
				ni += 1
				n_max = min(x, n_max)
	result.append(ni)
	return [len(result), result]





def run_tests():
	test1 = solution(
		[1, 3, 3, 3, 2]
	)
	assert test1 == [3, [1, 3, 1]], test1

	test2 = solution(
		[1, 9, 8, 7, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9],
	)
	assert test2 == [3, [1, 6, 9]], test2

	test3 = solution(
		[7, 2, 3, 4, 3, 2, 7],
	)
	assert test3 == [3, [2, 3, 2]], test3


if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	N = int(input())
	for i in range(N):
		Mi = int(input())
		numbers = list(map(int, input().split()))
		n, items = solution(numbers)
		print(n)
		print(*items)
