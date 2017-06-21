# Given key already exists in a dictionary
####Doing

# Given key already exists in a dictionary

x = {"a": 10, "b": 20, "c": 30, "d": 40}

def solution(a, b):
    c = 0
    for i in a.keys():
        if (i == b):
            print ("Key: ", b, " is present")
            return True
        else:
            continue
#     if (c == 0 ):
#         print ("Key: ", b, " is not present")
    return False
val = "c"
solution(x, val)
