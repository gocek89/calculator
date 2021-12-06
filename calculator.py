import logging
logging.basicConfig(level=logging.DEBUG)


def adding(numb_1, numb_2, numb_3=0, numb_4=0):
    x = str(input(
        "W wypadku tego działania mozesz dodac do siebie jeszcze dwie cyfry czy chcesz skorzystac z mozliwosci [T/N]"))
    if x == "T":
        numb_3 = int(input("Podaj liczbę 3: "))
        numb_4 = int(input("Podaj liczbę 4: "))
        logging.info(
            f"Dodaje składnik {numb_1} i {numb_2} i {numb_3} i {numb_4}")
        return numb_1 + numb_2 + numb_3 + numb_4
    else:
        logging.info(f"Dodaje składnik {numb_1} i {numb_2}")
        return numb_1 + numb_2


def subtraction(numb_1, numb_2):
    logging.info(f"odejmuję {numb_1} i {numb_2}")
    return numb_1 - numb_2


def multiplication(numb_1, numb_2, numb_3=1, numb_4=1):
    x = str(input(
        "W wypadku tego działania mozesz dodac do siebie jeszcze dwie cyfry czy chcesz skorzystac z mozliwosci [T/N]"))
    if x == "T":
        numb_3 = int(input("Podaj liczbę 3: "))
        numb_4 = int(input("Podaj liczbę 4: "))
        logging.info(
            f"Mnoze składnik {numb_1} i {numb_2} i {numb_3} i {numb_4}")
        return numb_1 * numb_2 * numb_3 * numb_4
    else:
        logging.info(f"Mnoze składniki{numb_1} i {numb_2}")
        return numb_1 * numb_2


def division(numb_1, numb_2):
    logging.info(f"dziele {numb_1} i {numb_2}")
    return numb_1 / numb_2


choice = int(input(
    "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: \n"))

numb_1 = int(input("Podaj liczbę 1: "))
numb_2 = int(input("Podaj liczbę 2: "))

if choice == 1:
    print(adding(numb_1, numb_2))
elif choice == 2:
    print(subtraction(numb_1, numb_2))
elif choice == 3:
    print(multiplication(numb_1, numb_2))
elif choice == 4:
    print(division(numb_1, numb_2))
