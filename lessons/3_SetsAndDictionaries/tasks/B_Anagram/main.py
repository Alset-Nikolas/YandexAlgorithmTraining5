


def solution(text1, text2):
	if len(text1) != len(text2):
		return 'NO'
	d1 = dict()
	for t in text1:
		if t not in d1:
			d1[t] = 0
		d1[t] += 1
	d2 = dict()
	for t in text2:
		if t not in d2:
			d2[t] = 0
		d2[t] += 1
	return 'YES' if d1 == d2 else 'NO'
def run_tests():
	test1 = solution(
		'dusty', 'study'
	)
	assert test1 == 'YES', test1

	test2 = solution(
		'rat', 'bat'
	)
	assert test2 == 'NO'


if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	t1 = input()
	t2 = input()
	res = solution(t1, t2)
	print(res)
