from collections import deque


def generate_events(lines):
	events = []
	for id, (x, y) in enumerate(lines):
		events.append([x, 0, x, y, id])
		events.append([y, 1, x, y, id])
	events.sort(key=lambda x: x[2], reverse=True)
	events.sort(key=lambda x: x[3], reverse=True)
	events.sort(key=lambda x: x[1], reverse=True)
	events.sort(key=lambda x: x[0])
	return events[::-1]


def check_norm_line(X, Y, ans, not_ans):
	while len(X) > 0 and len(Y) > 0 and (X[0] == Y[0] or X[0] == Y[-1] or X[-1] == Y[0]):
		while len(X) >0 and len(Y) >0 and X[0] == Y[0]:
			if X[0] not in not_ans:
				ans.add(X[0])
			X.popleft()
			Y.popleft()
		while len(Y) > 0 and len(X) > 0 and X[0] == Y[-1]:
			for yi in Y:
				not_ans.add(yi)
			X.popleft()
			Y.pop()
		while len(Y) > 0 and len(X) > 0 and X[-1] == Y[0]:
			for xi in X:
				not_ans.add(xi)
			X.pop()
			Y.popleft()
	return X, Y




def calc_not_crossing_line(lines):
	events = generate_events(lines)
	X = deque()
	Y = deque()
	not_ans = set()
	ans = set()
	while events:
		new_event = events.pop()
		x, is_y, _, _, id = new_event
		if is_y:
			Y.append(id)
		else:
			X.append(id)
		X, Y = check_norm_line(X, Y, ans, not_ans)
	return len(ans)


def tests():
	assert calc_not_crossing_line(
		[
			[1, 4],
			[2, 5],
			[3, 1],
			[4, 5],
			[5, 6],
		]
	) == 1
	assert calc_not_crossing_line(
		[
			[3, 1],
			[4, 5],
			[5, 6],
			[1, 4],
			[2, 5],

		]
	) == 1
	assert calc_not_crossing_line(
		[
			[2, 6],
			[3, 9],
			[4, 2],
			[6, 9],
			[9, 10],
		]
	) == 1
	assert calc_not_crossing_line(
		[
			[0, 1],
			[1, 0],
		]
	) == 0
	assert calc_not_crossing_line(
		[
			[0, 0],
			[1, 1],
		]
	) == 2
	assert calc_not_crossing_line(
		[
			[0, 0],
			[0, 1],
		]
	) == 0
	assert calc_not_crossing_line(
		[
			[0, 1],
			[1, 1],
		]
	) == 0
	assert calc_not_crossing_line(
		[
			[0, 1],
			[1, 1],
			[2, 1],
			[3, 5]
		]
	) == 1
	assert calc_not_crossing_line(
		[
			[2, 1],
			[0, 1],
			[3, 5],
			[1, 1],

		]
	) == 1
	assert calc_not_crossing_line(
		[
			[-100, 100],
			[0, 0],
			[1, 0],
			[2, 3],
			[3, 2]
		]
	) == 0
	assert calc_not_crossing_line(
		[
			[0, 5],
			[10, 5],
			[10, 15],
			[20, 15],
		]
	) == 0
	assert calc_not_crossing_line(
		[
			[0, 9],
			[1, 10],
			[9, 0],
			[10, 1],
		]
	) == 0
	assert calc_not_crossing_line(
		[
			[10, 1],
			[9, 0],
			[1, 10],
			[0, 9],
			[10, 1],
		]
	) == 0
	assert calc_not_crossing_line(
		[
			[0, 2],
			[0, 1],
		]
	) == 0
	assert calc_not_crossing_line(
		[
			[0, 1],
			[0, 2],

		]
	) == 0

if __name__ == '__main__':
	tests()
	N = int(input())
	lines = []
	for i, x in enumerate(range(N)):
		new_line = list(map(int, input().split()))
		lines.append(new_line)

	res = calc_not_crossing_line(lines)
	print(res)
