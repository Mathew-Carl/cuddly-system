#LOWB三人组,都是原地排序,都是O(n2)
    #冒泡排序 O(n2) (原地排序,不生成新列表)
def bubble_sort(li):
    for i in range(len(li)-1):
        exchance = False#标志
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchance = True
        if not exchance:#简化
            return li
    #直接选择排序
def select_sort_simple(li):#O(n2)
    li_new = []
    for i in range(li):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new
#缺陷生成两个列表占用内存大

def select_sort(li):#O(n2)
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1 , len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
    return li
    #直接插入排序O(n2)
def insert_sort(li):
    for i in range(1,len(li)):
        temp = li[i]
        j = i - 1#手中牌
        while li[j] > temp and j >= 0:
            li[j+1] = li[j]#往右移
            j -= 1
        li[j+1] = temp
        
        
            
        
        
        