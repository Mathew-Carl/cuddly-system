#默认已排序从小到大,

#顺序查找 O(n)
def linear_search(li,val):
    for ind , v in enumerate(li):
        if v == val:
            return ind
    else:
        return None
    return
#二分查找 O(logn)
def binary_search(li , val):
    left = 0
    right = len(li)-1
    while left <= right:
        mid = (left + right)//2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid -1
        else:# li[mid] < val:
            left = mid + 1
    else:
        return None