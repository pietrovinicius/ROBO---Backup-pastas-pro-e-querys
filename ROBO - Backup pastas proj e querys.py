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
    #fechando_explorer()    
    print("Backup finalizado com sucesso!")      
    pyautogui.alert("     Backup finalizado com sucesso!     " , timeout=5000)
    print("==================================== FIM ====================================")    
    #sys.exit()
    #fechando_explorer()
    
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
    print("***Função Backup Projetos***")
    log("Função Backup Projetos - início")
    print("Tecla windows + R;")
    pyautogui.hotkey("win" , "r")
    pausa(1)
    print("Inserindo: C:\Pietro")
    pyautogui.write("C:\Pietro")
    pausa(1)
    print("Enter;")
    pyautogui.hotkey("enter")
    pausa(1)
    print("click na pasta;")
    #pyautogui.click(975 , 531)
    pyautogui.hotkey("win" , "up")
    pyautogui.write("Projetos")
    botao_Apps()
    #selecionando arquivo zip recem criado
    print("selecionando arquivo zip recem criado")
    pyautogui.write("Projetos.zip")
    pausa(1)
    pyautogui.hotkey("f2")
    pausa(1)
    print("Registrando momento atual;")
    agora = datetime.datetime.now()    
    print("Agora: " , str(agora))    
    renomear = "Projetos_" + agora.strftime("%d/%m/%Y-%H:%M:%S")
    print("Renomear: " , renomear)
    pyautogui.write(renomear)
    pausa(2)
    print("enter")
    pyautogui.hotkey("enter")
    pausa(1)
    print("ctrl + x;")
    pyautogui.hotkey("ctrl" , "x")
    fechando_explorer()
    print("Tecla windows + R;")
    pyautogui.hotkey("win" , "r")
    pausa(1)
    print("Inserindo: C:\Pietro\OneDrive - PRONEP\Backup")
    pyautogui.write("C:\Pietro\OneDrive - PRONEP\Backup")
    pausa(1)
    print("Enter;")
    pyautogui.hotkey("enter")
    pausa(2)
    print("click na pasta;")
    #pyautogui.click(526,522)
    pyautogui.hotkey("win" , "up")    
    pausa(2)
    print("ctrl + v;")
    pyautogui.hotkey("ctrl" , "v")
    pausa(5)
    #todo
    fechando_explorer()
    log("Função Backup Projetos - fim")    
     

def backup_MV_QUERYs():
    print("Função Backup MV QUERYS - início")
    log("Função Backup MV QUERYS - início")    
    pausa(2)
    print("win + r")
    pyautogui.hotkey("win" , "r")
    pausa(1)
    print("backspace")
    pyautogui.hotkey("backspace")
    pausa(1)
    print("C:\Pietro\OneDrive - PRONEP")
    pyautogui.write("C:\Pietro\OneDrive - PRONEP")
    pausa(1)
    print("enter")
    pyautogui.hotkey("enter")
    pausa(1)
    print("16. Homologação")
    pyautogui.write("16. Homologação ")
    pausa(2)
    print("enter")
    pyautogui.hotkey("enter")
    pausa(1)
    print("MV QUERY")
    pyautogui.write("MV QUERY")
    pausa(1)
    botao_Apps()
    pausa(1)
    #selecionando arquivo zip recem criado
    print("selecionando arquivo zip recem criado")
    pyautogui.write("MV QUERYs.zip")
    pausa(1)
    print("f2")
    pyautogui.hotkey("f2")
    pausa(1)
    print("Registrando momento atual;")
    agora = datetime.datetime.now()    
    print("Agora: " , str(agora))    
    renomear = "MV_QUERYs_" + agora.strftime("%d/%m/%Y-%H:%M:%S")
    print("Renomear: " , renomear)
    pyautogui.write(renomear)
    pausa(2)
    print("enter")
    pyautogui.hotkey("enter")
    pausa(1)
    print("ctrl + c;")
    pyautogui.hotkey("ctrl" , "x")
    #todo
    fechando_explorer()
    print("Tecla windows + R;")
    pyautogui.hotkey("win" , "r")
    pausa(1)
    print("Inserindo: C:\Pietro\OneDrive - PRONEP\Backup")
    pyautogui.write("C:\Pietro\OneDrive - PRONEP\Backup")
    pausa(1)
    print("Enter;")
    pyautogui.hotkey("enter")
    pausa(2)
    print("click na pasta;")
    #pyautogui.click(526,522)
    pyautogui.hotkey("win" , "up")    
    pausa(2)
    print("ctrl + v;")
    pyautogui.hotkey("ctrl" , "v")
    pausa(5)
    #todo
    fechando_explorer()
    log("Função Backup MV QUERYS - fim")    
    
