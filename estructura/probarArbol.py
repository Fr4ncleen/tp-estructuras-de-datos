from .arbol_binario import ArbolBinarioBusqueda
from datos.gestor_datos import cargar_videojuegos

juegos = cargar_videojuegos()

arbol = ArbolBinarioBusqueda()

for juego in juegos:
    arbol.insertar(juego)

resultado = arbol.buscar("Minecraft")
resultado2 = arbol.buscar("League of Legends")
resultado3 = arbol.buscar ("Raibow six siege")

resultados = [
    ("Minecraft", resultado),
    ("League of Legends", resultado2),
    ("Rainbow six siege", resultado3)
    ]
print("Resultados de búsqueda:")

for nombre_buscado, juego in resultados:
    print(f"\nBuscando: '{nombre_buscado}'")
    if juego:
        print(f"Encontrado: {juego}")
    else:
        print("No se encontró el videojuego.")

print(resultado)

print("===== INORDER =====")
arbol.inorder()

print("\n===== PREORDER =====")
arbol.preorden()

print("\n===== POSTORDER =====")
arbol.postorden()
juegos_a_eliminar = "League of legends"
print(f""\n===== ELIMINANDO '{juego_a_eliminar}' =====")
elliminado= arbol.eliminar(juego_a_eliminar)

if eliminado:
    print(f"¡'{juego_a_eliminar}' fue eliminado correctamente del árbol!")
else:
    print(f"No se pudo eliminar '{juego_a_eliminar}' (no existía en el árbol).")

print("\n===== RECORRIDO INORDER ACTUALIZADO =====")
arbol.inorder()

print(f"\nBúsqueda tras eliminación de '{juego_a_eliminar}':")
res_busqueda = arbol.buscar(juego_a_eliminar)
if res_busqueda:
    print(f"Encontrado: {res_busqueda}")
else:
    print(f"Confirmado: '{juego_a_eliminar}' ya no está en el árbol.")

