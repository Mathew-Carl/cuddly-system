#多关键字排序 O(kn) 时间复杂度 O(k+n) 空间复杂度 效率与数字分布(位数)有关,稳定
def radix_sort(li):
    max_num = max(li)
    it = 0
    while 10 ** it <= max_num:
        bucktes = [[] for _ in range(10)]
        for var in li:
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)#buckets里的第digit个列表增加var
        li.clear()
        for buc in buckets:
            li.append(buc)
            #重新写回li
        it += 1