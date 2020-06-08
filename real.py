import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

with open('Book3 .csv', 'r') as f:
    content = f.readlines()
# print(content)
# a=numpy.array(content[0])
# print(a)
# x = numpy.array(range(1, len(content[0])+1))
# print(x)
X=[]
Y=[]
# for i in range(0, len(content)):
#     content[i] = content[i].strip('\n')
#     content[i] = content[i].split(',')
#     x=[]
#     y=[]
#     num=0
#     for j in range(1, len(content[i])):
#         if content[i][j]!='':
#             x.append(j)
#             y.append(num+float(content[i][j]))
#             num+=float(content[i][j])
#     for j in range(len(x)):
#         y[j]=y[j]/num
#     X.append(x)
#     Y.append(y)
    # ww = numpy.polyfit(x, numpy.log(y), 1)
#for i in range(len(X)):
    #plt.step(Y[i],X[i])
    #plt.show()

for i in range(0, len(content)):
    content[i] = content[i].strip('\n')
    content[i] = content[i].split(',')
    x=[]
    y=[]
    num=0
    for j in range(0, len(content[i])):
        if content[i][j]!='':
            x.append(j+1)
            y.append(num+float(content[i][j]))
            num += float(content[i][j])
    X.append(x)
    Y.append(y)

# for i in range(len(X)):
#     plt.step(Y[i],X[i])
#     plt.show()
#
X20=[]
Y20=[]
for i in range(len(Y)):
    for j in range(len(Y[i])):
        Y[i][j] = Y[i][j]/Y[i][len(Y[i])-1]

# test=pd.DataFrame(data=Y)
# print(test)
# test.to_csv('r2.csv',encoding='gbk')
#
# i1=[0,3,4,7,8,9,10,13,17,19,21,22,27]
# i2=[1,2,6,15,16,18,24]
# i3=[25,26,28]
# i4=[5,11,12,14,20,23]
# for i in i1:
#     plt.step(Y[i],X[i])
# plt.xlabel('Normalized time')
# plt.ylabel('Cumulative number of crimes',fontsize=10.0)
# # plt.savefig("%d_111.png" %i)
# plt.show()
# for i in i2:
#     plt.step(Y[i],X[i])
# plt.xlabel('Normalized time')
# plt.ylabel('Cumulative number of crimes',fontsize=10.0)
# # plt.savefig("%d_222.png" %i)
# plt.show()
# for i in i3:
#     plt.step(Y[i],X[i])
# plt.xlabel('Normalized time')
# plt.ylabel('Cumulative number of crimes',fontsize=10.0)
# # plt.savefig("%d_333.png" %i)
# plt.show()
# for i in i4:
#     plt.step(Y[i],X[i])
# plt.xlabel('Normalized time')
# plt.ylabel('Cumulative number of crimes',fontsize=10.0)
# # plt.savefig("%d_444.png" %i)
# plt.show()

# i1=[0,9,11,17,18]
# i2=[1,2,3,4,7,10,12,14,15,19]
# i3=[5,6,8,13,16]
# for i in i1:
#     plt.step(Y20[i],X20[i])
# plt.savefig("%d_111.png" %i)
# plt.show()
# for i in i2:
#     plt.step(Y20[i],X20[i])
# plt.savefig("%d_222.png" %i)
# plt.show()
# for i in i3:
#     plt.step(Y20[i],X20[i])
# plt.savefig("%d_333.png" %i)
# plt.show()
# y333=[]
# x333=[]
# for i in range(20):
#     y333.append(Y[2][i])
#     x333.append(i+1)
# plt.step(y333,x333)
# plt.show()


for i in range(len(Y)):
    plt.step(Y[i],X[i])
    plt.xlabel('Normalized time')
    plt.ylabel('Cumulative number of crimes',fontsize=10.0)
    plt.show()