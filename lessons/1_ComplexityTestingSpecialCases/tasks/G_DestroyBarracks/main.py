def calculation_rounds(my_army: int, health_other_tron: int, generation_other_army: int) -> int:
	result = 0
	other_army = 0
	while my_army > 0 and (other_army > 0 or health_other_tron > 0):
		result += 1
		damage_tron = my_army - other_army

		if damage_tron > 0:
			health_other_tron -= damage_tron
			other_army = 0
		else:
			if health_other_tron <= my_army:
				other_army -= my_army - health_other_tron
				health_other_tron = 0
			else:
				other_army -= my_army

		if other_army <= 0 and health_other_tron <= 0:
			return result

		my_army -= other_army

		if my_army <= 0:
			return -1

		if health_other_tron > 0:
			other_army += generation_other_army
	return result


def run_tests():
	assert calculation_rounds(10, 11, 15) == 4, calculation_rounds(10, 11, 15)


if __name__ == '__main__':
	# is_debug = True
	# if is_debug:
	# 	run_tests()
	x = int(input())
	y = int(input())
	p = int(input())
	res = calculation_rounds(x, y, p)
	print(res)
