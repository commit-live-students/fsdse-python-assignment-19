def solution(dic1, key1):
    key = key1
    my_dict = dic1
    for k, v in my_dict.items() :
         if key == k :
            return True
         else :
            return False



dict_available = {"arg1":3,"arg2":4}

print solution(dict_available ,"arg3")

print solution(dict_available ,"arg1")
