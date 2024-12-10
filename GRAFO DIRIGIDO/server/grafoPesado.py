import heapq
from collections import deque

class Vertice:
    def __init__(self, vertice_id):
        self.id = vertice_id
        self.vecinos = {}  # Usar un conjunto para evitar duplicados y mejorar eficiencia.

    def add_vecino(self, vecino, peso):
        self.vecinos[vecino] = peso  # Inserción rápida con un set.

    def get_vecinos(self):
        return self.vecinos  # Devolver los vecinos.

    def remove_vecino(self, vecino):
        self.vecinos.remove(vecino)

    def existe_vecino(self, vecino):
        return vecino in self.vecinos

    def get_peso(self, vecino):
        return self.vecinos.get(vecino, None)

class Grafo:
    def __init__(self):
        self.vertices = {}

    def add_vertice(self, vertice):
        if not isinstance(vertice, Vertice):
            raise ValueError("El vértice debe ser una instancia de la clase Vertex.")
        if vertice.id in self.vertices:
            raise ValueError("El vértice ya existe.")
        self.vertices[vertice.id] = vertice
        return True
    
    
    def remove_vertice(self, vertice_id):
        if vertice_id not in self.vertices:
            # return False  # Vértice no existe.
            raise KeyError("El vértice no existe.")
        
        vertice = self.vertices[vertice_id]

        # Hacer una copia de los vecinos antes de modificar el conjunto
        vecinos_copia = list(vertice.get_vecinos())

        print(vecinos_copia)

        # Eliminar todas las aristas que le llegan al vértice
        for verticeCopy in self.vertices:
            self.remove_arista(verticeCopy, vertice_id)

        # Eliminar todas las aristas que salen del vértice
        for vecino in vecinos_copia:
            self.remove_arista(vertice_id, vecino)

        # Finalmente, eliminar el vértice del grafo
        del self.vertices[vertice_id]

        return True


    def add_arista(self, v1, v2, peso):
        if v1 not in self.vertices or v2 not in self.vertices:
            raise KeyError("Ambos vértices deben existir en el grafo.")
        if self.vertices[v1].existe_vecino(v2):
            raise ValueError("La arista ya existe.")
        self.vertices[v1].add_vecino(v2, peso)
        return True
    

    def remove_arista(self, v1, v2):
        if v1 not in self.vertices or v2 not in self.vertices:
            raise KeyError("Ambos vértices deben existir en el grafo.")
        self.vertices[v1].vecinos.discard(v2)
        self.vertices[v2].vecinos.discard(v1)
        return True


    def get_vertices(self):
        return list(self.vertices.keys())  # Devolver como lista.

    def __iter__(self):
        return iter(self.vertices.values())  # Iterar sobre los objetos Vertex.

    def __str__(self):
        """Representación del grafo como una lista de adyacencia."""
        return "\n".join(
            f"{vertice.id}: {sorted(vertice.vecinos)}" for vertice in self.vertices.values()
        )

    def get_grafo(self):
        return {
            vertice.id: [(vecino, peso) for vecino, peso in vertice.vecinos.items()]
            for vertice in self.vertices.values()
        }

    def clear(self):
        self.vertices.clear()
    
    def dijkstra(self, inicio, fin):
        if inicio not in self.vertices or fin not in self.vertices:
            raise KeyError("Ambos vértices deben existir en el grafo.")
        
        distancias = {vertice: float('infinity') for vertice in self.vertices}
        distancias[inicio] = 0
        camino = {vertice: None for vertice in self.vertices}
        pq = [(0, inicio)]

        while pq:
            (dist_actual, vertice_actual) = heapq.heappop(pq)

            if dist_actual > distancias[vertice_actual]:
                continue

            for vecino, peso in self.vertices[vertice_actual].get_vecinos().items():
                distancia = dist_actual + peso

                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    camino[vecino] = vertice_actual
                    heapq.heappush(pq, (distancia, vecino))

        ruta = []
        paso = fin
        while paso is not None:
            ruta.insert(0, paso)
            paso = camino[paso]

        if distancias[fin] == float('infinity'):
            return None  # No hay camino

        return ruta, distancias[fin]
    
    def bfs(self, inicio):
        if inicio not in self.vertices:
            raise KeyError("El vértice de inicio debe existir en el grafo.")
        
        visitados = set()
        cola = deque([inicio])
        recorrido = []

        while cola:
            vertice_actual = cola.popleft()
            if vertice_actual not in visitados:
                visitados.add(vertice_actual)
                recorrido.append(vertice_actual)
                for vecino in self.vertices[vertice_actual].get_vecinos():
                    if vecino not in visitados:
                        cola.append(vecino)

        return recorrido

    def dfs(self, inicio):
        if inicio not in self.vertices:
            raise KeyError("El vértice de inicio debe existir en el grafo.")
        
        visitados = set()
        pila = [inicio]
        recorrido = []

        while pila:
            vertice_actual = pila.pop()
            if vertice_actual not in visitados:
                visitados.add(vertice_actual)
                recorrido.append(vertice_actual)
                for vecino in self.vertices[vertice_actual].get_vecinos():
                    if vecino not in visitados:
                        pila.append(vecino)

        return recorrido


# Crear el grafo
grafo = Grafo()

# Agregar vértices
for vertice_id in ['A', 'E', 'C', 'D', 'B']:
    grafo.add_vertice(Vertice(vertice_id))

# Agregar aristas con pesos
grafo.add_arista('A', 'B', 1)
grafo.add_arista('A', 'C', 4)
grafo.add_arista('B', 'C', 2)
grafo.add_arista('B', 'D', 5)
grafo.add_arista('C', 'D', 1)
grafo.add_arista('D', 'E', 3)

# Probar el método dijkstra
inicio = 'A'
fin = 'E'
ruta, distancia = grafo.dijkstra(inicio, fin)
# Probar el método bfs
inicio_bfs = 'B'
recorrido_bfs = grafo.bfs(inicio_bfs)
print(f"Recorrido BFS desde {inicio_bfs}: {recorrido_bfs}")
# Probar el método dfs
inicio_dfs = 'B'
recorrido_dfs = grafo.dfs(inicio_dfs)
print(f"Recorrido DFS desde {inicio_dfs}: {recorrido_dfs}")