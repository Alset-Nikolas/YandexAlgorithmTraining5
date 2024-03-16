def solution(mass: list[list[int]]):
	max_a = mass[0][0]
	max_last_jump = 0
	last_jump_index = 0
	max_profit_positive = 0
	for i, (a, b) in enumerate(mass):
		if a > max_a:
			max_a = a
		diff = a - b
		if diff > 0:
			profit_positive = max(diff, a) - min(diff, a)
			if profit_positive > max_profit_positive:
				max_profit_positive = profit_positive
				max_last_jump = a
				last_jump_index = i
		else:
			if max_profit_positive < a:
				max_profit_positive = a
				max_last_jump = a
				last_jump_index = i
	res = []
	H = 0
	end_res = []
	for i, (a, b) in enumerate(mass):
		diff = a - b
		if i == last_jump_index:
			H += max_last_jump
			continue
		if diff <= 0:
			end_res.append(i+1)
		else:
			res.append(i+1)
			H += diff
	return [H, res + [last_jump_index+1] + end_res]




def run_tests():
	assert solution(mass=[
		[1, 5], [8, 2], [4, 4]
	]) == [10, [2, 3, 1]], solution(mass=[[1, 5], [8, 2], [4, 4]])
	assert solution(mass=[[7, 6], [7, 4]]) == [10, [2, 1]], solution(mass=[[7, 6], [7, 4]])


if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	N = int(input())
	mass = []
	for x in range(N):
		mass.append(
			list(map(int, input().split()))
		)
	h, plan = solution(mass)
	print(h)
	print(' '.join(str(x) for x in plan))
