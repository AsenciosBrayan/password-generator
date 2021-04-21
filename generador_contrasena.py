import random
import string

def generador_contrasena(c, n):
    for i in range(c):
        miContrasena = ''
        for i in range(n):
            miContrasena += random.choice(string.printable[:-6])
        return miContrasena
        
cContrasenas = int(input('Ingrese la cantidad de contraseñas que quiere generar: '))
cCaracteres = int(input('Ingrese la cantidad de caracteres para la contraseña: '))

for i in range(cContrasenas):
    contrasena_generada = generador_contrasena(cContrasenas, cCaracteres)
    print('Contraseña #'+ str(i+1) + ': ' + contrasena_generada)
