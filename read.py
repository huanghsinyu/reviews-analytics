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
