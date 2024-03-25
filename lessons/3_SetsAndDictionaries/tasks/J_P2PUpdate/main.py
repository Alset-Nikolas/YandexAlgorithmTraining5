import math


class Request:
	def __init__(self, from_, to_, packet_id):
		self.from_ = from_
		self.to_ = to_
		self.packet_id = packet_id

	def __str__(self):
		return 'Request: from_ {} to_ {} (packet_id: {})'.format(self.from_.id_, self.to_.id_, self.packet_id)


class Gadget:
	def __init__(self, n, id_):
		self.downloads = set()
		self.id_ = id_
		self.value = {
			ni: 0 for ni in range(n) if ni != id_
		}

	def __str__(self):
		return 'Gadget {}. download {}. {} '.format(self.id_, self.downloads, self.value)


def get_rare_package(gadget: Gadget, packets: list[set]):
	rare_package = None
	min_len = math.inf
	for packet_id, packet in enumerate(packets):
		if packet_id in gadget.downloads:
			continue
		if len(packet) < min_len:
			min_len = len(packet)
			rare_package = packet_id
		elif len(packet) == min_len and rare_package > packet_id:
			rare_package = packet_id
	return rare_package


def get_gadget_to_send_packet(gadgets: list[Gadget], packets: list, rare_package_id: int):
	min_download = math.inf
	gadget_send = None
	for gadget_id in packets[rare_package_id]:
		gadget = gadgets[gadget_id]
		if len(gadget.downloads) < min_download:
			min_download = len(gadget.downloads)
			gadget_send = gadget
		elif len(gadget.downloads) == min_download and len(gadget_send.downloads) > len(gadget.downloads):
			min_download = len(gadget.downloads)
			gadget_send = gadget
		elif len(gadget.downloads) == min_download and len(gadget_send.downloads) == len(gadget.downloads) and gadget_send.id_ > gadget_id:
			min_download = len(gadget.downloads)
			gadget_send = gadget
	return gadget_send


def choose_valid_request(gadgets: list[Gadget], var_requests: list[Request], gadget_to_id: int):
	max_ = -math.inf
	request = None
	for req in var_requests:
		info_ = gadgets[req.to_.id_].value
		if info_[req.from_.id_] > max_:
			request = req
			max_ = info_[req.from_.id_]
		elif info_[req.from_.id_] == max_ and len(req.from_.downloads) < len(request.from_.downloads):
			request = req
			max_ = info_[req.from_.id_]
		elif info_[req.from_.id_] == max_ and len(req.from_.downloads) == len(request.from_.downloads) and request.from_.id_ > req.from_.id_ :
			request = req
			max_ = info_[req.from_.id_]
	return request


def gadgets_send_response(gadgets: list[Gadget], packets: list, requests: dict, answer: list[int]):
	valid_reqs = []
	for gadget_id, var_requests in requests.items():
		if not var_requests:
			continue
		valid_req: Request = choose_valid_request(
			gadgets=gadgets,
			var_requests=var_requests,
			gadget_to_id=gadget_id
		)
		valid_reqs.append(valid_req)

	for valid_req in valid_reqs:
		gadgets[valid_req.from_.id_].value[valid_req.to_.id_] += 1
		gadgets[valid_req.from_.id_].downloads.add(valid_req.packet_id)
		packets[valid_req.packet_id].add(valid_req.from_.id_)


def gadgets_create_request(gadgets: list[Gadget], packets: list, requests: dict, answer: list[int]):
	for gadget in gadgets:
		if gadget.id_ == 0:
			continue
		rare_package_id: int = get_rare_package(
			gadget=gadget,
			packets=packets,
		)
		if rare_package_id is None:
			continue
		gadget_send = get_gadget_to_send_packet(
			gadgets=gadgets,
			packets=packets,
			rare_package_id=rare_package_id,
		)
		new_request = Request(
			from_=gadget,
			to_=gadget_send,
			packet_id=rare_package_id,
		)
		requests[gadget_send.id_].append(
			new_request
		)


def add_answer(gadgets: list[Gadget], packets: list, answer: list[int]):
	for g in gadgets:
		if len(g.downloads) == len(packets):
			continue
		answer[g.id_] += 1


def next_time_slot(gadgets: list[Gadget], packets: list, requests: dict, answer: list[int]):
	add_answer(gadgets, packets, answer)
	gadgets_create_request(gadgets, packets, requests, answer)
	gadgets_send_response(gadgets, packets, requests, answer)



def solution(n, k) -> list[int]:
	gadgets = [
		Gadget(
			n=n,
			id_=i,
		)
		for i in range(n)
	]

	gadgets[0].downloads = set(range(k))
	packets = [
		{0} for ki in range(k)
	]

	answer = [
		0 for ni in range(n)
	]
	while any(len(packet) != n for packet in packets):
		requests = {
			i: [] for i in range(n)
		}
		next_time_slot(gadgets, packets, requests, answer)
	print(*answer[1:])


def run_tests():
	pass


if __name__ == '__main__':
	is_debug = True
	if is_debug:
		run_tests()
	n, k = list(map(int, input().split()))
	ans = solution(n, k)
