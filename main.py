import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox


def on_click(event):
    search_entry.configure(state=NORMAL)
    boton.configure(state=NORMAL)
    search_entry.delete(0, END)


def search(entry):
    search_entry.delete(0, "end")
    if len(entry) == 0:
        messagebox.showwarning("Advertencia", "Existen campos nulos.")
    elif len(entry) >= 1:
        root.geometry("500x350")
        show_info = Label(text="INFORMACION ENCONTRADA:", font=("Bahnschrift 15 italic bold"), bg=bg_global, fg="#AED6F1")
        show_info.grid(row=5, column=0, pady=10)

        # Etiqueta capital o nombre pais (viceversa)

        # Etiqueta poblacion cantidad
        poblation_label = Label(text="Poblacion total: ", font=("Bahnschrift 13 italic bold"), bg=bg_global, fg="#ABEBC6")
        poblation_label.grid(row=6)
        # Etiqueta continente
        continente_label = Label(text="Continente: ", font=("Bahnschrift 13 italic bold"), bg=bg_global, fg="#ABEBC6")
        continente_label.grid(row=7)

        # Etiqueta codigo de moneda
        moneda_label = Label(text="Codigo de monenda: ", font=("Bahnschrift 13 italic bold"), bg=bg_global, fg="#ABEBC6")
        moneda_label.grid(row=8)

        # Etiqueta codigo de pais
        moneda_label = Label(text="Codigo de pais: ", font=("Bahnschrift 13 italic bold"), bg=bg_global,
                             fg="#ABEBC6")
        moneda_label.grid(row=9)


if __name__ == "__main__":
    bg_global = "#34495E"
    root = Tk()
    root.geometry("500x300")
    root.config(bg=bg_global)
    root.eval('tk::PlaceWindow . center')

    # Etiqueta buscador informacion de paises.
    search_text = Label(root, text='INFORMACION DE PAISES', font=("Bahnschrift 20 italic bold"), bg=bg_global,
                        fg="#AED6F1")
    search_text.grid(row=0, column=0, pady=10, padx=80)

    # Entrada de buscador

    search_entry = Entry(root, bd=3, font=("Bahnschrift"), relief=SOLID, borderwidth=4, justify=CENTER, fg="#5D6D7E")
    search_entry.grid(row=3, column=0, pady=10, padx=10, ipadx=20, ipady=4)
    search_entry.insert(0, "Ingresa el pais o capital")
    search_entry.configure(state=DISABLED)
    search_entry.bind("<Button-1>", on_click)

    # Boton de busqueda

    boton = Button(root, text="Buscar", command=lambda: search(search_entry.get()), font=("Bahnschrift"),
                   state=DISABLED)
    boton.grid(row=4, column=0, pady=10)

    root.mainloop()
