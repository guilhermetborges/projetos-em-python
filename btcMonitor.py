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

#importando apis

api_link = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CCNY%2CBRL'

#api request
response = requests.get(api_link)

#convertendo api

dados = response.json()

print(dados)

valor_usd = float(dados['USD'])
valor_format_usd = "${:,.3f}".format(valor_usd)

valor_real = float(dados['BRL'])
valor_format_real = "R${:,.3f}".format(valor_real)

valor_euro = float(dados['EUR'])
valor_format_euro = "€{:,.3f}".format(valor_euro)

valor_yuan = float(dados['CNY'])
valor_format_yuan = "¥{:,.3f}".format(valor_yuan)




#criando frames

frame_cima = Frame(janela, width=350,height=60,pady=0,padx=0,bg=corbranca)
frame_cima.grid(row=0,column=0)


frame_baixo = Frame(janela, width=350,height=290,pady=0,padx=0,bg=corpreta)
frame_baixo.grid(row=1,column=0)


#criando labels

l_S = Label(frame_cima,text='$',height='1',padx=5,relief='solid',anchor='center',font="Ivy 20 bold",bg='white',fg=amarelocor)
l_S.place(x=3,y=12)

l_crypto = Label(frame_cima,text='Bitcoin em tempo real',height='1',padx=5,relief='flat',anchor='center',font="Ivy 14 bold",bg=corbranca,fg='black')
l_crypto.place(x=33,y=12)

#frame baixo

l_usd = Label(frame_baixo,text=valor_format_usd,width=14,padx=5,relief='flat',anchor='center',font="Arial 19",bg=corpreta,fg='red')
l_usd.place(x=50,y=20)

l_euro = Label(frame_baixo,text=valor_format_euro,width=14,padx=5,relief='flat',anchor='center',font="Ivy 15 bold",bg=corpreta,fg='red')
l_euro.place(x=15,y=90)

l_real = Label(frame_baixo,text=valor_format_real,width=14,padx=5,relief='flat',anchor='center',font="Ivy 15 bold",bg=corpreta,fg='red')
l_real.place(x=17,y=160)

l_kaz = Label(frame_baixo,text=valor_format_yuan,width=14,padx=5,relief='flat',anchor='center',font="Ivy 15 bold",bg=corpreta,fg='red')
l_kaz.place(x=15,y=230)



janela.mainloop()