n = int(input())
text = input()
cash = dict()
ans = set()


def get_ans(text):
	F = True
	pos = 0
	for i, t in enumerate(text):

		if t == 'R':
			F = True
		elif t == 'L':
			F = False
		else:
			pos += 1 if F else -1

	return pos


def calc_cash(text, start_direction='R'):
	word = ''.join(text)
	if word in cash:
		return cash[word]
	if
	i = len(text) // 2
	l_res = calc_cash(text[:i], start_direction)
	add_points, is_last_step_direction_important, next_step_direction = l_res
	r_res = calc_cash(text[i:], start_direction)





text = [x for x in text]
N = calc_cash(text)
is_last_step_direction_important = True
next_step_direction = 0
cash['F'] = [1, is_last_step_direction_important, next_step_direction]
cash['L'] = [0, False, -1]
cash['R'] = [0, False, 1]

for i, x in enumerate(text):
	for k in ['R', 'L', 'F']:
		if k == x:
			continue
		texti = text.copy()
		texti[i] = k
		ansi = get_ans(texti)
		ans.add(ansi)
	if N and N == len(ans):
		print(N)
		exit(0)
print(len(ans))
