def solution(n, m, numbers) -> str:
	info = set()
	k = min(n,m+1)
	for x in numbers[:k]:
		if x in info:
			return 'YES'
		info.add(x)
	if m >= n:
		return 'NO'
	for i in range(max(n - k,0)):
		info.remove(numbers[i])
		if numbers[i+k] in info:
			return 'YES'
		info.add(numbers[i+k])
	return 'NO'


def run_tests():
	test1 = solution(
		4, 2,
		[1, 2, 3, 1]
	)
	assert test1 == 'NO', test1

	test2 = solution(
		4, 1,
		[
			1, 0, 1, 1
		]
	)
	assert test2 == 'YES', test2

	test3 = solution(
		6, 2,
		[
			1, 2, 3, 1, 2, 3
		]
	)
	assert test3 == 'NO', test3


if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	n, m = list(map(int, input().split()))
	numbers = list(map(int, input().split()))
	res = solution(n, m, numbers)
	print(res)
