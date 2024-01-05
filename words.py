from math import floor
from constants import WORDS_BINARY, ALLOWED_WORDS


def export_words_less_than_lenght(file_handle, word_length):
    """
    Creates a new text file with words no longer than give length
    """
    with open(
        f"words_lenght_less_than_{word_length}.txt", "w", encoding="UTF-8"
    ) as file:
        for line in file_handle:
            if len(line.strip()) < word_length:
                file.write(line)


def sort_words_for_binary_search(file_handle):
    """
    Creates a file with sorted words so that binary search would work correctly
    """
    allowed_words = [line.strip() for line in file_handle.readlines()]
    allowed_words.sort()
    with open(WORDS_BINARY, "w", encoding="UTF-8") as file:
        for word in allowed_words:
            file.write(f"{word}\n")


def is_in_array_binary(element, array):
    left_index = 0
    right_index = len(array) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = floor((left_index + right_index) / 2)
        if array[mid_index] < element:
            left_index = mid_index + 1
        elif array[mid_index] > element:
            right_index = mid_index - 1
        else:
            return True
    return False


def check_if_words_allowed_binary(allowed_words, words):
    """
    Check if words are allowed using binary search.
    Returns True if all words correct else returns False
    """
    for word in words:
        word = word.lower()
        if not is_in_array_binary(word, allowed_words):
            return False
    return True


def check_if_words_allowed(file_handle, words):
    """
    Check if words are allowed.
    Returns True if all words correct else returns False
    """
    allowed_words = [line.strip() for line in file_handle.readlines()]
    for word in words:
        if word.lower() not in allowed_words:
            return False
    return True


def check_the_words(words):
    """
    Returns True if words are in allowed_words(are in WORDS_BINARY .txt file)
    else return False
    """
    with open(WORDS_BINARY, "r", encoding="UTF-8") as file:
        allowed_words = [line.strip() for line in file.readlines()]
        return check_if_words_allowed_binary(allowed_words, words)


if __name__ == "__main__":
    with open(ALLOWED_WORDS, "r", encoding="UTF-8") as file:
        sort_words_for_binary_search(file)
