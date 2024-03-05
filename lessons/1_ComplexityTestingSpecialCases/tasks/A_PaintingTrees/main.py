def calc_quantity_tree(p: int, q: int, v: int, m: int) -> int:
	'''

	:param p: Номер дерева, где стоит ведро 1 человека
	:param q: -//- 2 человека
	:param v: Расстояние от ведра 1 человека до последнего дерева
	:param m:  -//- 2 человека
	:return: Кол-во деревьев которые можно покрасить
	'''
	if p > q:
		p, q = q, p
		v, m = m, v
	if p + v < q - m:
		return 2 * (m + v + 1)
	return max(q + m, p + v) - min(q - m, p - v) + 1


def run_tests():
	assert calc_quantity_tree(p=0, q=12, v=7, m=5) == 25
	assert calc_quantity_tree(p=0, q=0, v=0, m=0) == 1
	assert calc_quantity_tree(p=0, q=0, v=3, m=4) == 9


if __name__ == '__main__':
	is_debug = False
	if is_debug:
		run_tests()
	p, v = list(map(int, input().split()))
	q, m = list(map(int, input().split()))
	result = calc_quantity_tree(p=p, q=q, v=v, m=m)
	print(result)
