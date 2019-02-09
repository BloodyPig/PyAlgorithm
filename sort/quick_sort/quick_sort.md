# 快速排序 quick sort

## 0、算法说明

- 稳定排序
- 时间复杂度![{\displaystyle \ O(n\log n)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/52de01bd6666792cf18fce11c058ae3e67694f02)

**描述**

快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为两个子序列（sub-lists）。

![](./Sorting_quicksort_anim.gif)

## 1、算法思想

步骤为：

1. 从数列中挑出一个元素，称为“基准”（pivot），
2. 重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（相同的数可以到任何一边）。在这个分割结束之后，该基准就处于数列的中间位置。这个称为**分割（partition）**操作。
3. [递归](https://zh.wikipedia.org/wiki/%E9%80%92%E5%BD%92)地（recursively）把小于基准值元素的子数列和大于基准值元素的子数列排序。

递归到最底部时，数列的大小是零或一，也就是已经排序好了。这个算法一定会结束，因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。

## 2、代码

```python
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
```

