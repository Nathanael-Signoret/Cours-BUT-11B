import math
def ecart_type(tab):
    """Renvoie l'ecart type d'une liste

    Args:
        tab (list): un tableau d'entiers ou de décimaux 

    Returns:
        float : l'ecart type de tous les nombres du tableau 
    """    
    s_tab = 0 #vaut la somme de tous les nombres rencontés dans le tableau
    for i in range(len(tab)):
        s_tab += tab[i]
    m_tab = s_tab/ len(tab)
    s_ecart  = 0 #contient la somme de l'écart entre chaque nombre rencontrés et s_tab
    for i in range (len(tab)):
        tab[i] = (tab[i] - m_tab)**2
        s_ecart += tab[i]
    m_ecart = s_ecart / len(tab)
    ecart_type = math.sqrt(m_ecart) 
    return ecart_type

def test_ecart_type():
    assert ecart_type([2,4,4,4,5,5,7,9]) == 2
    assert ecart_type([5,5,5,5,5,5,5,5,5,5,5]) == 0


def bissextile(annee):
    """Indique si une annee donnee est bissextile ou non
    
        Args:
            annee (int): une annee
    
        Returns:
            bool: True si l'anne donnee est bissextile, False sinon
        """    
    if annee % 4 == 0 :
        if annee % 100 != 0 or annee % 400 == 0 :
            return True
    return False

def test_bis():
    assert(bissextile(2020)) == True
    assert(bissextile(2100)) == False
    assert(bissextile(2400)) == True
    assert(bissextile(2017)) == False

def nb_bissextiles(annee1, annee2):
    """Indique le nombre d'annees bissextiles entre 2 années données

    Args:
        annee1 (int): l'annee de départ
        annee2 (int): l'annee d'arrivee

    Returns:
        int: le nombre d'annees bissextiles entre l'annee1 inclus et l'annee 2 exclus
    """    
    cpt_biss = 0
    for i in range (annee1, annee2):
        if bissextile(i) == True:
            cpt_biss += 1
    return cpt_biss

def test_nb_bis():
    assert nb_bissextiles(1999, 2021) == 6
    assert nb_bissextiles(2000, 2020) == 5
    assert nb_bissextiles(1998, 1999) == 0
    assert nb_bissextiles(0, 2026) == 492

def jeu_de(n, cible):
    """ Indique le nombre de possibilites possible pour un résultat cible en lancant 2DN

    Args:
        n (int): la taille des dés qu'on va lancer
        cible (int): le resultat qu'on doit obtenir

    Returns:
        int: le nombre de lancers différents qui donnent le résultat cible sur 2DN
    """    
    cpt = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i + j == cible:
                cpt = cpt + 1
    return cpt

def test_jeu_de():
    assert jeu_de(6, 7) == 6
    assert jeu_de(0, 8) == 0

def meilleur_chance(n):
    """Indique quel nombre possède la meillerue chance de tomber en lancant 2DN

    Args:
        n (int): le nombre de faces que va posseder notre dé

    Returns:
        int: le nombre le plus probable de tomber sur un lancer de dé (le nombre avec le plus de combinaisons possibles pour 2DN)
    """    
    maxi = 0
    for i in range(1, 2*n+1):
        if jeu_de(n, i) > jeu_de(n, maxi):
            maxi = i
    return maxi

def test_meilleur_chance():
    assert meilleur_chance(6) == 7
    assert meilleur_chance(0) == 0

test_bis()
test_ecart_type()
test_jeu_de()
test_meilleur_chance()
test_nb_bis()
