def solution(dic1, key1):
    sol = 0
    for keys_check in dic1.keys():
        if key1 == keys_check:
            sol +=1

    if sol == 0:
        return False
    else:
        return True
