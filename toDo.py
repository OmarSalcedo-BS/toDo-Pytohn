import json
import os

TODO_FILE = "tareas.json"

tareas = []


def cargar_tareas():
    if not os.path.exists(TODO_FILE) or os.path.getsize(TODO_FILE) == 0:
        return []
    try:
        with open(TODO_FILE, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        print("Error: El archivo de tareas está corrupto. Se iniciará una lista vacía.")
        return []



def guardar_tareas():
    with open(TODO_FILE, 'w', encoding='utf-8') as archivo:
        json.dump(tareas, archivo, ensure_ascii=False, indent=4)
        print(f" Tareas guardadas correctamente. en {TODO_FILE}")
        

def mostrar_menu():
  
    print("\n--- Bienvenido al To-Do ---")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. eliminar tareas")
    print("5. Salir")
    print("------------------")

def anadir_tarea(tarea):
    tareas.append((tarea, False))
    print(f" Tarea '{tarea}' añadida.")
    guardar_tareas()

def ver_tareas():
    if not tareas:
        print("La lista de tareas está vacía.")
        return

    print("\n--- Lista de Tareas ---")
    cargar_tareas()
    for i, (tarea, completada) in enumerate(tareas):
        estado = "[X] Completada" if completada else "[ ] Pendiente"
        print(f"{i + 1}. {estado} - {tarea}")
    print("-------------------------")

def marcar_completada(numero_tarea):
    try:
        indice = int(numero_tarea) - 1

        if 0 <= indice < len(tareas):
            tarea_actual = tareas[indice]
            tarea_actualizada = (tarea_actual[0], True)
            tareas[indice] = tarea_actualizada
            print(f" Tarea '{tarea_actual[0]}' marcada como completada.")
        else:
            print("Error: Número de tarea inválido.")

    except ValueError:
        print("Error: Por favor, introduce un número.")
        
        
def eliminar_tarea(numero_tarea):
    try:
        indice = int(numero_tarea) - 1
    except ValueError:
        print("Error: Por favor, introduce un número.")
        return
    
    if 0 <= indice < len(tareas):
        tarea_actual = tareas[indice]
        tareas.pop(indice)
        print(f" Tarea '{tarea_actual[0]}' eliminada.")
    else:
        print("Error: Número de tarea inválido.")
            

def principal():
    global tareas
    tareas = cargar_tareas()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción del 1 al 5: ")

        if opcion == '1':
            descripcion = input("Introduce la nueva tarea: ")
            if descripcion:
                anadir_tarea(descripcion)
            else:
                print("La descripción de la tarea no puede estar vacía.")

        elif opcion == '2':
            ver_tareas()

        elif opcion == '3':
            ver_tareas()
            if tareas:
                num = input("Introduce el número de la tarea a marcar como completada: ")
                marcar_completada(num)
        elif opcion == '4':
            ver_tareas()
            if tareas:
                num = input("Introduce el número de la tarea a eliminar: ")
                eliminar_tarea(num)

        elif opcion == '5':
            print(" ¡Gracias por usar el programa To-Do! Saliendo...")
            break

        else:
            print(" Opción no válida. Por favor, elige un número del 1 al 5.")


principal()