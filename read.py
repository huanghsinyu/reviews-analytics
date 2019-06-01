data = []
c = 0
with open('reviews.txt', 'r')as f:
	for line in f:
		data.append(line)
		c = c + 1
		if c % 100000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料！')

print(data[0])

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

g = [line for line in data if 'good' in line]
print(g[0])
print('一共有', len(g), '筆提到good')

#文字記數

wc = {}
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

# print(len(wc))
# print(wc['Amber'])

# for word in wc:
# 	if wc[word] > 100:
# 		print(word, wc[word])

while True:
	word = input('請問你想查什麼字？')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為：', wc[word])
	else:
		print('這個字沒出現過喔！')
print('感謝使用本功能')