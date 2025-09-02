# Algoritmo Genético – Problema da Mochila

Este projeto implementa um **algoritmo genético** para resolver o **problema da mochila 0/1**.  
O objetivo é selecionar um conjunto de itens que maximize o **valor total**, respeitando a restrição de **peso máximo**.

O código foi desenvolvido e testado no **Linux**.

---

## 🎯 Descrição do Problema

Temos uma mochila com capacidade máxima de **3000g**.  
Cada item possui **peso** e **valor**. O desafio é escolher quais itens colocar na mochila de modo que:

- O **peso total não ultrapasse 3000g**;  
- O **valor total seja o maior possível**.

---

## ⚙️ Parâmetros do Algoritmo

- **Itens disponíveis**: lista de 22 itens `(peso, valor)`  
- **Peso máximo da mochila**: `3000`  
- **Tamanho da população**: `100`  
- **Número de gerações**: `300`  
- **Taxa de crossover**: `0.8`  
- **Taxa de mutação**: `0.1`  

---

## 🧬 Funcionamento do Algoritmo

1. **Inicialização**  
   Gera uma população inicial de indivíduos (soluções), onde cada cromossomo é um vetor de `0`s e `1`s indicando se um item foi escolhido ou não.

2. **Avaliação (Fitness)**  
   Calcula o valor total dos itens escolhidos, penalizando soluções cujo peso ultrapasse `3000g`.

3. **Seleção por torneio**  
   Seleciona pais para reprodução, favorecendo indivíduos com maior fitness.

4. **Crossover (recombinação)**  
   Combina os genes dos pais para gerar novos indivíduos.

5. **Mutação**  
   Altera aleatoriamente alguns genes para manter diversidade.

6. **Iteração**  
   Repete o processo por `300` gerações, armazenando a melhor solução encontrada.

---

## ▶️ Como Executar no Linux

1. Abra o terminal e navegue até o diretório do projeto.  
2. Execute o código usando Python 3:

```bash
python3 Mochila.py

