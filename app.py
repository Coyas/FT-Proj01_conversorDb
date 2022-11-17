from tkinter import *

# funcoes
def converterValor() -> None:
    
    valor = textbox.get()

    # calcular o valor final
    valorFinal = valor + "FInal"

    label_Final = Label(app, text="Converte %s para %s = %s" % (valor, "Dbu", valorFinal))
    label_Final.grid(row=4, column=1)
    # btn['state'] = DESABLED

# def inserirTexto():
#     vartexto.set(textbox.get())

# GUI
app = Tk()
app.title("Conversor de unidades dB")
app.geometry("400x600")

# Criar os Widgets
label_1 = Label(app, text="Entre Com O Valor", pady=10, font="Arial 18 bold")
textbox = Entry(app, width=30)
btn = Button(app, text="Converter", command=converterValor)

# Organizar os widgets
label_1.grid(row=1, column=2)
textbox.grid(row=2, column=2)
btn.grid(row=3, column=2)

app.mainloop()