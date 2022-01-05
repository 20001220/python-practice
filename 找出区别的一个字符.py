class Solution(object):

    def find_diff(self, str1, str2):
        if str1 is None or str2 is None:
            raise TypeError('str1 or str2 cannot be None')
        lenth1 = len(str1)
        lenth2 = len(str2)
        temp1 = ""
        temp2 = ""
        if lenth1 > lenth2:
            temp1 += str1
            temp2 += str2
        else:
            temp1 += str2
            temp2 += str1
        temp1 = sorted(temp1)
        temp2 = sorted(temp2)
        lenth = len(temp2)
        for i in range(lenth):
            if temp1[i] != temp2[i]:
                return temp1[i]
        return temp1[lenth]
                                
