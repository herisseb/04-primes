""""
Module de test de nombres premiers.

Ce module définit une fonction isprime() qui permet de déterminer si un entier est
un nombre premier, ainsi qu'une fonction main() qui affiche les nombres premiers
strictement inférieurs à 100.
"""

from math import sqrt


def isprime(p):
    """
    Détermine si un nombre entier est premier.

    Un nombre premier est un entier naturel supérieur ou égal à 2
    qui n'admet exactement que deux diviseurs distincts : 1 et lui-même.

    Args:
        p (int): Nombre entier à tester.

    Returns:
        bool: True si p est un nombre premier, False sinon.
    """
    if p < 2:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False

    for i in range(3, int(sqrt(p)) + 1, 2):
        if p % i == 0:
            return False
    return True


def main():
    """
    Fonction principale du programme.

    Parcourt les entiers de 0 à 99 et affiche ceux qui sont premiers.
    Cette fonction sert à tester visuellement la validité de isprime().

    Returns:
        None
    """
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()  # retour à la ligne final


    if __name__ == "__main__":
        main()