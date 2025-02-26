import heapq


#K th Largest element in an Array
def find_kth_largest_element(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    for num in arr[k:]:  # first 2 elements from arrays is already in heap and has been heapify
        if num > heap[0]:
            heapq.heappushpop(heap, num)
    return heap[0]  # that would be the Kth largest element


# very similar is from AlgoExpert. Find Three largest Numbers However, it is dedicated to searching module
def find_three_largest_numbers(array):
    heap = array[:3]
    heapq.heapify(heap)
    for num in array[3:]:  # first 2 elements from arrays is already in heap and has been heapify
        if num > heap[0]:
            heapq.heappushpop(heap, num)
    heap.sort()
    return heap


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    find_kth_largest_element(nums, k)
