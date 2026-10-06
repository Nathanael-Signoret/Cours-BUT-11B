def sanction_exces_vitesse(limitation, vitesse, recidive):
    """Détermine les sanctions pour dépassement de vitesse

    Args:
        limitation (int): la limitation de vitesse de la route où l'infraction est produite
        vitesse (int): la vitesse de la voiture en infraction
        recidive (bool): indique si il y a récidive ou non

    Returns:
        tuple: indique la sanction délivrée sous la forme (amende, points_retirés, temps_sans_permis)
    """
    if vitesse - limitation > 50 :
        if recidive :
            return(3750, 6, 36)
        else :
            return (1500, 6, 36)
    elif vitesse - limitation > 40 :
        return (135, 4, 36)
    elif vitesse - limitation > 30 :
        return (135, 3, 36)
    elif vitesse - limitation > 20 :
        return (135, 2, 0)
    else :
        if limitation > 50:
            return (68, 1, 0)
        else :
            return (135, 1, 0)

def test_sanction():
    assert sanction_exces_vitesse(70, 90, False) == (68, 1, 0)
    assert sanction_exces_vitesse(30, 50, False) == (135, 1, 0)
    assert sanction_exces_vitesse(70, 95, False) == (135, 2, 0)
    assert sanction_exces_vitesse(70, 105, False) == (135, 3, 36)
    assert sanction_exces_vitesse(70, 115, False) == (135, 4, 36)
    assert sanction_exces_vitesse(70, 130, False) == (1500, 6, 36)
    assert sanction_exces_vitesse(70, 130, True) == (3750, 6, 36)

test_sanction()