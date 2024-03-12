FIBS = [0, 1]
CASH_MAX_VALUES = dict()

def calc_max_people_in_other_army(my_army: int) -> int:
	if my_army in CASH_MAX_VALUES:
		return CASH_MAX_VALUES[my_army]
	max_people = 0
	while FIBS[-1] <= my_army:
		FIBS.append(FIBS[-1] + FIBS[-2])
	while my_army > 0:

		for i in range(len(FIBS) - 1, -1, -1):
			x = FIBS[i]
			if x < my_army:
				max_people += FIBS[i + 1]
				my_army -= FIBS[i]
				break
			elif x == my_army:
				max_people += FIBS[i + 1]
				my_army -= FIBS[i]
				break
	CASH_MAX_VALUES[my_army] = max_people
	return max_people


def calculation_rounds(my_army: int, health_other_tron: int, generation_other_army: int,
                       is_pass_first_step: bool = True,) -> int:
	result = 0
	other_army = 0
	max_people_in_other_army = calc_max_people_in_other_army(my_army)
	# print('max_people_in_other_army', max_people_in_other_army)
	# print('='*100)
	while my_army > 0 and (other_army > 0 or health_other_tron > 0):


		if other_army == 0:
			# 1 ход
			health_other_tron -= my_army


		elif health_other_tron <= my_army and health_other_tron + generation_other_army <= max_people_in_other_army and not is_pass_first_step:
			# Теперь мы победим, но хз сколько ходов
			damage_other_army = max(my_army - health_other_tron, 0)
			other_army -= damage_other_army
			health_other_tron = 0
		else:
			if health_other_tron <= my_army and  health_other_tron + generation_other_army <= max_people_in_other_army:
				is_pass_first_step = False
			damage_tron = max(0, my_army - other_army)
			# Нужно уменьшать врагов

			if health_other_tron > 0 and damage_tron > 0 and health_other_tron + generation_other_army - max_people_in_other_army >= damage_tron:
				# Кол-во повторов убить всех врагов и нанести урон базе
				N = (health_other_tron + generation_other_army - max_people_in_other_army) // damage_tron
				result += N
				# print('N=', N)
				health_other_tron -= (my_army - other_army) * N
				if health_other_tron > 0:
					other_army = generation_other_army
				else:
					other_army = 0
				# print(result, my_army, health_other_tron, other_army)
				continue
			else:
				# Врагов много
				# print('!')
				health_other_tron -= damage_tron
				other_army -= my_army
				if damage_tron == 0 and other_army == 0 and generation_other_army == my_army:
					return  -1
		if other_army < 0:
			other_army = 0
		if other_army > 0:
			my_army -= other_army
			max_people_in_other_army = calc_max_people_in_other_army(my_army)
		# print('max_people_in_other_army', max_people_in_other_army)



		if health_other_tron > 0:
			other_army += generation_other_army

		if my_army <= 0:
			return -1
		result += 1

		# print(result, my_army, health_other_tron, other_army)

	return result


def get_answer_ebania_zadacha(my_army: int, health_other_tron: int, generation_other_army: int) -> int:
	var1 = calculation_rounds(my_army, health_other_tron, generation_other_army, True)
	var2 = calculation_rounds(my_army, health_other_tron, generation_other_army, False)
	# print(var1, var2)
	if var1 == var2 == -1:
		return -1
	elif var1 == -1:
		return var2
	elif var2 == -1:
		return var1
	return min(var1, var2)

def run_tests():
	assert get_answer_ebania_zadacha(10, 11, 15) == 4, get_answer_ebania_zadacha(10, 11, 15)
	assert get_answer_ebania_zadacha(250, 500, 230) == 8, get_answer_ebania_zadacha(250, 500, 230)
	assert get_answer_ebania_zadacha(25, 200, 10) == 13, get_answer_ebania_zadacha(25, 200, 10)
	assert get_answer_ebania_zadacha(250, 500, 240) == 13
	assert get_answer_ebania_zadacha(250, 500, 218) == 6
	assert get_answer_ebania_zadacha(499, 500, 499) == 3, get_answer_ebania_zadacha(499, 500, 499)
	assert get_answer_ebania_zadacha(250, 500, 250) == -1

if __name__ == '__main__':
	is_debug = False
	if is_debug:
		run_tests()
	x = int(input())
	y = int(input())
	p = int(input())
	res = get_answer_ebania_zadacha(x, y, p)
	print(res)
