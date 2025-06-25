num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if num1 > num2:
        num1, num2 = num2, num1

soma = 0
print(f"Números no intervalo entre {num1} e {num2}:")
for i in range(num1 + 1, num2):
    print(i, end=" ")
    soma += i

print(f"\nSoma dos números no intervalo: {soma}")