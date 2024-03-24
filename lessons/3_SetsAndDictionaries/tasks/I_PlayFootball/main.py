def check_team_in_system(team: str, total_goals_team: dict):
	if team not in total_goals_team:
		total_goals_team[team] = {
			"games": 0,
			"goals": 0,
			"score": 0,
		}


def check_user_in_system(user: str, team: str, total_goals_users: dict):
	if user not in total_goals_users:
		total_goals_users[user] = {
			"goals": 0,
			'goals_detail': [0 for x in range(91)],
			"score": 0,
			'team': team,
		}


def add_new_math_in_team(team: str, goals: int, total_goals_team: dict):
	total_goals_team[team]['games'] += 1
	total_goals_team[team]['goals'] += goals


def add_goal_score_in_system(goals_info: list, total_goals_team: dict, total_goals_users: dict):
	min_, user, c = goals_info[0]
	total_goals_team[c]['score'] += 1
	total_goals_users[user]['score'] += 1


def add_goal_user(
		user: str,
		min_: int,
		total_goals_users: dict,
):
	total_goals_users[user]['goals'] += 1
	total_goals_users[user]['goals_detail'][min_] += 1


def add_new_match_in_system(text_, total_goals_team: dict, total_goals_users: dict):
	words:list[str]= text_[0].split()
	n, m = list(map(int, words[-1].split(':')))
	c1 = []
	c2 = []
	f = False
	for w in words[:-1]:
		if w == '-':
			f = True
			continue
		if not f:
			c1.append(w)
		else:
			c2.append(w)
	c1 = '_'.join(c1)
	c2 = '_'.join(c2)
	check_team_in_system(c1, total_goals_team)
	check_team_in_system(c2, total_goals_team)
	add_new_math_in_team(c1, n, total_goals_team)
	add_new_math_in_team(c2, m, total_goals_team)
	goals_info = []
	for i, line in enumerate(text_[1:]):
		words = line.split()
		user = '_'.join(words[:-1])
		mins = words[-1][:-1]
		if i < n:
			c = c1
		else:
			c = c2
		goals_info.append(
			[int(mins), user, c]
		)
		check_user_in_system(user, team=c, total_goals_users=total_goals_users)
		add_goal_user(
			user=user,
			min_=int(mins),
			total_goals_users=total_goals_users
		)
	goals_info.sort(key=lambda x: x[0])
	if goals_info:
		add_goal_score_in_system(goals_info, total_goals_team, total_goals_users)


def handler_command(line: str, total_goals_team: dict, total_goals_users: dict):
	if line.startswith('Total goals for'):
		team_name = line[len('total goals for '):]
		words = team_name.split()
		team_name = '_'.join(words)
		if team_name in total_goals_team:
			return total_goals_team[team_name]['goals']
		return 0
	if line.startswith('Mean goals per game for'):
		team_name = line[len('mean goals per game for '):]
		words = team_name.split()
		team_name = '_'.join(words)
		return total_goals_team[team_name]['goals'] / total_goals_team[team_name]['games']
	if line.startswith('Total goals by'):
		user_name = line[len('total goals by '):]
		words = user_name.split()
		user_name = '_'.join(words)
		if user_name in total_goals_users:
			return total_goals_users[user_name]['goals']
		return 0
	if line.startswith('Mean goals per game by'):
		user_name = line[len('mean goals per game by '):]
		words = user_name.split()
		user_name = '_'.join(words)
		team_name = total_goals_users[user_name]['team']
		return total_goals_users[user_name]['goals'] / total_goals_team[team_name]['games']
	if line.startswith('Goals on minute'):
		min_and_user_name = line[len('goals on minute '):]
		words = min_and_user_name.split('by')
		user_name = '_'.join(words[1].split())
		min_ = int(words[0])
		if user_name in total_goals_users:
			return total_goals_users[user_name]['goals_detail'][min_]
		return 0
	if line.startswith('Goals on first'):
		min_and_user_name = line[len('goals on first '):]
		words = min_and_user_name.split('minutes by')
		user_name = '_'.join(words[1].split())
		min_ = int(words[0])
		if user_name in total_goals_users:
			return sum(total_goals_users[user_name]['goals_detail'][:min_+1])
		return 0
	if line.startswith('Goals on last'):
		min_and_user_name = line[len('goals on last '):]
		words = min_and_user_name.split('minutes by')
		user_name = '_'.join(words[1].split())
		min_ = int(words[0])
		if user_name in total_goals_users:
			return sum(total_goals_users[user_name]['goals_detail'][91-min_:])
		return 0
	if line.startswith('Score opens by'):
		user_or_team_name = line[len('score opens by '):]
		words = user_or_team_name.split()
		user_or_team_name = '_'.join(words)
		if user_or_team_name in total_goals_team:
			return total_goals_team[user_or_team_name]['score']
		if user_or_team_name in total_goals_users:
			return total_goals_users[user_or_team_name]['score']
		return 0


def solution(text) -> list[int]:
	total_goals_team = dict()
	total_goals_users = dict()
	lines = text.split('\n')
	j = None
	ans = []
	for i, line in enumerate(lines):
		if not line:
			continue
		if any(line.startswith(key_word) for key_word in [
			'Total', 'Mean', 'Goals', 'Score'
		]):
			res_ = handler_command(line, total_goals_team, total_goals_users)
			ans.append(res_)
		else:
			if j is None or i >= j:
				words = line.split()
				n, m = list(map(int, words[-1].split(':')))
				j = i + n + m + 1
				add_new_match_in_system(lines[i: j], total_goals_team, total_goals_users)
	return ans


def run_tests():
	test1 = solution(
		text='''"Juventus" - "Milan" 3:1
Inzaghi 45'
Del Piero 67'
Del Piero 90'
Shevchenko 34'
Total goals for "Juventus"
Total goals by Pagliuca
Mean goals per game by Inzaghi
"Juventus" - "Lazio" 0:0
Mean goals per game by Inzaghi
Mean goals per game by Shevchenko
Score opens by Inzaghi'''
	)
	assert test1 == [
		3,
		0,
		1.0,
		0.5,
		1.0,
		0,
	], test1

	test2 = solution(
		text='Total goals by Arshavin'
	)
	assert test2 == [0], test2


if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	with open('input.txt', 'r') as f:
		text = f.read()
	ans = solution(text)
	print('\n'.join(str(x) for x in ans))
