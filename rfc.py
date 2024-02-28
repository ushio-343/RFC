import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog, messagebox
import re

# Solicitar RFC
root = tk.Tk()
root.withdraw()
not_break_loop = True


def case_1():
    while True:
        rfc = simpledialog.askstring("RFC Ordenado", 'Ingrese su RFC ordenado')
        if rfc is None:  # El usuario cerró el diálogo
            break
        if len(rfc) != 4:
            messagebox.showerror("CADENA INVALIDA", "La cadena debe tener exactamente 4 caracteres")
            continue
        if re.fullmatch(pattern="^[rR][oO][mM][rR]", string=rfc):
            graph = nx.Graph()
            nodos = [0, 1, 2, 3, 4]
            labels = {0: 'q0', 1: 'q1', 2: 'q2', 3: 'q3', 4: "q4"}
            symbols = {(0, 1): rfc[0], (1, 2): rfc[1], (2, 3): rfc[2], (3, 4): rfc[3]}
            initial_state = 0
            final_state = 4
            graph.add_nodes_from(nodos)
            graph.add_edges_from(symbols.keys())
            nx.set_node_attributes(graph, labels, 'label')
            nx.set_edge_attributes(graph, symbols, 'symbol')
            pos = {0: (1, 0), 1: (2, 0), 2: (3, 0), 3: (4, 0), 4: (5, 0)}
            nx.draw(graph, pos, node_color='lightgreen', node_size=800)
            nx.draw_networkx_labels(graph, pos, labels=labels, font_color='blue')
            nx.draw_networkx_edge_labels(graph, pos, edge_labels=symbols, font_color='red')
            nx.draw_networkx_nodes(graph, pos, nodelist=[final_state], edgecolors='black', node_color='lightgreen')
            offset_x = 0.59
            offset_y = 0.1
            arrow_length = 0.3
            plt.arrow(pos[initial_state][0] - offset_x, pos[initial_state][1], arrow_length, 0, head_width=offset_y,
                      head_length=0.1, fc='k', ec='k')
            plt.axis('equal')
            plt.xlim(0, 6)
            plt.title("Diagrama de Transición de Estados para RFC Ordenado")
            plt.xlabel("Estados")
            plt.ylabel("Transiciones")
            plt.show()
            break
        else:
            messagebox.showerror("CADENA INVALIDA", "Los caracteres no son los esperados")


def case_2():
    while True:
        rfc = simpledialog.askstring("RFC Desordenado", 'Ingrese su RFC desordenado')
        if rfc is None:  # El usuario cerró el diálogo
            break
        if len(rfc) != 4:
            messagebox.showerror("CADENA INVALIDA", "La cadena debe tener exactamente 4 caracteres")
            continue
        if re.fullmatch(pattern="^[rRoOmM][oOmMrR][mMrRoO][oOrRmM]", string=rfc):
            graph = nx.Graph()
            nodos = [0, 1, 2, 3, 4]
            labels = {0: 'q0', 1: 'q1', 2: 'q2', 3: 'q3', 4: "q4"}
            symbols = {(0, 1): rfc[0], (1, 2): rfc[1], (2, 3): rfc[2], (3, 4): rfc[3]}
            initial_state = 0
            final_state = 4
            graph.add_nodes_from(nodos)
            graph.add_edges_from(symbols.keys())
            nx.set_node_attributes(graph, labels, 'label')
            nx.set_edge_attributes(graph, symbols, 'symbol')
            pos = {0: (1, 0), 1: (2, 0), 2: (3, 0), 3: (4, 0), 4: (5, 0)}
            nx.draw(graph, pos, node_color='lightgreen', node_size=800)
            nx.draw_networkx_labels(graph, pos, labels=labels, font_color='blue')
            nx.draw_networkx_edge_labels(graph, pos, edge_labels=symbols, font_color='red')
            nx.draw_networkx_nodes(graph, pos, nodelist=[final_state], edgecolors='black', node_color='lightgreen')
            offset_x = 0.59
            offset_y = 0.1
            arrow_length = 0.3
            plt.arrow(pos[initial_state][0] - offset_x, pos[initial_state][1], arrow_length, 0, head_width=offset_y,
                      head_length=0.1, fc='k', ec='k')
            plt.axis('equal')
            plt.xlim(0, 6)
            plt.title("Diagrama de Transición de Estados para RFC Desordenado")
            plt.xlabel("Estados")
            plt.ylabel("Transiciones")
            plt.show()
            break
        else:
            messagebox.showerror("CADENA INVALIDA", "Los caracteres no son los esperados")


def default_case():
    messagebox.showwarning('OPCION INVALIDA', 'Ingrese una opcion correcta')


switch_dict = {
    '1': case_1,
    '2': case_2
}

while not_break_loop:
    option = simpledialog.askstring("Seleccionar Opción", 'Seleccione una opción:\n1) RFC Ordenado\n2) RFC Desordenado')
    if option is None:  # El usuario cerró el diálogo
        break
    else:
        switch_dict.get(option, default_case)()

