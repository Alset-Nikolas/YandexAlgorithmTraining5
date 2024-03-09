def calc_min_pass_btn(m_tabs: list[int]) -> int:
	'''
	:param m_tabs: Кол-во пробелов в i строке
	:return: Кол-во нажатий клавиш
	'''

	def calc_min_pass_btn_in_line(m_tab: int) -> int:
		'''
		Space -> +1
		Tab -> +4
		Backspace -> -1
		'''
		result = m_tab // 4
		result += min(m_tab % 4, 2)
		return result

	cache = dict()
	result = 0
	for m_tab in m_tabs:
		if m_tab not in cache:
			cache[m_tab] = calc_min_pass_btn_in_line(m_tab)
		result += cache[m_tab]
	return result




def run_tests():
	assert calc_min_pass_btn([
		1, 4, 12, 9, 0
	]) == 8, calc_min_pass_btn([
		1, 4, 12, 9, 0
	])


if __name__ == '__main__':
	is_debug = False
	if is_debug:
		run_tests()
	n: int = int(input())
	m_tabs: list[int] = [int(input()) for _ in range(n)]
	result = calc_min_pass_btn(m_tabs=m_tabs)
	print(result)
