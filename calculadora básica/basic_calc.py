import math
import time

print('|======================================================|')
print('Olá, eu sou Calc, a sua calculadora amiga')
print('Voce me informa os valores e o operador, e eu farei o resto do trabalho :)')
print('|======================================================|')
print('O que você deseja calcular?')

def continuar():
    print('|=============================|')
    print('1 - Novos valores \n2 - Sair')
    escolha = int(input())

    while True:
        if escolha == 1:
            operador()
            break

        if escolha == 2:
            print('Obrigado e volte sempre :)')
            print('O programa se encerrará em breve.')
            time.sleep(4)
            quit()

        else:
            print('OPCÃO INVALIDA')
            continue
        
def operador():
    print('|======================================================================|')
    print('[A]adição \n[S]subtração \n[D]divisão \n[M]multiplicação \n[+]outros')
    print('|======================================================================|')

    while True:
        opcao = input('sua opção: ')

        if opcao == '+':
            mais_operador()

        if opcao == 'A' or opcao == 'a':
            num1 = int(input('Insira o primeiro valor: '))
            num2 = int(input('Insira o segundo valor: '))
            print(f'Resultado da soma: {num1 + num2}')
            break

        if opcao == 'S' or opcao == 's':
            num1 = int(input('Insira o primeiro valor: '))
            num2 = int(input('Insira o segundo valor: '))
            print(f'Resultado da subtração: {num1 - num2}')
            break

        if opcao == 'D' or opcao == 'd':
            num1 = int(input('Insira o primeiro valor: '))
            num2 = int(input('Insira o segundo valor: '))
            escolha = input('Resultado com decimal[d] ou apenas inteiro[i]?')
            while True:
                if escolha == 'D' or escolha == 'd':
                    print(f'Resultado da divisão: {num1 / num2}')
                    break
                if escolha == 'I' or escolha == 'i':
                    print(f'Resultado da divisão inteira: {num1 // num2}')
                    break
                else:
                    print('OPÇÃO INVÁLIDA')
                    continue
            break

        if opcao == 'M' or opcao == 'm':
            num1 = int(input('Insira o primeiro valor: '))
            num2 = int(input('Insira o segundo valor: '))
            print(f'Resultado da multiplicação: {num1 + num2}')
            break

        else:
            print('OPÇÃO INVÁLIDA')
            continue
    
    continuar()

def mais_operador():
    print('|======================================================|')
    print('[F]fatorial \n[L]logaritmo \n[P]potencia \n[V]voltar')
    print('|======================================================|')

    while True:
        opcao = input('sua opcao: ')
        
        if opcao == 'f' or opcao == 'F':
            x = int(input('Insira o valor: '))
            print(f'Resultado: {math.factorial(x)}')
            break

        if opcao == 'l' or opcao =='L':
            x = int(input('Insira o valor: '))
            print('Qual a base? \n[10] \n[2] \n[+]outros')
            base_log = input()

            while True:
                if base_log == '10':
                    print(f'Resultado: {math.log10(x)}')
                    break
                if base_log == '2':
                    print(f'Resultado: {math.log2(x)}')
                    break
                if base_log == '+':
                    y = int(input('Qual a base: '))
                    print(math.log(x[y]))
                    break
                else:
                    print('OPÇÃO INVÁLIDA')
                    continue
            break

        if opcao == 'p' or opcao == 'P':
            x = int(input('Insira o valor: '))
            y = int(input('Potencia de: '))
            print(math.pow(x,y))
            break 
        
        if opcao == 'v' or opcao == 'V':
            operador()
            break

        else:
            print('OPÇÃO INVÁLIDA')
            continue
        
    continuar()

operador()
