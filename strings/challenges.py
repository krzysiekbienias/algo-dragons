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


# 520. Detect capital
def detect_capital(word: str) -> bool:
    if word.isupper():
        return True

    if word.islower():
        return True

    if word[0].isupper and word[1:].islower():
        return True

    else:
        return False


# 389 Find the difference

def find_difference(word1: str, word2: str) -> str:
    #this is a difference of characters in words
    word_dict = dict()
    for i in range(len(word1)):
        if word1[i] in word_dict:
            word_dict[word1[i]] += 1
        else:
            word_dict[word1[i]] = 1
    for i in range(len(word2)):
        if word2[i] in word_dict:
            word_dict[word2[i]] -= 1
        else:
            word_dict[word2[i]] = 1
    for key, value in word_dict.items():
        if value != 0:
            return key


if __name__ == '__main__':
    test_case1 = "abccc"
    print(length_of_longest_substring("pwwkew"))
    word1 = 'a'
    word2 = 'aa'
