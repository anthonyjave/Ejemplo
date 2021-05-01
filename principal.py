import speech_recognition  as habla
import pyttsx3 
from funcion.funciones import buscando_funcion
inicio  = habla.Recognizer()
engine = pyttsx3.init()
def hablar(palabras):
    engine.say(palabras)
    engine.runAndWait()
def main():
    print("Hola soy K.O.N.E.K.O")
    encendido = False 
    while True:
        with  habla.Microphone() as source:
            audio = inicio.listen(source)
            try  :
                text = inicio.recognize_google(audio,language="es")
                if "estado del micro" in text:
                    text=text.replace('siri','')
                    hablar("El estado del micro es {}".format(encendido))  
                elif "activar" in text:
                    text=text.replace('Siri','')
                    hablar("Activando microfrono ")
                    encendido=True 
                if encendido == True:
                    buscando_funcion(text)
                elif "desactivar" in text:
                    encendido=False
                    hablar("Apagando telefono")
            except:
                hablar("Porfavor repetir ")


main()