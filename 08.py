numeros = []

for i in range(5):
        numero = float(input(f"Digite o número {i + 1}: "))
        numeros.append(numero) 

soma = sum(numeros)
media = soma / len(numeros) 

print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")