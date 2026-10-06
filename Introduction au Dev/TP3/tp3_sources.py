# exercice 1
def plus_de_pair(tab):
    """Détermine si un tableau contient plus de nombres pairs que de nombres impairs 

    Args:
        entree (list): le tableau d'entiers qui va être comparé

    Returns:
        bool: True si le tableau contient plus de nombres pairs que de nombres impairs, False sinon
    """
    pair = 0
    impair = 0
    # au début de chaque tour de boucle
    # Tour 1 xxx = 0 yyy = 0
    # Tour 2 xxx = 0 yyy = 1
    # Tour 3 xxx = 1 yyy = 1
    # Tour 4 xxx = 2 yyy = 1
    # Tour 5 xxx = 3 yyy = 1
    # Tour 6 xxx = 3 yyy = 2
    # Tour 7 xxx = 3 yyy = 3
    for val in tab:
        if val % 2 == 0:
            pair += 1
        else:
            impair += 1
    return pair >= impair

def test_pair():
    assert plus_de_pair([1,4,6,-2,-5,3,10]) == True
    assert plus_de_pair([-4,5,-11,-56,5,-11]) == False
    assert plus_de_pair([1,2,3,4,5,6,7,8]) == True
    assert plus_de_pair([]) == True

test_pair()

# exercice 2
def min_sup(liste_nombres, valeur):
    """trouve le plus petit nombre d'une liste supérieur à une certaine valeur

    Args:
        liste_nombres (list): la liste de nombres
        valeur (int ou float): la valeur limite du minimum recherché

    Returns:
        int ou float: le plus petit nombre de la liste supérieur à valeur
    """
    if liste_nombres == []:
        return None
    else :
        res = liste_nombres[0]
    # au début de chaque tour de boucle res est le plus petit élément
    # déjà énuméré supérieur à valeur
    for elem in liste_nombres:
        if valeur >= res :
            res = elem
        elif valeur < elem < res:
            res = elem
    if valeur >= res :
        return None
    return res


def test_min_sup():
    assert min_sup([8, 12, 7, 3, 9, 2, 1, 4, 9], 5) == 7
    assert min_sup([-2, -5, 2, 9.8, -8.1, 7], 0) == 2
    assert min_sup([5, 7, 6, 5, 7, 3], 10) is None
    assert min_sup([], 5) is None

test_min_sup()

# exercice 3
def nb_mots(phrase):
    """Fonction qui compte le nombre de mots d'une phrase

    Args:
        phrase (str): une phrase dont les mots sont
        séparés par des espaces (éventuellement plusieurs)

    Returns:
        int: le nombre de mots de la phrase
    """    
    resultat = 0
    c1 = ''
    # au début de chaque tour de boucle
    # c1 vaut le caractere précédent
    # c2 vaut le caractere éxaminé
    # resultat vaut un int positif, qui correspond au nombre de mots dans la phrase 
    for c2 in phrase:
        if (c1 == ' ' or c1 == "") and c2 != ' ':
            resultat = resultat + 1
        c1 = c2
    return resultat

def test_nb_mots():
    assert nb_mots("bonjour, il fait beau") == 4
    assert nb_mots("houla!     je    mets beaucoup   d'  espaces    ") == 6
    assert nb_mots(" ce  test ne  marche pas ") == 5
    assert nb_mots("") == 0  # celui ci non plus

test_nb_mots()