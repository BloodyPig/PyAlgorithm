# 斐波那契查找

## 0、算法说明

裴波那契数列是一串按照F(0)=1，F(1)=1, F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）这一条件递增的一串数字：

```
1、1、2、3、5、8、13、21 ... ...
```

两个相邻项的比值会逐渐逼近**0.618** —— **黄金分割比值**。

二分查找， 插值查找和裴波那契查找的基础其实都是：对数组进行分割， 只是各自的标准不同：二分是从数组的一半分， 插值是按预测的位置分， 而裴波那契是按它数列的数值分。

**假设有待查找数组array[n]和斐波那契数组F[k],并且n满足n>=F[k]-1&&n < F[k+1]-1，则它的第一个拆分点mid=F[k]-1**

**算法复杂度：**O(log N)

**算法优势：**

- 平均性能比二分查找好

- 它还有一个优点就是分割时候只需进行加减运算（二分和插值都有乘/除）

## 1、算法思想

算法涉及到三个数组：

- **待查数组**

  必须是顺序存储，必须有序，不考虑元素重复

- **斐波那契数组**

  数组的最大值刚好大于等于待查数组的长度

- **填充数组**

  填充数组的长度是斐波那契数

  如果待查数组长度是斐波那契数列中某个值，则填充数组就是待查数组本身

**举例：**

待查数组：长度为**9** 
$$
list = [1, 3, 6, 7, 9, 15, 89, 116, 666]
$$
则斐波那契数组：数组最大元素 **13 > 9**
$$
fibonacci = [1, 1, 2, 3, 5, 8, 13]
$$
则填充数组：
$$
fill\_arry = [1, 3, 6, 7, 9, 15, 89, 116, 666, 666, 666, 666, 666]
$$
**算法核心**

与二分查找和插值查找一样，是mid 标志位的值

斐波那契数列的特点就是当前元素是之前两个元素的和，利用这一特点，

斐波那契查找算法的算法循环中，填充数组不断被分割为f(n - 1) 和 f(n - 2)两部分，

其两部分的长度同样是斐波那契数，与二分查找中数组不断被平均分是一个道理。

## 2、代码

```python
def fibonacci_search(element, my_list):
    # 创建一个斐波那契数列，列表的最大元素刚好 >= 待查数组的长度
    fibonacci = []
    fibonacci.append(1)
    fibonacci.append(1)
    num = 2
    while max(fibonacci) < len(my_list):
        fibonacci.append(fibonacci[num - 1] + fibonacci[num - 2])
        num += 1

    # 创建填充数组,填充数组长度等于斐波那契数列的最大值
    # 使用浅拷贝初始化填充数组，不改变原来的列表
    fill_arry = my_list[:]
    for num in range(max(fibonacci) - len(my_list)):
        fill_arry.append(my_list[len(my_list) - 1])

    low = 0
    high = len(my_list) - 1
    k = len(fibonacci) - 1
    while low <= high:
        mid = low + fibonacci[k - 1] - 1
        if element < fill_arry[mid]:
            high = mid - 1
            k -= 1
        elif element > fill_arry[mid]:
            low = mid + 1
            k -= 2
        else:
            if mid > high:
                return high
            else:
                return mid

    return None


my_list = [1, 3, 6, 7, 9, 15, 89, 116, 666]
element = 16
element_pos = fibonacci_search(element, my_list)
print(element_pos)
```

