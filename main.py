import re


def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
        return None


def extract_first_sentence(text):
    sentences = re.split(r'(?<=[.!?])\s', text)
    if sentences:
        return sentences[0]
    return None


def clean_and_sort_words(text):
    ukrainian_words = []
    english_words = []

    words = re.findall(r'\w+', text, re.U)
    for word in words:
        if re.search(r'[а-яА-Я]', word):
            ukrainian_words.append(word)
        else:
            english_words.append(word)

    ukrainian_words = sorted(ukrainian_words, key=lambda word: (word.lower(), word))
    english_words = sorted(english_words, key=lambda word: (word.lower(), word))

    return ukrainian_words + english_words


def count_words(text):
    words = re.findall(r'\w+', text, re.U)
    return len(words)


filename = 'file.txt'
text = read_file(filename)

if text:
    first_sentence = extract_first_sentence(text)
    if first_sentence:
        print("Перше речення:")
        print(first_sentence)

        words = clean_and_sort_words(text)
        print("\nВсі слова в тексті (відсортовані по алфавіту):")
        for word in words:
            print(word)

        word_count = count_words(text)
        print(f"\nКількість слів в тексті: {word_count}")
