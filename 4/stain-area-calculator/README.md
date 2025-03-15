# 🖼️ Stain Area Calculator

Esta es una aplicación web desarrollada en **Angular 17** que permite calcular el área de una mancha en una imagen binaria utilizando el método de muestreo aleatorio de puntos.

## 📌 Características

- **Carga de imagen** binaria (blanco = mancha, negro = fondo).
- **Cálculo del área de la mancha** mediante muestreo de Monte Carlo.
- **Historial de cálculos** mostrados en una tabla.
- **Explicación del método en un carrusel interactivo**.

---

##  Instalación y Ejecución

### 1️⃣ **Clonar el repositorio**
```sh
git clone https://github.com/tu-usuario/stain-area-calculator.git
cd stain-area-calculator
```

### 2️⃣ **Instalar dependencias**
```sh
npm install
```

### 3️⃣ **Ejecutar la aplicación**
```sh
ng serve
```

Luego, abre tu navegador y accede a `http://localhost:4200/`.

## 🛠️ Explicación de Métodos

### `upload-image.component.ts`
- `onFileSelected(event: Event)`: Maneja la selección de una imagen por parte del usuario. Convierte la imagen en datos binarios y la almacena.

### `stain-calculator.component.ts`
- `calculateArea()`: Genera `n` puntos aleatorios dentro de la imagen y cuenta cuántos caen dentro de la mancha (pixeles blancos). Calcula el área usando la fórmula:

  \[ Area = (Total Image Area) 	imes (ni/n) \]

### `stain.service.ts`
- `saveResult(area: number)`: Guarda un nuevo resultado en la lista de cálculos previos.
- `getResults()`: Devuelve la lista de cálculos previos.

### `results-table.component.ts`
- Muestra una tabla con los resultados de cálculos anteriores.

### `carousel.component.ts`
- Explica paso a paso el método de muestreo usando un carrusel interactivo.

---
