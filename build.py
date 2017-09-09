def solution(dic1, key1):
    return key1 in dic1

if __name__ == "__main__":
    print solution ({10:1, 20:2, 30:3}, 10)
    print solution ({10:1, 20:2, 30:3}, 50)
