import time

print('Utilize A e a para representar os genes \n')

mãe1 = input('insira um gene da mãe: ')
mãe2 = input('insira um gene da mãe: ')
pai1 = input('insira um gene do pai: ')
pai2 = input('insira um gene do pai: ')
#irá transformar o texto do input em Int
if mãe1 == "A":
    mãe1 = 1
else:
    mãe1 = 0

if mãe2 == "A":
    mãe2 = 1
else:
    mãe2 = 0

if pai1 == "A":
    pai1 = 1
else:
    pai1 = 0

if pai2 == "A":
    pai2 = 1
else:
    pai2 = 0

combinação1 = [mãe1, pai1]
combinação2 = [mãe1, pai2]
combinação3 = [mãe2, pai1]
combinação4 = [mãe2, pai2]

teste1 = sum(combinação1)
teste2 = sum(combinação2)
teste3 = sum(combinação3)
teste4 = sum(combinação4)

#Determina, através do resultado da soma "teste", a combinação de genes
if teste1 == 1:
    print('\nAa')
elif teste1 == 2:
    print('\nAA')
else:
    print('\naa')

if teste2 == 1:
    print('\nAa')
elif teste2 == 2:
    print('\nAA')
else:
    print('\naa')

if teste3 == 1:
    print('\nAa')
elif teste3 == 2:
    print('\nAA')
else:
    print('\naa')
    
if teste4 == 1:
    print('\nAa')
elif teste4 == 2:
    print('\nAA')
else:
    print('\naa')

#Transforma os valores das somas dos genes dominantes e recessivos, determinando se a combinação é dominante ou recessiva. 1 = Dominante e 0 = Recessivo
if teste1 == 1:
    porcentagem1 = 1
elif teste1 == 2:
    porcentagem1 = 1
else:
    porcentagem1 = 0

if teste2 == 1:
    porcentagem2 = 1
elif teste2 == 2:
    porcentagem2 = 1
else:
    porcentagem2 = 0

if teste3 == 1:
    porcentagem3 = 1
elif teste3 == 2:
    porcentagem3 = 1
else:
    porcentagem3 = 0

if teste4 == 1:
    porcentagem4 = 1
elif teste4 == 2:
    porcentagem4 = 1
else:
    porcentagem4 = 0

conta = [porcentagem1, porcentagem2, porcentagem3, porcentagem4]
porcentagem = sum(conta)

#Utiliza do valor total das 'porcentagens' 1,2,3 e 4, para determinar a quantidade de Dominantes presente, printando a porcentagem de cada combinação fenótica
if porcentagem == 0:
    print('\n100% recessivo')
elif porcentagem == 1:
    print('\n75% recessivo e 25% dominante')
elif porcentagem == 2:
    print('\n50% recessivo e 50% dominante')
elif porcentagem == 3:
    print('\n25% recessivo e 75% dominante')
elif porcentagem == 4:
    print('\n100% dominante')
else:
    print('fail')

amostra = [teste1, teste2, teste3, teste4]

dominante1 = amostra.count(1)
dominante2 = amostra.count(2)
dominante = dominante1 + dominante2

recessivo = amostra.count(0)

#Utiliza da informação de quantos recessivos estão presentes no quadro de Punnet para determinar a pluralidade ou singularidade dos recessivos e dominantes
if recessivo <= 1:
    print('\nTemos', recessivo, 'recessivo e', dominante, 'dominantes')
elif recessivo >= 3:
    print('\nTemos', recessivo, 'recessivos e', dominante, 'dominante')
else:
    print('\nTemos', recessivo, 'recessivos e', dominante, 'dominantes')

input('Aperte Enter para sair')