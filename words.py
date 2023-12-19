def export_words_less_than_lenght(file_handle, word_length):
    with open(
        f"words_lenght_less_than_{word_length}.txt", "w", encoding="UTF-8"
    ) as file:
        for line in file_handle:
            if len(line.strip()) < word_length:
                file.write(line)


def check_if_word_allowed(file_handle, word):
    allowed_words = [line.strip() for line in file_handle.readlines()]
    return word in allowed_words


if __name__ == "__main__":
    with open("words.txt", "r", encoding="UTF-8") as file:
        #     export_words_less_than_lenght(file, 6)
        print(check_if_word_allowed(file, "kubek"))
