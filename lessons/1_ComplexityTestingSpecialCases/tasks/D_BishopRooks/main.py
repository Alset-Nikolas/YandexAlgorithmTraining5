import copy
from pprint import pprint


def calc_not_attack_position(table: list[list[str]]) -> int:
	_table: list[list[str]] = copy.deepcopy(table)
	rock = 'R'
	bishop = 'B'
	atack = 'X'
	position_all_figure: set[tuple[int, int]] = set()
	result = 0

	def set_attack_rooks(table: list[list[str]], x: int, y: int):
		'''Учет ладьи в клетке (x, y)'''
		result_ = 0
		if all(not 0 <= z < 8 for z in [x, y]):
			raise ValueError('index rook not correct in table')
		if table[y][x] != rock:
			raise ValueError('symvol rock in [{y}][{x}] err'.format(y=y, x=x))
		position_all_figure.add((x, y))
		for xi in range(x + 1, 8, 1):
			if table[y][xi] in {rock, bishop}:
				break
			elif table[y][xi] == atack:
				continue
			else:
				table[y][xi] = atack
				result_ += 1
		for xi in range(x - 1, -1, -1):
			if table[y][xi] in {rock, bishop}:
				break
			elif table[y][xi] == atack:
				continue
			else:
				table[y][xi] = atack
				result_ += 1

		for yj in range(y + 1, 8, 1):
			if table[yj][x] in {rock, bishop}:
				break
			elif table[yj][x] == atack:
				continue
			else:
				table[yj][x] = atack
				result_ += 1
		for yj in range(y - 1, -1, -1):
			if table[yj][x] in {rock, bishop}:
				break
			elif table[yj][x] == atack:
				continue
			else:
				table[yj][x] = atack
				result_ += 1
		return result_

	def set_attack_bishop(table: list[list[str]], x: int, y: int):
		'''Учет слона в клетке (x, y)'''
		result_ = 0
		if all(not 0 <= z < 8 for z in [x, y]):
			raise ValueError('index rook not correct in table')
		if table[y][x] != bishop:
			raise ValueError('symvol bishop in [{y}][{x}] err'.format(y=y, x=x))
		position_all_figure.add((x, y))
		for i in range(1, 8, 1):
			xi = x + i
			yj = y + i
			if xi < 0 or xi >= 8 or yj >= 8 or yj < 0:
				continue
			if (x == xi and y == yj) or table[yj][xi] == atack:
				continue
			if table[yj][xi] in {rock, bishop}:
				break
			else:
				table[yj][xi] = atack
				result_ += 1

		for i in range(0, -8, -1):
			xi = x + i
			yj = y + i
			if xi < 0 or xi >= 8 or yj >= 8 or yj < 0:
				continue
			if (x == xi and y == yj) or table[yj][xi] == atack:
				continue
			if table[yj][xi] in {rock, bishop}:
				break
			else:
				table[yj][xi] = atack
				result_ += 1

		for i in range(0, -8, -1):
			xi = x + i
			yj = y - i
			if xi < 0 or xi >= 8 or yj >= 8 or yj < 0:
				continue
			if (x == xi and y == yj) or table[yj][xi] == atack:
				continue
			if table[yj][xi] in {rock, bishop}:
				break
			else:
				table[yj][xi] = atack
				result_ += 1
		for i in range(0, 8, 1):
			xi = x + i
			yj = y - i
			if xi < 0 or xi >= 8 or yj >= 8 or yj < 0:
				continue
			if (x == xi and y == yj) or table[yj][xi] == atack:
				continue
			if table[yj][xi] in {rock, bishop}:
				break
			else:
				table[yj][xi] = atack
				result_ += 1
		return result_

	def set_all_figure_to_attack(table, position_all_figure: set[tuple[int, int]]):
		result_ = 0
		for xi, yi in position_all_figure:
			table[yi][xi] = atack
			result_ += 1
		return result_

	for yj in range(8):
		for xi in range(8):
			if _table[yj][xi] == rock:
				result += set_attack_rooks(_table, x=xi, y=yj)
			elif _table[yj][xi] == bishop:
				result += set_attack_bishop(_table, x=xi, y=yj)
	result += set_all_figure_to_attack(_table, position_all_figure=position_all_figure)
	if is_debug:
		pprint(_table)
		print('\n\n')
	return 8 * 8 - result


def __reformat_table_str_to_list(text_table: str) -> list[list[str]]:
	new_format_table: list[list[str]] = []
	for line in text_table.split():
		new_format_table.append(
			list(x for x in line)
		)
	return new_format_table


def run_tests():
	tests = [('''
			********
			********
			*R******
			********
			********
			********
			********
			********
			''', 49),
	         ('''
			********
			********
			*B******
			********
			********
			********
			********
			********
			''', 54),
	         ('''
			********
			*R******
			********
			*****B**
			********
			********
			********
			********
			''', 40),
	         ('''
			**R*****
			*R*R****
			****R***
			*****R**
			**R*****
			**R*****
			**R*****
			**R*****
			''', 0),
	         ('''
			*******B
			******B*
			*****B**
			****B***
			***B****
			**B*****
			*B******
			B*******
			''', 32),
	         ('''
			*******B
			******BB
			*****BB*
			****BB**
			***BB***
			**BB****
			*BB*****
			BB******
			''', 0),
	         ]
	for i, test_and_ans in enumerate(tests):
		test_i, answer_i = test_and_ans
		table_i = __reformat_table_str_to_list(test_i)
		assert calc_not_attack_position(table_i) == answer_i, calc_not_attack_position(table_i)


if __name__ == '__main__':
	is_debug = False
	if is_debug:
		run_tests()
	table_: list[str] = []
	for _ in range(8):
		table_.append(input())
	table: list[list[str]] = __reformat_table_str_to_list(text_table='\n'.join(table_))
	result = calc_not_attack_position(table)
	print(result)
