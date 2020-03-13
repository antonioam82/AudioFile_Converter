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
btnMp3 = Button(root,text='CONVERTIR A .MP3',bg='red',fg='white',width=40)
btnMp3.place(x=26,y=280)
btnFlv = Button(root,text='CONVERTIR A .FLV',bg='red',fg='white',width=40)
btnFlv.place(x=26,y=330)
btnOgg = Button(root,text='CONVERTIR A .OGG',bg='red',fg='white',width=40)
btnOgg.place(x=380,y=230)
btnWma = Button(root,text='CONVERTIR A .WMA',bg='red',fg='white',width=40)
btnWma.place(x=380,y=280)
btnMp4 = Button(root,text='CONVERTIR A .MP4',bg='red',fg='white',width=40)
btnMp4.place(x=380,y=330)


root.mainloop()

