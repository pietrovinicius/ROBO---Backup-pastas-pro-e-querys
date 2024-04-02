#03/10/2023
#@PLima
#ROBO - BACKUP PASTA C:
import pyautogui
import datetime
import time
import sys
import os
import tkinter as tk
import threading

import signal

#para sair da automacao colocando o mouse no topo a esquerda da janela
pyautogui.FAILSAFE = True
status = True
statusThread = False

varia = True


def pausa(tempo):
    global statusThread
    print("time de:" , tempo)
    print(f"statusThread: {statusThread}")
    time.sleep(tempo)   
    
def fechando_explorer():
    print("Fechando explorer;")
    #pyautogui.hotkey("win" , "d")#("Alt" , "f4")
    pausa(2)   

def agora():
    agora = datetime.datetime.now()
    agora = agora.strftime("%d/%m/%Y %H:%M:%S")
    return str(agora)
    
def fim():
    global statusThread
    print("Backup finalizado!")      
    pyautogui.alert("     Backup finalizado com sucesso!     " )
    print(f"statusThread: {statusThread}")
    print("==================================== FIM ====================================")    
    
def log(texto_):
    if not os.path.exists("log.txt"):
            with open("log.txt" , "a" , encoding="utf-8-sig") as log:
                print(f'Log é {os.path.exists("log.txt")}, então será criado na pasta')
                log.write("")
                        
    with open("log.txt" , "a", encoding="utf-8-sig")  as log:
        log.write(f"\n{str(texto_)} - {str(agora())}")   
            

def botao_Apps():
    #botao para habilitar as opções
    print("botao para habilitar as opções;")
    pyautogui.hotkey("apps")
    pausa(1)
    #posicao do 7 zip
    pyautogui.hotkey("7")
    #4x down:
    print("4x teclado down;")
    pyautogui.hotkey("down")
    pyautogui.hotkey("down")
    pyautogui.hotkey("down")
    pyautogui.hotkey("down")
    pausa(1)
    print("Enter botao_Apps;")
    pyautogui.hotkey("enter")
    pausa(90)
    
def backup_Projetos():
    global statusThread
    while statusThread:
        print("******** Função Backup Projetos ********\n\n")
        print(f"statusThread: {statusThread}\n")
        log("Função Backup Projetos - início")
        print("Tecla windows + R;")
        if statusThread:   
            pausa(3)
            pyautogui.hotkey("win" , "r")
            pausa(1)
            print("Inserindo: C:\Pietro")
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            pyautogui.write("C:\Pietro")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("Enter;")
            pyautogui.hotkey("enter")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread:
            print("click na pasta;")
            pyautogui.click(975 , 531)
            pausa(1)
            pyautogui.hotkey("win" , "up")
            pausa(1)
            print("Projetos")
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            pyautogui.write("Projetos")
            botao_Apps()
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        #selecionando arquivo zip recem criado
        if statusThread: 
            print("selecionando arquivo zip recem criado")
            pausa(35)
            pyautogui.write("Projetos.zip")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            pyautogui.hotkey("f2")
            pausa(1)
            print("Registrando momento atual;")
            agora = datetime.datetime.now()    
            print("Agora: " , str(agora))    
            renomear = "Projetos_" + agora.strftime("%d/%m/%Y-%H:%M:%S")
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread:
            print("Renomear: " , renomear)
            pyautogui.write(renomear)
            pausa(2)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("enter")
            pyautogui.hotkey("enter")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("ctrl + x;")
            pyautogui.hotkey("ctrl" , "x")
            pausa(2)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("Tecla windows + R;")
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            pyautogui.hotkey("win" , "r")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("Inserindo: C:\Pietro\OneDrive - PRONEP\Backup")
            pyautogui.write("C:\Pietro\OneDrive - PRONEP\Backup")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("Enter;")
            pyautogui.hotkey("enter")
            pausa(2)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("click na pasta;")
            pyautogui.hotkey("win" , "up")    
            pausa(2)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("ctrl + v;")
            pyautogui.hotkey("ctrl" , "v")
            pausa(5)
            log("Função Backup Projetos - fim")   
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        
        #mudando o status assim que finalizar o backup:
        statusThread=False     

