from tkinter import *




app = Tk()
app.title("Conversor de unidades dB")


# dimençẽs da janela e variaves globais ou locais
# largura = 800
# altura  = 600
texto = StringVar()
texto1 = StringVar()
texto2 = StringVar()
texto3 = StringVar()
texto4 = StringVar()

# Resolucao do sistema
# largura_janela = app.winfo_screenmmwidth()
# altura_janela = app.winfo_screenmmheight()

# # posicao da janela
# posX = largura_janela / 2 - largura_janela / 2
# posY = altura_janela / 2 - altura_janela / 2

# definir a geometria
# app.geometry("%dx%d+%d+%d" % (largura, altura, posX, posY ))

# entradas
entr1 = Entry(app)

# para para testar o codigos
texto.set("Conversor de unidades dB")
label_1 = Label(app, textvariable=texto, bg="#FFFFFF", fg="#000000", font="Arial 18 bold").grid(row=0,columnspan=3, sticky="WE")
# label_1.pack()

texto1.set("Valor Inicial")
labelInitvalue = Label(app, textvariable=texto1, font="Arial 13", bg="#FFFFFF").grid(row=1, columnspan=1, sticky="WE")
entr1.grid(row=1, column=1)
texto2.set("Calculo Final => ")
label_Initvalue = Label(app, textvariable=texto2, font="Arial 13", bg="#FFFFFF").grid(row=2, columnspan=1, sticky="WE")
texto3.set("converter %s para %s" % ("dBm", "dBu"))
label_Initvalue = Label(app, textvariable=texto3, font="Arial 13", fg="red").grid(row=2, column=1)

texto4.set('''
Valor %s
convertido para: 
%s
''')

label_Initvalue = Label(app, textvariable=texto4, font="Arial 13", bg="#FFF").grid(row=3, columnspan=2, sticky="WE")
# label_Initvalue.pack()

# btn = Button(app, text="Calcular")
# btn.pack()

app.mainloop()