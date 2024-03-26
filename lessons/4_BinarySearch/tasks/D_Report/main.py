def calc_h(width: int, mass: list[int]) -> int:
	'''Возвращает высоту листа если все блоки идут подрят'''
	h = 0
	li = 0
	for x in mass:
		if li == 0:
			if x == width:
				h += 1
				li =0
			elif x < width:
				li = x
				h += 1
		else:
			if li+x+1<=width:
				li += x+1
			else:
				li = x
				h += 1
	return h


def calc_optimal_width(h: int, mass: list[int]) -> int:
	width_min = max(mass)
	width_max = sum(mass) + len(mass)+1
	WIDTH = range(width_min, width_max)
	l = 0
	r = len(WIDTH) - 1
	ans = -1
	while l <= r:
		m = (l + r) // 2
		if calc_h(width=WIDTH[m], mass=mass) <= h:
			ans = m
			r = m - 1
		else:
			l = m + 1
	if ans != -1:
		return WIDTH[ans]


def get_min_width(h: int, mass1: list[int], mass2: list[int]) -> [int, int]:
	w1 = calc_optimal_width(h=h, mass=mass1)
	h1 = calc_h(width=w1, mass=mass1)
	w2 = calc_optimal_width(h=h, mass=mass2)
	h2 = calc_h(width=w2, mass=mass2)
	return w1 + w2, max(h1, h2)


def solution(W: int, N: int, M: int, A: list[int], B: list[int]) -> int:
	h_min = 1
	h_max = len(A) + len(B) + 1
	H = range(h_min, h_max)
	l = 0
	r = len(H) - 1
	ans = -1
	while l <= r:
		m = (l + r) // 2
		w_test, h_test = get_min_width(h=H[m], mass1=A, mass2=B)
		if w_test > W:
			l = m + 1
		else:
			ans = h_test
			r = m - 1
	if ans != -1:
		return ans


if __name__ == '__main__':
	W, N, M = list(map(int, input().split()))
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))
	res = solution(W, N, M, A, B)
	print(res)
	# print(calc_optimal_width(h=3, mass=[2, 2, 1, 1, 2]))
	# print(calc_h(width=4, mass=[2, 2, 1, 1, 2]))