# 3. longest substring without repeating characters (LeetCode) [medium]
def length_of_longest_substring(input_string: str) -> int:
    start_index = 0
    end_index = 0
    char_count = {}
    max_length = 0

    while end_index < len(input_string):
        current_char = input_string[end_index]
        if current_char in char_count:
            char_count[current_char] += 1
        else:
            char_count[current_char] = 1

        while char_count[current_char] > 1:
            start_char = input_string[start_index]
            char_count[start_char] -= 1
            start_index += 1

        max_length = max(max_length, end_index - start_index + 1)
        end_index += 1

    return max_length

if __name__ == '__main__':
    test_case1="abccc"
    length_of_longest_substring("pwwkew")





