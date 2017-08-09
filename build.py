def solution(dic1, key1):
    if key1 in dic1.keys():
        return True
    else:
        return False

dic = {1:10, 2:30}
print solution(dic,2)
