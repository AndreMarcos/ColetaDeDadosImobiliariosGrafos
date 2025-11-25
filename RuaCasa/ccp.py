import networkx as nx
import matplotlib.pyplot as plt
import itertools

# =========================================================
# 1. ENTRADA DE DADOS
# =========================================================

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

# Clusters
A_vertices = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,
                  27,28,29,30,31,32,33,34,35,41,42,43,44,45,
                  46,47,48,49,58,59,71,82,83,87,88])

B_vertices = set([19,20,21,22,23,24,25,26,36,37,38,39,40,50,51,52,
                  53,54,55,56,57,60,61,62,63,64,65,66,67,68,
                  69,70,71,72,73,74,75,76,77,78,79,80,81,
                  84,85,86,89,90,91,92])

START = 71  # Ponto inicial


# =========================================================
# 2. CONSTRUÇÃO DO GRAFO
# =========================================================
G = nx.Graph()

for u, v, dist, casas in dados:
    peso = 0.6 * dist + 0.4 * casas
    G.add_edge(u, v, distancia=dist, casas=casas, peso=peso)


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
