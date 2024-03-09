def get_plan_to_calc(numbers: list[int]) -> str:
	'''

	:param numbers: числа между кототрыми нужно поставить + *
	:return: Строка из + * в результате применения которых получается нечётный результат.
	'''

	if not numbers:
		return ''
	result = []
	last_2k_1 = None if numbers[0] % 2 == 0 else 0
	res = 0 if numbers[0] % 2 == 0 else 1
	for i in range(len(numbers)-1):
		x_i = numbers[i]
		x_next = numbers[i+1]

		result.append('+')

		if x_next % 2 == 1:
			last_2k_1 = i
			res += 1

	if res % 2 == 0:
		result[last_2k_1] = 'x'
	return ''.join(result)


def run_tests():
	assert get_plan_to_calc([5, 7, 2]) == 'x+', get_plan_to_calc([5, 7, 2])


if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	n = input()
	numbers = list(map(int, input().split()))
	res = get_plan_to_calc(numbers)
	print(res)
