from re import match
from art import logo

chars = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.----.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.',
}


# Function to convert Morse text to alphabetic text
def morse_code_translator(text):
    morse_codes = {value: key for key, value in chars.items()}

    morse_words = text.split('/')
    morse_letters = [word.split() for word in morse_words]

    text_converted = ''

    for morse_letter in morse_letters:
        converted_letter = [morse_codes[letter] for letter in morse_letter]
        morse_letter_converted_to_alpha = ''.join(converted_letter)
        text_converted += ' ' + morse_letter_converted_to_alpha

    return text_converted.upper()


# Function to alphabetic text to convert Morse text
def morse_decoder(text):
    alpha_words = text.split(' ')
    alpha_letters = [word.lower() for word in alpha_words]

    text_converted = ''

    for alpha_letter in alpha_letters:
        converted_letter = [chars[letter] for letter in alpha_letter]
        alpha_letter_converted_to_morse = ' '.join(converted_letter)
        text_converted += alpha_letter_converted_to_morse + '/'

    return text_converted


# Converting message in Morse code or otherwise with recursion
def translate_massage():
    print(logo)
    print('>>>> Type any message for translation , normal text or Morse code using ".", "-", separating letters by spaces and words by "/" <<<<')
    txt = input('Type your text here: ')

    should_continue = True
    while should_continue:
        if match("^[-./| ]*$", txt):
            translated_text = morse_code_translator(txt)
        else:
            translated_text = morse_decoder(txt)

        print('-' * 50)
        print('here your Translated message: ')
        print(f'>>>>> {translated_text}')
        print('-' * 50)

        if input('Type "y" to continue translation with above translate, or type "n" to start a new translation: ') == 'y':
            another_text = input(f'you can continue your message here: {txt} ')
            txt += ' ' + another_text
        else:
            should_continue = False
            translate_massage()


if __name__ == '__main__':
    translate_massage()
