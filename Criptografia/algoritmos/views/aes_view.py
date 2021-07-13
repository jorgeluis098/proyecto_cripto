from django.shortcuts import render
from django.views import View
#Para AES-ECB y AES-CBC
from Cryptodome.Cipher import AES

class AES_EBC(View):
    template_name = 'dummy.html'

    # Pueden ver a la función "get" como un main
    def get(self, request, *args, **kwargs):  
        #codigo
        #codigo
        #codigo

        context = {
            # Nota: El contexto son las variables que se van a mandar a la página web
            # Si quieren por el momento no vamos a mandar nada a la página web y todo lo manejamos por la consola
            # Y a variables que decidan imprimir al final, son las que se mandarán en el conexto a la pg web
            # Por el momento lo pueden dejar en blanco

            # La estructura es la siguiente
            # 'nombre_variable_html' : nombre_variable_python,
        }
        return render(request, self.template_name, context)
    

    def funcion_2(self, arg1, arg2):
        #codigo
        #codigo
        #codigo
        return 