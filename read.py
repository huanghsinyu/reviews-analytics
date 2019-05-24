data = []
c = 0
with open('reviews.txt', 'r')as f:
	for line in f:
		data.append(line)
		c = c + 1
		if c % 100000 == 0:
			print(len(data))

print(len(data))
print(data[0])
print('------------------------------')
print(data[1])