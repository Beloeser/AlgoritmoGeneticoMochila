import random

itens = [
    (350, 300),  
    (250, 400),  
    (160, 450),  
    (120, 350),  
    (200, 250),  
    (100, 300),  
    (120, 200),  
    (220, 250),  
    (40, 150),   
    (80, 400),   
    (100, 350),  
    (300, 300),  
    (180, 450),  
    (250, 500),  
    (220, 350),  
    (150, 400),  
    (280, 200),  
    (310, 300),  
    (120, 250),  
    (160, 300),  
    (110, 150),  
    (210, 200)
]


pesoMax = 3000
tamanhoPop = 50
geracoes = 300
taxaMutacao = 0.1
taxaCrossover = 0.8

def calcularFitness(genoma):
    pesoTotal = sum(itens[i][0] for i in range(len(genoma)) if genoma[i] == 1)
    if pesoTotal > pesoMax:
        return 0
    return sum(itens[i][1] for i in range(len(genoma)) if genoma[i] == 1)

def gerarPopulacaoInicial():
    return [[random.randint(0, 1) for _ in range(len(itens))] for _ in range(tamanhoPop)]

def selecaoTorneio(populacao, fitnessScores, k=3):
    torneio = random.sample(list(zip(populacao, fitnessScores)), k)
    torneio.sort(key=lambda x: x[1], reverse=True)
    probs = [0.7, 0.2, 0.1]
    if len(probs) < k:
        resto = (1 - sum(probs)) / (k - len(probs))
        probs.extend([resto] * (k - len(probs)))
    escolhido = random.choices(torneio, weights=probs, k=1)[0]
    return escolhido[0]

def aplicarCrossover(pai1, pai2, taxaCrossover):
    if (random.randint(0, 1000) / 1000) > taxaCrossover:
        return pai1.copy(), pai2.copy()
    ponto = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]
    return filho1, filho2

def aplicarMutacao(genoma, taxaMutacao):
    for i in range(len(genoma)):
        if (random.randint(0, 1000) / 1000) < taxaMutacao:
            genoma[i] = 1 - genoma[i]
    return genoma

def algoritmoGenetico():
    populacao = gerarPopulacaoInicial()
    melhorFitness = 0
    melhorGenoma = None
    geracaoMelhor = 0

    for geracao in range(geracoes):
        fitnessScores = [calcularFitness(genoma) for genoma in populacao]
        maxFitness = max(fitnessScores)
        if maxFitness > melhorFitness:
            melhorFitness = maxFitness
            melhorGenoma = populacao[fitnessScores.index(maxFitness)].copy()
            geracaoMelhor = geracao

        novaPopulacao = []
        for _ in range(tamanhoPop // 2):
            pai1 = selecaoTorneio(populacao, fitnessScores)
            pai2 = selecaoTorneio(populacao, fitnessScores)
            filho1, filho2 = aplicarCrossover(pai1, pai2, taxaCrossover)
            novaPopulacao.extend([aplicarMutacao(filho1, taxaMutacao), aplicarMutacao(filho2, taxaMutacao)])

        populacao = novaPopulacao

    return melhorGenoma, melhorFitness, geracaoMelhor

melhorSolucao, valorTotal, geracao = algoritmoGenetico()

print("=== MELHOR SOLUÇÃO ENCONTRADA ===")
print(f"Geração: {geracao}")
print(f"Valor total: {valorTotal}")
pesoTotal = sum(itens[i][0] for i in range(len(melhorSolucao)) if melhorSolucao[i] == 1)
print(f"Peso total: {pesoTotal}g")
print("\nItens selecionados:")
for i in range(len(melhorSolucao)):
    if melhorSolucao[i] == 1:
        print(f"Item {i+1}: Peso={itens[i][0]}g, Valor={itens[i][1]}")
