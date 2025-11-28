tareas = []

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

def ver_tareas():
    if not tareas:
        print("La lista de tareas está vacía.")
        return

    print("\n--- Lista de Tareas ---")
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


if __name__ == "__main__":
    principal()