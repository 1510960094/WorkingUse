class Solution:
    def find(self,arry,target):
        if arry == []:
            return False
        rawnum = len(arry)
        colnum = len(arry[0])
        if type(target) == float and type(array[0][0]) == int:
            if int(target) == target:
                return False
        elif type(target) == int and type(arry[0][0]) == float:
            target = float(int)
        elif type(target) != type(arry[0][0]):
            return False
        i = column -1
        j = 0
        while i >=0 and j<rawnum:
            if array[j][i] < target:
                j+=1
            elif array[j][i] < target:
                j-=1
            else:
                return True
        return False
