from collections import deque

##############################################################################################################################
                                    # Clase para gestionar una lista de tareas (lista)
##############################################################################################################################

class Lista:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, tarea):
        if tarea in self.tareas:
            self.tareas.remove(tarea)

    def buscar_tarea(self, tarea):
        return tarea in self.tareas

    def mostrar_tareas(self):
        return self.tareas

##############################################################################################################################
                                    # Clase para gestionar el pila (Pila)
##############################################################################################################################

class pila:
    def __init__(self):
        self.pila = []

    def agregar_accion(self, accion):
        self.pila.append(accion)

    def deshacer_accion(self):
        if self.pila:
            return self.pila.pop()
        return None

    def mostrar_pila(self):
        return self.pila

##############################################################################################################################
                        # Clase para gestionar la cola de tareas urgentes (cola)
##############################################################################################################################


class Cola:
    def __init__(self):
        self.cola = deque()

    def agregar_tarea(self, tarea):
        self.cola.append(tarea)

    def atender_tarea(self):
        if self.cola:
            return self.cola.popleft()
        return None

    def primer_tarea(self):
        return self.cola[0] if self.cola else None

    def ultima_tarea(self):
        return self.cola[-1] if self.cola else None

    def mostrar_tareas(self):
        return list(self.cola)
    
##############################################################################################################################
                        # Clase para gestionar arbol y subtareas (Árbol)
##############################################################################################################################

class arbol:
    def __init__(self):
        self.arbol = {}

    def agregar_proyecto(self, nombre):
        if nombre not in self.arbol:
            self.arbol[nombre] = []

    def agregar_tarea_a_proyecto(self, nombre_proyecto, tarea):
        if nombre_proyecto in self.arbol:
            self.arbol[nombre_proyecto].append(tarea)

    def mostrar_arbol(self):
        return self.arbol

##############################################################################################################################
                                                         # uso del sistema
##############################################################################################################################


if __name__ == "__main__":
    # Crear instancias de cada clase
    lista = Lista()
    pila = pila()
    cola = Cola()
    arbol = arbol()

    # Gestionar lista de tareas (lista)
    lista.agregar_tarea("Actualizar reporte")
    lista.agregar_tarea("Enviar correos")
    lista.eliminar_tarea("Enviar correos")
    print("Lista de tareas:", lista.mostrar_tareas())
    print("¿Existe 'Reunión con el equipo'?:", lista.buscar_tarea("Reunión con el equipo"))

    # Gestionar pila (pila)
    pila.agregar_accion("Creó tarea A")
    pila.agregar_accion("Actualizó tarea B")
    print("historial:", pila.mostrar_pila())
    print("Deshacer acción:", pila.deshacer_accion())
    print("historial después de deshacer:", pila.mostrar_pila())

    # Gestionar cola de tareas urgentes (cola)
    cola.agregar_tarea("Resolver ticket 101")
    cola.agregar_tarea("Atender llamada cliente")
    cola.agregar_tarea("Preparar informe urgente")
    print("Primera tarea urgente:", cola.primer_tarea())
    print("Última tarea urgente:", cola.ultima_tarea())
    print("Atendiendo tarea:", cola.atender_tarea())
    print("Tareas urgentes restantes:", cola.mostrar_tareas())

    # Gestionar arbol (árbol)
    arbol.agregar_proyecto("Proyecto Geminis")
    arbol.agregar_proyecto("Proyecto Aries")
    arbol.agregar_tarea_a_proyecto("Proyecto Geminis", "Tarea 1")
    arbol.agregar_tarea_a_proyecto("Proyecto Geminis", "Tarea 2")
    arbol.agregar_tarea_a_proyecto("Proyecto Aries", "Tarea 3")
    print("proyectos y tareas:")
    for proyecto, tareas in arbol.mostrar_arbol().items():
        print(f"\n{proyecto}:")
        for tarea in tareas:
            print(f" - {tarea}")
