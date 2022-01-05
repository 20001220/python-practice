import random
List2 = []
for i in range(20):
    List2.append(random.randint(1, 50))
print(List2) # 输出随机列表
ListLen = len(List2)
for i in range(ListLen):
    r2 = List2[i:ListLen]
    # 切片获得最小值
    r2MinNum = min(r2)  
     # 找出最小值的位置
    r2MinLoaction = r2.index(r2MinNum) 
    minNum = List2[i + r2MinLoaction] # 获取rList中最小的值,防止出现相同值时,反复横跳
    del List2[i + r2MinLoaction] # 删除获取到的最小值的索引
    List2.insert(i, minNum)  # 插入到当前i的位置
print(List2)
