
def solution(short_names, words) -> list:
	info = set(short_names)
	res = []
	for x in words:
		for i in range(1, len(x)):
			start_ = x[:i]
			if start_ in info:
				res.append(start_)
				break
		else:
			res.append(x)
	return res

def run_tests():
	test1 = solution(
		['a', 'b'],
		['abdafb', 'basrt', 'casds', 'dsasa', 'a'],
	)
	assert test1 ==  ['a', 'b', 'casds', 'dsasa', 'a'], test1

	test2 = solution(
		['aa', 'bc', 'aaa'],
		['a', 'aa', 'aaa', 'bcd', 'abcd'],
	)
	assert test2 == ['a', 'aa', 'aa', 'bc', 'abcd'], test2

if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	short_names = input().split()
	words =input().split()

	res = solution(short_names, words)
	print(*res)
