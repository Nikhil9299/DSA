def linear_search(A,key):
    n = len(A)
    index = 0
    while index < n:
        if A[index] == key:
            return index
        index += 1
    return -1

A = [2,4,5,7,8,9]
found = linear_search(A,9)
print("result:",found)
