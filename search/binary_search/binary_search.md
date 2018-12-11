# 二分查找

## 0、算法说明

输入是一个有序的元素列表

如果要查找的元素包含在列表中，二分查找返回其位置；否则返回 NULL

算法复杂度：O(log^N)

## 1、算法思想

1. 设置列表起始、结束、中点标志 low、high、mid

   ​	
   $$
   mid = low + \frac{(high - low)}{2}
   $$

2. 执行循环，循环中执行下列判断：

   a. element > mid 

   ​	将mid 置为 low

   b. element < mid

   ​	将mid 置为 high

   c. element = mid

   ​	返回mid 的下标

   循环进行条件是 low <= high (一定能在不断缩小的范围中找到目标元素) 

## 2、实现代码

```python
def binary_search(my_list, element):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if element < my_list[mid]:
            high = mid - 1
        elif element > my_list[mid]:
            low = mid + 1
        elif element == my_list[mid]:
            return mid

    return None


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 8
element_pos = binary_search(my_list, element)
print(element_pos)
```

## 3、算法优化

#### 1、有序列表经过循环右移

$$
list[1,2,3,4,5,6,7,8,9,10] —> list[5,6,7,8,9,10,1,2,3,4]
$$

**优化思想：**

- 每次循环都使用mid 与 low 做比较，总能确定某一边的空间是有序的
- 只对有序的一边做分析，看是否包含待查元素element，并改变low、high标志位

**代码：**

```python
def binary_search(my_list, element):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if element == my_list[mid]:
            return mid
        if my_list[low] < my_list[mid]:
            if element > my_list[mid] or element < my_list[low]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if element > my_list[high] or element < my_list[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return None


my_list = [5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4]
element = 9
element_pos = binary_search(my_list, element)
print(element_pos)
```

#### 2、有序列表中元素不唯一

小范围内的多重复数据

$$
list[1,1,1,2,2,3,3,4,5,5,6,6,9]
$$
**优化思想：**

- 先检查列表中是否存在该元素，获得其位置
- 统计该元素的出现次数，往前推移其起始位置，也可以使用**计数排序**对整个列表预处理
- 得到元素出现的位置范围

**代码：**

```python
def binary_search(my_list, element):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if element < my_list[mid]:
            high = mid - 1
        elif element > my_list[mid]:
            low = mid + 1
        elif element == my_list[mid]:
            return mid

    return None


def count_sort(my_list):
    new_list = [0 for num in range(max(my_list) + 1)]
    for number in my_list:
        new_list[number] += 1
    return new_list


my_list = [1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 9]
new_list = count_sort(my_list)
element = 3
element_pos = binary_search(my_list, element)
if element_pos:
    if new_list[element] != 1:
        print(str(element_pos + 1 - new_list[element]) + "-" + str(element_pos))
    else:
        print(element_pos)
else:
    print(element_pos)
```
