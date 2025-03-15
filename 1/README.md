# Torre de Hanoi con Restricciones de Color

Este programa resuelve el problema de la Torre de Hanoi con la restricción adicional de que no se pueden colocar discos del mismo color directamente uno sobre otro. Utiliza recursión para mover los discos desde la varilla de origen hasta la varilla de destino, siguiendo las reglas establecidas.

## Requisitos

Para ejecutar este script, necesitas tener instalado Python 3.

## Cómo ejecutar la aplicación

1. Abre una terminal o consola de comandos.
2. Ejecuta el script de Python e ingresa la lista de discos en una sola línea, respetando el formato requerido.

Ejemplo de ejecución:

```bash
python hanoi.py
```

Ejemplo de entrada:

```
Ingrese la lista de discos: [(5, "red"), (4, "blue"), (3, "red"), (2, "green"), (1, "blue")]
```

Ejemplo de salida:

```
[(1, 'A', 'C'), (2, 'A', 'B'), (1, 'C', 'B'), (3, 'A', 'C'), (1, 'B', 'A'), (2, 'B', 'C'), (1, 'A', 'C')]
```

Si el problema no tiene solución debido a la restricción de color, el programa devuelve `-1`.

---

## Explicación del Código

### `hanoi_with_colors(n, disks, source, target, auxiliary, moves, last_colors)`

Este método es la función recursiva que maneja la transferencia de discos siguiendo las reglas del problema.

1. Si `n` es 0, termina la recursión.
2. Intenta mover los `n-1` discos superiores a la varilla auxiliar.
3. Verifica que el disco actual pueda moverse a la varilla de destino sin violar la restricción de color.
4. Agrega el movimiento del disco más grande al destino y actualiza los registros de color.
5. Mueve los `n-1` discos desde la varilla auxiliar al destino.

### `solve_hanoi(disks)`

Esta función toma la lista de discos como entrada y ejecuta el algoritmo de la Torre de Hanoi con restricciones de color.

1. Determina el número total de discos.
2. Inicializa la estructura que almacena los movimientos.
3. Llama a la función recursiva para resolver el problema.
4. Si la solución no es posible, devuelve `-1`, de lo contrario, retorna la lista de movimientos.

### Entrada del Usuario

El programa solicita una lista de discos en el formato `[(size, "color"), ...]`, la convierte en una estructura de datos y la envía a `solve_hanoi()`.

---

## Notas
- El programa funciona con hasta `n = 8` discos.
- Se valida que la restricción de color se cumpla en cada paso.
- La salida muestra los movimientos necesarios en formato `(tamaño, origen, destino)`.

Este programa es ideal para comprender la recursión aplicada a problemas con restricciones adicionales. 

