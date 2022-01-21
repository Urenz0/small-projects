import random
import time

print('|===================================================|')
print('Olá, seja bem-vindo ao advinhador de número \nSeu objetivo é escolher o mesmo número que o robô ED.')
print('|===================================================|')

limite = input('Defina o limite: ')
print('|===================================================|')

if limite.isdigit(): #verifica se o limite é um numero
    limite = int(limite)

    if limite <= 0:
        print('Tente números maiores da próxima vez. Encerrando o programa!')
        time.sleep(2)
        quit()
else:
    print('OPCAO INVÁLIDA. POR FAVOR, REINICIE O PROGRAMA!')
    time.sleep(2)
    quit()

numero_ed = random.randint(1,limite)

while True:
    numero_user = input('Faça sua aposta: ')
    
    if numero_user.isdigit():
        numero_user = int(numero_user)
    else:
        print('Por favor, insira um número inteiro')
        continue

    if numero_user < 1:
        print('Tente números maiores que 0 :)')
        continue
    if numero_user > limite:
        print(f'Número acima do limite, por favor escolha números menores ou igual a {limite}')
    elif numero_user == numero_ed:
        print(f'Parabéns! Você e ED escolheram o número {numero_user}!')
        break
    else:
        print('Não foi dessa vez, tente novamente!')

print('\n|===================================================|')
print('Robô ED agradece por você brincar com ele!')
print('Até a próxima!!!')
print('|===================================================|')
time.sleep(3)
quit()
        


    
