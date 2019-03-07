# 对list中的两段有序序列[l,m)[m,h)合并
def merge(L, l, m, h):
    tmp = []
    i, j = l, m
    while i < m and j < h:
        if L[i] <= L[j]:
            tmp.append(L[i])
            i += 1
        else:
            tmp.append(L[j])
            j += 1
    if i == m:
        tmp += L[j:h]
    else:
        tmp += L[i:m]
    L[l:h] = tmp[:]


# 迭代每次合并的最小元素为1 2 4 8...个
def merge_sort(L):
    size = 1
    while size < len(L):
        l = 0
        while l+size < len(L):
            m = l+size
            h = m+size
            if h > len(L):
                h = len(L)
            merge(L, l, m, h)
            l = h
        size *= 2
    return L


my_list = [0, 3, 2, 4, 6, 7, 5, 9, 8, 1]
print(merge_sort(my_list))
