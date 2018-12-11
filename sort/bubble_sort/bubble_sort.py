def bubble_sort(my_list):
    for i in range(0, len(my_list)-1):
        for j in range(0, len(my_list)-1-i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list


my_list = [0, 3, 2, 4, 6, 7, 5, 9, 8, 1]
print(bubble_sort(my_list))
