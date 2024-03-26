def bin_search_first_x(x, mass):
	if not mass:
		return -1
	l = 0
	r = len(mass) - 1
	ans = -1
	while l <= r:
		m = (l + r) // 2
		if mass[m] >= x:
			r = m - 1
			ans = m
		else:
			l = m + 1
	if r == -1:
		return 0
	if l == len(mass):
		return len(mass)
	return ans


if __name__ == '__main__':
	n = int(input())
	mass = list(map(int, input().split()))
	mass.sort()
	k = int(input())
	for i in range(k):
		l, r = list(map(int, input().split()))
		i_ = bin_search_first_x(mass=mass, x=l)
		j_ = bin_search_first_x(mass=mass, x=r + 1)
		print(j_ - i_, end=' ')

