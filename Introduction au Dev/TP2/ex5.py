def sante(taille, poids):
    """permet de détécter un problème de santé par rapport à l'IMC

    Args:
        taille (float): La taille en m de la personne
        poids (int): Le poids en kg de la personne 

    Returns:
        str: le problème éventuel renvoyé
    """
    imc = poids/(taille*taille)
    if imc < 16.5:
        res = "famine"
    elif imc < 18.5:
        res = "maigreur"
    elif imc < 25:
        res = "normal"
    elif imc < 30:
        res = "surpoids"
    else:
        res = "obésité"
    return res

def tests_sante():
    assert sante(1.8, 80) == "normal"
    assert sante(1.6, 67) == "surpoids"

tests_sante()
