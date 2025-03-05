import numpy as np
import matplotlib.pyplot as plt

class ExperimentoDobleSRendijas:
    """
    Simulación del Experimento de la Doble Rendija en Mecánica Cuántica
    Este experimento muestra el comportamiento ondulatorio-particulado de la materia.
    """
    
    def __init__(self, num_particulas=10000, ancho_pantalla=100, distancia_rendijas=10):
        """
        Inicializa los parámetros del experimento.
        
        :param num_particulas: Número de partículas/fotones a simular
        :param ancho_pantalla: Ancho de la pantalla de detección
        :param distancia_rendijas: Distancia entre las dos rendijas
        """
        self.num_particulas = num_particulas
        self.ancho_pantalla = ancho_pantalla
        self.distancia_rendijas = distancia_rendijas
    
    def simular_experimento(self):
        """
        Simula el patrón del experimento de la doble rendija.
        :return: Distribución de probabilidad de impacto en la pantalla
        """
        # Crear una distribución gaussiana para simular el patrón de probabilidad
        x = np.linspace(-self.ancho_pantalla/2, self.ancho_pantalla/2, 200)
        
        # Simular el patrón de interferencia
        patron = np.sin(x / self.distancia_rendijas)**2
        patron = patron / np.max(patron)  # Normalizar
        
        # Generar distribución de impactos
        distribucion = patron * self.num_particulas
        
        return x, distribucion
    
    def visualizar_resultados(self):
        x, distribucion = self.simular_experimento()
        
        plt.figure(figsize=(10, 6))
        plt.title('Experimento de la Doble Rendija')
        plt.xlabel('Posición en la Pantalla')
        plt.ylabel('Número de Impactos')
        plt.plot(x, distribucion, 'b-', label='Patrón de Interferencia')
        plt.fill_between(x, distribucion, alpha=0.3)
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()

if __name__ == "__main__":
    experimento = ExperimentoDobleSRendijas(num_particulas=50000)
    experimento.visualizar_resultados()
    
    
    