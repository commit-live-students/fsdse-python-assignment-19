def solution(dic1, key1):
    alert = 0
    for keys_check in dic1.keys():
        if key1 == keys_check:
            alert +=1

    if alert == 0:
        return False
    else:
        return True
