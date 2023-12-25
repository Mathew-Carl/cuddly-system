#快速排序 O(nlogn)~O(n2)
def partition(li, left, right):
    temp = li[left]
    while left < right:
        while left < right and li[right] >= temp:#从右面找比temp小的数字
            right -= 1#往左走1
        li[left] = li[right]#左边的值写到右边
        while li[left] <= temp:
            left += 1
        li[right] = li[left]#把左边的值写到右边空位
    li[left] = temp#temp归位
def quick_sort(li, left, right):
    if left<right: #至少两个元素
        mid = partition(li, left, right)
        quick_sort(li, left, mid-1)
        quick_sort(li, mid+1, right)#递归
#避免特殊情况可以进行随机数抽取
            
        
        
    