def backup_MV_QUERYs():
    global statusThread
    statusThread = True
    while statusThread:
        print(" ******** Função Backup MV QUERYS Projetos.zip********\n\n")
        log("Função Backup MV QUERYS - início")
        print("Tecla windows + R;")
        pyautogui.hotkey("win" , "r")
        pausa(1)
        if statusThread: 
            print("backspace")
            pyautogui.hotkey("backspace")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("Inserindo: C:\Pietro\OneDrive - PRONEP")
            pyautogui.write("C:\Pietro\OneDrive - PRONEP")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("enter")
            pyautogui.hotkey("enter")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("click na pasta;")
            pyautogui.click(975 , 531)
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            pyautogui.hotkey("win" , "up")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("16. Homologação")
            pyautogui.write("16. Homologação ")
            pausa(2)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("enter")
            pyautogui.hotkey("enter")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("MV QUERY")
            pyautogui.write("MV QUERY")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            botao_Apps()
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            #selecionando arquivo zip recem criado
            print("selecionando arquivo zip recem criado")
            pausa(30)
            pyautogui.write("MV QUERYs.zip")
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            pausa(2)
            print("f2")
            pyautogui.hotkey("f2")
            pausa(2)
            print("Registrando momento atual;")
            agora = datetime.datetime.now()    
            print("Agora: " , str(agora))    
            renomear = "MV_QUERYs_" + agora.strftime("%d/%m/%Y-%H:%M:%S")
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("Renomear: " , renomear)
            pyautogui.write(renomear)
            pausa(3)
            print("enter")
            pyautogui.hotkey("enter")
            pausa(5)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("ctrl + x;")
            pyautogui.hotkey("ctrl" , "x")
            pausa(2)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("Tecla windows + R;")
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            pyautogui.hotkey("win" , "r")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("Inserindo: C:\Pietro\OneDrive - PRONEP\Backup")
            pyautogui.write("C:\Pietro\OneDrive - PRONEP\Backup")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("Enter;")
            pyautogui.hotkey("enter")
            pausa(2)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("click na pasta;")
            pyautogui.hotkey("win" , "up")    
            pausa(2)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("ctrl + v;")
            pyautogui.hotkey("ctrl" , "v")
            pausa(5)
            log("Função Backup Projetos - fim")    
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break

        statusThread=False 
    
def backup_IW_QUERIES_HOME_CARE():
    global statusThread
    statusThread = True
    while statusThread:
        print("******** Função Backup IW QUERIES HOME CARE ********\n\n")
        log("Função Backup IW QUERIES HOME CARE - início")        
        pausa(2)
        if statusThread: 
            print("win + r")
            pyautogui.hotkey("win" , "r")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("backspace;")
            pyautogui.hotkey("backspace")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("C:\Pietro\OneDrive - PRONEP")
            pyautogui.write("C:\Pietro\OneDrive - PRONEP")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("enter;")
            pyautogui.hotkey("enter")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("16. Homologação;")
            pyautogui.write("16. Homologação ")
            pausa(2)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("enter;")    
            pyautogui.hotkey("enter")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("IW QUERIES HOME_CARE;")
            pyautogui.write("IW QUERIES HOME_CARE")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            botao_Apps()
            pausa(5)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        #selecionando arquivo zip recem criado
        if statusThread: 
            print("selecionando arquivo zip recem criado;")
            pyautogui.write("IW QUERIES HOME_CARE.zip")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("f2;")
            pyautogui.hotkey("f2")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("Registrando momento atual;")
            agora = datetime.datetime.now()    
            print("Agora: " , str(agora))    
            renomear = "IW_QUERIES_HOME_CARE_" + agora.strftime("%d/%m/%Y-%H:%M:%S")
            print("Renomear: " , renomear)
            pyautogui.write(renomear)
            pausa(2)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("enter;")
            pyautogui.hotkey("enter")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("ctrl + x;")
            pyautogui.hotkey("ctrl" , "x")
            pausa(5)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            fechando_explorer()
            print("Tecla windows + R;")
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            pyautogui.hotkey("win" , "r")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("Inserindo: C:\Pietro\OneDrive - PRONEP\Backup")
            pyautogui.write("C:\Pietro\OneDrive - PRONEP\Backup")
            pausa(1)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("Enter;")
            pyautogui.hotkey("enter")
            pausa(2)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("click na pasta;")
            pyautogui.hotkey("win" , "up")    
            pausa(2)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            print("ctrl + v;")
            pyautogui.hotkey("ctrl" , "v")
            pausa(5)
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        if statusThread: 
            fechando_explorer()
            log("Função Backup Projetos - fim")    
        else:
            print(f"Aplicacao paralisada!\nstatusThread: {statusThread}\n")
            break
        statusThread=False 


