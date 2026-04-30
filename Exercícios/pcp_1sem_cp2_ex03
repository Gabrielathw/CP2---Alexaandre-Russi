# Entrada de dados
cp1 = float(input("Digite a nota do Checkpoint 1: "))
cp2 = float(input("Digite a nota do Checkpoint 2: "))
cp3 = float(input("Digite a nota do Checkpoint 3: "))
sp1 = float(input("Digite a nota da Sprint 1: "))
sp2 = float(input("Digite a nota da Sprint 2: "))
gs = float(input("Digite a nota da Global Solution: "))

print()

# Encontrar a menor nota entre os checkpoints
menor_cp = cp1
print("Verificando a menor nota dos checkpoints...")

if cp2 < menor_cp:
    menor_cp = cp2

if cp3 < menor_cp:
    menor_cp = cp3

print(f"Menor checkpoint final: {menor_cp}")

print()

# Soma dos checkpoints removendo o menor
soma_cp = cp1 + cp2 + cp3 - menor_cp
print("Somando checkpoints e removendo a menor nota")
print(f"Soma das 3 CPs: {cp1 + cp2 + cp3}")
print(f"Removendo menor ({menor_cp})")
print(f"Soma final: {soma_cp}")


# Calcular a média do semestre (sem peso)
media = (soma_cp + sp1 + sp2) / 4

# Calcular a média com peso
media_final = (media * 0.4) + (gs * 0.6)

print()

# Exibir resultados
print("=== RESULTADO ===")
print(f"Média do semestre (sem peso): {media:.1f}")
print(f"Média do semestre (com peso): {media_final:.1f}")
