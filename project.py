import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler

from_dir = "C:\Users\Suporte\Downloads" 

class FileEventHandler(FileSystemEventHandler): 

    def on_created(self,event):
        print(f"Olá, {event.src_path} foi criado" )

    def on_deleted(self,event):
        print(f"Opa!, Alguém exluiu {event.src_path}")
    
    def on_modified(self,event):
        print(f"Olá!, {event.src_path} foi modificado")
    
    def on_moved(self,event):
        print(f"Alguém moveu {event.src_path} para {event.dest_path}")


#Inicializando a classe Gerenciadora de Eventos
event_handler = FileMovementHandler()

#Inicialize o Observer
observer = Observer()

#Agende o observer
observer.schedule(event_hundler, from_dir, recursive = True)

#Inicie o observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("interrompido")
    observer.stop()