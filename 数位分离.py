#1到2020有多少个2
count = 0

for i in range(1, 2021):
    n = i
    while n != 0:
        m = n % 10
        n = n // 10
        if m == 2:
            count += 1

print(count)
# 624
