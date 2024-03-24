
def mix_sets(a_set, b_set):
	res = set()
	for x in a_set:
		if x in b_set:
			res.add(x)
	for x in b_set:
		if x in a_set:
			res.add(x)
	return res

def solution(table):
	if not table:
		return []
	ans = set(table[0])
	for user_songs in table[1:]:
		ans = mix_sets(set(user_songs), ans)
	res = sorted(list(ans))
	return len(res), res

def run_tests():
	test1 = solution(
		[
			['GoGetIt', 'Life'],
		]
	)
	assert test1 == (
		2,
		['GoGetIt', 'Life']
	), test1

	test2 = solution(
		[
			['Love', 'Life'],
			['Life', 'GoodDay'],
		]
	)
	assert test2 == (
		1,
		['Life']
	), test2


if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	table = []
	N = int(input())
	for i in range(N):
		M = int(input())
		table.append(input().split())

	n, text = solution(table)
	print(n)
	print(*text)