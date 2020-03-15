from tkinter import *
import tkinter
import threading
from tkinter import messagebox, filedialog
import os
from pydub import AudioSegment

def abrir_archivo(ex):
    global audio
    if ex in formatos:
        if ex == ".mp3":
            audio = AudioSegment.from_mp3(ruta)
        elif ex == ".ogg":
            audio = AudioSegment.from_ogg(ruta)
        elif ex == ".wav":
            audio = AudioSegment.from_wav(ruta)
        elif ex == ".flv":
            audio = AudioSegment.from_flv(ruta)
        else:
            audio = AudioSegment.from_file(ruta)
    else:
        messagebox.showwarning("ERROR","FORMATO NO SOPORTADO")
    print(audio)

def dire():
    currentDir.set(os.getcwd())

def busca_archivo():
    global nom, ex, ruta
    estat.configure(text="")
    file = ""
    ruta = filedialog.askopenfilename(initialdir="/",title="SELECCIONAR ARCHIVO")
    if ruta != "":
        file = ruta.split("/")[-1]
        nom,ex = os.path.splitext(file)
        etiName.configure(text=("ARCHIVO SELECCIONADO: "+file))
        abrir_archivo(ex)

def cambia_dir():
    directorio=filedialog.askdirectory()
    if directorio!="":
        os.chdir(directorio)
        currentDir.set(os.getcwd())
    
def convert():
    if audio != "":
        try:
            estat.configure(text="PROCESO EN CURSO...")
            audio.export(nom+"."+ty,format=ty)
            estat.configure(text="PROCESO FIANLIZADO")
        except:
            messagebox.showwarning("ERROR","HUBO UN PROBLEMA AL REALIZAR LA OPERACIÓN")

def inicia(tip):
    global ty
    ty=tip
    t = threading.Thread(target=convert)
    t.start()

root = tkinter.Tk()
root.title("AUDIO FILE CONVERTER")
root.configure(background="gray40")
root.geometry("700x500")
audio = ""
currentDir=StringVar()
ty = ""
formatos=[".mp3",".wav",".ogg",".flv",".mp2",".mp4"]

#ELEMENTOS
entryDir = Entry(root,textvariable=currentDir,width=116)
entryDir.place(x=0,y=0)
etiName = Label(root,text='NINGÚN ARCHIVO SELECCIONADO',bg="black",
                fg="red",width=91,height=2)
etiName.place(x=26,y=90)

btnBusca = Button(root,text='BUSCAR ARCHIVO',activebackground='firebrick1',activeforeground='blue',bg='blue',fg='firebrick1',command=busca_archivo)
btnBusca.place(x=294,y=160)

estat = Label(root,width=91,bg="gray40",fg="white")
estat.place(x=26,y=200)

btnDir = Button(root,text="GUARDAR EN...",activebackground='white',activeforeground='green',fg='white',bg ='green',command=cambia_dir)
btnDir.place(x=301,y=420)

btnWav = Button(root,text='CONVERTIR A .WAV',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("wav"))
btnWav.place(x=26,y=240)
btnMp3 = Button(root,text='CONVERTIR A .MP3',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("mp3"))
btnMp3.place(x=26,y=290)
btnFlv = Button(root,text='CONVERTIR A .FLV',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("flv"))
btnFlv.place(x=26,y=340)
btnOgg = Button(root,text='CONVERTIR A .OGG',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("ogg"))
btnOgg.place(x=380,y=240)
btnWma = Button(root,text='CONVERTIR A .MP2',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("mp2"))
btnWma.place(x=380,y=290)
btnMp4 = Button(root,text='CONVERTIR A .MP4',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("mp4"))
btnMp4.place(x=380,y=340)

dire()

root.mainloop()
