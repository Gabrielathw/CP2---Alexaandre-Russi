nome_funcionario = input("Digite o nome do funcionário: ")
cargo = int(input("Selecione o numero do cargo: "
                  " | 1 - Gerente"
                  " | 2 - Analista"
                  " | 3 - Assistente"
                  " | 4 - Estagiário | selecione uma das opções: "))
salario_b = float(input("Informe o salário base: "))
hrx = float(input("Informe a quantidade de horas extras trabalhadas: "))
faltas = int(input("Informe o total de faltas: "))
bonus = input("algum bônus recebido digite (s) ou (n): ")

print()
print()

descontof =  salario_b * 0.02 * faltas
salariof = salario_b - descontof

valorhrx = salario_b * 0.015 * hrx

if bonus == 's' and cargo == 1:
    salariob = salario_b + 1000
    valor_bonus = salariob - salario_b
elif bonus == 's' and cargo == 2:
    salariob = salario_b + 500
    valor_bonus = salariob - salario_b
elif bonus == 's' and cargo == 3:
    salariob = salario_b + 300
    valor_bonus = salariob - salario_b
elif bonus == 's' and cargo == 4:
    salariob = salario_b + 100
    valor_bonus = salariob - salario_b
else:
    salariob = salario_b
    valor_bonus = 0

total_acrecimos = valorhrx + valor_bonus
salario_final = valorhrx + salariob - descontof


print(f"Salário bruto: {salario_b}")
print(f"Total de acréscimos: {total_acrecimos}")
print(f"Total de descontos: {descontof}")
print(f"Salário final: {salario_final}")
print(f"O salário final do colaborador {nome_funcionario} é de R$ {salario_final}")
