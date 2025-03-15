# API REST

Bienvenido a la API REST desarrollada con **FastAPI** y **PostgreSQL** para gestionar resultados de procesamiento de imágenes médicas. Esta API permite recibir datos de imágenes médicas en formato de matriz, normalizarlos, calcular promedios y almacenarlos de manera estructurada.

---

## **Instrucciones para ejecutar la aplicación**

### **1 Requisitos previos**

Antes de ejecutar la aplicación, asegúrate de tener instalados:

- **Python 3.9 o superior**  
- **PostgreSQL** (Debe estar corriendo en local o en un servidor accesible)  
- **Poetry** (Opcional, pero recomendado para gestionar dependencias)  

### **2 Clonar el repositorio**

```sh
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```

### **3 Configurar la base de datos**

Crea una base de datos en PostgreSQL y agrega las credenciales en el archivo **`.env`**:

```
DATABASE_URL=postgresql+asyncpg://usuario:contraseña@localhost:5432/nombre_de_la_base
```

Luego, ejecuta las migraciones para crear las tablas:

```sh
alembic upgrade head
```

### **4 Ejecutar la API**

Inicia el servidor con:

```sh
uvicorn main:app --reload
```

La API estará disponible en [http://127.0.0.1:8000](http://127.0.0.1:8000)

Puedes ver la documentación interactiva en:  
- [Swagger UI](http://127.0.0.1:8000/docs)  

---

## **Descripción de los Endpoints**

### `POST /medical-results/` - **Crear resultados médicos**

Este endpoint recibe un conjunto de matrices representando imágenes médicas, normaliza sus valores, calcula los promedios antes y después de la normalización, y almacena los resultados en la base de datos.

 **Ejemplo de Request:**

```json
{
    "1": {
        "id": "aabbcc1",
        "data": [
            "78 83 21 68 96",
            "58 75 71 69 33"
        ],
        "deviceName": "CT SCAN"
    },
    "2": {
        "id": "aabbcc2",
        "data": [
            "14 85 30 41 64",
            "68 53 85 9 35"
        ],
        "deviceName": "MRI SCAN"
    }
}
```

 **Ejemplo de Respuesta:**

```json
[
    {
        "id": 1,
        "external_id": "aabbcc1",
        "device_id": 5,
        "average_before": 62.8,
        "average_after": 0.62,
        "data_size": 10
    },
    {
        "id": 2,
        "external_id": "aabbcc2",
        "device_id": 6,
        "average_before": 46.5,
        "average_after": 0.46,
        "data_size": 10
    }
]
```

⚠ **Errores posibles**:
- `400 Bad Request`: Si la matriz contiene valores no numéricos.
- `409 Conflict`: Si el `external_id` ya existe en la base de datos.
- `500 Internal Server Error`: Si ocurre un problema inesperado.

---

##  **Notas finales**

Si tienes dudas o encuentras errores, revisa los logs de la aplicación o consulta la documentación en `/docs`. También puedes contribuir al código con mejoras y optimizaciones. 🚀  
