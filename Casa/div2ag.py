import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------
# 1. ENTRADA DE DADOS
# ---------------------------
# Agora cada tupla tem apenas (u, v, casas)
dados = [
    (1, 2, 6), (1, 8, 7), (2, 3, 20), (2, 9, 10), (3, 4, 19), (3, 10, 9),
    (4, 5, 9), (4, 11, 6), (5, 6, 7), (5, 12, 5), (6, 7, 8), (6, 13, 7),
    (7, 15, 6), (8, 9, 12), (9, 10, 22), (9, 20, 13), (10, 11, 18), (10, 21, 10),
    (11, 12, 6), (11, 26, 16), (12, 13, 9), (12, 27, 11), (13, 14, 8), (13, 28, 5),
    (14, 15, 4), (14, 29, 7), (15, 16, 14), (15, 30, 11), (16, 17, 2), (16, 31, 2),
    (17, 18, 12), (17, 33, 2), (18, 35, 5), (19, 20, 9), (20, 21, 18), (20, 23, 5),
    (21, 25, 4), (22, 23, 13), (22, 36, 7), (23, 24, 9), (23, 37, 14), (24, 25, 14),
    (24, 38, 12), (25, 26, 13), (25, 39, 13), (26, 27, 4), (26, 40, 13), (27, 28, 6),
    (27, 41, 16), (28, 29, 8), (28, 42, 12), (29, 30, 9), (29, 43, 13), (30, 31, 11),
    (30, 44, 16), (31, 32, 4), (31, 45, 16), (32, 33, 0), (32, 46, 8), (33, 34, 3),
    (33, 47, 11), (34, 35, 10), (34, 48, 13), (35, 49, 10), (36, 37, 15), (36, 50, 9),
    (37, 38, 7), (37, 51, 9), (38, 39, 7), (39, 52, 7), (39, 40, 8), (40, 41, 7),
    (40, 53, 9), (41, 42, 11), (41, 54, 7), (42, 43, 7), (42, 55, 8), (43, 44, 4),
    (43, 56, 8), (44, 45, 4), (44, 57, 3), (45, 46, 8), (45, 58, 2), (46, 47, 5),
    (46, 59, 6), (47, 48, 5), (47, 60, 4), (48, 49, 4), (49, 61, 6), (50, 51, 12),
    (50, 62, 8), (51, 52, 16), (51, 63, 7), (52, 53, 10), (52, 65, 9), (53, 54, 6),
    (53, 66, 7), (54, 55, 7), (54, 67, 6), (55, 56, 7), (55, 68, 7), (56, 57, 8),
    (56, 69, 6), (57, 70, 4), (58, 59, 5), (58, 71, 3), (59, 60, 6), (59, 72, 7),
    (60, 61, 4), (60, 73, 5), (61, 74, 4), (62, 63, 13), (62, 75, 13), (63, 64, 10),
    (63, 76, 7), (64, 65, 4), (64, 77, 7), (65, 66, 6), (65, 78, 9), (66, 67, 7),
    (67, 68, 4), (67, 80, 6), (68, 69, 6), (68, 81, 6), (69, 70, 7), (69, 82, 5),
    (70, 71, 4), (71, 72, 5), (71, 83, 2), (72, 73, 6), (72, 84, 6), (73, 74, 16),
    (73, 85, 5), (75, 76, 6), (76, 77, 10), (77, 78, 6), (78, 79, 10), (79, 80, 2),
    (79, 86, 5), (80, 81, 2), (81, 82, 6), (81, 86, 4), (82, 83, 17), (82, 87, 6),
    (83, 84, 8), (83, 88, 6), (84, 85, 6), (84, 89, 8), (85, 90, 7), (90, 91, 9),
    (90, 92, 2)
]


# ---------------------------
# 2. CONSTRUÇÃO DO GRAFO
# ---------------------------

def build_graph(dados):
    G = nx.Graph()
    for u, v, casas in dados:
        G.add_edge(u, v, casas=casas)
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

def rooted_balanced_partition(G, root):

    # Normalizar distâncias e casas
    cn = normalize([G[u][v]["casas"] for u, v in G.edges()])

    for (edge, cnorm) in zip(G.edges(), cn):
        u, v = edge
        G[u][v]["peso"] = cnorm

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
# 5. CUSTO REAL BASEADO EM TEMPOS (MINUTOS)
# ------------------------------------------
def tempo_aresta(casas):
    return 0.5 * casas # minutos

# Tempo total se 1 agente fizer tudo
tempo_1_agente = sum(tempo_aresta(G[u][v]["casas"]) for u, v in G.edges())


# ------------------------------------------
# 6. CALCULAR TEMPO REAL POR AGENTE
# ------------------------------------------

def tempo_subgrafo(G, conjunto):
    tempo = 0
    for u, v in G.edges():
        if u in conjunto and v in conjunto:
            tempo += tempo_aresta(G[u][v]["casas"])
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