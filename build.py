def solution(dic1, key1):
    k = dic1.keys()
    if key1 in k:
        return True
    else:
        return False

print(solution({'a':1,'b':2},'s'))
