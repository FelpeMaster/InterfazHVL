#import serial

'''class App:
    def __init__(self, dev = 'COM5', baudrate = 115200):
        self.device = dev
        self.baudrate = baudrate
        try:
            self.connectToSerialPort()
        except:
            pass

    def connectToSerialPort(self):
        self.sp = serial.Serial(self.device, self.baudrate)

    def initMessage(self):
        self.sp.write("SC")

    def sendMsg(self, message):
        self.write(message)
'''

import tkinter as tk
import random

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.mainCanvas = tk.Canvas(self, width=500, height=420, bg="#f5f5dc")
        self.mainCanvas.pack()
        self.BotonEscanear = tk.Button(self.mainCanvas, text = "Escanear\nDatalogger",command = self.connectToArduino)
        self.BotonEscanear.place(x=300, y=80)
        self.Salir = tk.Button(self.mainCanvas, text="Salir", fg="black", command=root.destroy)
        self.Salir.place(x=245, y=380)
        self.label1 = tk.Label(self.mainCanvas)
        self.label1.place(x=0, y=0)
        self.saveButton = tk.Button(self.mainCanvas, text="Guardar", fg="black", command=self.processSaveData)
        self.saveButton.place(x=300, y=250)
        self.var_for_ext = tk.IntVar()
        self.canvas_rb_ext  = tk.Canvas(self.mainCanvas, width = 100, height = 100, bg="#f5f5dc")
        self.canvas_rb_ext.place(x=300,y=140)
        tk.Label(self.canvas_rb_ext, text = "Formato Salida").place(x=0,y=0)
        tk.Radiobutton(self.canvas_rb_ext, text = "CSV", variable = self.var_for_ext, value = 0).place(x=0,y=25)
        tk.Radiobutton(self.canvas_rb_ext, text = "XLSX", variable = self.var_for_ext, value = 1).place(x=0,y=45)
        tk.Radiobutton(self.canvas_rb_ext, text = "TXT", variable = self.var_for_ext, value = 2).place(x=0,y=65)
        tk.Label(self.mainCanvas, text = "Lista de Archivos").place(x=100, y=80)
        self.listOfFiles = tk.Listbox(self.mainCanvas, selectmode=tk.EXTENDED) #EXTENDED permite seleccionar mas de un fichero
        tk.Label(self.mainCanvas, text = "Fecha de Inicio Medición").place(x = 100, y = 300)
        tk.Label(self.mainCanvas, text = "Fecha de Finalización Medición").place(x = 100, y = 325)
        self.listOfFiles.place(x=100, y=100)

    def connectToArduino(self):
        '''simulacion de archivos'''
        self.listOfFiles.delete(0, tk.END)
        n = 1
        for a in self.simulateFiles():
            self.listOfFiles.insert(n, a)
            n = n + 1

    def processSaveData(self):
        try:
            s = self.listOfFiles.curselection()[0]
            print (s)
            print (">>>", self.listOfFiles.selection_set(s))
        except:
            pass

        if self.var_for_ext.get() == 0:
            print ("CSV")
        elif self.var_for_ext.get() == 1:
            print ("XLSX")
        elif self.var_for_ext.get() == 2:
            print ("TXT")

    def simulateFiles(self):
        ubicacion = random.randint(0,6)
        cantidad = random.randint(1,20)
        archivos_simulados = []
        for i in range(cantidad):
            a = "HLV%d_%d"%(ubicacion,i)
            archivos_simulados.append(a)
        return archivos_simulados









root = tk.Tk()
root.title("Datalogger Reader")
app = Application(master=root)
app.mainloop()
