from datos.gestor_datos import cargar_videojuegos
from ui.terminal import iniciar

if __name__ == "__main__":
    iniciar()
def iniciar():
    videojuegos = cargar_videojuegos()
    while True:
        print("\n=== GESTOR DE VIDEOJUEGOS ===")
        print("1. Listar videojuegos")
        print("2. Buscar videojuego")
        print("3. Agregar videojuego")
        print("4. Editar videojuego")
        print("5. Eliminar videojuego")
        print("6. Salir")
