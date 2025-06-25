while True:
    
     populacao_a = int(input("Informe a população inicial do país A: "))
     populacao_b = int(input("Informe a população inicial do país B: "))
     if populacao_a <= 0 or populacao_b <= 0:
            print("As populações devem ser maiores que zero.")
            continue
     
     taxa_a = float(input("Infome a Taxa de Crescimento da população A : ")) /100
     taxa_b = float(input("Infome a Taxa de Crescimento da população B : ")) /100
     if taxa_a <= 0 or taxa_b <= 0:
           print("As taxas de crescimento devem ser maiores que zero.")
           continue
     
     anos = 0

     while populacao_a <= populacao_b:
                populacao_a += populacao_a * taxa_a
                populacao_b += populacao_b * taxa_b
                anos += 1

     print(f"\nSerá necessário {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")
     print(f"População final de A: {int(populacao_a)}")
     print(f"População final de B: {int(populacao_b)}")
    
     repetir = input("\nDeseja realizar outra simulação? (Sim/Não): ")
     if repetir == 'sim'or'Sim':
            continue

     else :
            print("Programa encerrado.")
            break      