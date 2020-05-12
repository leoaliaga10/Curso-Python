# -*- coding: utf-8 -*-
import random


def run():
    number_found = False
    random_number = random.randint(0, 20)

    while not number_found:
        number = int(input('Intenta un nÃºmeroï¼š'))

        if number == random_number:
            print('Felicidades. Encontraste el nÃºmero')
            number_found = True
        elif number > random_number:
            print('El nÃºmero es mÃ¡s pequeÃ±o')
        else:
            print('El nÃºmero es mÃ¡s grande')


if __name__ == '__main__':
    run()