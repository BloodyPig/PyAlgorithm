def binary_search(my_list, element):
    low = 0
    high = len(my_list) - 1
    counter = 0
    while low <= high:
        counter += 1
        mid = low + (high - low) // 2
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
element = 8
element_pos = binary_search(my_list, element)
print(element_pos)
