#================= DICTIONARY ===============================
import json
def consulta(palabra):
    with open('data.json','r') as json_file: # Es importante el uso de a+ para realizar append sobre texto, el uso de r+ comienza a reescribir desde el pricipio
        data = json.load(json_file) # abrir archivo con 'a+' genera error 
        if palabra in data:
            return data[palabra] #returna lista con resultados
        elif palabra=='y': # retorna 'y' si es que ha sido ingresada para luego terminar el programa.
            return 'y'
        # else: #Si es que no se cumple ninguno de los if, por defecto se retornará None, por lo que no es necesario
        #     return None #incorporar esas 2 últimas líneas de código.

while True:
    resultado=consulta(input("Ingresa palabra a consultar ('y' para salir): ").lower()) #se realiza
    #la búsqueda y considerando todas las letras por minúsculas
    if resultado=='y': break # si has ingresado y, se termina el bucle
    if resultado != None: # Si la palabra incresada existe 
        id=0 #se crea variable id para indicar cantidad de definiciones disponibles en el diccionario
        for line in resultado: #se imprime lista de líneas encontradas
            id+=1
            print(id,".- ",line) #se imprime línea con número al inicio
    else: #si la palabra ingresada no existe
        print("Palabra no encontrada")
#Fin del programa
print("Adios!!!......gracias por utilizar este diccionario!!!!")