class Grafo:

    def __init__(self):
        self.adyacencia = {}
    
    def agregar_vertice(self, videojuego):
        if videojuego not in self.adyacencia:
            self.adyacencia[videojuego] = []
    
    def agregar_arista(self, juego1, juego2):

        if juego2 not in self.adyacencia[juego1]:
            self.adyacencia[juego1].append(juego2)

        if juego1 not in self.adyacencia[juego2]:
            self.adyacencia[juego2].append(juego1)
    
    def mostrar_vecinos(self, videojuego):
        if videojuego not in self.adyacencia:
            print("El videojuego no tiene conexiones.")
            return
        
        print(f"\n🎮 Juegos relacionados con {videojuego.nombre}:\n")
        
        for vecino in self.adyacencia[videojuego]:
            print(f"- {vecino.nombre}")

def bfs(self, inicio):
        if inicio not in self.adyacencia:
            return []

        visitados = {inicio}
        cola = [inicio]
        orden = []

        while cola:
            actual = cola.pop(0)
            orden.append(actual)
            for vecino in self.adyacencia[actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)

        return orden

    def dfs(self, inicio, visitados=None):
        if inicio not in self.adyacencia:
            return []

        if visitados is None:
            visitados = set()

        visitados.add(inicio)
        orden = [inicio]

        for vecino in self.adyacencia[inicio]:
            if vecino not in visitados:
                orden.extend(self.dfs(vecino, visitados))

        return orden
