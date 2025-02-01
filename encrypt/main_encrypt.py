import tkinter as tk
from New_encrypt import *

user_want = -1
user_message = ''


def close():
    print('Закрываемся')
    root.destroy()


def encrypt_message():
    user_want = -1
    error = 0

    if selected_want.get() == 'Шифровка':
        user_want = 1
    elif selected_want.get() == 'Расшифровка':
        user_want = 0
    elif selected_want.get() == "Выберите вариант":
        label_message.config(text='Выберите вариант!')
        return 0

    user_message = ent_message.get()
    user_key = ent_key.get()

    enc = enc_print(user_want, user_message, user_key)

    if enc[0] == 'error':
        if enc[1] == 'NotRusText':
            label_message.config(text='Введите русские буквы(без ё и ъ)')
        elif enc[1] == 'NullText':
            label_message.config(text='Введите сообщение')
        elif enc[1] == 'NullKey':
            label_message.config(text='Введите ключ')
        elif enc[1] == 'LenUnequal':
            label_message.config(text='Длина ключа не совпадает')
        error = 1

    if error == 0:
        if user_want == 1:
            label_message.config(text=f'Ваше зашифрованное сообщение: {enc[0]}')
            label_want.config(text=f'Ваш ключ: {enc[1]}')
        if user_want == 0:
            label_message.config(text=f'Ваше расшифрованное сообщение: {enc[0]}')


root = tk.Tk()
root.title("Шифратор")
root.geometry("300x250+400+200")

selected_want = tk.StringVar()
selected_want.set("Выберите вариант")

options_want = ["Шифровка", "Расшифровка"]
dropdown = tk.OptionMenu(root, selected_want, *options_want)
dropdown.pack()

# ent_want = tk.Entry()
ent_message = tk.Entry()
ent_key = tk.Entry()

# ent_want.pack()
label_text = tk.Label(root, text='Ваше сообщение: ')
label_text.pack()
ent_message.pack()
label_text = tk.Label(root, text='Ваш ключ(если имеется): ').pack()
ent_key.pack()

encrypt_button = tk.Button(root, text="Готово", command=encrypt_message)
encrypt_button.pack()

label_message = tk.Label(root, text='')
label_want = tk.Label(root, text='')
label_key = tk.Label(root, text='')

label_message.pack()
label_want.pack()

root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()
