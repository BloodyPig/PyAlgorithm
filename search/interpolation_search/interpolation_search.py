def binary_search(my_list, element):
    low = 0
    high = len(my_list) - 1
    counter = 0

    while my_list[low] != my_list[high] and my_list[low] <= element and my_list[high] >= element:
        counter += 1
        mid = low + (high - low) * (element - my_list[low]) // (my_list[high] - my_list[low])
        # mid = low + (element - my_list[low]) // (my_list[high] - my_list[low]) * (high - low)
        # mid = int(low + (high - low) * (element - my_list[low]) / (my_list[high] - my_list[low]))
        # mid = int(low + (element - my_list[low]) / (my_list[high] - my_list[low]) * (high - low))
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
element = 666
element_pos = binary_search(my_list, element)
print(element_pos)
