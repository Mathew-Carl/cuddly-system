#堆排序 O(nlogn)
import random
def sift(li, low, high):#low根节点的元素的位置, high最后一个元素的位置, sift调整
    i = low
    j = 2 * i + 1#左孩子结点
    tmp = li[low]#储存堆顶
    while j <= high:#j存在
        if j + 1 <= high and li[j+1] > li[j]:#右孩子存在且大
            j = j + 1#指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j#向下看一层
            j = 2  * i + 1
        else:#tmp更大,tmp放到i
            break
    li[i] = tmp#放到叶子结点,次级都比tmp大
    
def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2,-1,-1):
        sift(li, i, n-1)#建堆完成
    for i in range(n-1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)
    return li
li = list(range(10))
random.shuffle(li)
print(heap_sort(li))