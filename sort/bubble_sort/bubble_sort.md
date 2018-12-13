# 冒泡排序 bubble sort

## 0、算法说明

- 稳定排序

- 时间复杂度：![O(n^{2})](https://wikimedia.org/api/rest_v1/media/math/render/svg/6cd9594a16cb898b8f2a2dff9227a385ec183392)

**描述：**

它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。

## 1、算法思想

1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3. 针对所有的元素重复以上的步骤，除了最后一个。
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

![](./Bubble_sort_animation.gif)

## 2、代码

```python
def bubble_sort(my_list):
    for i in range(0, len(my_list)-1):
        for j in range(0, len(my_list)-1-i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list


my_list = [0, 3, 2, 4, 6, 7, 5, 9, 8, 1]
print(bubble_sort(my_list))
```

## 3、代码优化

#### 1、优化外层循环

若在某一趟排序中未发现元素位置的交换，则说明列表已经有序，冒泡排序过程可在此趟排序后终止。

每次循环中引入标志位flag，设置初值为flase，若发生交换则列表此时仍然无序，置flag = true ,否则为有序，停止循环

**代码：**

```python
def bubble_sort(my_list):
    for i in range(0, len(my_list)-1):
        flag = False
        for j in range(0, len(my_list)-1-i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                flag = True
        if not flag:
            return my_list
    return my_list


my_list = [0, 3, 2, 4, 6, 7, 5, 9, 8, 1]
print(bubble_sort(my_list))
```

#### 2、优化内层循环

在每趟扫描中，记住最后一次交换发生的位置p，（该位置之后的相邻记录均已有序）。下一趟排序开始时，R[1..p-1]是无序区，R[p..n]是有序区。这样，一趟排序可能使当前无序区扩充多个记录，因此记住最后一次交换发生的位置p，从而减少排序的趟数。

**代码：**

```python
def bubble_sort(my_list):
    p = len(my_list)-1
    for i in range(0, len(my_list)-1):
        flag = False
        for j in range(0, p):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                flag = True
                p = j
        if not flag:
            return my_list
    return my_list


my_list = [0, 3, 2, 4, 6, 7, 5, 9, 8, 1]
print(bubble_sort(my_list))
```

