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
    # 使用浅拷贝初始化填充数组，不改变原来的列表值
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

    # print(my_list)
    # print(fill_arry)
    # print(fibonacci)
    return None


my_list = [1, 3, 6, 7, 9, 15, 89, 116, 666]
element = 16
element_pos = fibonacci_search(element, my_list)
print(element_pos)