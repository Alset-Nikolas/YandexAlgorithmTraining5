from collections import deque


class DequeMin:
	def __init__(self):
		self.deq = deque()
		self.deq_min = deque()

	def add(self, x):
		self.deq.append(x)
		if len(self.deq_min) == 0:
			self.deq_min.append(x)
			return
		last_item = self.deq_min.pop()
		while last_item > x and len(self.deq_min) > 0:
			last_item = self.deq_min.pop()
		if last_item <= x:
			self.deq_min.append(last_item)
		self.deq_min.append(x)

	def pop(self):
		if len(self.deq) <= 0:
			raise ValueError('len <= 0')
		x = self.deq.popleft()
		x_min = self.deq_min.popleft()
		if x != x_min:
			self.deq_min.appendleft(x_min)

	def get_min(self):
		x_min = self.deq_min.popleft()
		self.deq_min.appendleft(x_min)
		return x_min

	def __len__(self):
		return len(self.deq)


def solution(mass, k):
	q = DequeMin()
	res = 0
	for x in mass:
		if len(q) > k:
			q.pop()
		q.add(x)
		x_min = q.get_min()
		res = max(res, x - x_min)
	return res


def run_tests():
	assert solution(k=2, mass=[1, 2, 3, 4, 5]) == 2, solution(k=2, mass=[1, 2, 3, 4, 5])
	assert solution(mass=[5, 4, 3, 2, 1], k=2) == 0


if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	N, K = list(map(int, input().split()))
	mass = list(map(int, input().split()))
	result = solution(mass, k=K)
	print(result)
