word = input()
arr = [0 for i in range(26)]

for alpha in word:
    arr[ord(alpha) - 97] += 1

num = max(arr)

alp = chr(arr.index(num)+97)

print(alp)
print(num)
