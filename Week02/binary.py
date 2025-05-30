import math

def binary_search(arr, target):
    lo = 0
    hi = len(arr)
    while lo < hi:
        m = math.floor(lo + (hi - lo)/2)
        print(m)
        v = arr[m]
        if v == target:
            return True
        if v > target:
            hi = m
        else:
            lo = m + 1

    return False

arr = [1,2,3,4,6,12,34,55,67,87,98,100]

res = binary_search(arr,4)

print(res)



