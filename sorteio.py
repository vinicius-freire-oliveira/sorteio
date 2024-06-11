# Importa o módulo random para geração de números aleatórios
import random

# Gera um número aleatório entre 0 e 1 (exclusivo)
sorteado = random.randrange(0, 2)

# Imprime o número sorteado
print(sorteado)

# Verifica o número sorteado e imprime um nome correspondente
if sorteado == 0:
    print("Paulo")
elif sorteado == 1:
    print("Juliana")
else:
    # Se por algum motivo o número sorteado não for 0 ou 1, imprime "Tamires"
    print("Tamires")
