def hanoi(n, source, auxiliary, target, moves, rods):
    if n == 1:
        disk = rods[source][-1]
        if can_place(rods[target], disk):
            rods[source].pop()
            rods[target].append(disk)
            moves.append((disk[0], source, target))
        else:
            return -1
    else:
        if hanoi(n - 1, source, target, auxiliary, moves, rods) == -1:
            return -1
        
        disk = rods[source][-1]
        if can_place(rods[target], disk):
            rods[source].pop()
            rods[target].append(disk)
            moves.append((disk[0], source, target))
        else:
            return -1
        
        if hanoi(n - 1, auxiliary, source, target, moves, rods) == -1:
            return -1
    
    return moves


def can_place(rod, disk):
    """Verifica si se puede colocar un disco en la vara según las reglas."""
    if not rod:
        return True
    top_disk = rod[-1]
    return disk[0] < top_disk[0] and disk[1] != top_disk[1]  # Tamaño menor y color diferente


def solve_hanoi(disks):
    """Función principal para inicializar las varas y ejecutar el algoritmo de Hanoi."""
    rods = {'A': list(disks), 'B': [], 'C': []}
    moves = []
    result = hanoi(len(disks), 'A', 'B', 'C', moves, rods)
    return result if result != -1 else -1


if __name__ == "__main__":
    import ast
    while True:
        user_input = input("Ingrese la lista de discos en el formato [(tamaño, 'color'), ...] o 'exit' para salir: ")
        if user_input.lower() == 'exit':
            break
        try:
            disks = ast.literal_eval(user_input)
            if not isinstance(disks, list) or not all(isinstance(d, tuple) and len(d) == 2 and isinstance(d[0], int) and isinstance(d[1], str) for d in disks):
                print("Entrada inválida. Intente de nuevo.")
                continue
            
            n = len(disks)
            if disks != sorted(disks, reverse=True, key=lambda x: x[0]):
                print(-1)
            else:
                result = solve_hanoi(disks)
                print(result)
        except Exception as e:
            print(f"Error en la entrada: {e}. Intente nuevamente.")
