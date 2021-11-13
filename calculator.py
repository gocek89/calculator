import logging
logging.basicConfig(level=logging.DEBUG)


def adding(numb_1, numb_2, numb_3=0, numb_4=0):
    x = str(input(
        "W wypadku tego działania mozesz dodac do siebie jeszcze dwie cyfry czy chcesz skorzystac z mozliwosci [T/N]"))
    if x == "T":
        numb_3 = int(input("Podaj liczbę 3:\n"))
        numb_4 = int(input("Podaj liczbę 4:\n"))
        logging.info(
            f"Dodaje składnik {numb_1} i {numb_2} i {numb_3} i {numb_4}")
        wynik = numb_1 + numb_2 + numb_3 + numb_4
        print(f"Wynik to : {wynik}")
    else:
        logging.info(f"Dodaje składnik {numb_1} i {numb_2}")
        wynik = numb_1 + numb_2
        print(f"Wynik to : {wynik}")


def subtraction(numb_1, numb_2):
    logging.info(f"odejmuję {numb_1} i {numb_2}")
    wynik = numb_1 - numb_2
    print(f"Wynik to : {wynik}")


def multiplication(numb_1, numb_2, numb_3=1, numb_4=1):
    x = str(input(
        "W wypadku tego działania mozesz dodac do siebie jeszcze dwie cyfry czy chcesz skorzystac z mozliwosci [T/N]"))
    if x == "T":
        numb_3 = int(input("Podaj liczbę 3:\n"))
        numb_4 = int(input("Podaj liczbę 4:\n"))
        wynik = numb_1 * numb_2 * numb_3 * numb_4
        logging.info(
            f"Mnoze składnik {numb_1} i {numb_2} i {numb_3} i {numb_4}")
        print(f"Wynik to : {wynik}")
    else:
        wynik = numb_1 * numb_2
        logging.info(f"Mnoze składniki{numb_1} i {numb_2}")
        print(f"Wynik to : {wynik}")


def division(numb_1, numb_2):
    logging.info(f"dziele {numb_1} i {numb_2}")
    wynik = numb_1 / numb_2
    print(f"Wynik to : {wynik}")
