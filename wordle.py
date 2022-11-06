#!/usr/bin/env python3

import random

def main():
    words = read_words()
    N = len(words)
    i = 0
    for riddle in words:
        print(f'== {N-i} words at your service ==')
        guessed_ok = conduct_guesses(riddle, words)

        if guessed_ok:
            print('yay! ^_^')
        else:
            print(f'alas u_u the word was: {riddle}')
        print()
        i += 1
    print('you sonowabich you did it')

def read_words():
    with open('/tmp/russian_nouns.txt') as f:
        words = (n.strip() for n in f.readlines())
        words = [n for n in words if len(n) == 5]
    random.shuffle(words)
    return words

def conduct_guesses(riddle, words):
    max_attempts = 6
    alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    for attempt in range(1, max_attempts+1):
        alphabet_str = ''.join(alphabet)
        while True:
            guess = input(f'[{attempt}/{max_attempts}] Guess the word -- {alphabet_str}\n> ')
            if guess == '-':
                return False
            if len(guess) != 5:
                print('! length should be 5')
                continue
            if guess not in words:
                print('! unknown word')
                continue
            break
        print('# ', end='')
        for g, r in zip(guess, riddle):
            if g == r:
                x = g
                if g in alphabet:
                    idx = alphabet.index(g)
                    alphabet[idx] = g.upper()
            elif g in riddle:
                x = '?'
                if g in alphabet:
                    idx = alphabet.index(g)
                    alphabet[idx] = g.upper()
            else:
                x = '_'
                if g in alphabet:
                    idx = alphabet.index(g)
                    alphabet[idx] = '_'
            print(x, end='')
        print()
        if guess == riddle:
            return True
    return False

if __name__ == '__main__':
    main()
