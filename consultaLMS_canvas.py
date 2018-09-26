# Import the Canvas class
from canvasapi import Canvas

# Canvas API URL
API_URL = "https://tecsup.instructure.com"
# Canvas API key
API_KEY = input("ingrese su token generado"+'\n')

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

class Curso:
    def imprimir():
        if API_KEY is None:
            print("Su Token es incorrecto")
        else:
            course = canvas.get_course(3430) 
            print("Nombre del curso:",course.name+'\n',
                  "Fecha de inicio:",course.start_at+'\n',
                  "Fecha fin:",course.end_at)
            user = canvas.get_user(29919)#codigo del alumno en CANVAS
            print(user.name)           

Curso.imprimir()
