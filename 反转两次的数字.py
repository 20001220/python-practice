num=eval(input('num='))
def reverse(num):
      text=str(num)
      a=text[::-1]
      return int(a)

reversed1=reverse(num)
reversed2=reverse(reversed1)
if reversed2==num:
      print(True)
else:
     print(False) 
