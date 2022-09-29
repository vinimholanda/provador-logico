import csv

def verifica(antecedentes, verdadeiros, antecedentes_e_descendentes, letra_usuario, alfabeto, abc):

    indice = 0
    julgamento = []
    alfabeto_julgado = []
    pode_ser_provado = []
    nao_pode_ser_provado = []

    antecedentes = [item.replace(" ", "") for item in antecedentes]

    # Atribuir valor True ou False a todas as letras do alfabeto
    for linha in alfabeto:
        if linha in verdadeiros:
            letra = "True"
            julgamento.append(letra)
        else:
            letra = "False"
            julgamento.append(letra)
    for linha in alfabeto:
        alfabeto_julgado.append(alfabeto[indice] + " = " + julgamento[indice])
        indice = indice + 1
            
    # Atualizar valores True ou False
    for linha in antecedentes_e_descendentes:
        senteca = True
        for letra in linha:
            if letra in abc:

                if linha.endswith(letra):
                    break
                else:
                    x = letra + " = True"

                    if x in alfabeto_julgado:
                        continue
                    else:
                        senteca = False
            else:
                continue
        if senteca == True:
            y = letra + " = False"
    
            for i in range(len(alfabeto_julgado)):
                if alfabeto_julgado[i] == y:
                    alfabeto_julgado[i] = letra + " = True"
    
    # Sentencas que podem ser geradas/provadas
    for linha in alfabeto_julgado:
            if "True" in linha and linha:
                pode_ser_provado.append(linha)
            elif "False" in linha and linha:
                nao_pode_ser_provado.append(linha)

    print("\nLetras que PODEM ser provadas:", end=" ")
    for linha in pode_ser_provado:
        for letra in linha:
            if letra in abc and letra in alfabeto and linha.startswith(letra):
                print(letra, end=", ")

    print("\nLetras que NAO PODEM ser provadas:", end=" ")
    for linha in nao_pode_ser_provado:
        for letra in linha:
            if letra in abc and letra in alfabeto and linha.startswith(letra):
                print(letra, end=", ")

    print("")

    if letra_usuario + " = True" in alfabeto_julgado:
        return True
    else:
        return False

if __name__ == "__main__":

    parar = False

    while parar == False:
        print("=== Provador ===")
        print("\n[1] base.csv + fatos.csv")
        print("[2] base2.csv + fatos2.csv")
        print("[3] base3.csv + fatos3.csv")

                
        opcao = int(input("\nEscolha um arquivo para executar: "))

        antecedentes = []
        descendentes = []
        antecedentes_e_descendentes = []
        alfabeto = []
        verdadeiros = []
        abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        match opcao:
            case 1:
                print("\nSeus dados:\n")
                with open("./csv/base.csv", "r") as base:
                    ler_base = csv.reader(base)
                    next(ler_base)

                    for linha in ler_base:
                        antecedentes.append(linha[0])
                        descendentes.append(linha[1])
                        antecedentes_e_descendentes.append(linha[0]+linha[1])

                        print(linha)

                print("")

                with open('./csv/fatos.csv', 'r') as fatos:
                    ler_fatos = csv.reader(fatos)
                    next(ler_fatos)
                        
                    for linha in ler_fatos:
                        verdadeiros.append(linha[0])
                        print(linha)
                parar = True
            case 2:
                print("\nSeus dados:\n")
                with open("./csv/base2.csv", "r") as base:
                    ler_base = csv.reader(base)
                    next(ler_base)

                    for linha in ler_base:
                        antecedentes.append(linha[0])
                        descendentes.append(linha[1])
                        antecedentes_e_descendentes.append(linha[0]+linha[1])

                        print(linha)

                print("")

                with open('./csv/fatos2.csv', 'r') as fatos:
                    ler_fatos = csv.reader(fatos)
                    next(ler_fatos)

                    for linha in ler_fatos:
                        verdadeiros.append(linha[0])
                        print(linha)
                parar = True
            case 3:
                print("\nSeus dados:\n")
                with open("./csv/base3.csv", "r") as base:
                    ler_base = csv.reader(base)
                    next(ler_base)

                    for linha in ler_base:
                        antecedentes.append(linha[0])
                        descendentes.append(linha[1])
                        antecedentes_e_descendentes.append(linha[0]+linha[1])

                        print(linha)

                print("")

                with open('./csv/fatos3.csv', 'r') as fatos:
                    ler_fatos = csv.reader(fatos)
                    next(ler_fatos)

                    for linha in ler_fatos:
                        verdadeiros.append(linha[0])
                        print(linha)
                parar = True
            case _:
                print("\n(!) Voce deve digitar um numero valido\n")

    # Criar alfabeto
    for linha in antecedentes_e_descendentes:
        for letra in linha:
            if letra in abc and letra not in alfabeto:
                alfabeto.append(letra)
            else:
                continue

    print(f"\nAlfabeto: {alfabeto}")
    print(f"Antecedentes: {antecedentes}")
    print(f"Descendentes: {descendentes}")
    print(f'Setado como "True": {verdadeiros}')

    x = str(input("\nDigite uma LETRA para ser verificada: "))
    x = x.upper()

    if (verifica(antecedentes, verdadeiros, antecedentes_e_descendentes, x, alfabeto, abc) == True):
        print(f"\nLogo, {x} PODE ser provado/gerado\n")
    else:
        print(f"\nLogo, {x} NAO PODE ser provado/gerado\n")
