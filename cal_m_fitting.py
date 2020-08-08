# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:50:53 2020

@author: ����
"""
import math
import matplotlib.pyplot as plt

#�t�B�b�e�B���O����������Ɖ����̃��X�g������
#�ȉ��ł�[]�Œ�`����Ă��邪���ۂ̓t�@�C������ǂݍ��ނȂ莩���ō��Ȃ肷��K�v������
z_list = []
B_list = []

#���z�I�Ȏ��ꕪ�z�̍쐬
#���Ɏ����Ă���M�̒l���t�B�b�e�B���O�̌��ʂŏo��͂�
M = 2.0
for i in range(1000):
    z = i*0.001
    z_list.append(z)
    B_list.append(math.exp(M*z))

#�t�B�b�e�B���O�������ʂ�����z�����������
#����̒l�ɂ���Ă͂��܂��t�B�b�e�B���O�ł��Ȃ��ꍇ������A���̕����̃f�[�^���΂���������邽��
#�v�Z���ʂ̃f�[�^�������̓f�[�^�ƈقȂ�ꍇ���o�Ă���
#��)exp�̃t�B�b�e�B���O���s���ۂ�ln������Ă���ꍇ�A���ꂪ0�̒l���Ƃ��Ă���ƃG���[�ƂȂ�
#   ���̎���̏ꍇ�͕ʂőΉ����Ă���
y_list = []
m_list = []

#�ȉ��̃��[�`����exp(my)�Ńt�B�b�e�B���O���郋�[�`��
num   = 9 #�t�B�b�e�B���O�̓_��
text  = []
text.append('y [m], By [T], m [1/m]\n')
for i in range(len(B_list)-(num-1)):                            #�t�B�b�e�B���O�̓_�������������̃f�[�^���g�p�ł��Ȃ�����(d_l[0])-(num-1)�ƂȂ��Ă���
    check = 0
    for j in range(num):
        if B_list[i+j] == 0:
            check = 1
    if check == 0:
        SUM = [0,0,0,0,0,0]                                         #���ꂼ��̑��a�̏�����
        for j in range(num):                                        #(num)�_�t�B�b�e�B���O
            SUM[0] += z_list[j]                                     #(num)�_��z�̑��a
            SUM[1] += (z_list[j])**2.0                              #(num)�_��z�̓��̑��a
            SUM[2] += math.log(abs(B_list[i+j]))                    #(num)�_�̎���̑��a(�J�n�ʒu�����炷���߂�[i+j]�Ƃ��Ă���)�Blog���Ƃ��Ă���̂�linear�ɂ��邽��
            SUM[3] += z_list[j]*math.log(abs(B_list[i+j]))          #(num)�_�̎����z�̑��a
        #���`�ŏ����@(�E�B�L�ɏ����Ă��鎮)����(y=bx+a)�̂����X��b�����߂Ă���B����b��m�l�ɑΉ�����
        b = (1.0*num*SUM[3] - SUM[0]*SUM[2])    /(1.0*num*SUM[1] - (SUM[0])**2.0)

        y_list.append(z_list[i])
        m_list.append(b)


plt.plot(y_list, m_list)
plt.ylim(0,4)

#table�t�@�C���̐���
#new_file = open(header + filename+'.csv','w')
#new_file.writelines(text)
#new_file.close()
