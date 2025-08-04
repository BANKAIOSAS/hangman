import random

def hangman(word):
    wrong_guesses = 0
    win = False
    word_letters = list(word)
    board = ['__'] * len(word)
    stages = ['',
              '________        ',
              '|               ',
              '|      |        ',
              '|      O        ',
              '|     /|\       ',
              '|     / \       '
              ]
    print("Добро Пожаловать на Казнь!")
    
    while wrong_guesses < len(stages) - 1:
        print('\n')
        letter = str(input("Введите Букву: "))
        if letter in word_letters:
            letter_index = word_letters.index(letter)
            board[letter_index] = letter
            word_letters[letter_index] = '$'
        else:
            wrong_guesses += 1
        print(' '.join(board))
        slice_end = wrong_guesses + 1
        print('\n'.join(stages[0: slice_end]))
        if '__' not in board:
            print("Вы Победили! Было Загадано Слово: ")
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses + 1]))
        print("Вы Проиграли! Было Загадано Слово: ", word)

print("Добро Пожаловать в Игру 'Виселица'!")
print("Правила Просты: Заполняете Список Трёмя Уникальными Словами, Затем Угадываете, Какое Было Выбрано")
print("Вводите Букву, Если Буква Есть в Загаданном Слове - Выводится Подсказка")
print("Сыграем?")

words_list = []

for i in range(3):
    response = str(input("Введите Уникальное Слово: "))
    words_list.append(response)

random_index = random.randint(0, 2)
hangman(words_list[random_index])
