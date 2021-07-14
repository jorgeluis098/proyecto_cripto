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
        listaLlaves = listaMensajes = []
        listaBytesCifrados = listaBytesDescifrados = []
        tiemposCifrado = tiemposDescifrado = []
        
        archivo_lectura = settings.MEDIA_ROOT + "/AES_EBC.rsp"

        listaLlaves, listaMensajes = self.leer_archivo(archivo_lectura, listaLlaves, listaMensajes)

        self.cifrado_aes_ecb(listaLlaves, listaMensajes, tiemposCifrado, listaBytesCifrados)
        self.descifrado_aes_ecb(listaLlaves, listaMensajes, tiemposDescifrado, listaBytesCifrados, listaBytesDescifrados)

        context = {
            'listaTiemposCifrado' : tiemposCifrado,
            'listaTtiemposDescifrado' : tiemposDescifrado,
            'listaBytesCifrados' : listaBytesCifrados,
            'listaBytesDescifrados' : listaBytesDescifrados,
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
    
    def cifrado_aes_ecb(self, listaLlaves, listaMensajes, tiemposCifrado, listaBytesCifrados):
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
            listaBytesCifrados.append(objetoCifrar.encrypt(mensajeConcatenado))
            tiempoFinal = time ()
            tiemposCifrado.append(tiempoFinal - tiempoInicio)
            #print("\nBytes Cifrados: ", bytesCifrados.hex())
        return
    

    def descifrado_aes_ecb(self, listaLlaves, listaMensajes, tiemposDescifrado, listaBytesCifrados):
        tamanioListaMensajes = len(listaMensajes)
        for i in range(0, tamanioListaMensajes):
            #Conversión de elementos
            mensajeConcatenado = mensaje = listaBytesCifrados[i]
            llave = bytearray.fromhex(listaLlaves[i])
            
            #Concatenamos el mensaje 
            for j in range(0, 111):
                mensajeConcatenado = mensajeConcatenado + mensaje
            #print("\nMENSAJE = ", mensajeConcatenado)
            
            objetoDescifrar = AES.new(llave, AES.MODE_ECB)
            tiempoInicio = time()
            listaBytesCifrados.append(objetoDescifrar.decrypt(mensajeConcatenado))
            tiempoFinal = time ()
            tiemposDescifrado.append(tiempoFinal - tiempoInicio)
            #print("\nBytes Descifrados: ", bytesDescifrados.hex())
        return
