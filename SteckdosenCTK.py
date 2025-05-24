import os
import customtkinter as ctk
import serial
import configparser as cp
import tkinter.colorchooser as cc


class Steckdosen(ctk.CTk):
    def __init__(st):
        super().__init__()
        st.title("Steckdosen")
        st.resizable(False, False)
        
        def taste_gedrueckt(event):
            taste_num = event.char
            if taste_num == '1':
                st.Schalten(1)
            if taste_num == '2':
                st.Schalten(2)
            if taste_num == '3':
                st.Schalten(3)
            if taste_num == '4':
                st.Schalten(4)
            if taste_num == '5':
                st.Schalten(5)
            if taste_num == '6':
                st.Schalten(6)
            if taste_num == '7':
                st.Schalten(7)
            if taste_num == '8':
                st.Schalten(8)
            if taste_num == '+':
                st.Schalten(9)
            if taste_num == '-':
                st.Schalten(10)


        st.bind('<KeyPress>', taste_gedrueckt)

# --- Konfigurationen
        st.configp = cp.ConfigParser()
        st.configp.read(f'{os.getcwd()}/stconfig.ini')
        print('getcwd:      ', os.getcwd())
        st.buttonText = st.configp['ButtonText']
        st.Farbe = st.configp['Farben']
        ctk.set_appearance_mode('dark')

        st.configure(background='#3D3D3E')

# --- Aufruf der Funktionen
        st.Buttons_erstellen()
        st.FarbenEinlesen()
        st.TextEinlesen()
        

# --- Steckdosen Buttons erstellen
    def Buttons_erstellen(st):
        st.frame1 = ctk.CTkFrame(st)
        st.frame1.configure(fg_color='#3D3D3E')
        st.stBg = '#3D3D3E'
        st.btn_st1 = ctk.CTkButton(st.frame1, command=lambda: st.Schalten(1))
        st.btn_st1.configure(width=100,background_corner_colors= (st.stBg,st.stBg,st.stBg,st.stBg), corner_radius=(st.btn_st1.cget('height')/2),border_width=2,border_color='#f9e4b3')
        st.btn_st1.grid(row=0, column=0, padx=5, pady=5)
        st.btn_st2 = ctk.CTkButton(st.frame1, command=lambda: st.Schalten(2))
        st.btn_st2.configure(width=100,background_corner_colors= (st.stBg,st.stBg,st.stBg,st.stBg), corner_radius=(st.btn_st1.cget('height')/2),border_width=2,border_color='#f9e4b3')
        st.btn_st2.grid(row=0, column=1, padx=5)
        st.btn_st3 = ctk.CTkButton(st.frame1, command=lambda: st.Schalten(3))
        st.btn_st3.configure(width=100,background_corner_colors= (st.stBg,st.stBg,st.stBg,st.stBg), corner_radius=(st.btn_st1.cget('height')/2),border_width=2,border_color='#f9e4b3')
        st.btn_st3.grid(row=0, column=2, padx=5)
        st.btn_st4 = ctk.CTkButton(st.frame1, command=lambda: st.Schalten(4))
        st.btn_st4.configure(width=100,background_corner_colors= (st.stBg,st.stBg,st.stBg,st.stBg), corner_radius=(st.btn_st1.cget('height')/2),border_width=2,border_color='#f9e4b3')
        st.btn_st4.grid(row=0, column=3, padx=5)
        st.btn_st5 = ctk.CTkButton(st.frame1, command=lambda: st.Schalten(5))
        st.btn_st5.configure(width=100,background_corner_colors= (st.stBg,st.stBg,st.stBg,st.stBg), corner_radius=(st.btn_st1.cget('height')/2),border_width=2,border_color='#f9e4b3')
        st.btn_st5.grid(row=1, column=0, pady=5)
        st.btn_st6 = ctk.CTkButton(st.frame1, command=lambda: st.Schalten(6))
        st.btn_st6.configure(width=100,background_corner_colors= (st.stBg,st.stBg,st.stBg,st.stBg), corner_radius=(st.btn_st1.cget('height')/2),border_width=2,border_color='#f9e4b3')
        st.btn_st6.grid(row=1, column=1)
        st.btn_st7 = ctk.CTkButton(st.frame1, command=lambda: st.Schalten(7))
        st.btn_st7.configure(width=100,background_corner_colors= (st.stBg,st.stBg,st.stBg,st.stBg), corner_radius=(st.btn_st1.cget('height')/2),border_width=2,border_color='#f9e4b3')
        st.btn_st7.grid(row=1, column=2)
        st.btn_st8 = ctk.CTkButton(st.frame1, command=lambda: st.Schalten(8))
        st.btn_st8.configure(width=100,background_corner_colors= (st.stBg,st.stBg,st.stBg,st.stBg), corner_radius=(st.btn_st1.cget('height')/2),border_width=2,border_color='#f9e4b3')
        st.btn_st8.grid(row=1, column=3)
        st.btn_stan = ctk.CTkButton(st.frame1, text="Alle an", command=lambda: st.Schalten(9))
        st.btn_stan.configure(width=100,background_corner_colors= (st.stBg,st.stBg,st.stBg,st.stBg), fg_color='#F9EDCB',text_color='#000000', corner_radius=(st.btn_st1.cget('height')/2),border_width=2,border_color='#f9e4b3')
        st.btn_stan.grid(row=2, column=0, pady=5)
        st.btn_staus = ctk.CTkButton(st.frame1, text="Alle aus", command=lambda: st.Schalten(10))
        st.btn_staus.configure(width=100,background_corner_colors= (st.stBg,st.stBg,st.stBg,st.stBg), fg_color='#F9EDCB',text_color='#000000', corner_radius=(st.btn_st1.cget('height')/2),border_width=2,border_color='#f9e4b3')
        st.btn_staus.grid(row=2, column=3)
        st.btn_selbst = ctk.CTkButton(st.frame1, text="Einstellungen", command=lambda: neuesFenster())
        st.btn_selbst.configure(width=100,background_corner_colors= (st.stBg,st.stBg,st.stBg,st.stBg), fg_color='#F9EDCB',text_color='#000000', corner_radius=(st.btn_st1.cget('height')/2),border_width=2,border_color='#f9e4b3')
        st.btn_selbst.grid(row=2, column=1, columnspan=2)
        #st.btn_check = ctk.CTkButton(st.frame1, command=lambda: st.update_buttons(st))
        #st.btn_check.grid(row=2,column=2)
        st.frame1.pack()



