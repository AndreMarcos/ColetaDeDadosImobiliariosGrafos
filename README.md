# Otimização de Coleta de Dados Imobiliários usando Grafos

## 📋 Sobre o Projeto

Este projeto visa abordar o problema de **planejamento de coleta de dados imobiliários** através de técnicas de otimização baseadas em teoria de grafos. O objetivo principal é melhorar o planejamento de coleta e reduzir o esforço e o tempo necessário para essa demanda.

## 🎥 Vídeo explicativo
- https://www.youtube.com/watch?v=_cC0mi8Cvt0

## Relatório
O relaório está na pasta `Relatorio/`

## 🎯 Objetivo

O estudo foi desenvolvido com o propósito de otimizar o processo de coleta de dados imobiliários, focando em:

- **Reduzir o tempo total de coleta**
- **Minimizar o esforço dos agentes coletores**
- **Distribuir equitativamente a carga de trabalho entre dois agentes**

## 🚀 Desafio

O problema consiste em traçar caminhos otimizados para **dois agentes de coleta**, considerando:

- **Divisão similar** da quantidade de imóveis a serem coletados pelos agentes
- **Distâncias iguais** percorridas por cada agente
- **Ponto de partida comum** (nó 71)

## 📊 Metodologia

Foram implementados **três métodos distintos** para resolver o problema de otimização:

### Método 1: Baseado em Distância (`Rua/`)
- **Critério**: Mensurado apenas pela distância percorrida pelos dois agentes
- **Algoritmo**: Utiliza o problema do carteiro chinês (Chinese Postman Problem - CPP)
- **Arquivos principais**:
  - `ccp.py`: Implementação do algoritmo CPP
  - `div2ag.py`: Divisão do grafo entre dois agentes
  - `norm_mtd.py`: Visualização e análise do grafo

### Método 2: Baseado em Quantidade de Imóveis (`Casa/`)
- **Critério**: Mensurado pela quantidade de imóveis a serem coletados
- **Algoritmo**: Partição balanceada baseada em raiz (Rooted Balanced Partition)
- **Arquivos principais**:
  - `ccp.py`: Implementação do algoritmo CPP
  - `div2ag.py`: Divisão do grafo entre dois agentes
  - `norm_mtd.py`: Visualização e análise do grafo

### Método 3: Método Combinado (`RuaCasa/`)
- **Critério**: Média ponderada da distância percorrida com a quantidade de imóveis coletados
- **Fórmula**: `peso = α × distância_normalizada + β × casas_normalizadas`
  - `α = 0.6` (importância da distância)
  - `β = 0.4` (importância da quantidade de casas)
- **Algoritmo**: Combina ambos os critérios através de normalização e ponderação
- **Arquivos principais**:
  - `ccp.py`: Implementação do algoritmo CPP
  - `div2ag.py`: Divisão do grafo entre dois agentes
  - `norm_mtd.py`: Visualização e análise do grafo

## 📁 Estrutura do Projeto

