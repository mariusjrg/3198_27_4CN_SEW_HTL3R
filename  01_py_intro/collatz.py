__author__ = "Marius Jörg"
__example__ = "SEW/01/F2"  # Gegenstand/Übungsblatt/Aufgabe(Kapitel)
__date__ = "1.10.2026"
__version__ = "1.2.0 "
__license__ = "GNU GPLv3"
__status__ = "Released"


def collatz(n: int,p=3) -> int:
    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = int((p * n) + 1)
    return n


def collatz_sequence(number: int) -> list[int]:
    """
    :param number: Startzahl
    :return: Collatz Zahlenfolge, resultierend aus n
    >>> collatz_sequence(19)
    [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    if number == 1:
        return [1]
    return [number] + collatz_sequence(collatz(number))


if __name__ == "__main__":
    print(collatz_sequence(19))
