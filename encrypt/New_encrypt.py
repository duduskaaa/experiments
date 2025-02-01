from random import *
#from my_fucntions import isPrime

alphabet = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й',
    'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
    'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я', ' '
]


def vigener(user_message, text_key):
    crypt = []
    for i in range(len(user_message)):
        crypt.append(alphabet[(alphabet.index(user_message[i]) - alphabet.index(text_key[i])) % 32])
    return crypt


def rsa(user_message, text_key):
    crypt = []
    vigener_crypt = vigener(user_message, text_key)

    for i in vigener_crypt:
        crypt.append(alphabet[(alphabet.index(i) ** 7) % 33])

    crypt = ''.join(crypt)
    return crypt


def re_rsa(user_message):
    re_crypt = []
    for i in user_message:
        re_crypt.append(((alphabet.index(i) ** 3) % 33))
    return re_crypt


def re_vigener(user_message, text_key):
    recrypt_rsa = re_rsa(user_message)
    recrypt = []
    for i in range(len(recrypt_rsa)):
        recrypt.append(alphabet[(recrypt_rsa[i] + alphabet.index(text_key[i])) % 32])

    recrypt = ''.join(recrypt)
    return recrypt


def enc(user_want, user_message, user_key):
    while True:
        flag_want = -1
        user_message = user_message.lower()
        open_prime_key = [7, 33]

        # Проверка
        if not user_message:
            return ['error', 'NullText']
        if len([letter for letter in user_message if letter not in alphabet]) > 0:
            return ["error", 'NotRusText']

        # Шифровка
        if user_want == 1:
            text_key = [alphabet[randint(1, 31)] for i in range(len(user_message))]
            text_key = ''.join(text_key)

            enc_message = rsa(user_message, text_key)
            enc_key = text_key
            flag_want = 1
            break

        # Расшифровка
        if user_want == 0:
            text_key = user_key

            if not text_key:
                return ['error', 'NullKey']
            if len(text_key) != len(user_message):
                return ['error', 'LenUnequal']

            close_prime_key = [3, 33]
            flag_want = 0
            re_enc = re_vigener(user_message, text_key)
            break

    if flag_want == 1:
        return [enc_message, enc_key]
    if flag_want == 0:
        return [re_enc, text_key]


def enc_print(user_want, user_message, user_key):
    enc_full = enc(user_want, user_message, user_key)
    if enc_full[0] == 'error':
        return [enc_full[0], enc_full[1]]

    enc_message = enc_full[0]
    enc_key = enc_full[1]

    return [enc_message, enc_key]
