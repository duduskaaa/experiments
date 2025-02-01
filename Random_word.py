import random
words = ("облако","яблоко", "стол", "книга", "программа", "компьютер",
    "кошка", "собака", "дом", "машина", "телефон",
    "человек", "музыка", "звезда", "дерево", "цветок",
    "солнце", "луна", "вода", "море", "гора",
    "облако", "небо", "земля", "планета", "галактика",
    "школа", "университет", "учитель", "студент", "учебник",
    "фильм", "актер", "режиссер", "камера", "экран",
    "игра", "консоль", "клавиатура", "мышь", "кнопка",
    "картина", "холст", "кисть", "палитра", "скульптура",
    "перо", "бумага", "ручка", "тетрадь", "карандаш", "аааааааааааааааааааааааааааааааааааааааааааааааааааааааааааа")

several_letters = 0
win = 0

def get_word():
    random_word = random.choice(words).upper()
    wordList = [i for i in random_word]
    return random_word
def display_hangman(tries):
    stages = [0, 1, 2, 3, 4, 5, 6]
    return stages[tries]
def gameplay(random_word):
    global several_letters, win
    tries = 6
    right_guess = len(random_word)
    word_guess = '_' * len(random_word)
    fool_list = []
    print('Хочешь сыграть в игру пупсик?')
    print("У тебя есть", display_hangman(tries), 'попыток')
    print(word_guess)
    print("Шо ты чепушила, вводи букву:")
    while tries != 0:
        guess = False
        player_letter = input().upper()
        if not player_letter.isalpha():
            print("Вводи букву пидор")
            continue
        if player_letter in fool_list:
            print("Ты уже вводил эту букву альцгей")
            continue
        fool_list.append(player_letter)
        for index in range(len(random_word)):
            if player_letter == random_word[index]:
                word_guess = word_guess[:index] + player_letter + word_guess[index + 1:]
                guess = True
                several_letters += 1
        if guess:
            if several_letters >= 2:
                print(word_guess, end='\r')
                right_guess -= several_letters
                several_letters = 0
            else:
                print(word_guess)
                right_guess -= 1
                several_letters = 0
        else:
            print("Нихуя подобного пидорок")
            tries -= 1
            print("Осталось попыток:", tries, end='\r')
        if right_guess == 0:
            print("Молодец, молодец, держи конфетку")
            win += 1
            break
        elif tries == 0:
            print("Ты проиграл лопух, загаданное слово было:", random_word)
while True:
    gameplay(get_word())
    print(f"Количество выигрышей: {win}")
