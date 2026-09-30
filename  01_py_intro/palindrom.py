__author__ = "Marius Jörg"
__example__ = "SEW/01/F1"  # Gegenstand/Übungsblatt/Aufgabe(Kapitel)
__date__ = "24.09.2026"
__version__ = "1.2.0"
__license__ = "GNU GPLv3"
__status__ = "Released"


def is_palindrom(s:str) -> bool:
    """
    Schaut ob ein Wort ein Palindrom ist

    :arg:
        s (String): Das Wort
    :returns
        boolean: Ob es ein Palindrom ist oder nicht

    :Examples:
        >>> is_palindrom("Marius")
        False
        >>> is_palindrom("Lagerregal")
        True
    """
    return s.lower() == s[::-1].lower()

def is_palindrom_sentence(s:str) -> bool:
    """
    Schaut ob ein Satz ein Palindrom ist
    :arg:
        s (String): Das Wort
    :returns
        boolean: Ob es ein Palindrom ist oder nicht
    :Examples:
        >>> is_palindrom_sentence("Ein Eselein, nie lese nie.")
        True
        >>> is_palindrom_sentence("Eine Rose ist rot, nie.")
        False
    """
    s = s.lower()
    string_stripped = ''
    for x in s:
        if x != ' ' and x != "?" and x != '!' and x != '.':
            string_stripped += x
        else:
            continue
    return string_stripped == string_stripped[::-1]

def palindrom_product(x:int) -> int:
    for i in range(x):
        if str(i) == str(i)[::-1] and 10000 <= i <= 998001:
            return i
    return 0

if __name__ == "__main__":
     print(is_palindrom("hannah"))
     print(is_palindrom_sentence("Was it a car or a cat I saw?"))
     print(palindrom_product(11000))

