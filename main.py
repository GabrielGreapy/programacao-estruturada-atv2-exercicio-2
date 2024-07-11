def q1():
    """
    Faça um programa que calcula a
    quantidade de divisores de um
    número (incluindo 1 e o próprio 
    número) que são divisíveis por 3.
    Parte 1 - programa que mostra os divisores de um numero
    """
    contador = 0
    numero = int(input("Digite um numero: "))
    # os divisiores deste numero
    for i in range(1,numero + 1):
        if (numero % i == 0):
            print(i)
            if (i % 3 == 0):
                contador += 1
            
    '''
    Parte 2 - Com os numeros divisores verificar se são divisiveis por 3 incrementa o contador
    '''
    print(f'Na lista de divisiveis deste numero há {contador} numeros divisiveis por 3.')
# q1()
def q2():
    numero1 = int(input("Digite um numero: "))
    numero2 = int(input("Digite um numero: "))
    soma = 0
    if numero1 > numero2:
        n1 = numero2
        n2 = numero1
    for i in range(n1, n2 + 1):
        if i < 0:
            soma += i
    print(soma)
def q3():
    media = 0
    nota = 0
    divisor = 0
    cont = 0
    while nota != -1:
        nota == float(input("Nota"))
        divisor += 1
        cont += nota
        if nota == -1:
            break
    media = cont // divisor
q3()
