def calc_min_gols_to_win(g11, g12, g21, g22, is_first_game_in_home_game1: bool) -> int:
	'''
	:param command_first_gols: Голы первый команды
	:param command_second_gols: Голы второй
	:param is_first_game_in_home_game1: 1 команда играла дома первую игру
	:return: Минимальное кол-во голов, чтобы победу одержала 1 команда
	'''
	all_gols_first_command: int = g11 + g21
	all_gols_second_command: int = g12 + g22
	if all_gols_first_command > all_gols_second_command:
		return 0

	delta_gols: int = all_gols_second_command - all_gols_first_command
	if is_first_game_in_home_game1:
		if g12 + delta_gols <= g21:
			return delta_gols + 1
		return delta_gols
	if g11 <= g22:
		return delta_gols + 1
	return delta_gols


def run_tests():
	pass


if __name__ == '__main__':
	is_debug = False
	if is_debug:
		run_tests()
	g11, g12 = list(map(int, input().split(':')))
	g21, g22 = list(map(int, input().split(':')))
	is_first_game_in_home_game1: bool = input() == '1'
	result = calc_min_gols_to_win(g11, g12, g21, g22, is_first_game_in_home_game1)
	print(result)
