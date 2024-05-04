def filter_words_by_letter(input_word_list, starting_letter):
    filtered_words = [word for word in input_word_list if word.startswith(starting_letter)]
    return filtered_words

# Функция для ввода списка слов с клавиатуры
def input_word_list():
    word_list = input("Введите список слов через запятую: ").split(",")
    return [word.strip() for word in word_list]

# Ввод списка слов с клавиатуры
words = input_word_list()
starting_letter = input("Введите букву, с которой должны начинаться слова: ")

# Фильтрация слов по заданной начальной букве
filtered_words = filter_words_by_letter(words, starting_letter)
print(filtered_words)
