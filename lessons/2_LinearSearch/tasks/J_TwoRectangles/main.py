def draw_rect(N: int, M: int, table: list[list[str]], i_start: int, j_start: int, s: str = 'a'):
	len_x = 0
	len_rec_inside = 0
	len_y = 0
	j = j_start
	flag_edd_inside_rec = True
	while j < M and table[i_start][j] != '.':
		if table[i_start][j] == '#':
			j += 1
			len_x += 1
			flag_edd_inside_rec = True
		else:
			j += 1
			len_rec_inside += 1
			flag_edd_inside_rec = False
			flag_edd_inside_rec = False

	if flag_edd_inside_rec:
		len_x += len_rec_inside
	i = i_start
	j = j_start
	while i < N and '.' not in table[i][j:j + len_x]  :
		for j_ in range(j, j + len_x):
			table[i][j_] = s
		i += 1
		len_y += 1
	return len_x, len_y, i - 1


def solution(N: int, M: int, table: list[list[str]]):
	rects = ['a', 'b']
	rect_i = 0
	j_start_line, last_line_i = None, None
	for i in range(N):
		for j in range(M):
			x = table[i][j]
			if x == '#':
				if rect_i >= len(rects):
					return ['NO', None]
				s = rects[rect_i]
				rect_i += 1
				len_x, len_y, last_line_i = draw_rect(N, M, table, i, j, s)
				j_start_line = j

	if rect_i == 0:
		return ['NO', None]
	if rect_i == 1:
		if len_y * len_x == 1:
			return ['NO', None]
		s = rects[rect_i]
		if len_y > 1:
			for j_ in range(j_start_line, j_start_line + len_x):
				table[last_line_i][j_] = s
		else:
			table[last_line_i][j_start_line + len_x - 1] = s
		return ['YES', table]
	return ['YES', table]


def run_tests():
	test1 = solution(
		2, 2,
		table=[
			['.', '.', ],
			['#', '#'],
		]
	)
	assert test1 == [
		'YES',
		[
			['.', '.'],
			['a', 'b'],
		]
	], test1

	test2 = solution(
		2, 1,
		table=[
			['#', ],
			['.'],
		]
	)
	assert test2 == [
		'NO',
		None
	], test2

	test3 = solution(
		1, 3,
		table=[
			['#', '#', '#', ],
		]
	)
	assert test3 == [
		'YES',
		[
			['a', 'a', 'b'],
		]
	], test3

	test4 = solution(
		1, 5,
		table=[
			['#', '#', '#', '#', '.'],
		]
	)
	assert test4 == [
		'YES',
		[
			['a', 'a', 'a', 'b', '.'],
		]
	], test4

	test5 = solution(
		3, 4,
		[
			['.', '#', '#', '.'],
			['#', '#', '#', '#'],
			['#', '#','#','#']
		]
	)
	assert test5 == [
		'YES',
		[
			['.', 'a', 'a', '.'],
			['b', 'b', 'b', 'b'],
			['b', 'b', 'b', 'b']
		]
	]


if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	N, M = list(map(int, input().split()))
	table = []
	for i in range(N):
		new_line = [x for x in input()]
		table.append(new_line)
	res, table = solution(N, M, table)
	print(res)
	if res == 'YES':
		for line in table:
			print(''.join(line))
