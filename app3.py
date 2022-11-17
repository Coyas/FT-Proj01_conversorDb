import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import Menu
from tkinter import Label
from tkinter import Button
from tkinter import Entry

########################################################""
# GUI PARA CONVERTER UNIDADES (dB, dBm, dBU, W, mW, etc)
#:. Ailton Duarte <coyas>
########################################################""

##  Variaveis Globais #####################
# unidades = ['dBm','dBu','dBr','Wat','mWt']
#########:.VG.:############################

# Funcoes
def getUni(*arg) -> None:
    Label(app, text= "The value at index " + str(uniConversaoList.current()) + " is " + " "+ str(unidadeConversao.get()), font= ('Helvetica 12')).pack()

def converterValor(valor) -> str:
    # print("calculado...")

    valor = unidadeConversao.get()

    # calcular o valor final
    # valorFinal = valor + "FInal"

    label_Final = Label(app, text="Converte %s para %s" % (valorEntrada.get(), valor))
    label_Final.pack()
    # pass


# GUI
app = tk.Tk()


# Meno do app
menu = Menu(app)

new_item = Menu(menu)

new_item.add_command(label='Contact us')
new_item.add_command(label='About kraki v0.01')

menu.add_cascade(label='File')
menu.add_cascade(label='Config')
menu.add_cascade(label='About', menu=new_item)

app.config(menu=menu)
## fim do meno do app

# config da janela app
app.geometry('405x600')
app.resizable(False, False)
app.title('Kraki - Conversor de Unidades')

# label
label = ttk.Label(text="CONVERSOR DE UNIDADES", font="Arial 20 bold")
label.pack(fill=tk.X, padx=20, pady=20)

label = ttk.Label(text="Entre com valor:.")
label.pack(fill=tk.X, padx=10, pady=10)

valorEntrada = Entry(app)
valorEntrada.pack(padx=10, pady=10)

# cria combobox de selecao
unidadeConversao = tk.StringVar()
uniConversaoList = ttk.Combobox(app, textvariable=unidadeConversao)
# get first 3 letters of every month name
uniConversaoList['values'] = ['dBm','dBu','dBr','Wat','mWt']

# prevent typing a value
uniConversaoList['state'] = 'readonly'

# place the widget
uniConversaoList.pack(padx=5, pady=5)

# apresenta "status" antes de proceguir
label = ttk.Label(text="Valor convertido:")
label.pack(fill=tk.X, padx=5, pady=5)

btn = Button(app, text="Converter", command=converterValor)
btn.pack()


# bind the selected value changes
def uni_changed(event):
    """ handle the uni changed event """
    showinfo(
        title='Resultado',
        message=f'Selecionou: {unidadeConversao.get()}!'
    )

uniConversaoList.bind('<<ComboboxSelected>>', uni_changed)


app.mainloop()