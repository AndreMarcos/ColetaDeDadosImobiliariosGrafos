import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------
# 1. ENTRADA DE DADOS
# ---------------------------

dados = [
    (1, 2, 49, 6), (1, 8, 52, 7), (2, 3, 102, 20), (2, 9, 55, 10), (3, 4, 93, 19), (3, 10, 55, 9),
    (4, 5, 53, 9), (4, 11, 53, 6), (5, 6, 58, 7), (5, 12, 50, 5), (6, 7, 92, 8), (6, 13, 48, 7),
    (7, 15, 42, 6), (8, 9, 52, 12), (9, 10, 109, 22), (9, 20, 67, 13), (10, 11, 86, 18), (10, 21, 62, 10),
    (11, 12, 54, 6), (11, 26, 89, 16), (12, 13, 58, 9), (12, 27, 84, 11), (13, 14, 62, 8), (13, 28, 79,5),
    (14, 15, 37, 4), (14, 29, 71, 7), (15, 16, 114, 14), (15, 30, 66, 11), (16, 17, 60, 2), (16, 31, 57, 2),
    (17, 18, 69, 12), (17, 33, 48, 2), (18, 35, 52, 5), (19, 20, 95, 9), (20, 21, 107, 18), (20, 23, 41, 5),
    (21, 25, 36, 4), (22, 23, 93, 13), (22, 36, 83, 7), (23, 24, 58, 9), (23, 37, 84, 14), (24, 25, 54, 14),
    (24, 38, 84, 12), (25, 26, 75, 13), (25, 39, 86, 13), (26, 27, 53, 4), (26, 40, 91, 13), (27, 28, 59, 6),
    (27, 41, 92, 16), (28, 29, 60, 8), (28, 42, 93, 12), (29, 30, 46, 9), (29, 43, 100, 13), (30, 31, 96, 11),
    (30, 44, 100, 16), (31, 32, 52, 4), (31, 45, 103, 16), (32, 33, 45, 0), (32, 46, 111, 8), (33, 34, 45, 3),
    (33, 47, 103, 11), (34, 35, 46, 10), (34, 48, 112, 13), (35, 49, 114, 10), (36, 37, 90, 15), (36, 50, 52, 9),
    (37, 38, 48, 7), (37, 51, 55, 9), (38, 39, 64, 7), (39, 52, 55, 7), (39, 40, 63, 8), (40, 41, 54, 7),
    (40, 53, 54, 9), (41, 42, 59, 11), (41, 54, 59, 7), (42, 43, 54, 7), (42, 55, 60, 8), (43, 44, 42, 4),
    (43, 56, 58, 8), (44, 45, 91, 4), (44, 57, 58, 3), (45, 46, 55, 8), (45, 58, 56, 2), (46, 47, 44, 5),
    (46, 59, 55, 6), (47, 48, 38, 5), (47, 60, 53, 4), (48, 49, 48, 4), (49, 61, 51, 6), (50, 51, 84, 12),
    (50, 62, 66, 8), (51, 52, 112, 16), (51, 63, 64, 7), (52, 53, 54, 10), (52, 65, 60, 9), (53, 54, 54, 6),
    (53, 66, 56, 7), (54, 55, 63, 7), (54, 67, 56, 6), (55, 56, 64, 7), (55, 68, 58, 7), (56, 57, 46, 8),
    (56, 69, 58, 6), (57, 70, 61, 4), (58, 59, 59, 5), (58, 71, 68, 3), (59, 60, 53, 6), (59, 72, 65, 7),
    (60, 61, 88, 4), (60, 73, 62, 5), (61, 74, 63, 4), (62, 63, 79, 13), (62, 75, 62, 13), (63, 64, 68, 10),
    (63, 76, 59, 7), (64, 65, 47, 4), (64, 77, 61, 7), (65, 66, 52, 6), (65, 78, 60, 9), (66, 67, 48, 7),
    (67, 68, 60, 4), (67, 80, 57, 6), (68, 69, 49, 6), (68, 81, 58, 6), (69, 70, 56, 7), (69, 82, 55, 5),
    (70, 71, 63, 4), (71, 72, 69, 5), (71, 83, 50, 2), (72, 73, 55, 6), (72, 84, 53, 6), (73, 74, 92, 16),
    (73, 85, 54, 5), (75, 76, 72, 6), (76, 77, 68, 10), (77, 78, 51, 6), (78, 79, 64, 10), (79, 80, 27, 2),
    (79, 86, 45, 5), (80, 81, 59, 2), (81, 82, 49, 6), (81, 86, 80, 4), (82, 83, 125, 17), (82, 87, 54, 6),
    (83, 84, 70, 8), (83, 88, 55, 6), (84, 85, 53, 6), (84, 89, 94, 8), (85, 90, 66, 7), (90, 91, 95, 9),
    (90, 92, 68, 2)
]


