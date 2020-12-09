import math

words = ["mathematic", "physic", "hemi"]
Alphabeth = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A = len(Alphabeth)


def GetSymbolID(char):
    return Alphabeth.index(str(char).upper())

def GeneratePassword(word1,word2,word3):
    passwd = ""

    ##Первый символ
    if(len(word1)%2 == 1):
        #Индекс середины третьего слова
        ID = GetSymbolID(word3[math.ceil(len(word3)/2)])
        addsymbol = Alphabeth[(ID + 3)%A]

        if addsymbol == 'z':
            addsymbol = 'a'
        passwd += addsymbol
    else:
        #Индекс первого серединного элемента первого слова
        ID = GetSymbolID(word1[math.ceil(len(word1)/2 - 1)])

        #Предшествующий сивмол
        ID-=1
        addsymbol = Alphabeth[(ID)%A]

        if addsymbol == 'a':
            addsymbol = 'z'
        passwd += addsymbol

    ##Второй символ
    #Индекс последнего символа второго слова
    ID = GetSymbolID(word2[len(word2)-1])
    ID-=1
    addsymbol = Alphabeth[(ID)%A]
    if addsymbol == 'a':
        addsymbol = 'z'
    passwd += addsymbol

    ##Третий символ
    #Индекс первого символа третьего слова
    ID = GetSymbolID(word3[0])
    addsymbol = Alphabeth[(ID + 1)%A]
    if addsymbol == 'z':
        addsymbol = 'a'
    passwd += addsymbol
        
    ##Четвертый символ
    #Элемент с индексом суммы длин первого и второго слова - 1
    #
    addsymbol = Alphabeth[(len(word1)+len(word2))%26-1]
    passwd += addsymbol

    return passwd

passwd = GeneratePassword(words[0],words[1],words[2])
print(f"{passwd} - ваш пароль")

InputPasswd = input('Введите ваш пароль ')
if(InputPasswd == passwd):
    print('Успешный вход. Добро пожаловать')
else:
    print('Неудача')
    
