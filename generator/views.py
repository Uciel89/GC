# Esta libreria nos permite leer un archivo, en este caso html, y devolverlo al cliente
from django.shortcuts import render
import random

# from django.http import HttpResponse

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    # Definiendo una lista de caractes, con los cuales vamos a interactuar a la hora de generar las contraseñas
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    # Vamos a leer la longitud que proviene del request de parte del metodo GET
    length = int(request.GET.get('length'))
    uppercaseC = request.GET.get('uppercase')
    specialC = request.GET.get('special')
    numbersC = request.GET.get('numbers')

    # Comprovamos que quiere el usuario que agreguemos a su contraseña
    if uppercaseC: 
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if specialC:
        characters.extend(list('!@#$%&*.'))

    if numbersC:
        characters.extend(list('123456789'))   


    # Miestras el bucle for va recorriendo la lista, los gurdamos en otra variable
    for char in range(length):

        # Utilizamos el modulo randow para guardar caracteres aleatorios dentro de la variable generate_password
        generated_password += random.choice(characters)


    return render(request, 'generator/password.html', {'password': generated_password})

# Creamos lo que nostros queremos que pueda recivir el cliente
def about(request): 
    return render(request, 'generator/about.html')
