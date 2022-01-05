def check_s(s):
    return s == '2020'
fo=open("test.txt","w")
fo.write("220000"+"\n"+"000000"+"\n"+"002202"+"\n"+"000000"+"\n"+"000022"+"\n"+"002020")
fo.close()

data = []
# test.txt
# 220000
# 000000
# 002202
# 000000
# 000022
# 002020

# 读取数据
with open('test.txt', mode='r', encoding='utf-8') as fp:
    for line in fp:
        line = list(line.strip())
        data.append(line)

print(data)
# 读出来的全是字符串
# [['2', '2', '0', '0', '0', '0'], 
#  ['0', '0', '0', '0', '0', '0'], 
#  ['0', '0', '2', '2', '0', '2'], 
#  ['0', '0', '0', '0', '0', '0'], 
#  ['0', '0', '0', '0', '2', '2'], 
#  ['0', '0', '2', '0', '2', '0']]

m, n = len(data), len(data[0])
count = 0

for i in range(m):
    for j in range(n):
        # 行
        if i + 3 < n and check_s(data[i][j] + data[i+1][j] + data[i+2][j] + data[i+3][j]):
            count += 1
        # 列
        if j + 3 < m and check_s(data[i][j] + data[i][j+1] + data[i][j+2] + data[i][j+3]):
            count += 1
        # 斜
        if i + 3 < n and j + 3 < m and check_s(data[i][j] + data[i+1][j+1] + data[i+2][j+2] + data[i+3][j+3]):
            count += 1

print(count)
# 5
