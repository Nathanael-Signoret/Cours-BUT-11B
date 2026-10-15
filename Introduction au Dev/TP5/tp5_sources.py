def mystere(liste, valeur):
    """ Renvoie l'indice du 4 eme élement de la liste égal à valeur

    Args:
        liste (list): la liste parcourue : on compare ses valeurs avec le paramètre valeur
        valeur (int): la valeur comparée

    Returns:
        int: l'indice de la 4eme répétition du nombre valeur
    """
    xxx = 0 #xxx = 0; 1; 2; 3; 4; 5; 6; 7; 8; 9; 10
    yyy = 0 #yyy = 0; 0; 0; 0; 0; 0; 0; 0; 0; 0
    for elem in liste:
        if elem == valeur:
            yyy += 1
            if yyy > 3:
                return xxx
        xxx += 1
    return None

def mystere_ind(liste, valeur):
    """ Renvoie l'indice du 4 eme élement de la liste égal à valeur

    Args:
        liste (list): la liste parcourue : on compare ses valeurs avec le paramètre valeur
        valeur (int): la valeur comparée

    Returns:
        int: l'indice de la 4eme répétition du nombre valeur
    """
    compteur = 0
    for i in range(len(liste)):
        if liste[i] == valeur:
            compteur += 1
            if compteur > 3:
                return i
    return None


mystere([12, 5, 8, 48, 12, 418, 185, 17, 5, 87], 20)


def premier_chiffre_str(chaine):
    for i in range(len(chaine)):
        if chaine[i] in "2134567890":
            return i
    return None

assert premier_chiffre_str("on est le 30/09/2021") == 10

# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238,
              136463,  25725]

def population_ville(liste_v, liste_pop, nom_v):
    for i in range(len(liste_v)):
        if liste_v[i] == nom_v:
            return liste_pop[i]
    return None

assert population_ville(liste_villes, population, "Olivet") == 22168
assert population_ville(liste_villes, population, "Blois") == 45871
assert population_ville(liste_villes, population, "Ascent") == None
assert population_ville(liste_villes, population, "Vierzon") == 25725

def verifie_tri(tab):
    for i in range(1, len(tab)):
        if tab[i] < tab[i-1]:
            return False
    return True

assert verifie_tri([1, 2, 3, 4, 5]) == True
assert verifie_tri([5, 4, 3, 2, 1]) == False
assert verifie_tri([]) == True

def somme_seuil(tab, seuil):
    somme = 0
    for i in range(len(tab)):
        somme = somme + tab[i]
        if somme > seuil :
            return True
    return False

assert somme_seuil([1, 4, 1, 2, 3, 4], 6) == True
assert somme_seuil([0, 0, 0, 5, 6, 0, 4], 15) == False
assert somme_seuil([], 1) == False
assert somme_seuil([54645646], 15) == True

def adresse_mail(chaine):
    if chaine[0] == "@" or chaine[-1] == ".":
        return False
    point = False
    arobase = False
    for i in range(len(chaine)):
        if chaine[i] == " ":
            return False
        elif chaine[i] == "." and arobase == True:
            point = True
        elif chaine[i] == "@":
            if arobase == True:
                return False
            arobase = True
    if point == True and arobase == True :
        return True
    else :
        return False

assert adresse_mail("nathanael.signoret@gmail.com") == True
assert adresse_mail("@nathanael.signoret@gmail.com") == False
assert adresse_mail("nathanael.signoret@gmail.com.") == False
assert adresse_mail("nathanael signoret@gmail.com") == False
assert adresse_mail("nathanaelsignoret@gmailcom") == False


# ---------------------------------------
# Exemple de scores
# ---------------------------------------
scores = [352100, 325410, 312785, 220199, 127853]
joueurs = ['Batman', 'Robin', 'Batman', 'Joker', 'Batman']

def meilleur_score_j(scores, joueurs, nom_joueur):
    max_joueur = 0
    for i in range(len(scores)):
        if joueurs[i] == nom_joueur:
            if scores[i] > max_joueur:
                max_joueur = scores[i]
    return max_joueur

def test_decroissant(scores):
    if scores == []:
        return True
    score_max = scores[0]
    for i in range(1, len(scores)):
        if scores[i] > score_max:
            return False
    return True

def nombre_rep_joueur(joueurs, nom_joueur):
    cpt_j = 0
    for i in range(len(joueurs)):
        if joueurs[i] == nom_joueur:
            cpt_j += 1
    return cpt_j

def meilleur_classement_j(joueurs, nom_joueur):
    for i in range(len(joueurs)):
        if joueurs[i] == nom_joueur:
            return i + 1
    return None

def trouver_i_score(scores, score):
    for i in range(len(scores)):
        if score < scores[i]:
            return i
    return i

def inserer_score(scores, joueurs,score, n_joueur):
    i_score = trouver_i_score(scores, score)
    scores.insert(i_score, score)
    joueurs.insert(i_score, n_joueur)
    return scores, joueurs

assert inserer_score([10000], ["Cypher"], 20000, "Jett") == ([20000, 10000], ["Jett", "Cypher"])