# 选择排序 selection sort

## 0、算法说明

- 不稳定排序
- 时间复杂度：![O(n^{2})](https://wikimedia.org/api/rest_v1/media/math/render/svg/6cd9594a16cb898b8f2a2dff9227a385ec183392)

**描述：**

首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

![](./Selection_sort_animation.gif)

## 1、算法思想

选择排序的主要优点与数据移动有关。如果某个元素位于正确的最终位置上，则它不会被移动。选择排序每次交换一对元素，它们当中至少有一个将被移到其最终位置上，因此对 n 个元素的表进行排序总共进行至多 n-1 次交换。在所有的完全依靠交换去移动元素的排序方法中，选择排序属于非常好的一种。

## 2、代码

```python
def selection_sort(my_list):
    for i in range(len(my_list)):
        j = i+1
        while j < len(my_list):
            if my_list[j] < my_list[i]:
                my_list[j], my_list[i] = my_list[i], my_list[j]
            j += 1
    return my_list


my_list = [0, 3, 2, 4, 6, 7, 5, 9, 8, 1]
print(selection_sort(my_list))
```

