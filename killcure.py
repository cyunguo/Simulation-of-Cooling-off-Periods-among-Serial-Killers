import numpy as np
import matplotlib.pyplot as plt
import random as rd

def coord(x,y,num):
    if num == 1:
        return [x-1,y+1,8]
    if num == 2:
        return [x-1,y,7]
    if num == 3:
        return [x-1,y-1,6]
    if num == 4:
        return [x,y+1,5]
    if num == 5:
        return [x,y-1,4]
    if num == 6:
        return [x+1,y+1,3]
    if num == 7:
        return [x+1,y,2]
    if num == 8:
        return [x+1,y-1,1]

def kill(points):
    num=len(points)
    newpoint=[]
    for i in range(num):
        x=points[i][0]
        y=points[i][1]
        if x < 999 and x > 0 and y < 999 and y >0:
            dead=points[i][2]
            poss=np.random.normal(1.00,0.004)
            if poss >= 1:
                who=rd.randint(1,8)
                other = poss % 1
                otherposs = rd.uniform(0,1)
                if who == dead:
                    who = (who+1) % 8 +1
                newpoint.append(coord(x,y,who))
                if otherposs < other:
                    who2=rd.randint(1,8)
                    if who == who2:
                        who2 = (who2+1) % 8 +1
                    if who2 == dead:
                        who2 = (who2 + 1) % 8 + 1
                    newpoint.append(coord(x, y, who2))
            else:
                other = poss % 1
                otherposs = rd.uniform(0, 1)
                if otherposs < other:
                    who2 = rd.randint(1, 8)
                    if who2 == dead:
                        who2 = (who2 + 1) % 8 + 1
                    newpoint.append(coord(x, y, who2))
        else:
            if x == 999 :
                if y == 999:
                    dead = points[i][2]
                    poss = np.random.normal(1.0047, 0.004)
                    list=[2,3,5]
                    list.remove(dead)
                    if poss >= 1:
                        b = rd.choices(list)
                        who = b[0]
                        other = poss % 1
                        otherposs = rd.uniform(0, 1)
                        newpoint.append(coord(x, y, who))
                        if otherposs < other:
                            list.remove(who)
                            who2 = list[0]
                            newpoint.append(coord(x, y, who2))
                    else:
                        other = poss % 1
                        otherposs = rd.uniform(0, 1)
                        if otherposs < other:
                            b = rd.choices(list)
                            who2 = b[0]
                            newpoint.append(coord(x, y, who2))
                if y == 0:
                    dead = points[i][2]
                    poss = np.random.normal(1.0047, 0.004)
                    list = [1, 2, 4]
                    list.remove(dead)
                    if poss >= 1:
                        b = rd.choices(list)
                        who = b[0]
                        other = poss % 1
                        otherposs = rd.uniform(0, 1)
                        newpoint.append(coord(x, y, who))
                        if otherposs < other:
                            list.remove(who)
                            who2 = list[0]
                            newpoint.append(coord(x, y, who2))
                    else:
                        other = poss % 1
                        otherposs = rd.uniform(0, 1)
                        if otherposs < other:
                            b = rd.choices(list)
                            who2 = b[0]
                            newpoint.append(coord(x, y, who2))
                if y > 0 and y<999:
                    dead = points[i][2]
                    poss = np.random.normal(1.00, 0.004)
                    list = [1,2, 3, 4, 5]
                    list.remove(dead)
                    if poss >= 1:
                        b = rd.choices(list)
                        who = b[0]
                        other = poss % 1
                        otherposs = rd.uniform(0, 1)
                        newpoint.append(coord(x, y, who))
                        if otherposs < other:
                            list.remove(who)
                            b = rd.choices(list)
                            who2 = b[0]
                            newpoint.append(coord(x, y, who2))
                    else:
                        other = poss % 1
                        otherposs = rd.uniform(0, 1)
                        if otherposs < other:
                            b = rd.choices(list)
                            who2 = b[0]
                            newpoint.append(coord(x, y, who2))
            if x == 0 :
                if y == 999:
                    dead = points[i][2]
                    poss = np.random.normal(1.00, 0.004)
                    list=[5,7,8]
                    list.remove(dead)
                    if poss >= 1:
                        b = rd.choices(list)
                        who = b[0]
                        other = poss % 1
                        otherposs = rd.uniform(0, 1)
                        newpoint.append(coord(x, y, who))
                        if otherposs < other:
                            list.remove(who)
                            who2 = list[0]
                            newpoint.append(coord(x, y, who2))
                    else:
                        other = poss % 1
                        otherposs = rd.uniform(0, 1)
                        if otherposs < other:
                            b = rd.choices(list)
                            who2 = b[0]
                            newpoint.append(coord(x, y, who2))
                if y == 0:
                    dead = points[i][2]
                    poss = np.random.normal(1.00, 0.004)
                    list = [4, 6, 7]
                    list.remove(dead)
                    if poss >= 1:
                        b = rd.choices(list)
                        who = b[0]
                        other = poss % 1
                        otherposs = rd.uniform(0, 1)
                        newpoint.append(coord(x, y, who))
                        if otherposs < other:
                            list.remove(who)
                            who2 = list[0]
                            newpoint.append(coord(x, y, who2))
                    else:
                        other = poss % 1
                        otherposs = rd.uniform(0, 1)
                        if otherposs < other:
                            b = rd.choices(list)
                            who2 = b[0]
                            newpoint.append(coord(x, y, who2))
                if y > 0 and y < 999:
                    dead = points[i][2]
                    poss = np.random.normal(1.00, 0.004)
                    list = [6,7, 8,4, 5]
                    list.remove(dead)
                    if poss >= 1:
                        b = rd.choices(list)
                        who = b[0]
                        other = poss % 1
                        otherposs = rd.uniform(0, 1)
                        newpoint.append(coord(x, y, who))
                        if otherposs < other:
                            list.remove(who)
                            b = rd.choices(list)
                            who2 = b[0]
                            newpoint.append(coord(x, y, who2))
                    else:
                        other = poss % 1
                        otherposs = rd.uniform(0, 1)
                        if otherposs < other:
                            b = rd.choices(list)
                            who2 = b[0]
                            newpoint.append(coord(x, y, who2))
            elif y == 999 and x >0 and x < 999:
                dead = points[i][2]
                poss = np.random.normal(1.00, 0.004)
                list = [2, 7, 8, 3, 5]
                list.remove(dead)
                if poss >= 1:
                    b = rd.choices(list)
                    who = b[0]
                    other = poss % 1
                    otherposs = rd.uniform(0, 1)
                    newpoint.append(coord(x, y, who))
                    if otherposs < other:
                        list.remove(who)
                        b = rd.choices(list)
                        who2 = b[0]
                        newpoint.append(coord(x, y, who2))
                else:
                    other = poss % 1
                    otherposs = rd.uniform(0, 1)
                    if otherposs < other:
                        b = rd.choices(list)
                        who2 = b[0]
                        newpoint.append(coord(x, y, who2))
            elif y == 0 and x >0 and x < 999 :
                dead = points[i][2]
                poss = np.random.normal(1.00, 0.004)
                list = [1, 2, 6, 4, 7]
                list.remove(dead)
                if poss >= 1:
                    b = rd.choices(list)
                    who = b[0]
                    other = poss % 1
                    otherposs = rd.uniform(0, 1)
                    newpoint.append(coord(x, y, who))
                    if otherposs < other:
                        list.remove(who)
                        b = rd.choices(list)
                        who2 = b[0]
                        newpoint.append(coord(x, y, who2))
                else:
                    other = poss % 1
                    otherposs = rd.uniform(0, 1)
                    if otherposs < other:
                        b = rd.choices(list)
                        who2 = b[0]
                        newpoint.append(coord(x, y, who2))
    return newpoint

def kill_make():
    a=1

def killer_function(data):
    a=1




