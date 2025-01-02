from typing import List


def kadanes_algorithms(array: List[int]) -> List[int]:
    max_sum = -float("inf")
    current_sum = 0
    for num in array:
        current_sum += num
        max_sum = max(current_sum, max_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum




if __name__ == '__main__':
    kadanes_algorithms([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4])
