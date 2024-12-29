def glob_matching(file_name, pattern):
    i, j = 0, 0
    star_idx = -1  # index of * in pattern
    match_idx = 0  # index in the filename that matched a'*'

    while i < len(file_name):
        # easy case when pattern has the same letter on the same position or is ? in the same index
        if j < len(pattern) and pattern[j] == (file_name[i] or pattern[j] == '?'):
            i += 1
            j += 1
        # there is * in the  pattern, so we record it
        elif j < len(pattern) and pattern[j] == '*':
            star_idx = j
            match_idx = i
            j += 1
        elif star_idx != -1:
            j = star_idx + 1
            match_idx += 1
            i = match_idx
        else:
            return False
    while j < len(pattern) and pattern[j] == '*':
        j += 1

    return j == len(pattern)  # pattern fully consumed

if __name__ == '__main__':
    glob_matching('abc', 'a?')
