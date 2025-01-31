from tkinter import *
from tkinter import ttk

#importando bibliotecas

import requests
import json

####################

coramarela = "#f1ff2e" ; corpreta = "#000000"  ;corcinza = "#21201f" 
corazul ="#072e6b" ; corbranca = "#cfe1ff" ;corverde = "#00ff59"
corlaranja = "#f27405"; cordefundo ="#291b0e"; corbranca1='#e6ecf5'; corlilas = '#5a48e0';co0 = "#444466"  
co1 = "#feffff"  ;amarelocor = "#f7eb07"
co2 = "#6f9fbd"  # azul / blue

janela = Tk()
janela.title("monitordeCRIPTO")
janela.geometry("350x350")
janela.config(bg=corcinza)

ttk.Separator(janela,orient=HORIZONTAL).grid(row=0,columnspan=1,ipadx=200)
def info():
    #importando apis

    api_link = 'https://min-api.cryptocompare.com/data/price?fsym=SOL&tsyms=USD%2CEUR%2CCNY%2CBRL'

    #api request
    response = requests.get(api_link)

    #convertendo api

    dados = response.json()

    print(dados)

    valor_usd = float(dados['USD'])
    valor_format_usd = "${:,.3f}".format(valor_usd)
    l_usd['text'] = ' USD: '+valor_format_usd


    valor_real = float(dados['BRL'])
    valor_format_real = "R${:,.3f}".format(valor_real)
    l_real['text'] = ' REAL: '+valor_format_real

    valor_euro = float(dados['EUR'])
    valor_format_euro = "€{:,.3f}".format(valor_euro)
    l_euro['text'] = ' EURO: '+valor_format_euro

    valor_yuan = float(dados['CNY'])
    valor_format_yuan = "¥{:,.3f}".format(valor_yuan)
    l_kaz['text'] = ' YUAN: '+valor_format_yuan

    frame_baixo.after(1000,info)






#criando frames

frame_cima = Frame(janela, width=410,height=60,pady=0,padx=0,bg=corlaranja)
frame_cima.grid(row=0,column=0)


frame_baixo = Frame(janela, width=410,height=290,pady=0,padx=0,bg=co0)
frame_baixo.grid(row=1,column=0)


#criando labels

l_S = Label(frame_cima,text='$',height='1',padx=5,relief='solid',anchor='center',font="Ivy 20 bold",bg=corlaranja,fg=amarelocor)
l_S.place(x=3,y=12)

l_crypto = Label(frame_cima,text='SOLANA em tempo real',height='1',padx=5,relief='flat',anchor='center',font="Ivy 14 bold",bg=corlaranja,fg='black')
l_crypto.place(x=33,y=12)

#frame baixo

l_usd = Label(frame_baixo,text='',width=25,padx=3,relief='flat',anchor='nw',font="Arial 18",bg=co0,fg=co1)
l_usd.place(x=20,y=20)

l_euro = Label(frame_baixo,text='',width=25,padx=3,relief='flat',anchor='nw',font="Ivy 12 bold",bg=co0,fg=co1)
l_euro.place(x=5,y=90)

l_real = Label(frame_baixo,text='',width=25,padx=3,relief='flat',anchor='nw',font="Ivy 12 bold",bg=co0,fg=co1)
l_real.place(x=6,y=160)

l_kaz = Label(frame_baixo,text='',width=25,padx=3,relief='flat',anchor='nw',font="Ivy 12 bold",bg=co0,fg=co1)
l_kaz.place(x=5,y=230)


info()
janela.mainloop()