import numpy as np
import scipy
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd

with open('datay.csv', 'r') as f:
    content = f.readlines()
# print(content[1])
# print(len(content))

# Y=[]
# X=[]
# for i in range(1, len(content)):
#     content[i] = content[i].strip('\n')
#     content[i] = content[i].split('[')
#     content[i].pop()
#     content[i] = content[i][0].split(',')
#     content[i].pop()
#     x1=[]
#     y1=[]
#     for j in range(2,len(content[i])):
#         x1.append(j-1)
#         y1.append(float(content[i][j])/float(content[i][len(content[i])-1]))
#     X.append(x1)
#     Y.append(y1)

Y=[]
X=[]
# for i in range(0, len(content)):
#     a=[]
#     content[i] = content[i].strip('\n')
#     content[i] = content[i].split('[')
#     content[i].pop()
#     content[i] = content[i][0].split(',')
#     content[i].pop()
#     x1=[]
#     y1=[]
#     for j in range(2,len(content[i])):
#         x1.append(j-1)
#         y1.append((float(content[i][j])-float(content[i][2]))/(float(content[i][len(content[i])-1])-float(content[i][2])))
#     X.append(x1)
#     Y.append(y1)

for i in range(1, 11):
    content[i] = content[i].strip('\n')
    content[i] = content[i].split('[')
    content[i].pop()
    content[i] = content[i][0].split(',')
    content[i].pop()
    x1=[]
    y1=[]
    for j in range(2,len(content[i])):
        x1.append(j-1)
        y1.append((float(content[i][j])-float(content[i][2]))/(float(content[i][len(content[i])-1])-float(content[i][2])))
    X.append(x1)
    Y.append(y1)
f.close()
with open('datayy2.csv', 'r') as f:
    content = f.readlines()
Y1=[]
X1=[]
for i in range(1, 11):
    content[i] = content[i].strip('\n')
    content[i] = content[i].split('[')
    content[i].pop()
    content[i] = content[i][0].split(',')
    content[i].pop()
    x1=[]
    y1=[]
    for j in range(2,len(content[i])):
        x1.append(j-1)
        y1.append((float(content[i][j])-float(content[i][2]))/(float(content[i][len(content[i])-1])-float(content[i][2])))
    X1.append(x1)
    Y1.append(y1)

f.close()
plt.figure(figsize=(5,4))
for i in range(len(Y)):
    plt.step(Y[i],X[i], color='red')
    #plt.step(Y1[i],X1[i], label='replication 2', color='blue')
    # plt.show()
    plt.step(Y1[i], X1[i], color='blue')
plt.step(Y[i],X[i], label='replication 1', color='red')
plt.step(Y1[i], X1[i], label='replication 2', color='blue')
plt.xlabel('Normalized time')
plt.ylabel('Cumulative number of crimes',fontsize=10.0)
plt.legend()
plt.show()
# r=[10,100,500,1000]
# print(len(r))
# print(len(Y))
# print(len(X))
# plt.figure(figsize=(8.5,4))
# for i in range(len(r)):
#     plt.step(Y[i], X[i],label=r[i])
#     plt.legend()
# plt.xlabel('Normalized time')
# plt.ylabel('Cumulative number of crimes',fontsize=10.0)
# plt.title('Different Number of Initial Fired Neurons')
# plt.savefig("randomness.png")
# plt.show()

#     ax1.legend()
# print(X,Y)
# for i in range(12):
#     fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
#     ax1.step(Y[0+i], X[0+i], label='0.05')
#     ax1.legend()
#     ax2.step(Y[1+i], X[1+i], label='0.1')
#     ax2.legend()
#     ax3.step(Y[2+i], X[2+i], label='0.15')
#     ax3.legend()
#     ax4.step(Y[3+i], X[3+i], label='0.2')
#     ax4.legend()
#     fig.suptitle(i)
#     # plt.savefig(str(i))
#     plt.show()


# X20=[]
# Y20=[]
# for i in range(len(Y)):
#     xx=[]
#     yy=[]
#     for j in range(20):
#         xx.append(X[i][j])
#         yy.append(Y[i][j]/Y[i][20])
#     X20.append(xx)
#     Y20.append(yy)
# #
# test=pd.DataFrame(data=Y20)
# print(test)
# test.to_csv('datay_N.csv',encoding='gbk')

