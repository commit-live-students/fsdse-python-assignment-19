def solution(dic1, key1):
    for k in dic1.keys():
        if k==key1:
            return True
        else:
            return False
print solution({'a':1,'b':2},'c')                
