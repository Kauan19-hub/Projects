#Mini calculadora no Python
#Numero1, numero2, oper, result

numero1 = 0
numero2 = 0
result = 0
oper = '' #Str vazia

while True:
    numero1 = int(input("Digite o primeiro número: "))
    oper = input("Digite o operação matemática: ")
    numero2 = int(input("Digite o segundo número: "))

    if oper == '+':
        result = numero1 + numero2
    elif oper == '-':
        result = numero1 - numero2
    elif oper == '*':
        result = numero1 * numero2
    elif oper == '/':
        result = numero1 / numero2
    else:
        print("Erro. Operação não identificada! ")

    print("{} {} {} = {}".format(numero1, oper, numero2, result))






