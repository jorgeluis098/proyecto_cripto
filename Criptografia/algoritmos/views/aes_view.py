from django.shortcuts import render
from django.views import View
from django.conf import settings
from itertools import repeat
from time import time


#Para AES-ECB y AES-CBCls -l
from Cryptodome.Cipher import AES

class AES_EBC(View):
    template_name = 'dummy.html'

    # Pueden ver a la función "get" como un main
    def get(self, request, *args, **kwargs):  
        tiemposCifrado = []
        tiemposDescifrado = []
        listaLlaves = []
        listaMensajes = []
        archivo_lectura = settings.MEDIA_ROOT + "/AES_EBC.rsp"

        listaLlaves, listaMensajes = self.leer_archivo(archivo_lectura, listaLlaves, listaMensajes)
        print("\n\n\n================================")
        print("Lista llaves: " + str(listaLlaves))
        print("\n\n\n================================")
        print("Lista mensajes: " + str(listaMensajes))
        print("\n\n\n")

        self.cifrado_aes_ecb(listaLlaves, listaMensajes, tiemposCifrado)

        context = {
            # Nota: El contexto son las variables que se van a mandar a la página web
            # Si quieren por el momento no vamos a mandar nada a la página web y todo lo manejamos por la consola
            # Y a variables que decidan imprimir al final, son las que se mandarán en el conexto a la pg web
            # Por el momento lo pueden dejar en blanco

            # La estructura es la siguiente
            # 'nombre_variable_html' : nombre_variable_python,
        }
        return render(request, self.template_name, context)
    

    def leer_archivo(self, archivo, listaLlaves, listaMensajes):
        archivo_lectura = open(archivo,"r")
        for linea in archivo_lectura.readlines():
            #Lectura de llaves
            if "KEY = " in linea:
                llave = linea.lstrip("KEY = ")
                listaLlaves.append(llave.rstrip("\n"))

            #Lectura de mensajes
            elif "PLAINTEXT = " in linea:
                mensaje = linea.lstrip("PLAINTEX = ")
                listaMensajes.append(mensaje.rstrip("\n"))
        archivo_lectura.close()
        return listaLlaves, listaMensajes
    
    def cifrado_aes_ecb(self, listaLlaves, listaMensajes, tiemposCifrado):
        tamanioListaLlaves = len(listaLlaves)
        tamanioListaMensajes = len(listaMensajes)

        for i in range(0, tamanioListaMensajes):
            #Conversión de elementos
            mensajeConcatenado = mensaje = bytearray.fromhex(listaMensajes[i]) 
            llave = bytearray.fromhex(listaLlaves[i])
            
            #Concatenamos el mensaje 
            for j in range(0, 111):
                mensajeConcatenado = mensajeConcatenado + mensaje
            #print("\nMENSAJE = ", mensajeConcatenado)
            
            objetoCifrar = AES.new(llave, AES.MODE_ECB)
            tiempoInicio = time()
            bytesCifrados = objetoCifrar.encrypt(mensajeConcatenado)
            tiempoFinal = time ()
            tiemposCifrado.append(tiempoFinal - tiempoInicio)
            #print("\nBytes Cifrados: ", bytesCifrados.hex())

        #print("Tamanio llaves: " + str(len(listaLlaves)))
        #print("Tamanio mensajes: " + str(len(listaMensajes)))