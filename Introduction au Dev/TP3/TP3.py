def somme_pair(tab):
    """Détermine la somme de tous les nombres pairs d'un tableau

    Args:
        tab (list): la liste de nombres sur laquelle on va travailler

    Returns:
        int: la somme des nombres pairs présents dans le tableau
    """
    res = 0
    for el in tab:
        if el % 2 == 0:
            res = res + el
    return res

def derniere_voyelle(ch):
    """Indique la dernière voyelle présente dans une chaine de caractères

    Args:
        ch (str): la chaine de caractères étudiée

    Returns:
        ch: la dernière voyelle de la chaine étudiée
    """
    res = None
    for el in ch:
        if el.lower() in "aeiouy":
            res = el.lower()
    return res

def ratio_nb_negatif(tab):
    """renvoie la proportion de nombres négatifs d'un tableau

    Args:
        tab (list): la liste de nombres étudiés 

    Returns:
        float: la proportion des nombres négatifs dans le tableau
    """
    ratio_n = 0
    for el in tab:
        if el < 0:
            ratio_n = ratio_n + 1
    if len(tab) == 0 :
        return 0
    return ratio_n/len(tab)

def test_somme():
    assert somme_pair([12,13,6,5,7]) == 18
    assert somme_pair([5,9,3,1,11,25]) == 0
    assert somme_pair([8,52,6,8,4]) == 78
    assert somme_pair([12,-8,5,6,-2]) == 8

def test_voyelle():
    assert derniere_voyelle("Bonjour") == "u"
    assert derniere_voyelle("") == None
    assert derniere_voyelle("nzrtpmlkjhh") == None
    assert derniere_voyelle("Argh") == "a"

def test_ratio():
    assert ratio_nb_negatif([4,-2,8,2,-2,-7]) == 0.5
    assert ratio_nb_negatif([4,8,8,29,52,7]) == 0
    assert ratio_nb_negatif([-40,-2,-8,-2,-2,-7]) == 1
    assert ratio_nb_negatif([]) == 0

test_somme()
test_voyelle()
test_ratio()

def somme_n_premiers(nb):
    """Renvoie la somme des n premiers entiers

    Args:
        nb (int): le nombre d'entiers qu'on va additionner

    Returns:
        int: la sommme des n premiers entiers
    """    
    s = 0
    for i in range (nb+ 1):
        s = s + i
    return s

def syracuse(val_init, nb_it):
    """Renvoie le terme numéro n de la suite de syracuse avec val_init en valeur initiale

    Args:
        val_init (int): la valeur initiale de la suite 
        nb_it (int): le nombre d'itérations avant de finir la boucle

    Returns:
        float: la valeur finale après la suite de syracuse 
    """    
    val = val_init
    for i in range (nb_it):
        if val % 2 == 0:
            val = val/2
        else :
            val = val*3 + 1
    return val

def test_somme2():
    assert somme_n_premiers(5) == 15
    assert somme_n_premiers(0) == 0
    assert somme_n_premiers(2) == 3
    assert somme_n_premiers(4) == 10

def test_syracuse():
    assert syracuse(6, 3) == 5.0
    assert syracuse(12,5) == 16
    assert syracuse(0, 5) == 0
    assert syracuse(1, 13) == 4
    assert syracuse(3726, 4861) == 4

test_somme2()
test_syracuse()

def minimum(tab):
    if tab!=[]:
        mini= tab[0]
        for i in range(1,len(tab)):
            if tab[i]<mini:
                mini = tab[i]
        return mini

def maximum(tab):
    if tab!=[]:
        maxi = tab[0]
        for i in range(1, len(tab)):
            if tab[i]>maxi:
                maxi = tab[i]
        return maxi

def diff_petit_grand(tab):
    minim = minimum(tab)
    maxim = maximum(tab)
    return maxim - minim

def plus_que_dix(tab):
    cpt = 0
    for el in tab:
        if el>10:
            cpt = cpt + 1
    return cpt

def moyenne_n(tab):
    if tab != []:
        s_neg = 0
        cpt = 0
        for el in tab:
            if el<0:
                s_neg += el
                cpt = cpt + 1
        return s_neg/cpt

def test6():
    assert minimum([12,113,6,5,7]) == 5
    assert maximum([12,113,6,5,7]) == 113
    assert diff_petit_grand([12,113,6,5,7]) == 108
    assert plus_que_dix([12,113,6,5,7]) == 2
    assert moyenne_n([-12,113,-6,-3,7]) == -7

test6()