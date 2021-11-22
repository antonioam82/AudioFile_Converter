#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter
import threading
from tkinter import messagebox, filedialog
import os
from pydub import AudioSegment

def abrir_archivo(ex):
    global audio, nom, audio
    if ex in formatos:
        try:
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
        except:
            messagebox.showwarning("ERROR","NO PUDO COMPLETARSE LA ACCIÓN")
            etiName.configure(text="NINGÚN ARCHIVO SELECCIONADO")
            nom = ""
            audio = ""
    else:
        messagebox.showwarning("ERROR","Formato no soportado")
        etiName.configure(text="NINGÚN ARCHIVO SELECCIONADO")
        audio = ""

def dire():
    currentDir.set(os.getcwd())

def busca_archivo():
    global nom, ex, ruta, file
    etiName.configure(text="IMPORTANDO ARCHIVO...")
    if executing == False:
        estat.configure(text="")
        ruta = filedialog.askopenfilename(initialdir="/",title="SELECCIONAR ARCHIVO",filetypes =(("mp3 files","*.mp3")
                                          ,("wav files","*.wav"),("mp4 files","*.mp4"),("flv files","*.flv")
                                          ,("ogg files","*.ogg"),("mp2 files","*.mp2"),("aac files","*.aiff")
                                          ,("au files","*.au"),("M4A files","*.m4a"),("all files","*")))
        if ruta != "":
            file = ruta.split("/")[-1]
            nom,ex = os.path.splitext(file)
            etiName.configure(text=("ARCHIVO SELECCIONADO: "+file))
            abrir_archivo(ex)
        else: 
            if file == "" or nom == "":
                etiName.configure(text="NINGÚN ARCHIVO SELECCIONADO")
            else:
                etiName.configure(text=("ARCHIVO SELECCIONADO: "+file))
    
def convert():
    global executing, file
    if audio != "":
        executing = True
        try:
            estat.configure(text="PROCESO EN CURSO...")
            file = filedialog.asksaveasfilename(initialdir="/",initialfile=nom,
                   title="SAVE AS",defaultextension="."+ty)
            
            if file != "":
                n_n = file.split("/")[-1]
                audio.export((file),format=ty)
                estat.configure(text="PROCESO FINALIZADO\nARCHIVO CREADO: "+n_n)
        except:
            messagebox.showwarning("ERROR","HUBO UN PROBLEMA AL REALIZAR LA OPERACIÓN")
            estat.configure(text="")
        executing=False
        
def inicia(tip):
    global ty
    if executing == False:
        ty=tip
        t = threading.Thread(target=convert)
        t.start()

root = tkinter.Tk()
root.title("AUDIO FILE CONVERTER")
root.configure(background="gray40")
root.geometry("700x265")
audio = ""
currentDir=StringVar()
currentDir.set(os.getcwd())
ty = ""
file = ""
executing = False

formatos = [".mp3",".mp4",".wav",".ogg",".flv",".aiff",".mp2",".au",".m4a",".flac"]

#ELEMENTOS
entryDir = Entry(root,textvariable=currentDir,width=116)
entryDir.place(x=0,y=0)
etiName = Label(root,text='NINGÚN ARCHIVO SELECCIONADO',bg="black",
                fg="red",width=91,height=2)
etiName.place(x=26,y=30)

btnBusca = Button(root,text='BUSCAR ARCHIVO',activebackground='firebrick1',width=90,activeforeground='blue',bg='blue',fg='firebrick1',command=busca_archivo)#
btnBusca.place(x=27,y=70)

estat = Label(root,width=91,bg="gray40",fg="white")
estat.place(x=26,y=97)

Button(root,text='EXPORTAR A FORMATO .WAV',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("wav")).place(x=26,y=134)
Button(root,text='EXPORTAR A FORMATO .MP3',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("mp3")).place(x=26,y=165)
Button(root,text='EXPORTAR A FORMATO .FLV',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("flv")).place(x=26,y=196)
Button(root,text='EXPORTAR A FORMATO .OGG',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("ogg")).place(x=380,y=134)
Button(root,text='EXPORTAR A FORMATO .MP2',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("mp2")).place(x=380,y=165)
Button(root,text='EXPORTAR A FORMATO .MP4',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("mp4")).place(x=380,y=196)
Button(root,text='EXPORTAR A FORMATO .AAC',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("aiff")).place(x=26,y=227)
Button(root,text='EXPORTAR A FORMATO    .AU',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("au")).place(x=380,y=227)

root.mainloop()
