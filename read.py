# 寫程式碼來讀取留言檔
data = []  #建立一個空清單
count = 0 # 寫一個計數器，
with open('reviews.txt', 'r') as f:
	for line in f: #每次都是一行一行(line)讀取
		data.append(line)
		count += 1 # count = count + 1
		if count % 10000 == 0: # % 用來求餘數 1001/1001=1 1002/1000=2
		# 讀取檔案的過程中，印出len(data)才知道讀取進度
			print(len(data))
print('檔案讀取玩了，總共有 ', len(data), '筆資料')
# print(data)
# print(data[0]) # 電腦裡的數字都是從0開始 0,1,2... 索引標籤(index)
# print('---------')
# print(data[1])

# 算留言平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d) # 等於 sum_len = sum_len + len(data)
print('留言平均長度為: ', sum_len / len(data))

# 清單的篩選
new = []
for d in data: # for loop的意思就是把清單中的東西一個一個拿出來
	if len(d) <100: # 是非題(會算成True/False)
		new.append(d)
print('一共有:', len(new), '筆留言長度小於100')
print(new[0])
print('---------------')
print(new[1])

good = []
for d in data: # for loop的意思就是把清單中的東西一個一個拿出來
	if 'good' in d: # 是非題(會算成True/False)
		good.append(d)
# 'a' in 'abc' -> True
# 'e' in 'abc' -> False
print('一共有:', len(good), '筆留言提到good')
print(good[0])