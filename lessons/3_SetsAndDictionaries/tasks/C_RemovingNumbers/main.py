def quantity_dict(numbers):
	info = dict()
	for x in numbers:
		if x not in info:
			info[x] = 0
		info[x] += 1
	return info


def solution(n, numbers):
	info_number: dict = quantity_dict(numbers)
	sorted_numbers = sorted(info_number.keys())
	i = 0
	res = n - info_number[sorted_numbers[0]]
	for j, x in enumerate(sorted_numbers[1:]):
		if sorted_numbers[j] - sorted_numbers[i] > 1:
			res = min(res, n - sum(info_number[sorted_numbers[k]] for k in range(i, j)))
			while i <= j and sorted_numbers[j] - sorted_numbers[i] > 1:
				i += 1
	while i < len(sorted_numbers) and sorted_numbers[len(sorted_numbers)-1] - sorted_numbers[i] > 1:
		i += 1
	if i < len(sorted_numbers):
		res = min(res, n - sum(info_number[sorted_numbers[k]] for k in range(i, len(sorted_numbers))))
	return res


def run_tests():
	test1 = solution(
		5, [
			1, 2, 3, 4, 5,
		]
	)
	assert test1 == 3, test1

	test2 = solution(
		10, [
			1, 1, 2, 3, 5, 5, 2, 2, 1, 5,
		]
	)
	assert test2 == 4, test2


if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	n = int(input())
	numbers = list(map(int, input().split()))
	res = solution(n, numbers)
	print(res)
