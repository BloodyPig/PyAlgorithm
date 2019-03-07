# 归并排序 merge sort

## 0、算法说明

- 稳定排序
- 时间复杂度：![O(n\log n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/9d2320768fb54880ca4356e61f60eb02a3f9d9f1)

**描述**：

采用分治法:

- 分割：递归地把当前序列平均分割成两半。
- 集成：在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）。

## 1、算法思想

归并操作（merge），也叫归并算法，指的是将两个已经排序的序列合并成一个序列的操作。

归并排序算法依赖归并操作。

### 递归法（Top-down）

1. 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
2. 设定两个指针，最初位置分别为两个已经排序序列的起始位置
3. 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
4. 重复步骤3直到某一指针到达序列尾
5. 将另一序列剩下的所有元素直接复制到合并序列尾

### 迭代法（Bottom-up）

原理如下（假设序列共有![n](https://wikimedia.org/api/rest_v1/media/math/render/svg/a601995d55609f2d9f5e233e36fbe9ea26011b3b)个元素）：

1. 将序列每相邻两个数字进行归并操作，形成![{\displaystyle ceil(n/2)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/284284713ad8f1ba13458b896c87efc4b9b7df9c)个序列，排序后每个序列包含两/一个元素

2. 若此时序列数不是1个则将上述序列再次归并，形成![{\displaystyle ceil(n/4)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0f7b6be8e0c402e981a78d573dc3072c3d24a3c4)个序列，每个序列包含四/三个元素

3. 重复步骤2，直到所有元素排序完毕，即序列数为1



​                                                 ![](./Merge_sort_animation2.gif)

## 2、代码

**递归实现**

```python
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
```

