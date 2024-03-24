
def solution(num1, num2, num3) -> list:
	d1 = set(num1)
	d2 = set(num2)
	d3 = set(num3)
	return sorted(list((d1 & d2) | (d2 & d3) | (d3 & d1)))

def run_tests():
	test1 = solution(
		[3, 1],
		[1, 3],
		[1, 2],
	)
	assert test1 ==  [1, 3], test1

	test2 = solution(
		[1, 2, 2],
		[3, 4, 3],
		[5],
	)
	assert test2 == [], test2



if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	n1 = int(input())
	numbers1 = list(map(int, input().split()))

	n2 = int(input())
	numbers2 = list(map(int, input().split()))

	n3 = int(input())
	numbers3 = list(map(int, input().split()))

	res = solution(numbers1, numbers2, numbers3)
	print(*res)
