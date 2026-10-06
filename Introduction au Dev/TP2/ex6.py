def algo1(a,b,c,d):
    """trouve le minimum parmi 4 nombres

    Args:
        a (int): un entier
        b (int): un entier
        c (int): un entier
        d (int): un entier

    Returns:
        int: le nombre le plus petit entre a, b, c et d
    """    
    if a < b:
        res = a
    else :
        res = b
    if c < res:
        res = c
    if d < res:
        res = d
    return res

def test_algo1():
    assert algo1(5, 2, 8, 372) == 2
    assert algo1(1, 47, 4, 2) == 1
    assert algo1(45, 30, 3, 3272) == 3
    assert algo1(25, 9, 36, 2) == 2

def algo2(mot):
    """_summary_

    Args:
        mot (str): Un mot

    Returns:
        bool: renvoie True si le mot contient plus de voyelles que de consonne, False sinon
    """    
    res = 0
    for lettre in mot:
        if lettre in 'aeiouy':
            res = res + 1
        else :
            res = res - 1
    return res > 0

def test_algo2():
    assert algo2("eau") == True
    assert algo2("Ethan") == False
    assert algo2("caca") == False
    assert algo2("oraoraoraoraoraoraoraoraoraoraoraoraoraoraora") == True

test_algo1()
test_algo2()