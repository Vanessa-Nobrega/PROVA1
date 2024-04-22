num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 >= num2 and num1 >= num3:
    maior = num1
    if num2 >= num3:
        meio = num2
        menor = num3
    else:
        meio = num3
        menor = num2
elif num2 >= num1 and num2 >= num3:
    maior = num2
    if num1 >= num3:
        meio = num1
        menor = num3
    else:
        meio = num3
        menor = num1
else:
    maior = num3
    if num1 >= num2:
        meio = num1
        menor = num2
    else:
        meio = num2
        menor = num1

print("Números em ordem decrescente:")
print(maior, meio, menor)


