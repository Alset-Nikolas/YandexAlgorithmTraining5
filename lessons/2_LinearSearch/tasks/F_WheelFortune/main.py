def solution_item(table, v, k):
	var1 = table[(int((v-0.001) // k)) % (len(table))]
	var2 = table[-(int((v-0.001) // k) )% (len(table))]
	return max(var1, var2)
def solution(table: list[int], vstart: int, vend:int, k):
	res = None
	max_ans = max(table)
	for v in range(min(vstart, vend), max(vstart, vend)+1, k):
		res_item = solution_item(table, v, k)
		if not res:
			res = res_item
		res = max(res, res_item)

		if max_ans == res:
			return max_ans
	return res


def run_tests():
	test1 = solution(
		[1, 2, 3, 4, 5], 3, 5 ,2
	)
	assert test1 == 5, test1

	test2 = solution(
	[1, 2, 3, 4, 5], 15, 15, 2
	)
	assert test2 == 4, test2

	test3 = solution(
	[5, 4, 3, 2, 1], 2, 5, 2
	)
	assert test3 == 5, test3

if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	N = int(input())
	table = list(map(int, input().split()))
	vstart, vend, k = list(map(int, input().split()))
	res = solution(table, vstart, vend, k)
	print(res)