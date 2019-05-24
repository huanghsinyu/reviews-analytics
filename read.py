data = []
c = 0
with open('reviews.txt', 'r')as f:
	for line in f:
		data.append(line)
		c = c + 1
		if c % 100000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料！')

sl = 0
for line in data:
	sl = sl + len(line)
print('平均長度為', sl/len(data),'！')

new = []
for line in data:
	if len(line) < 100:
		new.append(line)
print('一共有', len(new), '筆資料長度小於100')
print(new[0])