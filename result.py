import matplotlib.pyplot as plt
import numpy as np
import random
from scipy import optimize
with open('final1.csv', 'r') as f:
    content = f.readlines()

r=[]
s=[]
e=[]
for i in range(len(content)):
    content[i] = content[i].strip('\n')
    content[i] = content[i].split(',')
    if i == 0:
        for j in range(len(content[i])):
            r.append(float(content[i][j]))
    if i == 1:
        for j in range(len(content[i])):
            s.append(float(content[i][j]))
    if i == 2:
        for j in range(len(content[i])):
            e.append(float(content[i][j]))
print(len(r))
print(len(s))
print(len(e))
rr=[]
ss=[]
ee=[]
for i in range(len(r)):
    if (r[i] < 0.5 and e[i] < 0.01):
        rr.append(r[i])
        ss.append(s[i])
        ee.append(e[i])

print(len(rr))
print(len(ss))
print(len(ee))
# for i in range(len(r)):
#     plt.scatter(r[i],s[i])
# def f_1(x, A, B):
#     return A*x + B
#
# def f_2(x, A, B, C):
#     return A*x*x + B*x + C
#
# def f_3(x, A, B, C, D):
#     return A*x*x*x + B*x*x + C*x + D
plt.figure(figsize=(7,7))
plt.scatter(rr,ss)
plt.errorbar(rr,ss,yerr=ee,fmt='o',ecolor='r',color='b',elinewidth=2,capsize=4)
# A1, B1 = optimize.curve_fit(f_1, rr, ss)[0]
# print(A1)
# print(B1)
# x1 = np.arange(0, 0.25, 0.001)
# y1 = A1*x1 + B1
# plt.plot(x1, y1, "green")
# A2, B2, C2 = optimize.curve_fit(f_2, r, s)[0]
# x2 = np.arange(0, 0.05, 0.01)
# y2 = A2*x2*x2 + B2*x2 + C2
# plt.plot(x2, y2, "green")
# A3, B3, C3, D3= optimize.curve_fit(f_3, r, s)[0]
# x3 = np.arange(0, 6, 0.01)
# y3 = A3*x3*x3*x3 + B3*x3*x3 + C3*x3 + D3
# plt.plot(x3, y3, "purple")
plt.xlim(xmax=0.05,xmin=0)
plt.ylim(ymax=0.05,ymin=0)
# plt.yticks(np.arange(0,0.25,step=5))
# plt.xticks(np.arange(0,1,step=5))
plt.xlabel('Real')
plt.ylabel('Simulation',fontsize=10.0)
plt.show()