def plus_long_plateau(chaine):
    """recherche la longueur du plus grand plateau d'une chaine
    Args:
        chaine (str): une chaine de caractères

    Returns:
        int: la longueur de la plus grande suite de lettres consécutives égales
    """
    lg_max = 0  # longueur du plus grand plateau déjà trouvé
    lg_actuelle = 0  # longueur du plateau actuel
    for i in range (len(chaine)):
        if chaine[i] == chaine[i -1]:  # si la lettre actuelle est égale à la précédente
            lg_actuelle += 1
        else:  # si la lettre actuelle est différente de la précédente
            if lg_actuelle > lg_max:
                lg_max = lg_actuelle
            lg_actuelle = 1
    if lg_actuelle > lg_max:  # cas du dernier plateau
        lg_max = lg_actuelle
    return lg_max

def test_plateau():
    assert plus_long_plateau("googoogagaaaa") == 4
    assert plus_long_plateau("ooooo") == 5
    assert plus_long_plateau("viego") == 1
    assert plus_long_plateau("") == 0

test_plateau()

# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238, 136463,
              25725]
liste_villes2 = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Paris"]
population2 = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238, 136463,
              257222225]

def plus_grande_population(tab_villes, tab_popuation):
    """Determine quel est le nom de la ville avec le plus d'habitants 

    Args:
        tab_villes (list): un tableau contenant le nom des villes qu'on étudie 
        tab_popuation (list): un tableau avec le nombre d'habitants de la ville correspondante à l'indice

    Returns:
        str: le nom de la ville avec le plus grand nombre d'habitants 
    """    
    maximum = 0
    res = None
    for i in range(len(tab_villes)):
        if tab_popuation[i] > maximum:
            maximum = tab_popuation[i]
            res = tab_villes[i]
    return res

def test_populace():
    assert plus_grande_population(liste_villes, population) == "Tours"
    assert plus_grande_population([], []) == None
    assert plus_grande_population(liste_villes2, population2) == "Paris"
    assert plus_grande_population(["Saint-Cyr","Rochefourchat"], [2400, 2]) == "Saint-Cyr"

test_populace()

def chaine_en_nombre(chaine):
    nb = 0
    for i in range(len(chaine)):
        if chaine[i] == "1":
            nb += 1*10**(len(chaine)-1-i)
        elif chaine[i] == "2":
            nb += 2*10**(len(chaine)-1-i)
        elif chaine[i] == "3":
            nb += 3*10**(len(chaine)-1-i)
        elif chaine[i] == "4":
            nb += 4*10**(len(chaine)-1-i)
        elif chaine[i] == "5":
            nb += 5*10**(len(chaine)-1-i)
        elif chaine[i] == "6":
            nb += 6*10**(len(chaine)-1-i)
        elif chaine[i] == "7":
            nb += 7*10**(len(chaine)-1-i)
        elif chaine[i] == "8":
            nb += 8*10**(len(chaine)-1-i)
        elif chaine[i] == "9":
            nb += 9*10**(len(chaine)-1-i)
    return nb

def chaine_en_nombre2(chaine):
    nb = 0
    ch = "0123456789"
    for i in range(len(chaine)):
        for j in range(len(ch)):
            if chaine[i] == ch[j]:
                nb += j*10**(len(chaine)-1-i)
    return nb

assert chaine_en_nombre2("2021") == 2021
assert chaine_en_nombre2("9876543210") == 9876543210
assert chaine_en_nombre2("") == 0
assert chaine_en_nombre2("VIEGO") == 0
            
def recherche_mot(tab, l):
    tab_res = []
    for i in range(len(tab)):
        if tab[i][0] == l :
            tab_res.append(tab[i])
    return tab_res

def test_recherche():
    assert recherche_mot(["salut","hello","hallo","ciao","hola"], "h") == ["hello", "hallo", "hola"]
    assert recherche_mot(["salut","hello","hallo","ciao kombucha","hola"], "a") == []
    assert recherche_mot(["s"], "s") == ["s"]
    assert recherche_mot([], "z") == []

test_recherche()

def alpha(chaine):
    tab = []
    ch = ""
    for i in range (len(chaine)):
        if chaine[i].isalpha():
            ch = ch + chaine[i]
        else:
            if ch != "":
                tab.append(ch)
                ch = ""
    if ch != "":
        tab.append(ch)
    return tab

def recherche_mot2(chaine, l):
    tab_ch = alpha(chaine)
    return recherche_mot(tab_ch, l)

print(recherche_mot2("Cela fait déjà 28 jours! 28 jours à l’IUT’O! Cool!!", "C"))

def liste_true(n):
    tab = [False, False]
    for i in range(2, n+1):
        tab.append(True)
    return tab

def multiple_false(tab, x):
    for i in range(2, len(tab)):
        if i % x == 0 and i != x:
            tab[i] = False
    return tab

def eratosthene(n):
    tab_era = liste_true(n)
    for i in range(2, n+1):
        multiple_false(tab_era, i)
    return tab_era

print(multiple_false([False, False, True, True, True, True, True], 2))
print(eratosthene(12))
