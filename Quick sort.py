def sort(array, low, high):
    # en array kan hålla mer en ett värde
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quick(array, low, high):
    if low < high:

        pi = sort(array, low, high)

        quick(array, low, pi - 1)

        quick(array, pi + 1, high)


tal = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted")
print(tal)

size = len(tal)

quick(tal, 0, size - 1)

print("Sorted")
print(tal)
