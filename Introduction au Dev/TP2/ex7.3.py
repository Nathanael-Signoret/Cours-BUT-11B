def qualif_jo(record, nb_victoires, champion, sexe):
    """Détermine si une personne est qualifiée aux JO ou non

    Args:
        record (int): le record de 100m de l'athlète, arrondi au plus proche
        nb_victoires (int): le nombre de courses gagnées par l'athlète
        champion (bool): détermine si l'athlète est cahmpion du monde ou non
        sexe (str): F si l'athlète est une femme, M si c'est un homme

    Returns:
        bool: True si l'athlète est qualifié aux JO, False sinon
    """
    if sexe == "F" :
        if record < 15 and nb_victoires >= 3 :
            res = True
        else :
            res = False
    elif sexe == "M":
        if record < 12 and nb_victoires >= 3:
            res = True
        else :
            res = False
    if champion == True:
        res = True
    return res

def test_qualif():
    assert qualif_jo(13, 4, False, "F") == True
    assert qualif_jo(16, 4, False, "F") == False
    assert qualif_jo(12, 2, False, "F") == False
    assert qualif_jo(11, 1, True, "F") == True
    assert qualif_jo(13, 4, False, "M") == False
    assert qualif_jo(11, 2, False, "M") == False
    assert qualif_jo(9, 2, True, "M") == True
    assert qualif_jo(11, 4, False, "M") == True

test_qualif()