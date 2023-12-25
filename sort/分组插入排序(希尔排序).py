#时间复杂度取决于gap的选择,稳定
def insert_sort(li, gap):
    for i in range(gap,len(li)):
        temp = li[i]
        j = i - gap#手中牌
        while li[j] > temp and j >= 0:
            li[j+gap] = li[j]#往右移
            j -= gap
        li[j+1] = temp
        
def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2
        