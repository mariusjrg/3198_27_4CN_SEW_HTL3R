__author__ = "Marius Jörg"
__example__ = "SEW/01/F3"  # Gegenstand/Übungsblatt/Aufgabe(Kapitel)
__date__ = "1.10.2026"
__version__ = "1.2.0"
__license__ = "GNU GPLv3"
__status__ = "Released"
from time import time

def M(n):
    if n <= 100:
        return M(M(n + 11))
    else:
        return n - 10

if __name__ == "__main__":
    t0 = time()
    m_list = []
    for n in range(200):
        m_list.append(M(n))
    m_dict = {}
    for n in range(200):
        m_dict[n] = M(n)
    t1 = time()
    print("m_list:", m_list)
    print("m_dict:", m_dict)
    print("Berechnungszeit:", t1 - t0, "Sekunden")
