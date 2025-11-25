import networkx as nx
import matplotlib.pyplot as plt
import itertools

# =========================================================
# 1. ENTRADA DE DADOS
# =========================================================
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

# Clusters
A_vertices = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,
                  19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,
                  35,45,46,58,59,71,82,83,84,85,87,88,89,90,
                  91,92])

B_vertices = set([22,36,37,38,39,40,41,42,43,44,47,48,49,50,
                  51,52,53,54,55,56,57,60,61,62,63,64,65,66,
                  67,68,69,70,71,72,73,74,75,76,77,78,79,80,
                  81,86])

START = 71  # Ponto inicial


# =========================================================
# 2. CONSTRUÇÃO DO GRAFO
# =========================================================
G = nx.Graph()

for u, v, dist in dados:
    peso = dist
    G.add_edge(u, v, distancia=dist, peso=peso)


# =========================================================
# 3. SUBGRAFO DOS AGENTES
# =========================================================
edges_A = [(u, v) for u, v in G.edges() if u in A_vertices and v in A_vertices]
edges_B = [(u, v) for u, v in G.edges() if u in B_vertices and v in B_vertices]

G_A = G.edge_subgraph(edges_A).copy()
G_B = G.edge_subgraph(edges_B).copy()

# =========================================================
# 3.1 TRATAR ARESTAS ENTRE CLUSTERS (A <-> B)
# =========================================================

edges_AB = [(u, v) for u, v in G.edges() 
            if (u in A_vertices and v in B_vertices) or
               (u in B_vertices and v in A_vertices)]

for u, v in edges_AB:
    # Distâncias do START até as extremidades
    d_u = nx.shortest_path_length(G, START, u, weight="peso")
    d_v = nx.shortest_path_length(G, START, v, weight="peso")

    # Aresta vai para o cluster mais próximo do START
    if d_u < d_v:
        if u in A_vertices:
            G_A.add_edge(u, v, **G[u][v])
        else:
            G_B.add_edge(u, v, **G[u][v])
    else:
        if v in A_vertices:
            G_A.add_edge(u, v, **G[u][v])
        else:
            G_B.add_edge(u, v, **G[u][v])


# =========================================================
# 4. FUNÇÃO CPP
# =========================================================
def chinese_postman(G_sub, start):
    # Garantir que start esteja no subgrafo
    if start not in G_sub:
        start = list(G_sub.nodes())[0]  # usa outro nó

    # 1. Vértices ímpares
    odd = [v for v in G_sub.nodes() if G_sub.degree(v) % 2 == 1]

    # 2. Grafo completo entre ímpares (distâncias reais)
    K = nx.Graph()
    for u, v in itertools.combinations(odd, 2):
        dist = nx.shortest_path_length(G_sub, u, v, weight="peso")
        K.add_edge(u, v, weight=dist)

    # 3. Matching mínimo
    M = nx.min_weight_matching(K, weight="weight")

    # 4. Duplicação correta das arestas do caminho mínimo
    G_euler = nx.MultiGraph(G_sub)

    for u, v in M:
        path = nx.shortest_path(G_sub, u, v, weight="peso")
        for a, b in zip(path, path[1:]):
            G_euler.add_edge(a, b, peso=G_sub[a][b]["peso"])

    # 5. Agora é Euleriano
    circuito = list(nx.eulerian_circuit(G_euler, source=start))

    rota = [start]
    for u, v in circuito:
        rota.append(v)

    return rota


# =========================================================
# 5. ROTAS
# =========================================================
rota_A = chinese_postman(G_A, START)
rota_B = chinese_postman(G_B, START)

print("\nROTA AGENTE A:")
print(rota_A)

print("\nROTA AGENTE B:")
print(rota_B)


# =========================================================
# 6. PLOTAR MAPA DESTACANDO AS ROTAS A E B
# =========================================================
# Converter rotas em arestas
edges_rota_A = list(zip(rota_A[:-1], rota_A[1:]))
edges_rota_B = list(zip(rota_B[:-1], rota_B[1:]))

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(12, 10))

# Todas as ruas em cinza
nx.draw_networkx_edges(G, pos, edge_color='lightgray', width=2)

# Rota A (azul)
nx.draw_networkx_edges(G, pos,
                       edgelist=edges_rota_A,
                       edge_color='blue',
                       width=3,
                       label='Agente A')

# Rota B (vermelho)
nx.draw_networkx_edges(G, pos,
                       edgelist=edges_rota_B,
                       edge_color='red',
                       width=3,
                       label='Agente B')

# Nós
nx.draw_networkx_nodes(G, pos, node_size=300, node_color='white', edgecolors='black')
nx.draw_networkx_labels(G, pos, font_size=9)

plt.legend()
plt.title("Divisão ótima do percurso entre dois agentes (partindo do 71)")
plt.axis('off')
plt.show()