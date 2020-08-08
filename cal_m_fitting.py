# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:50:53 2020

@author: 足立
"""
import math
import matplotlib.pyplot as plt

#フィッティングしたい磁場と横軸のリストを準備
#以下では[]で定義されているが実際はファイルから読み込むなり自分で作るなりする必要がある
z_list = []
B_list = []

#理想的な磁場分布の作成
#下に示しているMの値がフィッティングの結果で出るはず
M = 2.0
for i in range(1000):
    z = i*0.001
    z_list.append(z)
    B_list.append(math.exp(M*z))

#フィッティングした結果を入れる配列を準備する
#磁場の値によってはうまくフィッティングできない場合があり、その部分のデータを飛ばす操作をするため
#計算結果のデータ数が入力データと異なる場合が出てくる
#例)expのフィッティングを行う際にlnを取っている場合、磁場が0の値をとっているとエラーとなる
#   負の磁場の場合は別で対応している
y_list = []
m_list = []

#以下のルーチンはexp(my)でフィッティングするルーチン
num   = 9 #フィッティングの点数
text  = []
text.append('y [m], By [T], m [1/m]\n')
for i in range(len(B_list)-(num-1)):                            #フィッティングの点数分だけ末尾のデータが使用できないため(d_l[0])-(num-1)となっている
    check = 0
    for j in range(num):
        if B_list[i+j] == 0:
            check = 1
    if check == 0:
        SUM = [0,0,0,0,0,0]                                         #それぞれの総和の初期化
        for j in range(num):                                        #(num)点フィッティング
            SUM[0] += z_list[j]                                     #(num)点のzの総和
            SUM[1] += (z_list[j])**2.0                              #(num)点のzの二乗の総和
            SUM[2] += math.log(abs(B_list[i+j]))                    #(num)点の磁場の総和(開始位置をずらすために[i+j]としている)。logをとっているのはlinearにするため
            SUM[3] += z_list[j]*math.log(abs(B_list[i+j]))          #(num)点の磁場とzの総和
        #線形最小二乗法(ウィキに書いてある式)から(y=bx+a)のうち傾きbを求めている。このbがm値に対応する
        b = (1.0*num*SUM[3] - SUM[0]*SUM[2])    /(1.0*num*SUM[1] - (SUM[0])**2.0)

        y_list.append(z_list[i])
        m_list.append(b)


plt.plot(y_list, m_list)
plt.ylim(0,4)

#tableファイルの生成
#new_file = open(header + filename+'.csv','w')
#new_file.writelines(text)
#new_file.close()
