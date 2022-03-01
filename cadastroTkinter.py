from cProfile import label
from msilib.schema import ComboBox
import tkinter as tk
from tkinter import ttk
import datetime as dt

list_types = ["galao", "caixa", "saco", "unidade"]

window = tk.Tk()

window.title('ferramenta de cadastro de materiais')

label_description = tk.Label(text="Descriçao do material")
label_description.grid(row=1, column=0, padx=10, pady=10,
                       sticky='nswe', columnspan=4)

entry_description = tk.Entry()
entry_description.grid(row=2, column=0, padx=10, pady=10,
                       sticky='nswe', columnspan=4)

label_type_unit = tk.Label(text="Tipo da unidade do material")
label_type_unit.grid(row=3, column=0, padx=10, pady=10,
                     sticky='nswe', columnspan=2)

ComboBox_select_type = ttk.Combobox(values=list_types)
ComboBox_select_type.grid(row=3, column=2, padx=10, pady=10,
                          sticky='nswe', columnspan=2)

label_amount = tk.Label(text="Quantidade na unidade de material")
label_amount.grid(row=4, column=0, padx=10, pady=10,
                  sticky='nswe', columnspan=2)

label_amount = tk.Entry()
label_amount.grid(row=4, column=2, padx=10, pady=10,
                  sticky='nswe', columnspan=2)

button_create_code = tk.Button(text="Criar codigo")
button_create_code.grid(row=5, column=0, padx=10,
                        pady=10, sticky='nswe', columnspan=4)


window.mainloop()
