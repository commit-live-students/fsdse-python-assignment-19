def solution(d1,Key1):
    for key in d1:
        if key == Key1:
            return True
    else:
        return False

print solution({'abc':20,'efg':10},'efg')
