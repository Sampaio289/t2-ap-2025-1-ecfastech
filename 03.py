while True:
        nome = input("Digite o nome (mais de 3 caracteres): ")
        if len(nome) <= 3:
            print("Nome inválido. Deve ter mais de 3 caracteres.")
            continue

        idade = int(input("Digite a idade (entre 0 e 150): "))
        if idade < 0 or idade > 150:
            print("Idade inválida. Deve estar entre 0 e 150.")
            continue

        salario = float(input("Digite o salário (maior que 0): "))
        if salario <= 0:
            print("Salário inválido. Deve ser maior que 0.")
            continue

        sexo = input("Digite o sexo ('f' para feminino ou 'm' para masculino): ").lower()
        if sexo not in ['f', 'm']:
            print("Sexo inválido. Deve ser 'f' ou 'm'.")
            continue

        estado_civil = input("Digite o estado civil ('s' para solteiro(a), 'c' para casado(a), 'v' para viúvo(a), 'd' para divorciado(a)): ").lower()
        if estado_civil not in ['s', 'c', 'v', 'd']:
            print("Estado civil inválido. Deve ser 's', 'c', 'v' ou 'd'.")
            continue

        print("\nInformações válidas:")
        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
        print(f"Salário: R$ {salario:.2f}")
        print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
        print(f"Estado Civil: {estado_civil}")
        break