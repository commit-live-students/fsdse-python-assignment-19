def solution(dic1, key1):
    '''Enter Code Here'''
    count = 0
    for k in dic1.keys():
        if k == key1:
            count += 1
    if count == 0:
        return False
    else:
        return True
