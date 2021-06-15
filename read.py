data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完畢，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
print('留言的平均長度為:', sum_len/len(data))


search = []
for d in data:
    if len(d) < 100:
        search.append(d)
print('一共有', len(search),'筆留言長度小於100')
print(search[0])
print(search[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good文字')
print(good[0])