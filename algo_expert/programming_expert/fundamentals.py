import random


def sort_employees(employees, sort_by):
    sorting_hash = {"name": 0, "age": 1, "salary": 2}

    sorted_emp = sorted(employees, key=lambda x: x[sorting_hash[sort_by]])
    return sorted_emp


def get_n_longest_unique_words(words, n):
    word_freq = dict()
    results = []
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    for word in word_freq:
        if word_freq[word] == 1:
            results.append(word)
    results = sorted(results, key=lambda x: len(x), reverse=True)
    return results[:n]


# the solution below  does not pass all tests. Solution is much simpler but has O(n^2) but i,m not sure if we may get
# more optimose solution
def pairs_sum_to_target(list1, list2, target):
        result = []
        for i, v1 in enumerate(list1):
            for j, v2 in enumerate(list2):
                if v1 + v2 == target:
                    result.append([i, j])
        return result



if __name__ == '__main__':
    employees_t1 = [
        ["Sarah", 24, 75000],
        ["Connor", 25, 110000],
        ["Jason", 26, 55000],
        ["Josie", 29, 100000],
        ["John", 33, 65000],
    ]
    list1_t1 = [1, -2, 4, 5, 9]
    list1_t2 = [4, 2, -4, -4, 0]
    pairs_sum_to_target(list1_t1, list1_t2, 5)

    sort_employees(employees_t1, sort_by="name")

    words_t1 = ["Longer", "Whatever", "Longer",
                "Ball", "Rock", "Rocky", "Rocky"]
    get_n_longest_unique_words(words_t1, 3)

    # program for Random Number Guesser.
    start_range = input("Enter the start of range: ")
    if not start_range.isnumeric():
        print("Please enter a valid range")
        start_range = input("Enter the start of range: ")
    end_range = input("Enter the end of range: ")
    if not end_range.isnumeric():
        print("Please enter a valid range")
        end_range = input("Enter the start of range: ")

    number_to_guess = random.randint(int(start_range), int(end_range))
    attempt = 1
    my_guess = input("Guess a number: ")
    if not my_guess.isnumeric():
        print("Please enter a valid number")

    while int(my_guess) != number_to_guess:
        attempt += 1
        my_guess = int(input("Guess a number: "))
    if attempt == 1:
        print(f"You guessed the number in {attempt} attempt")
    else:
        print(f"You guessed the number in {attempt} attempts")
