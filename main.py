import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import json


def on_click(event):
    search_entry.configure(state=NORMAL)
    boton.configure(state=NORMAL, bg="#ABEBC6")
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
        messagebox.showwarning("Advertencia", "Existen campos nulos. \n\nIngresa un pais o capital. \n\nEj: Chile")
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
        messagebox.showerror("Error", "El pais o capital ingresado no existe. \n\nEj: Chile, ej2: Santiago \n\nNo olvidar primera letra mayuscula.")

    elif entry in pais or entry in capital:
        print(all_info)
        root.geometry("585x390")
        sucess = Label(root, text=f"INFORMACION DE \"{entry.upper()}\'", font=("Bahnschrift 11 italic bold"), bg="#FCF3CF", fg="#5D6D7E")
        sucess.grid(row=5, column=0, sticky=W+E)
        frame = LabelFrame(root, font=("Bahnschrift 15 italic bold"), bg=bg_global,
                           fg="#AED6F1", relief=FLAT, padx=110)
        frame.grid(row=6, column=0, pady=25, sticky=W+E)

        # Etiqueta capital o nombre pais (viceversa)
        if entry in capital:
            pais_label = Label(frame, text="Pais: ", font=("Bahnschrift 13 italic bold"), bg=bg_global,
                               fg="#ABEBC6")
            pais_label.grid(row=7, column=0, sticky=W)

            # Etiqueta nombre pais
            pais_nombre = Label(frame, text=all_info[5], font=("Bahnschrift 13 italic bold"), fg="#FEF9E7",
                                bg=bg_global)
            pais_nombre.grid(row=7, column=1)
        elif entry in pais:
            capital_label = Label(frame, text="Capital: ", font=("Bahnschrift 13 italic bold"), bg=bg_global,
                                  fg="#ABEBC6")
            capital_label.grid(row=8, column=0, sticky=W)

            # Etiqueta nombre pais
            capital_nombre = Label(frame, text=all_info[4], font=("Bahnschrift 13 italic bold"), fg="#FEF9E7",
                                   bg=bg_global)
            capital_nombre.grid(row=8, column=1)

        # Etiqueta poblacion cantidad
        population_label = Label(frame, text="Poblacion total: ", font=("Bahnschrift 13 italic bold"), bg=bg_global,
                                 fg="#ABEBC6")
        population_label.grid(row=9, column=0, sticky=W)

        # POBLACION
        total_population = Label(frame, text=f"{all_info[0]} +", font=("Bahnschrift 13 italic bold"), fg="#FEF9E7",
                                 bg=bg_global)
        total_population.grid(row=9, column=1)

        # Etiqueta continente
        continente_label = Label(frame, text="Continente: ", font=("Bahnschrift 13 italic bold"), bg=bg_global,
                                 fg="#ABEBC6")
        continente_label.grid(row=10, column=0, sticky=W)

        # CONTINENTE
        get_continente = Label(frame, text=all_info[1], font=("Bahnschrift 13 italic bold"), fg="#FEF9E7",
                                 bg=bg_global)
        get_continente .grid(row=10, column=1)

        # Etiqueta codigo de moneda
        moneda_label = Label(frame, text="Codigo de monenda: ", font=("Bahnschrift 13 italic bold"), bg=bg_global,
                             fg="#ABEBC6")
        moneda_label.grid(row=11, column=0, sticky=W)

        # TIPO MONEDA
        get_moneda = Label(frame, text=all_info[2], font=("Bahnschrift 13 italic bold"), fg="#FEF9E7",
                                 bg=bg_global)
        get_moneda.grid(row=11, column=1)

        # Etiqueta codigo de pais
        cod_label = Label(frame, text="Codigo de pais: ", font=("Bahnschrift 13 italic bold"), bg=bg_global,
                             fg="#ABEBC6")
        cod_label .grid(row=12, column=0, sticky=W)

        # CODIGO DE PAIS
        get_cod = Label(frame, text=all_info[3], font=("Bahnschrift 13 italic bold"), fg="#FEF9E7",
                                 bg=bg_global)
        get_cod.grid(row=12, column=1)


bg_global = "#34495E"

root = Tk()
root.geometry("585x300")
root.config(bg=bg_global)
root.title("COUNTRY INFORMATION")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')

#Frame para busqueda
frame_search = LabelFrame(root, text='INFORMACION DE PAISES', font=("Bahnschrift 20 italic bold"), bg=bg_global,
                    fg="#AED6F1", relief=FLAT)
frame_search.grid(row=0, column=0, pady=10, padx=130)


# Entrada de buscador

search_entry = Entry(frame_search, bd=3, font=("Bahnschrift"), relief=FLAT, borderwidth=4, justify=CENTER, fg="#5D6D7E",
                     highlightthickness=2)
search_entry.grid(row=3, column=0, pady=10, padx=35, ipadx=20, ipady=4)
search_entry.insert(0, "Ingresa el pais o capital")
search_entry.configure(state=DISABLED)
search_entry.config(highlightbackground="#ABEBC6", highlightcolor="#ABEBC6")
search_entry.bind("<Button-1>", on_click)

# Boton de busqueda

boton = Button(frame_search, text="Buscar", command=lambda: search(search_entry.get()), font=("Bahnschrift"),
               state=DISABLED, bg="#FF7272", fg="white", relief=FLAT)
boton.grid(row=4, column=0, pady=10)

root.mainloop()
