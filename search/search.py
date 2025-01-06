def binary_search(array, target):
    l, r = 0, len(array)
    while r - l > 1:
        mid = (l + r) // 2
        if array[mid] < target:
            l = mid
        else:
            r = mid
    return array[l] == target


def binary_search_index(array, target):
    l, r = 0, len(array)
    while r - l > 1:
        mid = (l + r) // 2
        if array[mid] > target:
            r = mid
        else:
            l = mid
    return l if array[l] == target else -1


if __name__ == '__main__':
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 33
    print(binary_search_index(array, target))
