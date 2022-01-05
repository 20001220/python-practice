def compress(string):
      count=1
      b=''
      m=string
      string=string+'b'
      for i in range(len(string)):
            if i<len(string)-1:
                  if string[i]==string[i+1]:
                        count+=1
                  else:
                        if count==1:
                              b=b+string[i]
                        else:
                              b=b+string[i]+str(count)
                        count=1
      if string is None:
            print(m)
      elif len(b)<len(string):
            print(b)
      elif len(b)>=len(string):
            print(m)
a='AAABCCDDDD'
compress(a)

'''
class CompressString(object):

    def compress(self, string):
        count=1
        b=''
        m=string
        string=string+'b'
        for i in range(len(string):
            if i<len(string)-1:
                if string[i]==string[i+1]:
                    count+=1
                else:
                    if count==1:
                        b=b+string[i]
                    else:
                        b=b+string[i]+str(count)
                    count=1         
        if string is None:
            print(m)
        elif len(b)<len(string):
            print(b)
        elif len(b)>=len(string):
            print(m)

'''
