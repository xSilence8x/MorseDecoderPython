"""
Morse Encoder/Decoder

Tento skript umožňuje zakódovat běžný text do Morseovy abecedy a dekódovat
Morseův kód zpět do textu.
"""

from alphabet import MORSE_ALPHABET_DICT


def encode_to_morse(text: str) -> str:
    """
    Zakóduje zadaný text do Morseovy abecedy.
    Odděluje znaky mezerou a slova lomítkem (/).
    Celé věty odděluje dvěma lomítky (//).
    Neznámý znak nahradí otazníkem (?).
    """
    text = text.upper().strip()
    if text == '':
        return "Prázdný vstup."

    words = text.split()
    encoded = []

    for i, word in enumerate(words):
        morse_word = []
        for char in word:
            morse_word.append(MORSE_ALPHABET_DICT.get(char, '?'))
        encoded.append(' '.join(morse_word))

        is_last_word = i == len(words) - 1

        if not is_last_word:
            if word[-1] in ['.', '!', '?']:
                encoded.append('//')
            else:
                encoded.append('/')

    return ' '.join(encoded)


def decode_from_morse(morse_code: str) -> str:
    """
    Dekóduje zprávu v Morseově abecedě do běžného textu.
    """
    if morse_code == '':
        return "Prázdný vstup."

    decoded_chars = []
    morse_letters = morse_code.strip().split(' ')

    for code in morse_letters:
        if code in ['/', '//']:
            decoded_chars.append(' ')
        else:
            found = False
            for letter, morse in MORSE_ALPHABET_DICT.items():
                if morse == code:
                    decoded_chars.append(letter)
                    found = True
                    break
            if not found:
                decoded_chars.append('?')
    return ''.join(decoded_chars)


def run_morse_program() -> None:
    """
    Spustí interaktivní smyčku pro zakódování nebo dekódování Morseovy abecedy.

    Uživatel si může vybrat mezi třemi režimy:
    - 'e' pro zakódování běžného textu do Morseovy abecedy,
    - 'd' pro dekódování Morseovy abecedy zpět do textu,
    - 'k' pro ukončení programu.

    Všechny vstupy a výstupy probíhají přes příkazovou řádku.
    """
    print("Morseův enkodér / dekodér")
    choice = ''
    while choice != 'k':
        choice = input(
            "Zvolte\n'e' pro enkódování,\n"
            "'d' pro dekódování, \n"
            "'k' pro ukončení programu: "
        ).strip().lower()
        if choice == 'e':
            text = input("Zadejte text k zakódování: ")
            print("Zakódovaný text:")
            print(encode_to_morse(text))
        elif choice == 'd':
            morse = input("Zadejte Morseův kód k dekódování: ")
            print("Dekódovaný text:")
            print(decode_from_morse(morse))
        elif choice == 'k':
            print("Ukončení programu.")
            break
        else:
            print("Neplatná volba.")


def main() -> None:
    """Hlavní funkce, která spustí program."""
    run_morse_program()


if __name__ == "__main__":
    main()
