import random
numMag=2 #random.randint(1, 9)
tenta=int(input("Tente advinhar o número mágico: "))
if numMag == tenta:
    print('Parabéns, você acertou!')
else:
    print('Tente novamente.')