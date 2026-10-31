
class Nodo:
    def __init__(self, videojuego):
        self.videojuego = videojuego
        self.izquierdo = None
        self.derecho = None
    

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, videojuego):
        if self.raiz is None :
            self.raiz = Nodo(videojuego)
        else : self._insertar_recursivo(self.raiz, videojuego)

    def _insertar_recursivo(self, nodo_actual, videojuego):
        if videojuego.nombre < nodo_actual.videojuego.nombre:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(videojuego)
            else:
                  self._insertar_recursivo(nodo_actual.izquierdo, videojuego)
        
        elif videojuego.nombre > nodo_actual.videojuego.nombre :
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(videojuego)

            else:
                  self._insertar_recursivo(nodo_actual.derecho, videojuego)
    
    def buscar(self, nombre, ):
        if self.raiz is None:
            return None
        
        elif self.raiz.videojuego.nombre == nombre:
            return self.raiz.videojuego
        else: 
            return self._busqueda_recursiva(self.raiz, nombre)


    def _busqueda_recursiva(self, nodo_actual, nombre):
        if nodo_actual is None:
             return None
             
        if nombre == nodo_actual.videojuego.nombre:
                  return nodo_actual.videojuego

        if nombre < nodo_actual.videojuego.nombre:
               return self._busqueda_recursiva(nodo_actual.izquierdo , nombre)

        elif nombre > nodo_actual.videojuego.nombre:
                return self._busqueda_recursiva(nodo_actual.derecho , nombre)
    
    def inorder(self):
       self._inorder_recursivo(self.raiz)

    def _inorder_recursivo(self, nodo_actual):
      if nodo_actual is None:
        return

      self._inorder_recursivo(nodo_actual.izquierdo)

      print(nodo_actual.videojuego)

      self._inorder_recursivo(nodo_actual.derecho)
    
    def preorden(self):
         self._preorden_recursivo(self.raiz)
    
    def _preorden_recursivo(self, nodo_actual):
         if nodo_actual is None:
              return
         
         print(nodo_actual.videojuego)
         
         self._preorden_recursivo(nodo_actual.izquierdo)

         self._preorden_recursivo(nodo_actual.derecho)
        
    def postorden(self):
         self._postorden_recursivo(self.raiz)
    
    def _postorden_recursivo(self, nodo_actual):
         if nodo_actual is None:
              return
         
         self._postorden_recursivo(nodo_actual.izquierdo)

         self._postorden_recursivo(nodo_actual.derecho)

        print(nodo_actual.videojuego)  
class GrafoVideojuegos:
    def __init__(self):
    
        self.adyacencias = {}

    def agregar_vertice(self, videojuego):
        
        if videojuego not in self.adyacencias:
            self.adyacencias[videojuego] = []

    def agregar_arista(self, juego1, juego2):
    
        self.agregar_vertice(juego1)
        self.agregar_vertice(juego2)
        
        if juego2 not in self.adyacencias[juego1]:
            self.adyacencias[juego1].append(juego2)
        if juego1 not in self.adyacencias[juego2]:
            self.adyacencias[juego2].append(juego1)

    def obtener_recomendaciones(self, videojuego):
        return self.adyacencias.get(videojuego, [])
