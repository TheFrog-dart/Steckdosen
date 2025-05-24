import tkinter as tk
from tkinter import ttk

import serial
import configparser as cp
import tkinter.colorchooser as cc


class Steckdosen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Steckdosen")
        self.resizable(False, False)
        
        def taste_gedrueckt(event):
            taste_num = event.char
            if taste_num == '1':
                self.Schalten(1)
            if taste_num == '2':
                self.Schalten(2)
            if taste_num == '3':
                self.Schalten(3)
            if taste_num == '4':
                self.Schalten(4)
            if taste_num == '5':
                self.Schalten(5)
            if taste_num == '6':
                self.Schalten(6)
            if taste_num == '7':
                self.Schalten(7)
            if taste_num == '8':
                self.Schalten(8)
            if taste_num == '+':
                self.Schalten(9)
            if taste_num == '-':
                self.Schalten(10)


        self.bind('<KeyPress>', taste_gedrueckt)

# --- Konfigurationen
        self.configp = cp.ConfigParser()
        self.configp.read('stconfig.ini')
        self.buttonText = self.configp['ButtonText']
        self.Farben = self.configp['Farben']

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure("button1.TButton", foreground="white", background='#bb0000',)
        style.map("button1.TButton", background=[('active', '#ff0000')])
        style.configure("button2.TButton", foreground="black", background='green3')
        style.map("button2.TButton", background=[('active', 'green1')])
        self.configure(background='#3D3D3E')

# --- Aufruf der Funktionen
        self.Buttons_erstellen()
        self.FarbenEinlesen()
        self.TextEinlesen()

# --- Steckdosen Buttons erstellen
    def Buttons_erstellen(self):
        self.frame1 = tk.Frame(self)
        self.btn_st1 = tk.Button(self.frame1, command=lambda: self.Schalten(1),width=10)
        self.btn_st1.grid(row=0, column=0, padx=5, pady=5)
        self.btn_st2 = tk.Button(self.frame1, command=lambda: self.Schalten(2),width=10)
        self.btn_st2.grid(row=0, column=1, padx=5)
        self.btn_st3 = tk.Button(self.frame1, command=lambda: self.Schalten(3),width=10)
        self.btn_st3.grid(row=0, column=2, padx=5)
        self.btn_st4 = tk.Button(self.frame1, command=lambda: self.Schalten(4),width=10)
        self.btn_st4.grid(row=0, column=3, padx=5)
        self.btn_st5 = tk.Button(self.frame1, command=lambda: self.Schalten(5),width=10)
        self.btn_st5.grid(row=1, column=0, pady=5)
        self.btn_st6 = tk.Button(self.frame1, command=lambda: self.Schalten(6),width=10)
        self.btn_st6.grid(row=1, column=1)
        self.btn_st7 = tk.Button(self.frame1, command=lambda: self.Schalten(7),width=10)
        self.btn_st7.grid(row=1, column=2)
        self.btn_st8 = tk.Button(self.frame1, command=lambda: self.Schalten(8),width=10)
        self.btn_st8.grid(row=1, column=3)
        self.btn_stan = tk.Button(self.frame1, text="Alle an", command=lambda: self.Schalten(9),width=10)
        self.btn_stan.grid(row=2, column=0, pady=5)
        self.btn_staus = tk.Button(self.frame1, text="Alle aus", command=lambda: self.Schalten(10),width=10)
        self.btn_staus.grid(row=2, column=3)
        self.btn_selbst = tk.Button(self.frame1, text="Einstellungen", command=lambda: neuesFenster(),width=10)
        self.btn_selbst.grid(row=2, column=1, columnspan=2)
        #self.btn_check = tk.Button(self.frame1, command=lambda: self.update_buttons(self))
        #self.btn_check.grid(row=2,column=2)
        self.frame1.pack()

# --- Farben der Steckdosen Buttons einlesen
    def FarbenEinlesen(self):
        for i in range(1,9):
            try:
                bu = f"self.btn_st{i}.configure(background='" + str(self.Farben[f'st{i} bg']) + "')"
                exec(bu)
                bu = f"self.btn_st{i}.configure(foreground='" + str(self.Farben[f'st{i} fg']) + "')"
                exec(bu)
            except:
                pass

# --- Text der Steckdosen Buttons einlesen
    def TextEinlesen(self):
        self.configp.read('stconfig.ini')
        for i in range(1,9):
            try:
                bu = f"self.btn_st{i}.configure(text='" + str(self.configp['ButtonText'][f'steckdose{i}']) + "')"
                exec(bu)
            except:
                pass

# --- Steckdosen schalten
    def Schalten(self, Zahl):
        ser = serial.Serial('/dev/ttyUSB0', 2400)
        m_string = chr(13) + chr(1) + "T" + str(int(Zahl)) + chr(110 - int(Zahl))
        #print(m_string)
        if (Zahl == 9):
            m_string = "b'\r\x01S9f"
        if (Zahl == 10):
            m_string = "b'\r\x01C9v"
        mstring = m_string.encode("utf-8")
        #print(mstring)
        mstring = mstring + mstring
        mstring = mstring + mstring
        ser.write(mstring)
        ser.close
    

