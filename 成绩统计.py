def round_2(s):
    s = str(s)
    if len(s) > 3:
        if int(s[3]) > 4:
            s = s[0] + str(int(s[1]) + 1)
        else:
            s = s[:2]
    return s


n = int(input())
jige = good = 0
for i in range(n):
    s = int(input())
    if 60 <= s < 85:
        jige += 1
    elif s >= 85:
        good += 1


r1 = round_2(((jige+good) / n) * 100)
r2 = round_2((good/n) * 100)

print(r1, '%', sep='')
print(r2, '%', sep='')
