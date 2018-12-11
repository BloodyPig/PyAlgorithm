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
