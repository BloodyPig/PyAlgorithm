# 插值查找

## 0、算法说明

在一个数据分布均匀的列表中，寻找某个元素

```
list[0,1,2,.....9999,10000] find 9 or 9837
```

预测其位置而不是每次像二分查找一样从中间开始划分，会使得查找效率很高

适用场景：

- 数据不仅是已被排好序的，而且呈现均匀分布特征
- 每一次对数据的访问与通常的指令相比，费用都是相当昂贵的。例如，待查找的表一定是在磁盘而非内存中，因而每一次比较都要进行磁盘访问

算法复杂度：O(log N)

## 1、算法思想：

根据element的值对查找范围进行更加精确的划分，表现为改变二分查找中 mid 值的设定

插值查找算法与二分查找基本一致，不同点在于：

- **mid 计算公式**

$$
mid = low + (high - low)*\frac{(element - list[low])}{(list[high] - list[low])}
$$

​	**解释说明：**

​	将比例系数 1/2 替换为元素在寻找范围中相对位置

1.  ***list[low] != list[high]***

- **循环条件**

$$
list[low] != list[high]  \&  list[low] <= element  \&  list[high] >= element
$$

​	**解释说明：**

1. 保证了mid 计算公式中不出现分母为0的情况

2.  ***list[low] <= element <= list[high]***

   保证 element 时钟在我们确定的范围内

3. **为什么不使用 low<=high**

   在mid 的计算公式中，key - list[low] 不总是正值，若查找的元素element 不在列表中，会使的算法陷入死循环。

   在[这一篇博客](https://www.cnblogs.com/penghuwan/p/8021809.html)中有更加详细的图文解释。

## 2、代码

``` python
def binary_search(my_list, element):
    low = 0
    high = len(my_list) - 1
    counter = 0

    while my_list[low] != my_list[high] and my_list[low] <= element and my_list[high] >= element:
        counter += 1
        mid = low + (high - low) * (element - my_list[low]) // (my_list[high] - my_list[low])
        # mid = low + (element - my_list[low]) // (my_list[high] - my_list[low]) * (high - low)

        if element < my_list[mid]:
            high = mid - 1
        elif element > my_list[mid]:
            low = mid + 1
        elif element == my_list[mid]:
            print(counter)
            return mid

    return None


my_list = [num for num in range(1000)]
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 555
element_pos = binary_search(my_list, element)
print(element_pos)
```

**特殊说明：**

代码段1：

```python
mid = low + (high - low) * (element - my_list[low]) // (my_list[high] - my_list[low])
```

代码段2：

```python
mid = low + (element - my_list[low]) // (my_list[high] - my_list[low]) * (high - low)
```

代码段1 和代码段2 逻辑相同 但是python 执行结果不同，是运算顺序导致的,其中代码段1 是正确代码

在python 中 “//” 表示除法并对结果向下取整，代码二先执行除法，导致计算结果永远等价于

```
mid = low + 0
```

代码段1 和以下两段代码具有相同效果

```
mid = int(low + (high - low) * (element - my_list[low]) / (my_list[high] - my_list[low]))
```

```
mid = int(low + (element - my_list[low]) / (my_list[high] - my_list[low]) * (high - low))
```

即先对所有数据进行浮点运算，最后统一转换

## 3、算法优化

插值查找的算法优化情况与二分查找基本一致