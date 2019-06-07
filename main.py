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
from tkinter import ttk
import random
import serial
import serial.tools.list_ports

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.identifyPort()
        #self.arduino = serial.Serial(port = device, baudrate = 115200)

    def identifyPort(self):
        comlist = serial.tools.list_ports.comports()
        devices = []
        for element in comlist:
            devices.append(element.device)
        return devices

    def create_widgets(self):
        # Canvas principal donde estará la aplicación
        self.mainCanvas = tk.Canvas(self, width=500, height=420, bg="#f5f5dc")
        self.mainCanvas.pack()
        # Botón que ejecuta el escaneo de arduino
        self.BotonEscanear = tk.Button(self.mainCanvas, text = "Escanear\nDatalogger",command = self.connectToArduino)
        self.BotonEscanear.place(x=300, y=80)
        # Guarda fichero en formato ya definido
        self.saveButton = tk.Button(self.mainCanvas, text="Guardar", fg="black", command=self.processSaveData)
        self.saveButton.place(x=300, y=250)
        # Guarda la selección de la extensión
        self.var_for_ext = tk.IntVar()
        # Canvas auxiliar que sirve para ubicar los Radiobutton
        self.canvas_rb_ext  = tk.Canvas(self.mainCanvas, width = 100, height = 100, bg="#f5f5dc")
        self.canvas_rb_ext.place(x=300,y=140)
        # Etiqueta que solo muestra el mensaje para seleccionar el formato de salida
        tk.Label(self.canvas_rb_ext, text = "Formato Salida").place(x=0,y=0)
        # Opciones de formato de salida para el archvio que se está analizando
        tk.Radiobutton(self.canvas_rb_ext, text = "CSV", variable = self.var_for_ext, value = 0).place(x=0,y=25)
        tk.Radiobutton(self.canvas_rb_ext, text = "XLSX", variable = self.var_for_ext, value = 1).place(x=0,y=45)
        tk.Radiobutton(self.canvas_rb_ext, text = "TXT", variable = self.var_for_ext, value = 2).place(x=0,y=65)
        # Etiqueta que sirve para indicar la lista de archivos que está en el arduino
        tk.Label(self.mainCanvas, text = "Lista de Archivos").place(x=100, y=80)
        # ListBox muestra Lista de archivos que están disponibles en la SD que se conecta al arduino.
        self.listOfFiles = tk.Listbox(self.mainCanvas, selectmode=tk.EXTENDED) #EXTENDED permite seleccionar mas de un fichero
        tk.Label(self.mainCanvas, text = "Fecha de Inicio Medición").place(x = 100, y = 300)
        tk.Label(self.mainCanvas, text = "Fecha de Finalización Medición").place(x = 100, y = 325)
        self.listOfFiles.place(x=100, y=100)
        # Botón para identificar puerto serial
        self.SerialPortsButton = tk.Button(self.mainCanvas, text="Buscar", fg="black", command=self.findSerialPorts)
        self.SerialPortsButton.place(x=100, y=385)
        tk.Label(self.mainCanvas, text = "Seleccione Puerto Serial").place(x=170,y=360)
        #Selección de puerto Serial
        self.comboSerial = ttk.Combobox(self.mainCanvas)
        self.comboSerial.place(x=170,y=385)
        # Botón para salir
        self.Salir = tk.Button(self.mainCanvas, text="Salir", fg="black", command=root.destroy)
        self.Salir.place(x=390, y=385)

    def findSerialPorts(self):
        #Buscar puertos seriales disponibles en PC
        self.comboSerial["values"] = self.identifyPort()
        pass

    def connectToArduino(self):
        '''simulacion de archivos'''
        self.listOfFiles.delete(0, tk.END)
        n = 1
        files_list = self.simulateFiles()
        for a in files_list:
            self.listOfFiles.insert(n, a)
            n = n + 1

    def processSaveData(self):
        try:
            filesToRead = self.getFilesNames()
            print (filesToRead)
        except:
            pass
        if self.var_for_ext.get() == 0:
            pass
        elif self.var_for_ext.get() == 1:
            pass
        elif self.var_for_ext.get() == 2:
            pass

    def getFilesNames(self):
        if len(self.listOfFiles.curselection())!=0:
            allFiles = []
            for posicion in self.listOfFiles.curselection():
                allFiles.append(self.listOfFiles.get(posicion))
        return allFiles

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
