def bin_search_first_key(mass: list, key: str):
	l = 0
	r = len(mass) - 1
	result = -1
	while l <= r:
		m = (l + r) // 2
		if mass[m].startswith(key):
			r = m - 1
			result = m
		elif mass[m] < key:
			l = m + 1
		else:
			r = m - 1
	return result


def solution(mass: list[str], x: str, offset: int):
	j = bin_search_first_key(mass, x)
	if j == -1 or j + offset - 1 >= len(mass) or not mass[j + offset - 1].startswith(x):
		return -1
	return j + offset


if __name__ == '__main__':
	n, q = list(map(int, input().split()))
	mass = []
	for _ in range(n):
		mass.append(input())
	for qi in range(q):
		k, x = input().split()
		res = solution(mass, x, offset=int(k))
		print(res)
