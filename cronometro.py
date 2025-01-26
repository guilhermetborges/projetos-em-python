from tkinter import  *
import tkinter

#cores

coramarela = "#f1ff2e" ; corpreta = "#000000"  ;corcinza = "#21201f" 
corazul ="#072e6b" ; corbranca = "#cfe1ff" ;corverde = "#00ff59"
corlaranja = "#f27405"; cordefundo ="#291b0e"; corbranca1='#e6ecf5'; corlilas = '#5a48e0'

janela = Tk()
janela.title('cronometro')
janela.geometry("600x300")
janela.configure(bg=corpreta)
janela.resizable(width=FALSE,height=FALSE)

global tempo
global rodar
global contador
global limitador


tempo = "00:00:00"
rodar = False
contador = 0
limitador = 59

def iniciar():
    global tempo
    global contador
    global limitador

    if rodar:
       # antes do cronometro aparecer
       if contador <= -1:
           inicio = 'comecando em' +str(contador)
           l_tempo['text'] = inicio
           l_tempo['font'] = 'Arial 10' 
       else:
        l_tempo['font'] = 'Times 50 bold '

        temporaria = str(tempo)
        h,m,s = map(int,temporaria.split(":"))
        h = int(h)
        m = int(m)
        s = int(contador)

        if (s >=limitador):
           contador = 0
           m+=1
        
        s = str(0)+str(s)
        m = str(0)+str(m)
        h = str(0)+str(h)
           
        #atualizando os valores
        temporaria = str(h[-2:])+":"+str(m[-2:])+":"+str(s[-2:])
        l_tempo['text'] = temporaria
        tempo = temporaria

    
       
           



    l_tempo.after(1000,iniciar)
    contador +=1

def pausar():
   global rodar
   rodar = False
   


def reiniciar():
   global tempo
   global contador
   #reiniciando
   contador = 0
   tempo = "00:00:00"
   l_tempo['text'] = tempo



def start():
    global rodar
    rodar = True
    iniciar()






#---------------criando labels---------------

l_cronometro = Label(janela,text='Cronometro',height='1',padx=5,relief='flat',anchor='center',font="Ivy 14 bold",bg=corpreta,fg='white')
l_cronometro.place(x=7,y=12)

l_tempo = Label(janela,text=tempo,padx=5,relief='raised',anchor='center',font="Times 50 bold",bg=corpreta,fg='white')
l_tempo.place(x=165,y=98)




#------------criando botões ---------------------
b_iniciar = Button(janela,command=start,text='Iniciar',height=1,width=6,relief='flat',anchor='center',overrelief='solid',font=('Ivy 12 bold'),bg=corlilas,fg='white')
b_iniciar.place(x=160,y=230)

b_pausar = Button(janela,command=pausar,text='Pausar',height=2,width=6,padx=10,relief='flat',anchor='center',overrelief='solid',font=('Ivy 12 bold'),bg=corlilas,fg='white')
b_pausar.place(x=240,y=220)

b_reiniciar = Button(janela,command=reiniciar,text='restaurar',height=1,width=6,padx=10,relief='flat',anchor='center',overrelief='solid',font=('Ivy 12 bold'),bg=corlilas,fg='white')
b_reiniciar.place(x=337,y=230)





janela.mainloop()