# --- Buttons aktualieren
    def update_buttons(self):
        self.configp.read('stconfig.ini')
        self.Farben = self.configp['Farben']
        for i in range(1,9):
            if f'st{i} bg' in self.Farben:
                setbg = str(self.configp['Farben'][f'st{i} bg'])
                setf =f"self.btn_st{i}.configure(background=\'{setbg}')"
                exec(setf)
            if f'st{i} fg' in self.Farben:
                setfg = str(self.configp['Farben'][f'st{i} fg'])
                setf =f"self.btn_st{i}.configure(foreground=\'{setfg}')"
                exec(setf)

class neuesFenster(tk.Toplevel):
    def __init__(self):
        #E = tk.Toplevel(app)
        super().__init__(app)
        self.title("Eistellungen")
        self.resizable(False, False)
        self.geometry("294x336+1518+644")
        
# --- Konfigurationen
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure("bg.TNotebook", background='#3b3b3e', foreground='white')
        
        self.configp = cp.ConfigParser()
        self.configp.read('stconfig.ini')
        self.buttonText1 = self.configp['ButtonText']
        self.Farben_conf = self.configp['Farben']

# --- beginn Komponeten Erstellung --------------
        self.nb = ttk.Notebook(self, style='bg.TNotebook')
        self.frame11 = ttk.Frame(self.nb,padding=5,style='bg.TNotebook')
        
    # --- Text Einstellungen Komponeten erstellen
        for i in range(1,9):
            st=f"""self.Text1{i} = tk.StringVar(value='Steckdose {i}')
if (self.configp['ButtonText']['Steckdose{i}']):
    self.Text1{i}.set(value=self.buttonText1["Steckdose{i}"])
self.Label{i} = tk.Label(self.frame11, text='Steckdose {i}',padx=5,pady=5,background='#3b3b3e', foreground='white')
self.Label{i}.grid(row={i-1}, column=0)
self.Input{i} = ttk.Entry(self.frame11, textvariable=self.Text1{i})
self.Input{i}.grid(row={i-1}, column=1,padx=5)"""
            #print(st)
            exec(st)
    
        self.Save = ttk.Button(self.frame11, text="Speichern", command=lambda: Speichern())
        self.Save.grid(row=8,column=0,pady=5, columnspan=2)
        #self.Ceck1 = tk.Button(self.frame11, command=lambda: print(self.nb.winfo_height()))
        #self.Ceck1.grid(row=8, column=1,pady=5)

        self.nb.add(self.frame11, text="Text")
        self.frame12 = ttk.Frame(self.nb, width=294, height=336)
        self.frame12.config(padding=(40,20,20,20))

    # --- Farben Einstellungen Komponenten erstellen
        for i in range(1,9):
            fa = f"""self.L{i} = ttk.Label(self.frame12, text='Steckdose {i}').grid(column=0,row={i-1}, padx=5)
self.bg{i} = tk.Button(self.frame12, text='bg', name='bg{i}')
self.bg{i}.bind('<Button-1>', self.Farben)
self.bg{i}.grid(column=1,row={i-1},padx=5)
self.frame1g{i} = tk.Button(self.frame12, text='fg', name='fg{i}')
self.frame1g{i}.bind('<Button-1>', self.Farben)
self.frame1g{i}.grid(column=2,row={i-1},padx=5)\n"""
            exec(fa)

        self.nb.add(self.frame12, text="Farben")
        self.nb.pack()
# --- Ende Komponenten Erstellung ---------------

# --- Text Einstellungen speichern
    def Speichern():
        self.configp['ButtonText'] = {}
        ButtonText1 = self.configp['ButtonText']
        ButtonText1['Steckdose1'] = self.Text11.get()
        ButtonText1['Steckdose2'] = self.Text12.get()
        ButtonText1['Steckdose3'] = self.Text13.get()
        ButtonText1['Steckdose4'] = self.Text14.get()
        ButtonText1['Steckdose5'] = self.Text15.get()
        ButtonText1['Steckdose6'] = self.Text16.get()
        ButtonText1['Steckdose7'] = self.Text17.get()
        ButtonText1['Steckdose8'] = self.Text18.get()
        with open('stconfig.ini', 'w') as configfile:
            self.configp.write(configfile)
        app.TextEinlesen()

# --- Farben Einstellungen speichern
    def Farben(self, b):
        but = str(b.widget).split('.')[-1]
        print(b.widget)
        print(but)
        color = cc.askcolor(parent=self)
        print(color)
        if (color[1] != None):
            if (but[0]=='b'):
                self.Farben_conf[f'St{but[2]} bg'] = f'{color[1]}'
                with open('stconfig.ini', 'w') as configfile:
                    self.configp.write(configfile)
                
            else:
                self.Farben_conf[f'St{but[2]} fg'] = f'{color[1]}'
                with open('stconfig.ini', 'w') as configfile:
                    self.configp.write(configfile)
            app.update_buttons()


            
if __name__ == "__main__":
    app = Steckdosen()
    app.mainloop()
