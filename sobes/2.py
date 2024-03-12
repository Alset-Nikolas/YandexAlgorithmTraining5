def binSearch(a: list, key):
	l = 0
	r = len(a) - 1
	result = -1
	while l <= r:
		m = (l + r) // 2

		if a[m].startswith(key):
			r = m - 1
			result = m
		elif a[m] < key:
			l = m + 1
		else:
			r = m - 1
	return result


n, q = list(map(int, input().split()))
mass = []
for _ in range(n):
	mass.append(input())
for qi in range(q):
	k, x = input().split()
	k = int(k)
	j = binSearch(mass, x)
	# print(mass[j:])
	if j == -1 or j + k - 1 >= len(mass) or not mass[j + k-1].startswith(x):
		print(-1)
	else:
		print(j + k)
