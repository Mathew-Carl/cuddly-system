#取决于数据的分布 时间复杂度, 平均O(n+k) ,最坏(O(n2+k),空间O(nk)
def bucket_sort(li, n=100, max_num=10000):
    bucket = [[] for _ in range(n)]#创建桶
    for var in li:
        i = min(var // (maxmum // n), n-1)#f放到i号桶
        bucket[i].append(var)#把var加到桶内
        #排序(冒泡颠倒)
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j -1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    sort_li = []
    for buck in buckets:
        sort_li.extend(buck)
    return sort_li