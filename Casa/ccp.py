import networkx as nx
import matplotlib.pyplot as plt
import itertools

# =========================================================
# 1. ENTRADA DE DADOS
# =========================================================
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

# Clusters
A_vertices = set([1,2,3,4,5,6,7,15,16,17,18,31,32,33,34,35,
                  45,46,47,48,49,58,59,60,61,71,72,73,74,85,
                  90,91,92])

B_vertices = set([8,9,10,11,12,13,14,19,20,21,22,23,24,25,26,
                  27,28,29,30,36,37,38,39,40,41,42,43,44,50,
                  51,52,53,54,55,56,57,62,63,64,65,66,67,68,
                  69,70,71,75,76,77,78,79,80,81,82,83,84,86,87,
                  88,89])

START = 71  # Ponto inicial


# =========================================================
# 2. CONSTRUÇÃO DO GRAFO
# =========================================================
G = nx.Graph()

for u, v, casas in dados:
    peso = casas
    G.add_edge(u, v, casas=casas, peso=peso)


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