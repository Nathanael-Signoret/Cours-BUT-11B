def point_dans_carre(xc, yc, cote, xp, yp):
    if xc <= xp and xc+cote >= xp:
        if yc <= yp and yc + cote >= yp:
            return True
        else :
            return False
    else :
        return False

print(point_dans_carre(25, 25, 3, 1, 1))


def carre_dans_carre(xc1, yc1, cote1, xc2, yc2, cote2):
    if cote1 < cote2:
        xp, yp, cote_p = xc1, yc1, cote1
        xg, yg, cote_g = xc2, yc2, cote2
    else:
        xp, yp, cote_p = xc2, yc2, cote2
        xg, yg, cote_g = xc1, yc1, cote1
    if point_dans_carre(xg, yg, cote_g, xp, yp) == True:
        res1 = True
    else :
        res1 = False
    if point_dans_carre(xg, yg, cote_g, xp, yp) == True:
        res2 = True
    else :
        res2 = False
    if point_dans_carre(xg, yg, cote_g, xp, yp) == True:
        res3 = True
    else :
        res3 = False
    if point_dans_carre(xg, yg, cote_g, xp, yp) == True:
        res4 = True
    else :
        res4 = False
    if res1 == True and res2 == True and res3 == True and res4 == True:
        if xp == xg or yp == yg or xp + cote_p == xg + cote_g or yp + cote_p == yg + cote_g:
            res = True
        else :
            res = False
    elif res1 == True or res2 == True or res3 == True or res4 == True:
        res = True
    else:
        res = False
    print(res)
    return res
        

carre_dans_carre(5, 5, 3, 3, 3, 4)
carre_dans_carre(0, 0, 3, 5, 8, 4)