# --- Farben der Steckdosen Buttons einlesen
    def FarbenEinlesen(st):
        #try:
            st.configp.read('stconfig.ini')
            st.Farbe = st.configp['Farben']

            if f'st1bg' in st.Farbe: st.btn_st1.configure(text_color=st.Farbe['st1fg'])
            if f'st1fg' in st.Farbe: st.btn_st1.configure(fg_color=st.Farbe['st1bg'])
            if f'st1rf' in st.Farbe: st.btn_st1.configure(border_color=st.Farbe['st1rf'])
            if f'st2bg' in st.Farbe: st.btn_st2.configure(text_color=st.Farbe['st2fg'])
            if f'st2fg' in st.Farbe: st.btn_st2.configure(fg_color=st.Farbe['st2bg'])
            if f'st2rf' in st.Farbe: st.btn_st2.configure(border_color=st.Farbe['st2rf'])
            if f'st3bg' in st.Farbe: st.btn_st3.configure(text_color=st.Farbe['st3fg'])
            if f'st3fg' in st.Farbe: st.btn_st3.configure(fg_color=st.Farbe['st3bg'])
            if f'st3rf' in st.Farbe: st.btn_st3.configure(border_color=st.Farbe['st3rf'])
            if f'st4bg' in st.Farbe: st.btn_st4.configure(text_color=st.Farbe['st4fg'])
            if f'st4fg' in st.Farbe: st.btn_st4.configure(fg_color=st.Farbe['st4bg'])
            if f'st4rf' in st.Farbe: st.btn_st4.configure(border_color=st.Farbe['st4rf'])
            if f'st5bg' in st.Farbe: st.btn_st5.configure(text_color=st.Farbe['st5fg'])
            if f'st5fg' in st.Farbe: st.btn_st5.configure(fg_color=st.Farbe['st5bg'])
            if f'st5rf' in st.Farbe: st.btn_st5.configure(border_color=st.Farbe['st5rf'])
            if f'st6bg' in st.Farbe: st.btn_st6.configure(text_color=st.Farbe['st6fg'])
            if f'st6fg' in st.Farbe: st.btn_st6.configure(fg_color=st.Farbe['st6bg'])
            if f'st6rf' in st.Farbe: st.btn_st6.configure(border_color=st.Farbe['st6rf'])
            if f'st7bg' in st.Farbe: st.btn_st7.configure(text_color=st.Farbe['st7fg'])
            if f'st7fg' in st.Farbe: st.btn_st7.configure(fg_color=st.Farbe['st7bg'])
            if f'st7rf' in st.Farbe: st.btn_st7.configure(border_color=st.Farbe['st7rf'])
            if f'st8bg' in st.Farbe: st.btn_st8.configure(text_color=st.Farbe['st8fg'])
            if f'st8fg' in st.Farbe: st.btn_st8.configure(fg_color=st.Farbe['st8bg'])
            if f'st8rf' in st.Farbe: st.btn_st8.configure(border_color=st.Farbe['st8rf'])
            if f'stan' in st.Farbe: st.btn_stan.configure(fg_color=st.Farbe['stan'])
            if f'stanfg' in st.Farbe: st.btn_stan.configure(text_color=st.Farbe['stanfg'])
            if f'stanrf' in st.Farbe: st.btn_stan.configure(border_color=st.Farbe['stanrf'])
            if f'staus' in st.Farbe: st.btn_staus.configure(fg_color=st.Farbe['staus'])
            if f'stausfg' in st.Farbe: st.btn_staus.configure(text_color=st.Farbe['stausfg'])
            if f'stausrf' in st.Farbe: st.btn_staus.configure(border_color=st.Farbe['stausrf'])
            if f'stselbst' in st.Farbe: st.btn_selbst.configure(fg_color=st.Farbe['stselbst'])
            if f'stselbstfg' in st.Farbe: st.btn_selbst.configure(text_color=st.Farbe['stselbstfg'])
            if f'stselbstrf' in st.Farbe: st.btn_selbst.configure(border_color=st.Farbe['stselbstrf'])
            
        #except:
        #    pass

