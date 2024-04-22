populacao_a = 80000
taxa_crescimento_a = 3
populacao_b = 200000
taxa_crescimento_b = 1.5

anos = 0
while populacao_a < populacao_b:
    populacao_a *= 1 + taxa_crescimento_a / 100
    populacao_b *= 1 + taxa_crescimento_b / 100
    anos += 1

print("Número de anos necessários para a população do país A ultrapassar ou igualar a população do país B:", anos)
