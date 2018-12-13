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
