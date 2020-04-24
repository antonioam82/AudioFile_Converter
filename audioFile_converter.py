#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter
import threading
from tkinter import messagebox, filedialog
import os
from pydub import AudioSegment

def abrir_archivo(ex):
    global audio
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
    else:
        messagebox.showwarning("ERROR","FORMATO NO SOPORTADO")

def dire():
    currentDir.set(os.getcwd())

def busca_archivo():
    global nom, ex, ruta, file
    etiName.configure(text="IMPORTANDO ARCHIVO...")
    if executing == False:
        estat.configure(text="")
        #file = ""
        ruta = filedialog.askopenfilename(initialdir="/",title="SELECCIONAR ARCHIVO",filetypes =(("mp3 files","*.mp3")
                                          ,("wav files","*.wav"),("mp4 files","*.mp4"),("flv files","*.flv")
                                          ,("ogg files","*.ogg"),("mp2 files","*.mp2"),("aac files","*.aiff")
                                          ,("au files","*.au"),("all files","*.*")))
        if ruta != "":
            file = ruta.split("/")[-1]
            nom,ex = os.path.splitext(file)
            etiName.configure(text=("ARCHIVO SELECCIONADO: "+file))
            abrir_archivo(ex)
        else: ###################################################################################################
            if file == "":
                etiName.configure(text="NINGÚN ARCHIVO SELECCIONADO")
            else:
                etiName.configure(text=("ARCHIVO SELECCIONADO: "+file))

def cambia_dir():
    if executing == False:
        directorio=filedialog.askdirectory()
        if directorio!="":
            os.chdir(directorio)
            currentDir.set(os.getcwd())
    
def convert():
    global executing
    if audio != "":
        executing = True
        try:
            estat.configure(text="PROCESO EN CURSO...")
            name = nom+"."+ty
            audio.export((name),format=ty)
            estat.configure(text="PROCESO FINALIZADO\nARCHIVO CREADO: "+name)
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
root.geometry("700x550")
audio = ""
currentDir=StringVar()
ty = ""
file = ""
executing = False
formatos=[".mp3",".wav",".ogg",".flv",".mp2",".mp4",".aiff",".au"]

#ELEMENTOS
entryDir = Entry(root,textvariable=currentDir,width=116)
entryDir.place(x=0,y=0)
etiName = Label(root,text='NINGÚN ARCHIVO SELECCIONADO',bg="black",
                fg="red",width=91,height=2)
etiName.place(x=26,y=90)

btnBusca = Button(root,text='BUSCAR ARCHIVO',activebackground='firebrick1',activeforeground='blue',bg='blue',fg='firebrick1',command=busca_archivo)#
btnBusca.place(x=294,y=158)

estat = Label(root,width=91,bg="gray40",fg="white")
estat.place(x=26,y=190)

Button(root,text="CARPETA DESTINO",activebackground='white',activeforeground='green',fg='white',bg ='green',command=cambia_dir).place(x=292,y=490)
Button(root,text='EXPORTAR A FORMATO .WAV',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("wav")).place(x=26,y=240)
Button(root,text='EXPORTAR A FORMATO .MP3',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("mp3")).place(x=26,y=290)
Button(root,text='EXPORTAR A FORMATO .FLV',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("flv")).place(x=26,y=340)
Button(root,text='EXPORTAR A FORMATO .OGG',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("ogg")).place(x=380,y=240)
Button(root,text='EXPORTAR A FORMATO .MP2',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("mp2")).place(x=380,y=290)
Button(root,text='EXPORTAR A FORMATO .MP4',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("mp4")).place(x=380,y=340)
Button(root,text='EXPORTAR A FORMATO .AAC',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("aiff")).place(x=26,y=390)
Button(root,text='EXPORTAR A FORMATO    .AU',activeforeground='red',bg='red',fg='white',width=40,command=lambda:inicia("au")).place(x=380,y=390)

dire()

root.mainloop()

