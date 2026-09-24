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
    """
    return s.lower() == s[::-1].lower()

def is_palindrom_sentence(s:str) -> bool:
    # DocString mit Tests noch schreiben
    s = s.lower()
    string_stripped = ''
    for x in s:
        if x != ' ' and x != "?" and x != '!' and x != '.':
            string_stripped += x
        else:
            continue
    return string_stripped == string_stripped[::-1]

if __name__ == "__main__":
     print(is_palindrom("hannah"))
     print(is_palindrom_sentence("Was it a car or a cat I saw?"))

