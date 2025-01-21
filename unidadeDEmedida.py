from tkinter import *
from tkinter import ttk
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from PIL import ImageTk


#---------------------------------------fazendo---funções------------------------------







#cores

coramarela = "#f1ff2e" ; corpreta = "#000000"  ; corcinza = "#21201f" ; corazul ="#072e6b" ; corbranca = "#cfe1ff" ; corverde = "#00ff59"; corlaranja = "#f27405"; cordefundo ="#291b0e"; corbranca1='#e6ecf5'


janela = Tk()
janela.title('')

janela.geometry('650x250')
janela.configure(bg='black')

#-------------------criando frames ----------------------
frame_1 = Frame(janela, width=400,height=80,pady=0,padx=3,relief=FLAT,bg=corbranca)
frame_1.grid(row=0,column=0)


frame_2 = Frame(janela, width=400,height=170,pady=0,padx=0,relief=FLAT,bg=corpreta)
frame_2.grid(row=1,column=0)

##

frame_2.grid(row=1, column=0, sticky='nw')

##


frame_3 = Frame(janela, width=250,height=80,pady=0,padx=0,relief=FLAT,bg=corbranca)
frame_3.grid(row=0,column=1)


frame_4 = Frame(janela, width=250,height=170,pady=0,padx=0,relief=FLAT,bg=corazul)
frame_4.grid(row=1,column=1)

estilo = ttk.Style(janela)
estilo.theme_use("clam")

#-------------criando unidades---------------


unidades = {
    'massa': [
        {'kg': 1000}, {'hg': 100}, {'dag': 10}, {'g': 1}, {'dg': 0.1}, {'cg': 0.01}, {'mg': 0.001}
    ],
    'comprimento': [
        {'km': 1000}, {'hm': 100}, {'dam': 10}, {'m': 1}, {'dm': 0.1}, {'cm': 0.01}, {'mm': 0.001}
    ],
    'tempo': [
        {'hora': 3600}, {'minuto': 60}, {'segundo': 1}, {'milissegundo': 0.001}
    ],
    'area': [
        {'km²': 1000000}, {'hectare': 10000}, {'m²': 1}, {'dm²': 0.01}, {'cm²': 0.0001}, {'mm²': 0.000001}
    ],
    'quantidade': [
        {'mol': 1}, {'mmol': 0.001}, {'µmol': 0.000001}
    ],
    'velocidade': [
        {'km/h': 1}, {'m/s': 0.277778}, {'cm/s': 0.01}, {'mm/s': 0.001}
    ],
    'temperatura': [
        {'celsius': 1}, {'kelvin': 1}, {'fahrenheit': 0.5555555556}  # Fórmula adicional necessária para Fahrenheit
    ],
    'energia': [
        {'joule': 1}, {'kilojoule': 1000}, {'caloria': 4.184}, {'quilocaloria': 4184}
    ],
    'pressão': [
        {'pascal': 1}, {'kilopascal': 1000}, {'bar': 100000}, {'atm': 101325}, {'mmHg': 133.322}
    ]
}


def mostrar_menu(i):
    unidade_de = []
    unidade_para = []
    unidade_valores = []

    for j in unidades[i]:
        for k, v, in j.items():
            unidade_de.append(k)
            unidade_para.append(k)
            unidade_valores.append(v)

    c_de['values'] = unidade_de
    c_para['values'] = unidade_para

    l_unidade['text'] = i
    l_unidade['fg'] = corpreta
    l_unidade['bg'] = corbranca

    # criando função calcular

    def calcular():
        #obtendo as unidades
        a = c_de.get()
        b = c_para.get()

        #obtendo o numero
        numero_para_converter = float(e_numero.get())

        dist = unidade_para.index(b) - unidade_de.index(a)

        if(dist > 0):
            l_resultado = numero_para_converter*(10**dist)
            l_result['text']= l_resultado
        elif(dist < 0):
            l_resultado = numero_para_converter/(10**abs(dist))
            l_result['text']= l_resultado
        else:
            l_resultado = numero_para_converter  # Sem conversão necessária
            l_result['text']= l_resultado

            print(dist,a,b,numero_para_converter)



    #criando botao e caixa de entrada para calcular 
    b_calcular = Button(frame_4,command=calcular, text='CALCULAR',width=9,height=1,relief='flat',anchor='center',overrelief='solid',font=('Ivy 9 bold'),bg=coramarela,fg=corpreta)
    b_calcular.place(x=138,y=80)

    info = Label(frame_4,text='Digite o Numero abaixo',height='1',padx=2,pady=2,relief='flat',anchor='center',font="Ivy 10 bold",bg=corazul,fg=corbranca)
    info.place(x=40,y=55)

    e_numero = Entry(frame_4,width=9,font=('ivy 14 bold'), justify='center',relief=SOLID)
    e_numero.place(x=25,y=80)

    l_result = Label(frame_4,text='---' ,width=9,font=('ivy 16 bold'), justify='center',relief=SOLID)
    l_result.place(x=60,y=125)