# for i in range(1):
#     fig, (ax1, ax2,ax3, ax4,ax5) = plt.subplots(5, 1)
#     ax1.step(Y20[0+i], X20[0+i], label='0.05')
#     ax1.legend()
#     ax2.step(Y20[1+i], X20[1+i], label='0.1')
#     ax2.legend()
#     ax3.step(Y20[2+i], X20[2+i], label='0.15')
#     ax3.legend()
#     ax4.step(Y20[3+i], X20[3+i], label='0.2')
#     ax4.legend()
#     ax5.step(Y20[4 + i], X20[4 + i], label='0.25')
#     ax5.legend()
#     fig.suptitle("1_5_180")
#     plt.show()

# ii=[0,10]
# print(Y)
# plt.step(Y[0],X[0])
# plt.step(Y[10],X[10])
# plt.show()
# for i in range(1):
#     fig, ((ax1, ax2), (ax3, ax4),(ax5, ax6),(ax7, ax8),(ax9, ax10)) = plt.subplots(5, 2)
#     ax1.step(Y[0+i], X[0+i], label='0.05_1')
#     ax1.step(Y[10+i], X[10+i], label='0.05_2')
#     ax1.legend()
#     ax2.step(Y[1+i], X[1+i], label='0.1_1')
#     ax2.step(Y[11 + i], X[11 + i], label='0.1_2')
#     ax2.legend()
#     ax3.step(Y[2+i], X[2+i], label='0.15_1')
#     ax3.step(Y[12 + i], X[12 + i], label='0.15_2')
#     ax3.legend()
#     ax4.step(Y[3+i], X[3+i], label='0.2_1')
#     ax4.step(Y[13 + i], X[13 + i], label='0.2_2')
#     ax4.legend()
#     ax5.step(Y[4+i], X[4+i], label='0.25_1')
#     ax5.step(Y[14 + i], X[14 + i], label='0.25_2')
#     ax5.legend()
#     ax6.step(Y[5 + i], X[5 + i], label='0.3_1')
#     ax6.step(Y[15 + i], X[15 + i], label='0.3_2')
#     ax6.legend()
#     ax7.step(Y[6 + i], X[6 + i], label='0.35_1')
#     ax7.step(Y[16 + i], X[16 + i], label='0.35_2')
#     ax7.legend()
#     ax8.step(Y[7 + i], X[7 + i], label='0.40_1')
#     ax8.step(Y[17 + i], X[17 + i], label='0.40_2')
#     ax8.legend()
#     ax9.step(Y[8 + i], X[8 + i], label='0.45_1')
#     ax9.step(Y[18 + i], X[18 + i], label='0.45_2')
#     ax9.legend()
#     ax10.step(Y[9 + i], X[9 + i], label='0.5_1')
#     ax10.step(Y[19 + i], X[19 + i], label='0.5_2')
#     ax10.legend()
#     fig.suptitle("Simulation Replications")
    # plt.xlabel('Normalized time')
    # plt.ylabel('Cumulative number of crimes',fontsize=10.0)
    # fig.text(0.5, 0.04, 'Normalized time', ha='center')
    # fig.text(0.04, 0.5, 'Cumulative number of crimes', va='center', rotation='vertical')
    # plt.show()
#
# ii=[0,10,20]
# for i in range(1):
#     fig, ((ax1, ax2), (ax3, ax4),(ax5, ax6),(ax7, ax8),(ax9, ax10)) = plt.subplots(5, 2)
#     ax1.step(Y20[0+i], X20[0+i], label='0.05')
#     ax1.legend()
#     ax2.step(Y20[1+i], X20[1+i], label='0.1')
#     ax2.legend()
#     ax3.step(Y20[2+i], X20[2+i], label='0.15')
#     ax3.legend()
#     ax4.step(Y20[3+i], X20[3+i], label='0.2')
#     ax4.legend()
#     ax5.step(Y20[4 + i], X20[4 + i], label='0.25')
#     ax5.legend()
#     ax6.step(Y20[5 + i], X20[3 + i], label='0.3')
#     ax6.legend()
#     ax7.step(Y20[6 + i], X20[3 + i], label='0.35')
#     ax7.legend()
#     ax8.step(Y20[7 + i], X20[3 + i], label='0.40')
#     ax8.legend()
#     ax9.step(Y20[8 + i], X20[3 + i], label='0.45')
#     ax9.legend()
#     ax10.step(Y20[9 + i], X20[3 + i], label='0.5')
#     ax10.legend()
#     fig.suptitle("10_10_90")
#     plt.show()





