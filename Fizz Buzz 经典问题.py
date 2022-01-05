def fizz_buzz(num):
      list=[]
      if num is None:
            raise TypeError('num cannot be None')
      if num < 1:
            raise ValueError('num cannot be less than one')
      for i in range(1,num+1):
            if i%3==0 and i%5==0:
                list.append('FizzBuzz')
            elif i%3==0:
                list.append('Fizz')
            elif i%5==0:
                list.append('Buzz')
            elif i%3!=0 and i%5!=0:
                list.append(str(i))
      print(list)
a=10
fizz_buzz(a)