def Executar():
    try:        
        global varia
        global statusThread   
        
        print("============================== Executar() ========================")
        print(f"statusThread: {statusThread}\n")
        print("Agora: " , str(agora()))

        while statusThread:
            #tempo para clicar nas 2 opções:
            um_segundo = 1
            pausa(um_segundo)
            if statusThread:             
                print(f"Iniciando as {agora()}\nbackup_Projetos()")
                backup_Projetos()
                pausa(5)
                print(f"Iniciando as {agora()}\nbackup_MV_QUERYs")
                backup_MV_QUERYs()
                pausa(5)
                print(f"Iniciando as {agora()}\nbackup_IW_QUERIES_HOME_CARE")
                backup_IW_QUERIES_HOME_CARE()   
                fim()            
            else:
                print(f"statusThread: {statusThread}\n{agora()}")
                print("finalizando o looping que prende a thread")
                #esse break abaixo esta finalizando o looping que prende a thread
                um_segundo = 0.3
                break            
    except Exception as erro:
        print(f"\n{agora()}\nError: {erro}") 
        pyautogui.alert(title="==== Exception ====" , text=erro , timeout=2000) 
        exit()
        
def pausar():
    global statusThread
    statusThread=False
    print("============================== Pausar() ========================")
    print(f"global statusThread: {statusThread}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#"============================== inicio ========================"  
    
if __name__ == "__main__":    
    print("============================== inicio ========================")

    root = tk.Tk()
    root.maxsize(450,420)
    #root.minsize(720,500)
    root.geometry("450x420")
    root.title("ROBO - BACKUP PASTA C")
    root.configure(bg="white")
    
    def start():        
        global statusThread

        print("============================== start() ========================")
        print(f"statusThread: {statusThread}\n")
        #criando evento na thread, para ser usado apos ser setado, ser verificado e encerrar a thread
        if statusThread:
            print(f"Thread já foi iniciada, statusThread: \n{statusThread}")
        else:        
            #iniciando thread para usar na funcao Executar()    
            threadExecutar = threading.Thread(target=Executar).start()
            statusThread = True
            print(f"statusThread: {statusThread}\nthreadExecutar.start()\n")
            
            
    imagem = tk.PhotoImage(file="BACKUP.png")
    lb_barra_superior = tk.Label(root, image=imagem , border =0)
    lb_barra_superior.pack()
    
    lb_console = tk.Label(root, text="...não inicializado...")
    lb_console.pack(fill="both" , expand=True , pady=10)   
        
    bt_Iniciar = tk.Button(root, text="Iniciar", command=lambda: [ lb_console.config(text="Robo inicializado!") , start()])
    bt_Iniciar.pack(fill="both", expand=True , padx=100 , pady=5 )    

    bt_Sair = tk.Button(root, text="Parar", command=lambda: [ lb_console.config(text="Robo pausado!") , pausar()]) #sys.exit()
    bt_Sair.pack(fill="both", expand=True , padx=100 , pady=5)
    
    root.mainloop()
