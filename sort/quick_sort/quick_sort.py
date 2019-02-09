def quick_sort(lst):
    if len(lst) <= 1:
            return lst
    less = []
    greater = []
    pivot = lst.pop()
    for item in lst:
        if item < pivot:
            less.append(item)
        else:
            greater.append(item)
    lst.append(pivot)
    return quick_sort(less) + [pivot] + quick_sort(greater)

my_list = [0, 3, 2, 4, 6, 7, 5, 9, 8, 1]
print(quick_sort(my_list))
