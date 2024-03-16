def solution(mass: list[list[int]]):
	table = [
		[0] * 10 for y in range(10)
	]
	res = 0
	for xi, yi in mass:
		table[yi][xi] = 1
	for xi, yi in mass:
		res += 4
		res -= table[yi - 1][xi] + table[yi + 1][xi] + table[yi][xi - 1] + table[yi][xi + 1]
	return res


def run_tests():
	assert solution(mass=[
		[1, 1], [1, 2], [2, 1]
	]) == 8, solution(mass=[[1, 1], [1, 2], [2, 1]])
	assert solution(mass=[[8, 8]]) == 4, solution(mass=[[8, 8]])


if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	N = int(input())
	mass = []
	for x in range(N):
		mass.append(
			list(map(int, input().split()))
		)
	result = solution(mass)
	print(result)
