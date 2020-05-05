
lines = []
with open('input3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][0:5]   #字串可以當作清單,取第一個字串的前五的字為時間 [0,1,2,3,4]  不包含5
	name = s[0][5:]
	print(name)
	#print(s)

