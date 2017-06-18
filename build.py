def solution(dic1, key1):
    count = 0
    for key in dic1.keys():
        if key == key1:
            count += 1
        if count == 0:
            return False
        else:
            return True
