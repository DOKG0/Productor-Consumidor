import threading
from threading import Thread, Event, Condition
from queue import Queue
from time import sleep
import random

casillerosVacios = threading.Semaphore(value=9)
casillerosLibres = threading.Semaphore(value=0)
cinta = threading.Semaphore(value=1)
Ca_Llenos = 0 #Casilleros llenos
Tot_Llenos = 0
Tot_Vacios = 0

def Productor(Cinta, Vacios):
    global Ca_Llenos
    global Tot_Llenos 
    print("PRODUCTOR: Entro a productor")
    while True:
        print("PRODUCTOR: Valor Ca_Llenos: ", Ca_Llenos)
        print("PRODUCTOR: Valor casillerosVacios._value: ", casillerosVacios._value)
        sleep(2)
        
        if Ca_Llenos == 9:
            print("PRODUCTOR: Todos los casilleros llenos, productor en espera")    
            while Ca_Llenos > 5: #Si tengo mas de 5 vacios
                print("PRODUCTOR: Hay ", 10 - Ca_Llenos, " vacios, productor esperando a que sean mas de 5.")
                sleep(5)
                        
        print("PRODUCTOR: Entro a if del productor")
        casillerosVacios.acquire()
        Casillero = Vacios.get()
        print("PRODUCTOR: Obtengo casillero")
        while ("VACIO") in Casillero:
            print("PRODUCTOR: Existe palabra VACIO en el casillero: ", casillerosVacios._value)
            Casillero[Casillero.index("VACIO")] = "LLENO"
        
        print("PRODUCTOR: Sali del While Productor")
        #Seccion critica 
        cinta.acquire()    
        Ca_Llenos = Ca_Llenos + 1 #Sumo uno al total
        Tot_Llenos = Tot_Llenos + 1
        cinta.release()
        #Fin Seccion critica
        Cinta.put(Casillero)
        casillerosLibres.release()
        
        print("PRODUCTOR: Llene 1 casillero completo")
        
        if Tot_Llenos > 15:
            print("PRODUCTOR: Termine hilo")
            break

def Consumidor(Cinta, Vacios):
    global Tot_Vacios
    global Ca_Llenos
    print("CONSUMIDOR: Entro a Consumidor") 
    while True:
        print("CONSUMIDOR: Valor Ca_Llenos: ", Ca_Llenos)
        sleep(6)
        if Ca_Llenos > 0:
            casillerosLibres.acquire()
            Casillero = Cinta.get()
            print("CONSUMIDOR: Obtengo casillero")
            while ("LLENO") in Casillero:
                print("CONSUMIDOR: Existe palabra LLENO en el casillero: ", casillerosLibres._value)
                Casillero[Casillero.index("LLENO")] = "VACIO"

            print("CONSUMIDOR: Sali del While")

            #Seccion critica
            cinta.acquire()
            Ca_Llenos = Ca_Llenos - 1 #Resto del total de casilleros llenos        
            cinta.release()
            #Fin Seccion critica
            Tot_Vacios = Tot_Vacios + 1
            Vacios.put(Casillero)
            casillerosVacios.release()
            print("CONSUMIDOR: Vacie un casillero completo")


        if Tot_Vacios > 15:
            print("CONSUMIDOR: Termine hilo")
            break

def main():
    Cinta = Queue(10)
    Vacios = Queue(10)
    for n in range(10):
        print("MAIN: Creo casillero: ", n)
        Casillero = ["VACIO","VACIO","VACIO","VACIO",
                     "VACIO","VACIO","VACIO","VACIO",
                     "VACIO","VACIO","VACIO","VACIO",]
        Vacios.put(Casillero)
    
    print("MAIN: Creo hilos de ejecucion")
    args = [Cinta, Vacios]
    hp = threading.Thread(target=Productor, args=(args))
    hc = threading.Thread(target=Consumidor, args=(args))
    
    print("MAIN: Ejecuto HP")
    hp.start()
    print("MAIN: Ejecuto HC")
    hc.start() 
    print("MAIN: Ejecuto joins")
    #hc.join()      
    hp.join()  
        
main()
    