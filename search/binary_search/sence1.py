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
