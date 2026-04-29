cod = int(input("Insira o código do estado de origem do caminhão (1 a 5): "))
carga = int(input("Insira o código da carga (10 a 40): "))
peso = int(input("Insira o peso do caminhão em toneladas: "))
print()

imposto = 0
valorCarga = 0
kg = peso * 1000

if 10 <= carga <= 20:
    valorCarga = 100 * kg
elif 21 <= carga <= 30:
    valorCarga = 250 * kg
elif 31 <= carga <= 40:
    valorCarga = 340 * kg
else:
    print("Código da Carga Inválido")
    exit()

match cod:
    case 1:
        imposto = 35
    case 2:
        imposto = 25
    case 3:
        imposto = 15
    case 4:
        imposto = 5
    case 5:
        imposto = 0
    case _:
        print("Código de Estado inválido.")
        exit()

valorImposto = valorCarga * (imposto / 100)
valorTotal = valorCarga + valorImposto

print(f"Peso da carga do caminhão convertido em quilos: {kg}kg")
print(f"Preço da carga do caminhão: R${valorCarga}")
print(f"Valor do Imposto: R${valorImposto}")
print(f"Valor total transportado pelo caminhão (carga + impostos): {valorTotal}")