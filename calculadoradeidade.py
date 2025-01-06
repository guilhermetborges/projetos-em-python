from tkinter import *
from tkinter import ttk
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

#definindo o ano atual
atual = datetime.now().year

#---------------------------------------fazendo---funções------------------------------

def calcular():
    inicio = calendario1.get()
    termino = calendario2.get()

    #separando os valores
    mes,dia,ano = [int(f) for f in inicio.split('/')]
    data_inicial = date(ano,mes,dia)


    mes1,dia1,ano1 = [int(f) for f in termino.split('/')]
    data_nascimento = date(ano1,mes1,dia1)

    anos = relativedelta(data_inicial,data_nascimento).years
    meses = relativedelta(data_inicial,data_nascimento).months
    dias = relativedelta(data_inicial,data_nascimento).days


    l_app_anos['text'] = anos,"Anos"
    l_app_meses['text'] = meses,"Meses"
    l_app_dias['text'] = dias,"Dias"

    l_app_anos['fg'] = corbranca
    l_app_meses['fg'] = corbranca
    l_app_dias['fg'] = corbranca




#importando calendario

from tkcalendar import Calendar, DateEntry

janela = Tk()
janela.title("calculadora de idade")
janela.geometry('600x353')

#cores

corpreta = "#000000"  ; corcinza = "#21201f" ; corazul ="#072e6b" ; corbranca = "#cfe1ff" ; corverde = "#00ff59"; corlaranja = "#f27405"; cordefundo ="#291b0e"


#-------------------criando frames ----------------------
frame_1 = Frame(janela, width=600,height=130,pady=0,padx=0,relief=FLAT,bg=corpreta)
frame_1.grid(row=0,column=0)

frame_estilo1 = Frame(janela, width=600,height=3,pady=0,padx=0,relief=FLAT,bg=cordefundo)
frame_estilo1.grid(row=1,column=0)

frame_2 = Frame(janela, width=600,height=220,pady=0,padx=0,relief=FLAT,bg=corcinza)
frame_2.grid(row=2,column=0)

#---------------criando labels---------------
l_calculadora = Label(frame_1 , text="CALCULADORA \nDE \nIDADE", width=20,height=4,padx=3,relief=FLAT,anchor=CENTER,font="Ivy 18 bold",bg=corpreta,fg=corbranca)
l_calculadora.place(x=145,y=10)

#---------------criando labels---------------
l_data_inicio = Label(frame_2 , text="data ATUAL:", width=13,height=2,padx=56,relief=FLAT,anchor=CENTER,font="Ivy 11 bold",bg=corlaranja,fg=corpreta)
l_data_inicio.place(x=15,y=15)

calendario1 = DateEntry(frame_2,width=24,height=10,bg='darkblue',fg=corbranca,borderwidth=2,date_pattern = 'mm/dd/y',y=atual)
calendario1.place(x=300,y=25)

l_data_nascimento = Label(frame_2 , text="data nascimento: ", width=13,height=2,padx=56,relief=FLAT,anchor=CENTER,font="Ivy 11 bold",fg=corlaranja,bg=corpreta)
l_data_nascimento.place(x=15,y=80)

calendario2 = DateEntry(frame_2,width=24,height=10,bg='darkblue',fg=corbranca,borderwidth=2,date_pattern = 'mm/dd/y',y=atual)
calendario2.place(x=300,y=91)


#---------------label--app---------
l_app_anos = Label(frame_2 , text="--\nanos", width=5,height=2,padx=13,relief=FLAT,anchor=CENTER,font="Ivy 15 bold ",bg=corcinza,fg=corpreta)
l_app_anos.place(x=30,y=130)

l_app_meses = Label(frame_2 , text="--\nmeses", width=5,height=2,padx=13,relief=FLAT,anchor=CENTER,font="Ivy 15 bold ",bg=corcinza,fg=corpreta)
l_app_meses.place(x=230,y=130)

l_app_dias = Label(frame_2 , text="--\ndias", width=5,height=2,padx=13,relief=FLAT,anchor=CENTER,font="Ivy 15 bold ",bg=corcinza,fg=corpreta)
l_app_dias.place(x=410,y=130)


#------------criando botão calcular---------------------


b_calcular = Button(frame_2 , command= calcular, text="calcular", width=10,height=1,padx=20,relief=RAISED,overrelief=RIDGE,anchor=CENTER,font="Ivy 10 bold ",bg=corcinza,fg=corpreta)
b_calcular.place(x=215,y=185)


janela.mainloop()