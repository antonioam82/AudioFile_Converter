from tkinter import *
import tkinter
import threading
from tkinter import messagebox, filedialog
import os
from pydub import AudioSegment

def abrir_archivo(ex):
    global audio
    if ex == ".mp3":
        audio = AudioSegment.from_mp3(ruta)
    elif ex == ".ogg":
        audio = AudioSegment.from_ogg(ruta)
    elif ex == ".wav":
        audio = AudioSegment.from_wav(ruta)
    elif ex == ".flv":
        audio = AudioSegment.from_mp3(ruta)
    else:
        audio = AudioSegment.from_file(ruta)
    print(audio)
    

def busca_archivo():
    global nom, ruta
    file = ""
    ruta = filedialog.askopenfilename(initialdir="/",title="SELECCIONAR ARCHIVO")
    if ruta != "":
        file = ruta.split("/")[-1]
        nom,ex = os.path.splitext(file)
        etiName.configure(text=("ARCHIVO SELECCIONADO: "+file))
        abrir_archivo(ex)

def convert():
    if audio != "":
        audio.export(nom+"."+ty,format=ty)
        print("FIN")

def inicia(tip):
    global ty
    ty=tip
    t = threading.Thread(target=convert)
    t.start()
    
    

root = tkinter.Tk()
root.title("AUDIO FILE CONVERTER")
root.configure(background="gray40")
root.geometry("700x500")
actf = 'red'
audio = ""
ty = ""

etiName = Label(root,text='NINGÚN ARCHIVO SELECCIONADO',bg="black",
                fg="red",width=91,height=2)
etiName.place(x=26,y=80)

btnBusca = Button(root,text='BUSCAR ARCHIVO',activebackground='firebrick1',activeforeground='blue',bg='blue',fg='firebrick1',command=busca_archivo)
btnBusca.place(x=294,y=150)

btnWav = Button(root,text='CONVERTIR A .WAV',activeforeground=actf,bg='red',fg='white',width=40,command=lambda:inicia("wav"))
btnWav.place(x=26,y=230)
btnMp3 = Button(root,text='CONVERTIR A .MP3',activeforeground=actf,bg='red',fg='white',width=40,command=lambda:inicia("mp3"))
btnMp3.place(x=26,y=280)
btnFlv = Button(root,text='CONVERTIR A .FLV',activeforeground=actf,bg='red',fg='white',width=40,command=lambda:inicia("flv"))
btnFlv.place(x=26,y=330)
btnOgg = Button(root,text='CONVERTIR A .OGG',activeforeground=actf,bg='red',fg='white',width=40,command=lambda:inicia("ogg"))
btnOgg.place(x=380,y=230)
btnWma = Button(root,text='CONVERTIR A .WMA',activeforeground=actf,bg='red',fg='white',width=40,command=lambda:inicia("wma"))
btnWma.place(x=380,y=280)
btnMp4 = Button(root,text='CONVERTIR A .MP4',activeforeground=actf,bg='red',fg='white',width=40,command=lambda:inicia("mp4"))
btnMp4.place(x=380,y=330)

root.mainloop()

