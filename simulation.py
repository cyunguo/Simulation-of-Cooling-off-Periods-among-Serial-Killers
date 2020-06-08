import numpy as np
import matplotlib.pyplot as plt
import random as rd
import Scripts.killcure as kl
import pandas as pd
import math as mt

rddd=0.1

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

def fire(points):
    num=len(points)
    newpoint=[]
    for i in range(num):
        x=points[i][0]
        y=points[i][1]
        if x < 999 and x > 0 and y < 999 and y >0:
            dead=points[i][2]
            poss=np.random.normal(1.0047,0.1)
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
                    poss = np.random.normal(1.0047, 0.1)
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
                    poss = np.random.normal(1.0047, 0.1)
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
                if y > 0 and y < 999:
                    dead = points[i][2]
                    poss = np.random.normal(1.0047, 0.1)
                    list = [1,2, 3,4, 5]
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
                    poss = np.random.normal(1.0047, 0.1)
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
                    poss = np.random.normal(1.0047, 0.1)
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
                    poss = np.random.normal(1.0047, 0.1)
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
            if y == 999 and x > 0 and x < 999:
                dead = points[i][2]
                poss = np.random.normal(1.0047, 0.1)
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
            if y == 0 and x >0 and x < 999:
                dead = points[i][2]
                poss = np.random.normal(1.0047, 0.1)
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

def plots(fire,dead):
    data = np.zeros([1000,1000])
    data=data+128
    for i in range(len(fire)):
        x=fire[i][0]
        y=fire[i][1]
        data[x][y] = 0
    for i in range(len(dead)):
        x=dead[i][0]
        y=dead[i][1]
        data[x][y] = 254
    plt.imshow(data,cmap='bwr')
    plt.show()

def effect(fire,kill):
    data = np.zeros([1000,1000])
    data=data+254
    firen=[]

    for i in range(len(kill)):
        x = kill[i][0]
        y = kill[i][1]
        data[x][y]=60

    for i in range(len(fire)):
        x=fire[i][0]
        y=fire[i][1]
        if x == 1000 or y == 1000:
            print(x,y)
        if data[x][y]!=60:
            data[x][y] = 0
            firen.append(fire[i])

    #plt.imshow(data,cmap='gist_ncar')
    #plt.show()
    return firen

data = np.zeros([1000,1000])
firedata=[]
killdata=[]

N_FIRE=50000
N_CURE=50000
N_TIME=90
N_DECRE=0.05
Period=[]

N=0



while N_FIRE <= 50000.001:
    while N_CURE <= 50000.001:
        while N_TIME <= 90.001:
            while N_DECRE <= 0.501:
                for i in range(1000):
                    x = rd.randint(1, 998)
                    y = rd.randint(1, 998)
                    firedata.append([x, y, 1])

                while N <= N_FIRE:
                    firedata = fire(firedata)
                    N = len(firedata)
                N=0
                count = 0
                count1= 0
                last=[]
                i = 0
                decre=N_TIME
                last.append(0)
                while count<=20:
                    firedata=fire(firedata)
                    if len(firedata) > N_FIRE:
                        for c in range(N_CURE):
                            x1 = rd.randint(1, 998)
                            y1 = rd.randint(1, 998)
                            killdata.append([x1, y1, 1])
                        count=count+1
                        last.append(i)
                        if (last[count]-last[count-1]) == 1:
                            count1+=1
                        for k in range(round(decre* mt.pow((1-N_DECRE),(count-1)))):
                            firedata = fire(firedata)
                            killdata = kl.kill(killdata)
                            firedata = effect(firedata, killdata)
                            #print(len(firedata))
                            i = i + 1
                            if len(firedata) > N_FIRE:
                                for c in range(N_CURE):
                                    x1 = rd.randint(1, 998)
                                    y1 = rd.randint(1, 998)
                                    killdata.append([x1, y1, 1])
                                count = count + 1
                                last.append(i)
                                if (last[count] - last[count - 1]) == 1:
                                    count1 += 1
                                for z in range(round(decre* mt.pow((1-N_DECRE),(count-1)))):
                                    firedata = fire(firedata)
                                    killdata = kl.kill(killdata)
                                    firedata = effect(firedata, killdata)
                                    #print(len(firedata))
                                    i = i + 1
                        killdata=[]
                        decre=decre*(1-N_DECRE)
                    i=i+1
                last.append([N_FIRE, N_CURE, N_TIME, N_DECRE])
                N_DECRE +=0.05
                print(N_DECRE)
                Period.append(last)
                firedata=[]
            N_DECRE = 0.05
            N_TIME+=30
        N_DECRE = 0.05
        N_TIME = 30
        N_CURE+=90000
    N_DECRE = 0.05
    N_TIME  = 30
    N_CURE  = 10000
    N_FIRE+=90000

print(Period)

file=pd.DataFrame(data=Period)
file.to_csv("./data.csv")





