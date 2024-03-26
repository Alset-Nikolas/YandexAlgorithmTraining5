
def __sum_slice_k_in_mass(r:int, pref_sum:list[int], k: int) -> int:
	del_ = 0
	if r - k >= 0:
		del_ = pref_sum[r-k]
	return pref_sum[r] - del_


def bin_search(sum_slise: int, pref_sum:list[int], k:int):
	l = k-1
	r = len(mass) - 1
	while l < r:
		m = (l + r) // 2
		sum_ = __sum_slice_k_in_mass(r=m, pref_sum=pref_sum, k=k)
		if sum_slise == sum_:
			return m-(k-1)
		elif sum_ > sum_slise:
			r = m
		else:
			l = m + 1
	if __sum_slice_k_in_mass(r=l, pref_sum=pref_sum, k=k) == sum_slise:
		return l - (k-1)


def solution_item(n, k, sum_slise, pref_sum):
	'''
	:param n: len(mass)
	:param k: Кол-во полков
	:param sum_slise: Суммарное кол-во орков в полках
	:return:
	'''
	if k > n or k < 1:
		return -1
	ans = bin_search(sum_slise=sum_slise, pref_sum=pref_sum, k=k,)
	if ans is None:
		return -1
	return ans + 1

def __get_pref_sum(n:int,mass:list[int]) -> list[int]:
	if not mass:
		return []
	mass_ = [mass[0]]
	for i in range(1, n):
		mass_.append(mass_[-1] + mass[i])
	return mass_

if __name__ == '__main__':
	table = []
	n, k = list(map(int, input().split()))
	mass = list(map(int, input().split()))
	pref_sum = __get_pref_sum(n, mass)
	for ki in range(k):
		k, sum_slise = list(map(int, input().split()))
		res = solution_item(n, k, sum_slise, pref_sum)
		print(res)
