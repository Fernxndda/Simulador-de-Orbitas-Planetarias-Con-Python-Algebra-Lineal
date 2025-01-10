import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Planeta:
    def __init__(self, nombre, radio_orbital, velocidad_angular, factor_escala):
        self.nombre = nombre
        self.radio_orbital = radio_orbital
        self.velocidad_angular = np.deg2rad(velocidad_angular)  
        self.factor_escala = factor_escala
        self.angulo = 0  

    def matriz_rotacion(self, angulo):
        return np.array([[np.cos(angulo), -np.sin(angulo)],
                         [np.sin(angulo),  np.cos(angulo)]])

    def matriz_escalado(self, factor_escala):
        return np.array([[factor_escala, 0],
                         [0, factor_escala]])

    def obtener_posicion(self):
        vector_posicion = np.array([self.radio_orbital, 0])  
        rotacion = self.matriz_rotacion(self.angulo)
        escalado = self.matriz_escalado(self.factor_escala)
        posicion = escalado @ (rotacion @ vector_posicion)
        return posicion[0], posicion[1]

    def actualizar_posicion(self, dt):
        self.angulo += self.velocidad_angular * dt
        self.angulo %= 2 * np.pi  

planetas = []

def configurar_planetas():
    num_planetas = int(input("Ingrese el número de planetas a simular: "))
    for i in range(num_planetas):
        nombre = input(f"Nombre del planeta {i + 1}: ")
        radio_orbital = float(input(f"Radio orbital del planeta {nombre} (en unidades arbitrarias): "))
        velocidad_angular = float(input(f"Velocidad angular del planeta {nombre} (en grados/segundo): "))
        factor_escala = float(input(f"Factor de escala del planeta {nombre}: "))
        planetas.append(Planeta(nombre, radio_orbital, velocidad_angular, factor_escala))


configurar_planetas()


print("\nParámetros de los planetas:")
for planeta in planetas:
    print(f"Nombre: {planeta.nombre}, Radio orbital: {planeta.radio_orbital}, Velocidad angular: {np.rad2deg(planeta.velocidad_angular)} grados/segundo, Factor de escala: {planeta.factor_escala}")


fig, ax = plt.subplots()
ax.set_aspect('equal', 'box')
ax.set_xlim(-200, 200)
ax.set_ylim(-200, 200)
sol = plt.Circle((0, 0), 2, color='yellow')
ax.add_artist(sol)
trayectorias = [ax.plot([], [], label=f"{planeta.nombre} (Radio: {planeta.radio_orbital:.2f}, Velocidad: {np.rad2deg(planeta.velocidad_angular):.2f} grados/s)")[0] for planeta in planetas]
puntos = [ax.plot([], [], 'o')[0] for _ in planetas]


def init():
    for trayectoria in trayectorias:
        trayectoria.set_data([], [])
    for punto in puntos:
        punto.set_data([], [])
    return trayectorias + puntos


def update(frame):
    for i, planeta in enumerate(planetas):
        planeta.actualizar_posicion(0.1)
        x, y = planeta.obtener_posicion()
        trayectorias[i].set_data(planeta.radio_orbital * planeta.factor_escala * np.cos(np.linspace(0, 2 * np.pi, 100)),
                                 planeta.radio_orbital * planeta.factor_escala * np.sin(np.linspace(0, 2 * np.pi, 100)))
        puntos[i].set_data(x, y)
    return trayectorias + puntos

ani = FuncAnimation(fig, update, frames=np.arange(0, 100, 0.1), init_func=init, blit=True, interval=50)
ax.legend()
plt.show()
