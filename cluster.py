import numpy as np
import scipy
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd

with open('datayN_cl.csv', 'r') as f:
    content = f.readlines()

y1=[] ; y2=[] ;y3=[] ; y4=[]; y5=[];
for i in range(len(content)):
    content[i] = content[i].strip('\n')
    content[i] = content[i].split(',')
    if int(content[i][1]) == 1:
        y1.append(int(content[i][0]))
    if int(content[i][1]) == 2:
        y2.append(int(content[i][0]))
    if int(content[i][1]) == 3:
        y3.append(int(content[i][0]))
    if int(content[i][1]) == 4:
        y4.append(int(content[i][0]))
    if int(content[i][1]) == 5:
        y5.append(int(content[i][0]))
f.close()

with open('datayy2N_cl.csv', 'r') as f:
    content1 = f.readlines()

y11=[] ; y22=[] ;y33=[] ; y44=[]; y55=[];
for i in range(len(content1)):
    content1[i] = content1[i].strip('\n')
    content1[i] = content1[i].split(',')
    if int(content1[i][1]) == 1:
        y11.append(int(content1[i][0]))
    if int(content1[i][1]) == 2:
        y22.append(int(content1[i][0]))
    if int(content1[i][1]) == 3:
        y33.append(int(content1[i][0]))
    if int(content1[i][1]) == 4:
        y44.append(int(content1[i][0]))
    if int(content1[i][1]) == 5:
        y55.append(int(content1[i][0]))
f.close()

# print(len(y1))
# print(len(y2))
# print(len(y3))
# print(len(y4))
# print(len(y5))

with open('datay.csv', 'r') as f:
    content = f.readlines()
X=[]
Y=[]
for i in range(1, len(content)):
    a=[]
    content[i] = content[i].strip('\n')
    content[i] = content[i].split('[')
    content[i].pop()
    content[i] = content[i][0].split(',')
    content[i].pop()
    xx=[]
    yx=[]
    for j in range(2,23):
        xx.append(j-1)
        # yx.append(float(content[i][j])-float(content[i][2]))
        yx.append((float(content[i][j]) - float(content[i][2])) / (
                    float(content[i][len(content[i]) - 1]) - float(content[i][2])))
    X.append(xx)
    Y.append(yx)
f.close()

with open('datayy2.csv', 'r') as f:
    content = f.readlines()
X2=[]
Y2=[]
for i in range(1, len(content)):
    a=[]
    content[i] = content[i].strip('\n')
    content[i] = content[i].split('[')
    content[i].pop()
    content[i] = content[i][0].split(',')
    content[i].pop()
    xx=[]
    yx=[]
    for j in range(2,23):
        xx.append(j-1)
        # yx.append(float(content[i][j])-float(content[i][2]))
        yx.append((float(content[i][j]) - float(content[i][2])) / (
                    float(content[i][len(content[i]) - 1]) - float(content[i][2])))
    X2.append(xx)
    Y2.append(yx)
f.close()
# for i in range(0, len(content)):
#     content[i] = content[i].strip('\n')
#     # content[i] = content[i].split('[')
#     # content[i].pop()
#     content[i] = content[i].split(',')
#     # content[i].pop()
#     xx=[]
#     yx=[]
#     for j in range(len(content[i])):
#         xx.append(j+1)
#         yx.append(float(content[i][j]))
#     X.append(xx)
#     Y.append(yx)
# print(len(X))
#
# X51=[]
# Y51=[]
# for i in range(len(Y)):
#     xx=[]
#     yy=[]
#     for j in range(5):
#         xx.append(X[i][j])
#         yy.append(Y[i][j]/Y[i][4])
#     X51.append(xx)
#     Y51.append(yy)
# X52=[]
# Y52=[]
# for i in range(len(Y2)):
#     xx=[]
#     yy=[]
#     for j in range(5):
#         xx.append(X2[i][j])
#         yy.append(Y2[i][j]/Y2[i][4])
#     X52.append(xx)
#     Y52.append(yy)
#
# for i in y1:
#     plt.step(Y[i-1],X[i-1])
# plt.show()
# for i in y2:
#     plt.step(Y[i - 1], X[i - 1])
# plt.show()
# for i in y3:
#     plt.step(Y[i - 1], X[i - 1])
# plt.show()
# for i in y4:
#     plt.step(Y[i - 1], X[i - 1])
# plt.show()
# for i in y5:
#     plt.step(Y[i - 1], X[i - 1])
# plt.show()
# for i in y6:
#     plt.step(Y[i - 1], X[i - 1])
# plt.show()
#

fig, ((ax1, ax2), (ax3, ax4),(ax5, ax6),(ax7, ax8),(ax9, ax10)) = plt.subplots(5, 2)
fig.set_size_inches(5.5,9.5)
for i in y1:
    ax1.step(Y[i-1], X[i-1], label='1')
for i in y44:
    ax2.step(Y2[i-1], X2[i-1], label='1')

for i in y2:
    ax3.step(Y[i-1], X[i-1], label='1')
for i in y22:
    ax4.step(Y2[i-1], X2[i-1], label='1')

for i in y3:
    ax5.step(Y[i - 1], X[i - 1], label='1')
for i in y55:
    ax6.step(Y2[i - 1], X2[i - 1], label='1')

for i in y4:
    ax7.step(Y[i - 1], X[i - 1], label='1')

for i in y11:
    ax8.step(Y2[i - 1], X2[i - 1], label='1')

for i in y5:
    ax9.step(Y[i - 1], X[i - 1], label='1')

for i in y33:
    ax10.step(Y2[i - 1], X2[i - 1], label='1')

fig.suptitle("Simulation Replications")
fig.text(0.5, 0.04, 'Normalized time', ha='center')
fig.text(0.04, 0.5, 'Cumulative number of crimes', va='center', rotation='vertical')
# plt.savefig("sr.png")
plt.show()
# for i in y1:
#     plt.step(Y20[i-1],X20[i-1])
# plt.show()
# for i in y2:
#     plt.step(Y20[i - 1], X20[i - 1])
# plt.show()
# for i in y3:
#     plt.step(Y20[i - 1], X20[i - 1])
# plt.show()
# for i in y4:
#     plt.step(Y20[i - 1], X20[i - 1])
# plt.show()
# for i in y5:
#     plt.step(Y20[i - 1], X20[i - 1])
# plt.show()
# for i in y6:
#     plt.step(Y20[i - 1], X20[i - 1])
# plt.show()
