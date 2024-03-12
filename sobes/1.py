if __name__ == '__main__':
	text = input() + ' '
	len_line = 0
	words = []
	i = 0
	for j in range(len(text)):
		t = text[j]
		if t == ' ':
			new_w = text[i:j]
			if new_w:
				words.append(new_w)
				len_line = max(len_line, len(new_w))
			i = j + 1
		elif t == ',' and text[j-1] == ' ':
			last_w = words.pop()
			words.append(last_w+',')
			i = j + 1
		elif t == ',':
			new_w = text[i:j+1]
			if new_w:
				words.append(new_w)
				len_line = max(len_line, len(new_w) - 1)
			i = j + 1

	resule = []
	line = ''
	for w in words:
		if not line:
			line = w
		else:
			if len(w) + len(line) + 1 <= len_line * 3:
				line = line + ' ' + w

			else:
				resule.append(line)
				line = w
	resule.append(line)
	print('\n'.join(resule))
