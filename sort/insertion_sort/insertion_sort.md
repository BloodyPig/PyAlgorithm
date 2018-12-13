# 插入排序 insertion sort

## 0、算法说明

- 稳定排序
- 时间复杂度![O(n^{2})](https://wikimedia.org/api/rest_v1/media/math/render/svg/6cd9594a16cb898b8f2a2dff9227a385ec183392)

##### **描述**

通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。**插入排序**在实现上，通常采用in-place排序（即只需用到![{\displaystyle O(1)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e66384bc40452c5452f33563fe0e27e803b0cc21)的额外空间的排序），因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。

![](./Insertion_sort_animation.gif)

## 1、算法思想

一般来说，**插入排序**都采用in-place在数组上实现。具体算法描述如下：

1. 从第一个元素开始，该元素可以认为已经被排序
2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
3. 如果该元素（已排序）大于新元素，将该元素移到下一位置
4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5. 将新元素插入到该位置后
6. 重复步骤2~5

## 2、代码

``` python
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while j >= 0 and temp < my_list[j]:
            my_list[j+1] = my_list[j]
            j -= 1
        my_list[j+1] = temp
    return my_list


my_list = [0, 3, 2, 4, 6, 7, 5, 9, 8, 1]
print(insertion_sort(my_list))
```