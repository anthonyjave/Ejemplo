import time as tiempo 
import wikipedia as wiki 
import pywhatkit 
import pyttsx3 

engine = pyttsx3.init()
def hablar(palabras):
    engine.say(palabras)
    engine.runAndWait()
def saludos(text):
    saludos_arreglo = {'como estas':['bien','mal'], 'me podrias dar la hora ': 'porsupuesto',"aprobamos  ":[False,True]}
    print("hola")
    print(saludos_arreglo['como estas'])
def hora():
    hora=tiempo.localtime().tm_hour
    dia = tiempo.localtime().tm_min
    string = "La hora  es {} con {} minutos".format(hora,dia)
    return string
def buscar_wikipedia(definicion):
    wiki.set_lang('es')
    order = definicion.replace('wiki','')
    return wiki.summary(order)
def reproducir_musica_youtube(link):
    tiempo.sleep(2)
    pywhatkit.playonyt(link)
    
def buscando_funcion(texto):
    if 'hora' in texto:
        text=hora()
        hablar(text)
    else: 
        if 'wiki' in texto :
            print(text)
            hablar(buscar_wikipedia(texto))
        elif 'youtube' in texto:
            buscar_wikipedia(texto)