```
Projeto - Grafos/
│
├── Casa/                    # Método baseado em quantidade de imóveis
│   ├── ccp.py              # Algoritmo Chinese Postman Problem
│   ├── div2ag.py           # Divisão entre dois agentes
│   ├── norm_mtd.py         # Visualização e normalização
│   ├── CcpCasa.png         # Visualização do CPP
│   ├── Div2AgCasa.png      # Visualização da divisão
│   ├── HistoGrafoCasa.png  # Histograma do grafo
│   └── ImpactoPesoCasa.png # Impacto dos pesos
│
├── Rua/                     # Método baseado em distância
│   ├── ccp.py              # Algoritmo Chinese Postman Problem
│   ├── div2ag.py           # Divisão entre dois agentes
│   ├── norm_mtd.py         # Visualização e normalização
│   ├── CcpRua.png          # Visualização do CPP
│   ├── Div2AgRua.png       # Visualização da divisão
│   ├── HistografoRua.png   # Histograma do grafo
│   └── ImpactoPesoRua.png  # Impacto dos pesos
│
├── RuaCasa/                 # Método combinado
│   ├── ccp.py              # Algoritmo Chinese Postman Problem
│   ├── div2ag.py           # Divisão entre dois agentes
│   ├── norm_mtd.py         # Visualização e normalização
│   ├── CcpCasaRua.png      # Visualização do CPP
│   ├── Div2AgCasaRua.png   # Visualização da divisão
│   ├── HistoGrafoCasaRua.png # Histograma do grafo
│   └── ImpactoPesoCasaRua.png # Impacto dos pesos
│
├── comparativo_resultados.py # Script para comparar resultados dos três métodos
│
└── ReferencialTeorico/       # Documentos teóricos de referência
    ├── ALGORITHMS BEFORE COMPUTERS.pdf
    ├── An efficient heuristic procedure for partitioning graphs.pdf
    ├── Computers and Intrac tability - A Guide to the Theory of NP Completeness.pdf
    ├── Graph clustering. Computer Science Review.pdf
    └── Solutio problematis ad geometriam situs.pdf
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **NetworkX**: Biblioteca para manipulação e análise de grafos
- **Matplotlib**: Visualização de grafos e geração de gráficos
- **NumPy**: Operações numéricas e normalização de dados

## 🚀 Como Executar

### Executar um método específico

Para executar um dos três métodos, navegue até o diretório correspondente e execute os scripts:

```bash
# Método 1: Baseado em distância
cd Rua
python div2ag.py

# Método 2: Baseado em quantidade de imóveis
cd Casa
python div2ag.py

# Método 3: Método combinado
cd RuaCasa
python div2ag.py
```

### Comparar resultados de todos os métodos

Execute o script comparativo na raiz do projeto:

```bash
python comparativo_resultados.py
```

Este script executa todos os três métodos e apresenta uma tabela comparativa com as seguintes métricas:

- Tempo total com 1 agente
- Tempo do Agente A
- Tempo do Agente B
- Tempo total da equipe (makespan)
- Economia de tempo
- Redução percentual

## 📈 Resultados

Os scripts geram visualizações e métricas de desempenho para cada método:

- **Grafos visuais**: Representação das rotas dos agentes
- **Histogramas**: Distribuição dos pesos das arestas
- **Métricas de tempo**: Comparação entre os métodos
- **Análise de eficiência**: Redução de tempo e esforço

### Métricas Calculadas

- **Tempo total (1 agente)**: Tempo necessário se apenas um agente realizasse toda a coleta
- **Tempo por agente**: Tempo individual de cada agente
- **Makespan**: Tempo total da equipe (máximo entre os dois agentes)
- **Economia**: Diferença entre tempo com 1 agente e makespan
- **Redução percentual**: Percentual de redução de tempo ao usar dois agentes

## 🔬 Algoritmos Implementados

### Chinese Postman Problem (CPP)
Algoritmo para encontrar o caminho mais curto que percorre todas as arestas do grafo pelo menos uma vez, retornando ao ponto inicial.

### Rooted Balanced Partition
Algoritmo de partição balanceada que divide o grafo em dois subgrafos conectados, garantindo distribuição equilibrada de pesos (distância ou quantidade de imóveis).

## 📚 Referências Teóricas

O projeto foi desenvolvido com base em referências teóricas sobre:
- Teoria de Grafos
- Problemas de Otimização Combinatória
- Algoritmos de Partição de Grafos
- Problema do Carteiro Chinês

Documentos de referência estão disponíveis na pasta `ReferencialTeorico/`.

## 👥 Autores

ANDRE MARCOS FERREIRA

JUAN PABLO RIBEIRO

MARIA EDUARDA RIBEIRO

PEDRO HENRIQUE BORGES DA SILVA


---

**Nota**: Este projeto foi desenvolvido para fins de pesquisa e estudo sobre otimização de rotas usando teoria de grafos aplicada à coleta de dados imobiliários.

