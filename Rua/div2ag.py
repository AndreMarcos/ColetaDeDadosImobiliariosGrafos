import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------
# 1. ENTRADA DE DADOS
# ---------------------------
# Agora cada tupla tem apenas (u, v, distancia)
dados = [
    (1, 2, 49), (1, 8, 52), (2, 3, 102), (2, 9, 55), (3, 4, 93), (3, 10, 55),
    (4, 5, 53), (4, 11, 53), (5, 6, 58), (5, 12, 50), (6, 7, 92), (6, 13, 48),
    (7, 15, 42), (8, 9, 52), (9, 10, 109), (9, 20, 67), (10, 11, 86), (10, 21, 62),
    (11, 12, 54), (11, 26, 89), (12, 13, 58), (12, 27, 84), (13, 14, 62), (13, 28, 79),
    (14, 15, 37), (14, 29, 71), (15, 16, 114), (15, 30, 66), (16, 17, 60), (16, 31, 57),
    (17, 18, 69), (17, 33, 48), (18, 35, 52), (19, 20, 95), (20, 21, 107), (20, 23, 41),
    (21, 25, 36), (22, 23, 93), (22, 36, 83), (23, 24, 58), (23, 37, 84), (24, 25, 54),
    (24, 38, 84), (25, 26, 75), (25, 39, 86), (26, 27, 53), (26, 40, 91), (27, 28, 59),
    (27, 41, 92), (28, 29, 60), (28, 42, 93), (29, 30, 46), (29, 43, 100), (30, 31, 96),
    (30, 44, 100), (31, 32, 52), (31, 45, 103), (32, 33, 45), (32, 46, 111), (33, 34, 45),
    (33, 47, 103), (34, 35, 46), (34, 48, 112), (35, 49, 114), (36, 37, 90), (36, 50, 52),
    (37, 38, 48), (37, 51, 55), (38, 39, 64), (39, 52, 55), (39, 40, 63), (40, 41, 54),
    (40, 53, 54), (41, 42, 59), (41, 54, 59), (42, 43, 54), (42, 55, 60), (43, 44, 42),
    (43, 56, 58), (44, 45, 91), (44, 57, 58), (45, 46, 55), (45, 58, 56), (46, 47, 44),
    (46, 59, 55), (47, 48, 38), (47, 60, 53), (48, 49, 48), (49, 61, 51), (50, 51, 84),
    (50, 62, 66), (51, 52, 112), (51, 63, 64), (52, 53, 54), (52, 65, 60), (53, 54, 54),
    (53, 66, 56), (54, 55, 63), (54, 67, 56), (55, 56, 64), (55, 68, 58), (56, 57, 46),
    (56, 69, 58), (57, 70, 61), (58, 59, 59), (58, 71, 68), (59, 60, 53), (59, 72, 65),
    (60, 61, 88), (60, 73, 62), (61, 74, 63), (62, 63, 79), (62, 75, 62), (63, 64, 68),
    (63, 76, 59), (64, 65, 47), (64, 77, 61), (65, 66, 52), (65, 78, 60), (66, 67, 48),
    (67, 68, 60), (67, 80, 57), (68, 69, 49), (68, 81, 58), (69, 70, 56), (69, 82, 55),
    (70, 71, 63), (71, 72, 69), (71, 83, 50), (72, 73, 55), (72, 84, 53), (73, 74, 92),
    (73, 85, 54), (75, 76, 72), (76, 77, 68), (77, 78, 51), (78, 79, 64), (79, 80, 27),
    (79, 86, 45), (80, 81, 59), (81, 82, 49), (81, 86, 80), (82, 83, 125), (82, 87, 54),
    (83, 84, 70), (83, 88, 55), (84, 85, 53), (84, 89, 94), (85, 90, 66), (90, 91, 95),
    (90, 92, 68)
]


# ---------------------------
# 2. CONSTRUÇÃO DO GRAFO
# ---------------------------

def build_graph(dados):
    G = nx.Graph()
    for u, v, dist in dados:
        G.add_edge(u, v, distancia=dist)
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
    dn = normalize([G[u][v]["distancia"] for u, v in G.edges()])

    for (edge, dnorm) in zip(G.edges(), dn):
        u, v = edge
        G[u][v]["peso"] = dnorm

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
def tempo_aresta(dist):
    return 0.0075 * dist # minutos

# Tempo total se 1 agente fizer tudo
tempo_1_agente = sum(tempo_aresta(G[u][v]["distancia"]) for u, v in G.edges())


# ------------------------------------------
# 6. CALCULAR TEMPO REAL POR AGENTE
# ------------------------------------------

def tempo_subgrafo(G, conjunto):
    tempo = 0
    for u, v in G.edges():
        if u in conjunto and v in conjunto:
            tempo += tempo_aresta(G[u][v]["distancia"])
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