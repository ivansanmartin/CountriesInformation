import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import json


def on_click(event):
    search_entry.configure(state=NORMAL)
    boton.configure(state=NORMAL)
    search_entry.delete(0, END)


def load_countries():
    with open("countries.json") as f:
        countries = json.load(f)

    return countries


def search(entry):
    #
    search_entry.delete(0, "end")
    # Obtener datos de json.

    if len(entry) == 0:
        messagebox.showwarning("Advertencia", "Existen campos nulos. \n\nIngresa pais o una capital.")
        return

    # Info country
    all_info = []

    # Datos y validaciones json
    countries = load_countries()
    pais = []
    capital = []

    for i in countries:
        pais.append(i["countryName"])
        capital.append(i["capital"])
        if entry == i["countryName"] or entry == i["capital"]:
            all_info.append(i["population"])
            all_info.append(i["continentName"])
            all_info.append(i["currencyCode"])
            all_info.append(i["countryCode"])
            all_info.append(i["capital"])
            all_info.append(i["countryName"])

    if entry not in pais and entry not in capital:
        messagebox.showerror("Error", "El pais o capital ingresado no existe.")

    elif entry in pais or entry in capital:
        print(all_info)
        root.geometry("500x350")
        frame = LabelFrame(root, text="INFORMACION ENCONTRADA", font=("Bahnschrift 15 italic bold"), bg=bg_global,
                           fg="#AED6F1", relief=FLAT)
        frame.grid(row=5, column=0, pady=10)

        # Etiqueta capital o nombre pais (viceversa)
        if entry in capital:
            pais_label = Label(frame, text="Pais: ", font=("Bahnschrift 13 italic bold"), bg=bg_global,
                               fg="#ABEBC6")
            pais_label.grid(row=6, column=0, sticky=W)

            # Etiqueta nombre pais
            pais_nombre = Label(frame, text=all_info[5], font=("Bahnschrift 13 italic bold"), fg="#FEF9E7",
                                bg=bg_global)
            pais_nombre.grid(row=6, column=1)
        elif entry in pais:
            capital_label = Label(frame, text="Capital: ", font=("Bahnschrift 13 italic bold"), bg=bg_global,
                                  fg="#ABEBC6")
            capital_label.grid(row=6, column=0, sticky=W)

            # Etiqueta nombre pais
            capital_nombre = Label(frame, text=all_info[4], font=("Bahnschrift 13 italic bold"), fg="#FEF9E7",
                                   bg=bg_global)
            capital_nombre.grid(row=6, column=1)

        # Etiqueta poblacion cantidad
        population_label = Label(frame, text="Poblacion total: ", font=("Bahnschrift 13 italic bold"), bg=bg_global,
                                 fg="#ABEBC6")
        population_label.grid(row=7, column=0, sticky=W)

        # POBLACION
        total_population = Label(frame, text=all_info[0], font=("Bahnschrift 13 italic bold"), fg="#FEF9E7",
                                 bg=bg_global)
        total_population.grid(row=7, column=1)

        # Etiqueta continente
        continente_label = Label(frame, text="Continente: ", font=("Bahnschrift 13 italic bold"), bg=bg_global,
                                 fg="#ABEBC6")
        continente_label.grid(row=8, column=0, sticky=W)

        # CONTINENTE
        total_population = Label(frame, text=all_info[1], font=("Bahnschrift 13 italic bold"), fg="#FEF9E7",
                                 bg=bg_global)
        total_population.grid(row=8, column=1)

        # Etiqueta codigo de moneda
        moneda_label = Label(frame, text="Codigo de monenda: ", font=("Bahnschrift 13 italic bold"), bg=bg_global,
                             fg="#ABEBC6")
        moneda_label.grid(row=9, column=0, sticky=W)

        # TIPO MONEDA
        total_population = Label(frame, text=all_info[2], font=("Bahnschrift 13 italic bold"), fg="#FEF9E7",
                                 bg=bg_global)
        total_population.grid(row=9, column=1)

        # Etiqueta codigo de pais
        moneda_label = Label(frame, text="Codigo de pais: ", font=("Bahnschrift 13 italic bold"), bg=bg_global,
                             fg="#ABEBC6")
        moneda_label.grid(row=10, column=0, sticky=W)

        # CODIGO DE PAIS
        total_population = Label(frame, text=all_info[3], font=("Bahnschrift 13 italic bold"), fg="#FEF9E7",
                                 bg=bg_global)
        total_population.grid(row=10, column=1)


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
