def bubble_sort(my_list):
    p = len(my_list)-1
    for i in range(0, len(my_list)-1):
        flag = False
        for j in range(0, p):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                flag = True
                p = j
        if not flag:
            return my_list
    return my_list


my_list = [0, 3, 2, 4, 6, 7, 5, 9, 8, 1]
print(bubble_sort(my_list))
