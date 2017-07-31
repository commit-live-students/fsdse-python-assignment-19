def solution(dic1, key1):
    '''Enter Code Here'''
    # print(dic1.keys())
    if(key1 in dic1.keys()):
        return True
    else:
        return False
    return False


dic1 = {10:1, 20:2, 30:3}
key1 = 10
key2 = 40
res1 = solution(dic1, key1)
res2 = solution(dic1, key2)
res1
res2
dic1={1:22,3:33}
print(solution(dic1,2))
print(solution(dic1,3))
