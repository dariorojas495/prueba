# File Processor

## Descripción

Este script en Python permite analizar el contenido de una carpeta, generando reportes sobre archivos y subcarpetas presentes en ella. Además, procesa archivos CSV para obtener estadísticas y archivos DICOM para extraer información y generar imágenes.

## Requisitos

Antes de ejecutar el script, asegúrate de tener instaladas las siguientes librerías:

```sh
pip install pandas pydicom numpy pillow
```

## Cómo ejecutar la aplicación

1. Abre una terminal o línea de comandos en la carpeta donde se encuentra el script.
2. Ejecuta el script con el siguiente comando:

```sh
python file_processor.py
```

El script automáticamente analizará la carpeta donde se encuentra y guardará un archivo de log en la misma ubicación.

## Funcionalidades

### `__init__(self, base_path: str, log_path: str)`
Inicializa el procesador de archivos con:
- `base_path`: La ruta base donde se analizarán los archivos.
- `log_path`: La ruta donde se guardará el archivo de log.

Configura el sistema de logging para registrar los eventos en un archivo llamado `logfile.log` dentro de la misma carpeta.

### `analyze_folder(self) -> None`
Este método recorre la carpeta base y analiza su contenido. Realiza las siguientes acciones:
- Cuenta y muestra la cantidad de archivos y carpetas dentro de la carpeta base.
- Muestra los nombres, tamaños y fechas de modificación de los archivos.
- Muestra los nombres y fechas de modificación de las carpetas.
- Si encuentra archivos `.csv`, llama a `read_csv()` para analizarlos.
- Si encuentra archivos `.dcm`, llama a `read_dicom()` para procesarlos.
- Registra toda la información en el archivo de log.

### `read_csv(self, file_path: str) -> None`
Este método analiza archivos CSV:
- Lee el archivo CSV e imprime el número de columnas y filas.
- Calcula y muestra la media y desviación estándar de las columnas numéricas.
- Muestra un resumen de valores únicos en columnas no numéricas.
- En caso de error, lo registra en el log y muestra un mensaje en la consola.

### `read_dicom(self, file_path: str, extract_image: bool = False) -> None`
Este método analiza archivos DICOM:
- Lee el archivo y muestra información del paciente, la fecha del estudio y la modalidad.
- Extrae y muestra valores de etiquetas DICOM específicas.
- Si `extract_image` es `True`, extrae la imagen del archivo DICOM y la guarda en la misma ubicación con formato `.png`.
- Registra la información en el log y maneja errores si el archivo no es válido o no se puede leer.

## Ejemplo de salida

```
Folder: ./data/test_folder
Number of elements: 5
Files:
 - file1.txt (1.2 MB, Last Modified: 2024-01-01 12:00:00)
 - file2.csv (0.8 MB, Last Modified: 2024-01-02 12:00:00)
Folders:
 - folder1 (Last Modified: 2024-01-01 15:00:00)
 - folder2 (Last Modified: 2024-01-03 16:00:00)

CSV Analysis:
Columns: ["Name", "Age", "Height"]
Rows: 100
Numeric Columns:
 - Age: Average = 30.5, Std Dev = 5.6
 - Height: Average = 170.2, Std Dev = 10.3
Non-Numeric Summary:
 - Name: Unique Values = 50
Saved summary report to ./reports

DICOM Analysis:
Patient Name: John Doe
Study Date: 2024-01-01
Modality: CT
Tag 0x0010, 0x0010: John Doe
Tag 0x0008, 0x0060: CT
Extracted image saved to ./data/sample-01-dicom.png
```

## Notas
- El script procesará automáticamente todos los archivos CSV y DICOM en la carpeta base.
- Se recomienda ejecutar el script en una carpeta con archivos de prueba para verificar su funcionamiento.
- Los errores se registran en el archivo `logfile.log` para facilitar la depuración.
