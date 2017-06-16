def solution(dic1, key1):
    '''Enter Code Here'''
    a=dic1.keys()
    for i in range(0,len(a)):
        if(key1==a[i]):
            return True
    return False
