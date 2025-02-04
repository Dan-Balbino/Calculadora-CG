import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as patches

class Malha():
    
    def __init__(self, ):
        self.lado = 10
        pass
    
    def plotar(self):
        # Criar a figura do Matplotlib com margens ajustadas
        fig, ax = plt.subplots(figsize=(3, 3))
        plt.subplots_adjust(left=0.005, right=1, top=1, bottom=0.005)

        # Desenhar a grade
        for x in range(self.lado + 1):
            ax.axvline(x, color='gray', linestyle='-', linewidth=0.5)
        for y in range(self.lado + 1):
            ax.axhline(y, color='gray', linestyle='-', linewidth=0.5)

        # Destacar as linhas que passam pelo ponto (0,0)
        ax.axvline(0, color='black', linewidth=5)
        ax.axhline(0, color='black', linewidth=5)
        
        # Configurar o gráfico
        ax.set_xlim(0, self.lado)
        ax.set_ylim(0, self.lado)
        ax.set_aspect('equal', adjustable='box')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.margins(0)
        ax.grid(False)
        
        return fig
    
