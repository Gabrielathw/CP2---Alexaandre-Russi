def pode_aprovar(idade, renda, valor):
    if idade >= 18 and valor <= renda * 20:
        return True
    else:
        return False


def definir_taxa(parcelas):
    if parcelas >= 3 and parcelas <= 6:
        return 0.05
    elif parcelas >= 7 and parcelas <= 12:
        return 0.08
    elif parcelas >= 13 and parcelas <= 24:
        return 0.10
    else:
        return 0


def calcular_parcela(valor, taxa, parcelas):
    pmt = valor * (taxa * (1 + taxa)**parcelas) / ((1 + taxa)**parcelas - 1)
    return pmt


def calcular_total(parcela, parcelas):
    return parcela * parcelas


def calcular_juros(total, valor):
    return total - valor



nome_cliente = input("Digite o nome do cliente: ")
idade_cliente = int(input("Digite a idade do cliente: "))
renda_mensal = float(input("Digite a renda mensal do cliente: "))
valor_desejado = float(input("Digite o valor desejado do empréstimo: "))
numero_parcelas = int(input("Digite o número de parcelas (3 até 24): "))



if pode_aprovar(idade_cliente, renda_mensal, valor_desejado):
    taxa = definir_taxa(numero_parcelas)

    if taxa != 0:
        parcela = calcular_parcela(valor_desejado, taxa, numero_parcelas)
        total = calcular_total(parcela, numero_parcelas)
        juros = calcular_juros(total, valor_desejado)

        print()
        print("financiamento aprovado")
        print()
        print("Nome do cliente:", nome_cliente)
        print("Valor financiado:", valor_desejado)
        print("Taxa de juros:", taxa * 100, "%")
        print("Valor da parcela:", round(parcela, 2))
        print("Valor total pago:", round(total, 2))
        print("Total de juros pagos:", round(juros, 2))
        print()

    else:
        print()
        print("Número de parcelas inválido")
        print()

else:
    print()
    print("financiamento negado")
    print()
