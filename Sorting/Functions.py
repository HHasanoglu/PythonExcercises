def linear_search(my_list, key):
    for i in range(0, len(my_list)):
        if my_list[i] == key:
            return i

    return -1


def linear_search_recursive(my_list, key):
    s = len(my_list)-1
    if s < 0:
        return -1
    if my_list[s] == key:
        return s
    else:
        return linear_search_recursive(my_list[:-1], key)


def binary_search(my_list, key):
    lower_bound = 0
    upper_bound = len(my_list) - 1

    while lower_bound <= upper_bound:
        mid_index = (lower_bound + upper_bound) // 2
        if key == my_list[mid_index]:
            return mid_index
        elif key < my_list[mid_index]:
            upper_bound = mid_index - 1
        else:
            lower_bound = mid_index + 1

    return -1


def bubble_sort(my_list):
    for i in range(0, len(my_list) - 1):
        for j in range(i, len(my_list) - 1 - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
