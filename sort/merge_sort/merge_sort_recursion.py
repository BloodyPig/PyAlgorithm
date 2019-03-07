# 归并排序的递归描述
def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result


def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    mid = len(my_list)//2
    left = my_list[:mid]
    right = my_list[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


my_list = [0, 3, 2, 4, 6, 7, 5, 9, 8, 1]
print(merge_sort(my_list))