# ---------------------------
# 2. CONSTRUÇÃO DO GRAFO
# ---------------------------

def build_graph(dados):
    G = nx.Graph()
    for u, v, dist, casas in dados:
        G.add_edge(u, v, distancia=dist, casas=casas)
    return G

G = build_graph(dados)


# ---------------------------
# 3. NORMALIZAÇÃO DOS VALORES
# ---------------------------

def normalize(values):
    arr = np.array(values)
    return (arr - arr.min()) / (arr.max() - arr.min())


# ------------------------------------------
# 4. ALGORITMO DE PARTIÇÃO (ROOTED BALANCED)
# ------------------------------------------

def rooted_balanced_partition(G, root, alpha=0.6, beta=0.4):

    # Normalizar distâncias e casas
    dn = normalize([G[u][v]["distancia"] for u, v in G.edges()])
    cn = normalize([G[u][v]["casas"] for u, v in G.edges()])

    for (edge, dnorm, cnorm) in zip(G.edges(), dn, cn):
        u, v = edge
        G[u][v]["peso"] = alpha*dnorm + beta*cnorm

    # distâncias ao root
    dist_root = nx.single_source_dijkstra_path_length(G, root, weight="peso")
    ordem = sorted(dist_root, key=lambda x: dist_root[x])

    A = set([root])
    B = set([root])
    pesoA = 0
    pesoB = 0

    def can_add(S, v):
        S2 = S | {v}
        return nx.has_path(G.subgraph(S2), root, v)

    for v in ordem:
        if v == root:
            continue

        incA = sum(G[v][u]["peso"] for u in G.neighbors(v) if u in A)
        incB = sum(G[v][u]["peso"] for u in G.neighbors(v) if u in B)

        if pesoA <= pesoB:
            if can_add(A, v):
                A.add(v)
                pesoA += incA
            else:
                B.add(v)
                pesoB += incB
        else:
            if can_add(B, v):
                B.add(v)
                pesoB += incB
            else:
                A.add(v)
                pesoA += incA

    return A, B

root = 71
A, B = rooted_balanced_partition(G, root=root)


# ------------------------------------------
# 5. CUSTO REAL BASEADO EM TEMPOS (MINUTOS
# ------------------------------------------
def tempo_aresta(dist, casas):
    return 0.0075 * dist + 0.5 * casas  # minutos

# Tempo total se 1 agente fizer tudo
tempo_1_agente = sum(tempo_aresta(G[u][v]["distancia"], G[u][v]["casas"]) for u, v in G.edges())


# ------------------------------------------
# 6. CALCULAR TEMPO REAL POR AGENTE
# ------------------------------------------

def tempo_subgrafo(G, conjunto):
    tempo = 0
    for u, v in G.edges():
        if u in conjunto and v in conjunto:
            tempo += tempo_aresta(G[u][v]["distancia"], G[u][v]["casas"])
    return tempo

tempo_A = tempo_subgrafo(G, A)
tempo_B = tempo_subgrafo(G, B)

tempo_equipa = max(tempo_A, tempo_B)


# ------------------------------------------
# 7. RESULTADOS
# ------------------------------------------

print("\n------------ RESULTADOS ------------")
print(f"Tempo total se apenas 1 agente trabalhar: {tempo_1_agente:.2f} minutos")
print(f"Tempo Agente A: {tempo_A:.2f} minutos")
print(f"Tempo Agente B: {tempo_B:.2f} minutos")
print(f"Tempo total da equipe (2 agentes): {tempo_equipa:.2f} minutos")
print("------------------------------------")

print("\nRedução total:")
print(f"Economia = {tempo_1_agente - tempo_equipa:.2f} minutos")
print(f"Redução percentual = {(1 - tempo_equipa / tempo_1_agente) * 100:.2f}%")

# -------------------------------
# 8. PLOT DO GRAFO COM HISTOGRAMA
# -------------------------------

pos = nx.spring_layout(G, seed=42)

colors = []
for node in G.nodes():
    if node == root:
        colors.append("yellow")
    elif node in A:
        colors.append("red")
    else:
        colors.append("blue")

plt.figure(figsize=(18, 12))
nx.draw(
    G, pos,
    node_color=colors,
    with_labels=True,
    node_size=200,
    edge_color="gray",
    font_size=8
)

plt.title("Partição do grafo entre dois agentes (root = 71)")
plt.show()