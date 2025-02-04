import customtkinter as ctk
from plotador_malha import Malha
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.geometry("700x500")
root.resizable(False, False)
root.title("Calculadora de CG e momento de inércia")

frame_malha = ctk.CTkFrame(root)
frame_malha.pack(padx=10, pady=10, side="left")

malha = Malha()

fig = malha.plotar()

fig.set_size_inches(5.5, 5.5)  # Ajuste o tamanho para o que você preferir

canvas = FigureCanvasTkAgg(fig, master=frame_malha)
canvas.draw()
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# Posicionamento dos botões

frame = ctk.CTkFrame(root)
frame.pack(padx=20, pady=20, side="right")

add_figura = ctk.CTkButton(frame, text="Adicionar figura")
rmv_figura = ctk.CTkButton(frame, text="Remover figura")
calc_figura = ctk.CTkButton(frame, text="Calcular figura")

add_figura.pack(pady=10)
rmv_figura.pack(pady=10)
calc_figura.pack(pady=10)


def on_closing():
    canvas.get_tk_widget().destroy()  # Destrói o widget do canvas
    plt.close(fig)  # Fecha a figura do Matplotlib
    root.destroy()   # Fecha a aplicação Tkinter

root.protocol("WM_DELETE_WINDOW", on_closing)

if __name__ == "__main__":
    root.mainloop()
