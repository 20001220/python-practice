word=input()
d={}
for i in word:
      d[i]=d.get(i,0)+1
ls=list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
print(ls[0][0])
print(ls[0][1])