# --- Text der Steckdosen Buttons einlesen
    def TextEinlesen(st):
        st.configp.read('stconfig.ini')
        for i in range(1,9):
            try:
                bu = f"st.btn_st{i}.configure(text='" + str(st.configp['ButtonText'][f'steckdose{i}']) + "')"
                exec(bu)
            except:
                pass

# --- Steckdosen schalten
    def Schalten(st, Zahl):
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
    
class neuesFenster(ctk.CTkToplevel):
    def __init__(st):
        #E = ctk.Toplevel(app)
        super().__init__()
        st.title("Eistellungen")
        st.resizable(False, False)
        geo = app.geometry().split('x')
        geo2 = geo[1].split('+')
        geo2.insert(0,geo[0])
        st.geometry(f"294x420+{int(geo2[0])+int(geo2[2])}+{geo2[3]}")
        st.configure(fg_color='#3D3D3E')

# --- Konfigurationen
        #style = ctk.Style(st)
        #style.theme_use('clam')
        #style.configure("bg.TNotebook", background='#3b3b3e', foreground='white')
        
        st.configp = cp.ConfigParser()
        st.configp.read('stconfig.ini')
        st.buttonText1 = st.configp['ButtonText']
        st.Farben_conf = st.configp['Farben']

# --- beginn Komponeten Erstellung --------------
        st.nb = ctk.CTkTabview(st)
        st.nb.configure(fg_color='#3D3D3E')
        st.nb.pack()
        st.nb.add('Text').configure(fg_color='#3D3D3E')
        st.nb.add('Farben').configure(fg_color='#3D3D3E')
        st.frame11 = ctk.CTkFrame(st.nb.tab('Text'))
        st.frame11.configure(fg_color='#3D3D3E')
        
    # --- Text Einstellungen Komponeten erstellen
        for i in range(1,9):
            
            sts=f"""st.Text1{i} = ctk.StringVar(name='Steckdose {i}')
if (st.configp['ButtonText']['Steckdose{i}']):
    st.Text1{i}.set(value=st.buttonText1["Steckdose{i}"])
st.Label{i} = ctk.CTkLabel(st.frame11, text='Steckdose {i}',padx=5,pady=5)
st.Label{i}.grid(row={i-1}, column=0)
st.Input{i} = ctk.CTkEntry(st.frame11, textvariable=st.Text1{i})
st.Input{i}.grid(row={i-1}, column=1,padx=5,pady=7)"""
            #print(sts)
            exec(sts)
    
        st.Save = ctk.CTkButton(st.frame11, text='Speichern', command=lambda: Speichern())
        st.Save.grid(row=8,column=0,pady=5, columnspan=2)
        st.Save.bind()
        st.frame11.pack()
        st.frame12 = ctk.CTkFrame(st.nb.tab('Farben'))
        st.frame12.configure(fg_color='#3D3D3E')

