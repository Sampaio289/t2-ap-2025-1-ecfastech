numeros = [] 

for i in range(5):
        numero = float(input(f"Digite o número {i + 1}: "))
        numeros.append(numero)

maior_numero = max(numeros) 
print(f"O maior número é: {maior_numero}")