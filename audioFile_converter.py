from tkinter import *
import tkinter
import pydub

root = tkinter.Tk()
root.title("AUDIO FILE CONVERTER")
root.configure(background="gray40")
root.geometry("700x500")

etiName = Label(root,text='NINGÚN ARCHIVO SELECCIONADO',bg="black",
                fg="red",width=91,height=2)
etiName.place(x=26,y=80)

btnBusca = Button(root,text='BUSCAR ARCHIVO',bg='blue',fg='firebrick1')
btnBusca.place(x=291,y=150)

btnWav = Button(root,text='CONVERTIR A .WAV',bg='red',fg='white',width=40)
btnWav.place(x=26,y=230)



root.mainloop()