def backup_IW_QUERIES_HOME_CARE():
    print("Função Backup IW QUERIES HOME CARE - início")
    log("Função Backup IW QUERIES HOME CARE - início")        
    pausa(2)
    print("win + r")
    pyautogui.hotkey("win" , "r")
    pausa(1)
    print("backspace;")
    pyautogui.hotkey("backspace")
    pausa(1)
    print("C:\Pietro\OneDrive - PRONEP")
    pyautogui.write("C:\Pietro\OneDrive - PRONEP")
    pausa(1)
    print("enter;")
    pyautogui.hotkey("enter")
    pausa(1)
    print("16. Homologação;")
    pyautogui.write("16. Homologação ")
    pausa(2)
    print("enter;")    
    pyautogui.hotkey("enter")
    pausa(1)
    print("IW QUERIES HOME_CARE;")
    pyautogui.write("IW QUERIES HOME_CARE")
    pausa(1)
    botao_Apps()
    pausa(1)
    #selecionando arquivo zip recem criado
    print("selecionando arquivo zip recem criado;")
    pyautogui.write("IW QUERIES HOME_CARE.zip")
    pausa(1)
    print("f2;")
    pyautogui.hotkey("f2")
    pausa(1)
    print("Registrando momento atual;")
    agora = datetime.datetime.now()    
    print("Agora: " , str(agora))    
    renomear = "IW_QUERIES_HOME_CARE_" + agora.strftime("%d/%m/%Y-%H:%M:%S")
    print("Renomear: " , renomear)
    pyautogui.write(renomear)
    pausa(2)
    print("enter;")
    pyautogui.hotkey("enter")
    pausa(1)
    print("ctrl + c;")
    pyautogui.hotkey("ctrl" , "x")
    pausa(1)
    #todo
    fechando_explorer()
    pausa(1)    
    print("Tecla windows + R;")
    pyautogui.hotkey("win" , "r")
    pausa(1)
    print("Inserindo: C:\Pietro\OneDrive - PRONEP\Backup")
    pyautogui.write("C:\Pietro\OneDrive - PRONEP\Backup")
    pausa(1)
    print("Enter;")
    pyautogui.hotkey("enter")
    pausa(2)
    print("click na pasta;")
    pyautogui.hotkey("win" , "up")    
    pausa(2)
    print("ctrl + v;")
    pyautogui.hotkey("ctrl" , "v")
    pausa(5)
    #todo
    fechando_explorer()
    log("Função Backup IW QUERIES HOME CARE - fim")        

def Executar():
    print(f"#==================================== Executar()")
    try:
        print("Iniciando...")
        backup_Projetos()
        backup_MV_QUERYs()
        backup_IW_QUERIES_HOME_CARE()
        fim()
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
    root.maxsize(600,600)
    root.minsize(600,150)
    root.geometry("400x50")
    root.title("ROBO - BACKUP PASTA C")
    #criando evento na thread, para ser usado apos ser setado, ser verificado e encerrar a thread        
    fechar_thread = threading.Event()    
    
    #iniciando thread para usar na funcao Executar()    
    threadExecutar = threading.Thread(target=Executar)
    
    #para interromper 
    threadExecutar.daemon = True
        
    bt_Iniciar = tk.Button(root, text="Iniciar", command=lambda: [ print("Botao Iniciar") , threadExecutar.start()])
    bt_Iniciar.pack( fill="both" , expand=True)     

    bt_Sair = tk.Button(root, text="Fechar", command=lambda: [ print("Botao Fechar\nroot.destroy()\nfechar_thread.set()\n\n") , root.destroy(), fechar_thread.set()])
    bt_Sair.pack(fill="both" , expand=True)
    
    root.mainloop()  
try:
    if __name__ == "__main__":
        print("==================================== INÍCIO ====================================")
        pausa(2)
        interface()

except KeyboardInterrupt:
    print("==================================== FIM ====================================")
    print("Interrompido pelo ctrl + c!!!\n")        
except Exception as erro:
    print("==================================== FIM ====================================")
    print(f"Erro: {erro=}, {type(erro)=}")  