#---------------criando labels---------------

L_calculadora = Label(frame_1,text='calculadora de unidade de medida',height=2,padx=4,relief='groove',anchor=CENTER,font="Ivy 15 bold",bg=corbranca1,fg=corpreta)
L_calculadora.place(x=30,y=15)


#---------------criando labels---------------
l_unidade = Label(frame_3,text='Unidade',height='3',padx=83,relief='flat',anchor='center',font="Ivy 16 bold",bg=corpreta,fg=corbranca)
l_unidade.place(x=0,y=2)


l_de = Label(frame_4,text='De',height='1',padx=3,relief='groove',anchor=CENTER,font="Ivy 10 bold",bg=corbranca,fg=corpreta)
l_de.place(x=10,y=20)

c_de =ttk.Combobox(frame_4,width=7,justify='center',font="Ivy 8 bold")
c_de.place(x=45,y=22)

l_para = Label(frame_4,text='Para',height='1',padx=3,relief='groove',anchor=CENTER,font="Ivy 10 bold",bg=corbranca,fg=corpreta)
l_para.place(x=120,y=20)

c_para =ttk.Combobox(frame_4,width=8,justify='center',font="Ivy 8 bold")
c_para.place(x=168,y=22)







#---------------label--app---------



#------------criando botão calcular---------------------
b_0 = Button(frame_2,command=lambda:mostrar_menu('massa'),text='Massa',width=14,height=2,relief='flat',anchor='nw',overrelief='solid',font=('Ivy 10 bold'),bg='blue',fg=corbranca)
b_0.grid(row=0,column=0,sticky='nw',pady=5,padx=6)

b_1 = Button(frame_2,command=lambda:mostrar_menu('tempo'),text='Tempo',width=14,height=2,relief='flat',anchor='nw',overrelief='solid',font=('Ivy 10 bold'),bg='blue',fg=corbranca)
b_1.grid(row=0,column=1,sticky='nw',pady=5,padx=6)

b_2 = Button(frame_2,command=lambda:mostrar_menu('comprimento'),text='Comprimento',width=14,height=2,relief='flat',anchor='nw',overrelief='solid',font=('Ivy 10 bold'),bg='blue',fg=corbranca)
b_2.grid(row=0,column=2,sticky='nw',pady=5,padx=6)

b_3 = Button(frame_2,command=lambda:mostrar_menu('area'),text='AREA',width=14,height=2,relief='flat',anchor='nw',overrelief='solid',font=('Ivy 10 bold'),bg='blue',fg=corbranca)
b_3.grid(row=1,column=0,sticky='nw',pady=5,padx=6)

b_4 = Button(frame_2,command=lambda:mostrar_menu('quantidade'),text='Quantidade',width=14,height=2,relief='flat',anchor='nw',overrelief='solid',font=('Ivy 10 bold'),bg='blue',fg=corbranca)
b_4.grid(row=1,column=1,sticky='nw',pady=5,padx=6)

b_5 = Button(frame_2,command=lambda:mostrar_menu('velocidade'),text='velocidade',width=14,height=2,relief='flat',anchor='nw',overrelief='solid',font=('Ivy 10 bold'),bg='blue',fg=corbranca)
b_5.grid(row=1,column=2,sticky='nw',pady=5,padx=6)

b_6 = Button(frame_2,command=lambda:mostrar_menu('temperatura'),text='Temperatura',width=14,height=2,relief='flat',anchor='nw',overrelief='solid',font=('Ivy 10 bold'),bg='blue',fg=corbranca)
b_6.grid(row=2,column=0,sticky='nw',pady=8,padx=6)

b_7 = Button(frame_2,command=lambda:mostrar_menu('energia'),text='Energia',width=14,height=2,relief='flat',anchor='nw',overrelief='solid',font=('Ivy 10 bold'),bg='blue',fg=corbranca)
b_7.grid(row=2,column=1,sticky='nw',pady=8,padx=6)

b_8 = Button(frame_2,command=lambda:mostrar_menu('pressão'),text='Pressao',width=14,height=2,relief='flat',anchor='nw',overrelief='solid',font=('Ivy 10 bold'),bg='blue',fg=corbranca)
b_8.grid(row=2,column=2,sticky='nw',pady=8,padx=6)






janela.mainloop()