from cProfile import label
from msilib.schema import ComboBox
import tkinter as tk
from tkinter import N, ttk
import datetime as dt


list_types = ["galao", "caixa", "saco", "unidade"]
list_codes = []



def insert_code():
    description = entry_description.get()
    type = ComboBox_select_type.get()
    amount = entry_amount.get()
    cost_price = entry_cost_price.get()
    sale_price = entry_sale_price.get()
    create_date = dt.datetime.now()
    create_date = create_date.strftime("%d/%m/%Y %H:%M")
    code = len(list_codes)+1
    code_str = "COD-{}".format(code)
    list_codes.append((code_str, description, type, amount,cost_price,sale_price, create_date))


window = tk.Tk()

window.title('ferramenta de cadastro de materiais')


label_description = tk.Label(text="Descriçao do produto")
label_description.grid(row=1, column=0, padx=10, pady=10,
                       sticky='nswe', columnspan=2)

entry_description = tk.Entry()
entry_description.grid(row=1, column=2, padx=10, pady=10,
                       sticky='nswe', columnspan=2)

label_type_unit = tk.Label(text="Tipo da unidade do material")
label_type_unit.grid(row=3, column=0, padx=10, pady=10,
                     sticky='nswe', columnspan=2)

ComboBox_select_type = ttk.Combobox(values=list_types)
ComboBox_select_type.grid(row=3, column=2, padx=10, pady=10,
                          sticky='nswe', columnspan=2)

label_amount = tk.Label(text="Quantidade na unidade de material")
label_amount.grid(row=4, column=0, padx=10, pady=10,
                  sticky='nswe', columnspan=2)

entry_amount = tk.Entry()
entry_amount.grid(row=4, column=2, padx=10, pady=10,
                  sticky='nswe', columnspan=2)


label_cost_price = tk.Label(text="Preço de compra")
label_cost_price.grid(row=5, column=0, padx=10, pady=10,
                  sticky='nswe', columnspan=2)

entry_cost_price = tk.Entry()
entry_cost_price.grid(row=5, column=2, padx=10, pady=10,
                  sticky='nswe', columnspan=2)

label_sale_price = tk.Label(text="Preço de venda")
label_sale_price.grid(row=6, column=0, padx=10, pady=10,
                  sticky='nswe', columnspan=2)

entry_sale_price = tk.Entry()
entry_sale_price.grid(row=6, column=2, padx=10, pady=10,
                  sticky='nswe', columnspan=2)



button_create_code = tk.Button(text="Criar codigo", command=insert_code)
button_create_code.grid(row=7, column=0, padx=10,
                        pady=10, sticky='nswe', columnspan=4)


window.mainloop()

print(list_codes)
