from enum import Enum


class Months(str, Enum):
	yanuary = 'yanuary'
	february = 'february'
	march = 'march'
	april = 'april'
	may = 'may'
	june = 'june'
	jule = 'jule'
	augest = 'augest'
	september = 'september'
	october = 'october'
	november = 'november'
	december = 'december'


MonthsDays = {
	'yanuary': 31,
	'february': 28,
	'march': 31,
	'april': 30,
	'may': 31,
	'june': 30,
	'jule': 31,
	'augest': 31,
	'september': 30,
	'october': 31,
	'november': 30,
	'december': 31,
}


class Week(str, Enum):
	monday = 'monday'
	tuesday = 'tuesday'
	wednesday = 'wednesday'
	thursday = 'thursday'
	friday = 'friday'
	saturday = 'saturday'
	sunday = 'sunday'


def get_answer(year, good_days, start_january_day):
	MANTH_ALL_DAYS = dict()
	MANTH_START_DAY = dict()
	YEAR_WEEK_DAYS = dict(list([x, 0] for x in Week))
	WEEK_CORELATION = dict(list([x, i] for i, x in enumerate(Week)))
	WEEK_CORELATION_NUMBER = dict(list([i, x] for i, x in enumerate(Week)))

	def generate_year_info():
		start_day: Week = start_january_day
		if year % 400 == 0 or year % 4 == 0 or year % 100 == 0:
			MonthsDays.february = 29
		for month in Months:
			MANTH_START_DAY[month] = start_day
			month_days = MonthsDays[month]
			MANTH_ALL_DAYS[month] = month_days
			add_all = month_days // 7
			for w in Week:
				YEAR_WEEK_DAYS[w] += add_all
			for n in range(month_days % 7):
				w: Week = WEEK_CORELATION_NUMBER[n]
				print('w', w)
				YEAR_WEEK_DAYS[w] += 1
			start_day_number = (WEEK_CORELATION[start_day] + month_days) % 7
			start_day = WEEK_CORELATION_NUMBER[start_day_number]

	def add_good_days():
		for n, month in good_days:
			start_day = MANTH_START_DAY[month]
			start_day_number = WEEK_CORELATION[start_day]
			good_day_number = (start_day_number + n) % 7
			good_day = WEEK_CORELATION_NUMBER[good_day_number]
			for w in Week:
				if w != good_day:
					YEAR_WEEK_DAYS[good_day] += 1


	generate_year_info()
	add_good_days()
	print(MANTH_ALL_DAYS)
	print()
	print(MANTH_START_DAY)
	print()
	print(YEAR_WEEK_DAYS)


def run_tests():
	pass


if __name__ == '__main__':
	is_debug = False
	if is_debug:
		run_tests()
	N = int(input())
	year = int(input())
	good_days = []
	for x in range(N):
		n, month = input().split()
		n = int(n)
		good_days.append([n, month.lower()])
	start_january_day = input()
	res = get_answer(
		year=year,
		good_days=good_days,
		start_january_day=start_january_day.lower(),
	)
	print(res)
