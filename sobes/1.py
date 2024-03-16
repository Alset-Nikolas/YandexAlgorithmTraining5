def solution(text: str):
	text = text + ' '
	max_len_word = 0
	words = []
	i = 0
	for j in range(len(text)):
		t = text[j]
		if t == ' ':
			new_w = text[i:j]
			if new_w:
				words.append(new_w)
				max_len_word = max(max_len_word, len(new_w))
			i = j + 1
		elif t == ',' and text[j - 1] == ' ':
			last_w = words.pop()
			words.append(last_w + ',')
			i = j + 1
		elif t == ',':
			new_w = text[i:j + 1]
			if new_w:
				words.append(new_w)
				max_len_word = max(max_len_word, len(new_w) - 1)
			i = j + 1

	result = []
	line = words[0]
	for w in words[1:]:
		if len(line + ' ' + w) <= max_len_word * 3:
			line = line + ' ' + w
		else:
			result.append(line)
			line = w
	result.append(line)
	return '\n'.join(result)


if __name__ == '__main__':
	text = input()
	res = solution(text)
	print(res)
