def partition(array, left, right):
    # Choose the rightmost element as pivot
    pivot = array[right]

    # Pointer for greater element
    i = left
    j = right - 1
    while i < j:
        while i < right and array[i] < pivot:
            i += 1
        while j > left and array[j] > pivot:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]
    if  array[i]>pivot:
        array[i], array[right] = array[right], array[i]

    return i


def quick_sort(array, left, right):
    if left < right:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, left, right)

        # Recursive call on the left of pivot
        quick_sort(array, left, pi - 1)

        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, right)


# Driver code
array = [10, 7, 8, 9, 1, 5]
quick_sort(array, 0, len(array) - 1)

print(f'Sorted array: {array}')
