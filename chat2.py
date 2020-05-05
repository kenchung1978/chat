
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			lines.append(line.strip())  #strip把換行符號去掉
	return lines

def convert(lines):
	person = None    #用none當預設值
	吳純榕_word_count = 0 
	吳純榕_sticker_count = 0
	eric_word_count = 0
	eric_sticker_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == '吳純榕':
			if s[2] == '貼圖':
				吳純榕_sticker_count += 1
			else:
				for m in s[2:]:
					吳純榕_word_count += len(m)   # += 只是把len(m)加上去吳純榕_word_count
		elif name == 'eric':
			if s[2] == '貼圖':
				eric_sticker_count += 1
			else:
				for m in s[2:]:
					eric_word_count += len(m)
	print('吳純榕說了', 吳純榕_word_count, '個字,', '傳了', 吳純榕_sticker_count, '個貼圖')
	print('eric說了', eric_word_count, '個字,', '傳了', eric_sticker_count, '個貼圖')
	

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():	
	lines = read_file('input2.txt')	
	lines = convert(lines)
	#write_file('output.txt', lines)

main()   #function 值行的進入點