# --- Farben Einstellungen speichern
        def Farben(b):
            #exec(f'st.ST{b[1]}.set(value="")')
            #print(b)
            color = cc.askcolor(parent=st)
            
            if (color[1] != None):
                if (b == 'stan'):
                    st.Farben_conf['stan'] = f'{color[1]}'
                    with open('stconfig.ini', 'w') as configfile:
                        st.configp.write(configfile)
                if (b == 'staus'):
                    st.Farben_conf['staus'] = f'{color[1]}'
                    with open('stconfig.ini', 'w') as configfile:
                        st.configp.write(configfile)
                if (b == 'stselbst'):
                    st.Farben_conf['stselbst'] = f'{color[1]}'
                    with open('stconfig.ini', 'w') as configfile:
                        st.configp.write(configfile)
                if (b == 'stanrf'):
                    st.Farben_conf['stanrf'] = f'{color[1]}'
                    with open('stconfig.ini', 'w') as configfile:
                        st.configp.write(configfile)
                if (b == 'stausrf'):
                    st.Farben_conf['stausrf'] = f'{color[1]}'
                    with open('stconfig.ini', 'w') as configfile:
                        st.configp.write(configfile)
                if (b == 'stselbstrf'):
                    st.Farben_conf['stselbstrf'] = f'{color[1]}'
                    with open('stconfig.ini', 'w') as configfile:
                        st.configp.write(configfile)
                if (b == 'stanfg'):
                    st.Farben_conf['stanfg'] = f'{color[1]}'
                    with open('stconfig.ini', 'w') as configfile:
                        st.configp.write(configfile)
                if (b == 'stausfg'):
                    st.Farben_conf['stausfg'] = f'{color[1]}'
                    with open('stconfig.ini', 'w') as configfile:
                        st.configp.write(configfile)
                if (b == 'stselbstfg'):
                    st.Farben_conf['stselbstfg'] = f'{color[1]}'
                    with open('stconfig.ini', 'w') as configfile:
                        st.configp.write(configfile)
                
                if (b[0]=='b'):
                    st.Farben_conf[f'St{b[1]}bg'] = f'{color[1]}'
                    with open('stconfig.ini', 'w') as configfile:
                        st.configp.write(configfile)
                elif(b[0]=='r'):
                    st.Farben_conf[f'St{b[1]}rf'] = f'{color[1]}'
                    with open('stconfig.ini', 'w') as configfile:
                        st.configp.write(configfile)
                else:
                    st.Farben_conf[f'St{b[1]}fg'] = f'{color[1]}'
                    with open('stconfig.ini', 'w') as configfile:
                        st.configp.write(configfile)
                app.FarbenEinlesen()


    # --- Farben Einstellungen Komponenten erstellen
        st.L1 = ctk.CTkLabel(st.frame12, text='Steckdose 1').grid(column=0,row=0, padx=5)
        st.bg1 = ctk.CTkButton(st.frame12, text='bg', width= 40, command=lambda: Farben('b1'))
        st.bg1.grid(column=1,row=0,padx=5)
        st.fg1 = ctk.CTkButton(st.frame12, text='fg', width= 40, command=lambda: Farben('f1'))
        st.fg1.grid(column=2,row=0,padx=5,pady=3)
        st.Rahmen1 = ctk.CTkButton(st.frame12, text='rf', width= 40, command=lambda: Farben('r1'))
        st.Rahmen1.grid(column=3,row=0,padx=5,pady=3)

        st.L2 = ctk.CTkLabel(st.frame12, text='Steckdose 2').grid(column=0,row=1, padx=5)
        st.bg2 = ctk.CTkButton(st.frame12, text='bg', width= 40, command=lambda: Farben('b2'))
        st.bg2.grid(column=1,row=1,padx=5)
        st.fg2 = ctk.CTkButton(st.frame12, text='fg', width= 40, command=lambda: Farben('f2'))
        st.fg2.grid(column=2,row=1,padx=5,pady=3)
        st.Rahmen2 = ctk.CTkButton(st.frame12, text='rf', width= 40, command=lambda: Farben('r2'))
        st.Rahmen2.grid(column=3,row=1,padx=5,pady=3)

        st.L3 = ctk.CTkLabel(st.frame12, text='Steckdose 3').grid(column=0,row=2, padx=5)
        st.bg3 = ctk.CTkButton(st.frame12, text='bg', width= 40, command=lambda: Farben('b3'))
        st.bg3.grid(column=1,row=2,padx=5)
        st.fg3 = ctk.CTkButton(st.frame12, text='fg', width= 40, command=lambda: Farben('f3'))
        st.fg3.grid(column=2,row=2,padx=5,pady=3)
        st.Rahmen3 = ctk.CTkButton(st.frame12, text='rf', width= 40, command=lambda: Farben('r3'))
        st.Rahmen3.grid(column=3,row=2,padx=5,pady=3)

        st.L4 = ctk.CTkLabel(st.frame12, text='Steckdose 4').grid(column=0,row=3, padx=5)
        st.bg4 = ctk.CTkButton(st.frame12, text='bg', width= 40, command=lambda: Farben('b4'))
        st.bg4.grid(column=1,row=3,padx=5)
        st.fg4 = ctk.CTkButton(st.frame12, text='fg', width= 40, command=lambda: Farben('f4'))
        st.fg4.grid(column=2,row=3,padx=5,pady=3)
        st.Rahmen4 = ctk.CTkButton(st.frame12, text='rf', width= 40, command=lambda: Farben('r4'))
        st.Rahmen4.grid(column=3,row=3,padx=5,pady=3)

        st.L5 = ctk.CTkLabel(st.frame12, text='Steckdose 5').grid(column=0,row=4, padx=5)
        st.bg5 = ctk.CTkButton(st.frame12, text='bg', width= 40, command=lambda: Farben('b5'))
        st.bg5.grid(column=1,row=4,padx=5)
        st.fg5 = ctk.CTkButton(st.frame12, text='fg', width= 40, command=lambda: Farben('f5'))
        st.fg5.grid(column=2,row=4,padx=5,pady=3)
        st.Rahmen5 = ctk.CTkButton(st.frame12, text='rf', width= 40, command=lambda: Farben('r5'))
        st.Rahmen5.grid(column=3,row=4,padx=5,pady=3)

        st.L6 = ctk.CTkLabel(st.frame12, text='Steckdose 6').grid(column=0,row=5, padx=5)
        st.bg6 = ctk.CTkButton(st.frame12, text='bg', width= 40, command=lambda: Farben('b6'))
        st.bg6.grid(column=1,row=5,padx=5)
        st.fg6 = ctk.CTkButton(st.frame12, text='fg', width= 40, command=lambda: Farben('f6'))
        st.fg6.grid(column=2,row=5,padx=5,pady=3)
        st.Rahmen6 = ctk.CTkButton(st.frame12, text='rf', width= 40, command=lambda: Farben('r6'))
        st.Rahmen6.grid(column=3,row=5,padx=5,pady=3)

        st.L7 = ctk.CTkLabel(st.frame12, text='Steckdose 7').grid(column=0,row=6, padx=5)
        st.bg7 = ctk.CTkButton(st.frame12, text='bg', width= 40, command=lambda: Farben('b7'))
        st.bg7.grid(column=1,row=6,padx=5)
        st.fg7 = ctk.CTkButton(st.frame12, text='fg', width= 40, command=lambda: Farben('f7'))
        st.fg7.grid(column=2,row=6,padx=5,pady=3)
        st.Rahmen7 = ctk.CTkButton(st.frame12, text='rf', width= 40, command=lambda: Farben('r7'))
        st.Rahmen7.grid(column=3,row=6,padx=5,pady=3)

        st.L8 = ctk.CTkLabel(st.frame12, text='Steckdose 8').grid(column=0,row=7, padx=5)
        st.bg8 = ctk.CTkButton(st.frame12, text='bg', width= 40, command=lambda: Farben('b8'))
        st.bg8.grid(column=1,row=7,padx=5)
        st.fg8 = ctk.CTkButton(st.frame12, text='fg', width= 40, command=lambda: Farben('f8'))
        st.fg8.grid(column=2,row=7,padx=5,pady=3)
        st.Rahmen8 = ctk.CTkButton(st.frame12, text='rf', width= 40, command=lambda: Farben('r8'))
        st.Rahmen8.grid(column=3,row=7,padx=5,pady=3)

        st.Lan = ctk.CTkLabel(st.frame12, text='Alle an').grid(column=0,row=8, padx=5)
        st.bgan = ctk.CTkButton(st.frame12, text='bg', width= 40, command=lambda: Farben('stan'))
        st.bgan.grid(column=1,row=8,padx=5,pady=3)
        st.bganfg = ctk.CTkButton(st.frame12, text='fg', width= 40, command=lambda: Farben('stanfg'))
        st.bganfg.grid(column=2,row=8,padx=5,pady=3)
        st.bganrf = ctk.CTkButton(st.frame12, text='rf', width= 40, command=lambda: Farben('stanrf'))
        st.bganrf.grid(column=3,row=8,padx=5,pady=3)

        st.Laus = ctk.CTkLabel(st.frame12, text='Alle aus').grid(column=0,row=9, padx=5)
        st.bgaus = ctk.CTkButton(st.frame12, text='bg', width= 40, command=lambda: Farben('staus'))
        st.bgaus.grid(column=1,row=9,padx=5,pady=3)
        st.bgausfg = ctk.CTkButton(st.frame12, text='fg', width= 40, command=lambda: Farben('stausfg'))
        st.bgausfg.grid(column=2,row=9,padx=5,pady=3)
        st.bgausrf = ctk.CTkButton(st.frame12, text='rf', width= 40, command=lambda: Farben('stausrf'))
        st.bgausrf.grid(column=3,row=9,padx=5,pady=3)


        st.Lselbst = ctk.CTkLabel(st.frame12, text='Einstellungen').grid(column=0,row=10, padx=5)
        st.bgselbst = ctk.CTkButton(st.frame12, text='bg', width= 40, command=lambda: Farben('stselbst'))
        st.bgselbst.grid(column=1,row=10,padx=5,pady=3)
        st.bgselbstfg = ctk.CTkButton(st.frame12, text='fg', width= 40, command=lambda: Farben('stselbstfg'))
        st.bgselbstfg.grid(column=2,row=10,padx=5,pady=3)
        st.bgselbstrf = ctk.CTkButton(st.frame12, text='rf', width= 40, command=lambda: Farben('stselbstrf'))
        st.bgselbstrf.grid(column=3,row=10,padx=5,pady=3)


        st.frame12.pack()
        
# --- Ende Komponenten Erstellung ---------------

# --- Text Einstellungen speichern
        def Speichern():
            st.configp['ButtonText'] = {}
            ButtonText1 = st.configp['ButtonText']
            ButtonText1['Steckdose1'] = st.Text11.get()
            ButtonText1['Steckdose2'] = st.Text12.get()
            ButtonText1['Steckdose3'] = st.Text13.get()
            ButtonText1['Steckdose4'] = st.Text14.get()
            ButtonText1['Steckdose5'] = st.Text15.get()
            ButtonText1['Steckdose6'] = st.Text16.get()
            ButtonText1['Steckdose7'] = st.Text17.get()
            ButtonText1['Steckdose8'] = st.Text18.get()
            with open('stconfig.ini', 'w') as configfile:
                st.configp.write(configfile)
            app.TextEinlesen()


        
            
if __name__ == "__main__":
    app = Steckdosen()
    app.mainloop()
