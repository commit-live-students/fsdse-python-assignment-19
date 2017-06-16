def solution(dic1, key1):
    '''Enter Code Here'''
    flag = 0
    for keys_check in dic1.keys():
        if key1 == keys_check:
            flag +=1

    if flag == 0:
        return False
    else:
        return True
