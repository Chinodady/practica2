'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Proceso:
    def __init__(self, nombre, tiempo):
        # Inicializa el proceso con su nombre y tiempo requerido
        self.nombre = nombre
        self.tiempo = tiempo

class PilaFIFO:
    def __init__(self):
        # Inicializa la pila como una lista vacía
        self.pila = []

    def agregar_proceso(self, proceso):
        # Agrega un proceso al final de la pila (FIFO)
        self.pila.append(proceso)
        print(f"Proceso {proceso.nombre} agregado a la pila con tiempo de {proceso.tiempo} unidades.")

    def ejecutar_proceso(self):
        # Ejecuta el proceso que está al frente de la pila (FIFO)
        if self.pila:
            proceso = self.pila.pop(0)
            print(f"Ejecutando proceso {proceso.nombre} con tiempo de {proceso.tiempo} unidades.")
        else:
            print("No hay procesos en la pila para ejecutar.")

    def mostrar_pila(self):
        # Muestra los procesos en la pila
        if self.pila:
            print("Procesos en la pila:")
            for proceso in self.pila:
                print(f"Proceso {proceso.nombre} con tiempo de {proceso.tiempo} unidades.")
        else:
            print("La pila está vacía.")

# Ejemplo de uso del script

# Crear instancia de la pila FIFO
pila_procesos = PilaFIFO()

# Crear algunos procesos
proceso1 = Proceso("A", 5)
proceso2 = Proceso("B", 2)
proceso3 = Proceso("C", 8)
proceso4 = Proceso("D", 3)

# Agregar procesos a la pila
pila_procesos.agregar_proceso(proceso1)
pila_procesos.agregar_proceso(proceso2)
pila_procesos.agregar_proceso(proceso3)
pila_procesos.agregar_proceso(proceso4)

# Mostrar la pila
pila_procesos.mostrar_pila()

# Ejecutar procesos en el orden FIFO
pila_procesos.ejecutar_proceso()
pila_procesos.ejecutar_proceso()
pila_procesos.ejecutar_proceso()
pila_procesos.ejecutar_proceso()

# Mostrar la pila después de ejecutar los procesos
pila_procesos.mostrar_pila()
