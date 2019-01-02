def selection_sort(my_list):
    for i in range(len(my_list)):
        j = i+1
        while j < len(my_list):
            if my_list[j] < my_list[i]:
                my_list[j], my_list[i] = my_list[i], my_list[j]
            j += 1
    return my_list


my_list = [0, 3, 2, 4, 6, 7, 5, 9, 8, 1]
print(selection_sort(my_list))
