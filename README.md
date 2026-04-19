# 🪐 Simulador de Órbitas Planetarias

Simulación animada de órbitas planetarias usando transformaciones
lineales (matrices de rotación y escalado) en Python.

## ¿Cómo funciona?
- El usuario define cuántos planetas simular y sus parámetros
- Cada planeta usa una **matriz de rotación** para calcular su posición
- La animación se actualiza en tiempo real con **matplotlib**

## Conceptos aplicados
- Álgebra lineal: matrices de rotación y escalado
- Programación orientada a objetos (clase `Planeta`)
- Animaciones con `FuncAnimation` de matplotlib

## Tecnologías
- Python 3
- numpy, matplotlib

## Cómo usarlo
1. Clona el repositorio
2. Ejecuta el archivo principal
3. Ingresa el número de planetas y sus parámetros:
   - Nombre
   - Radio orbital
   - Velocidad angular (grados/segundo)
   - Factor de escala
