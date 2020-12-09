import math
import random

def S(V,T,P):
    return math.ceil(V*T/P)

def FindPassLength(AlphabethLength, V, T, P):
    #Длина пароля, удовлетворяющая условию
    foundLength = 1
    while(math.pow(AlphabethLength,foundLength) < S(V, T, P)):
        foundLength+=1
    return foundLength

def GeneratePassword(PassLength, Alphabeth):
    passwd = ""
    for i in range(PassLength):
        passwd += Alphabeth[random.randint(0,len(Alphabeth)-1)]
    return passwd

def GetTime(AlphLen, PassLen, P, V):
    return AlphLen**PassLen * P / V

#Вероятность подбора
P = 1e-7
#Количество паролей за 1 день при 11 в минуту
V = 11*60*24
#Время в днях
T = 6
#Длина алфавита
Alphabeth = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A = len(Alphabeth)


L = FindPassLength(A, V, T, P)
print("{0} - длина пароля удовлетворяющая условиям".format(L))

passwd = GeneratePassword(L,Alphabeth)
print("{0} - ваш пароль".format(passwd))

time = GetTime(A, L, P, V)
print("{0} - время взлома".format(time))
