# Import the Canvas class
from canvasapi import Canvas

# Canvas API URL
API_URL = "https://tecsup.instructure.com"
# Canvas API key
API_KEY = "POMlFGipLsYwltgTCinK5HSHwemI5848gipzwJhJCnb6x3qUgaxJOOVKRCupX5WE"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)


def menu():
    opcion = 0
    while opcion!=3:
        print("1 - Imprimir curso")
        print("2 - Mostrar asignaciones del curso")
        print("3 - Mostrar Alumnos")
        opcion = int(input("Ingresar opcion"))
        if opcion ==1:
            imprimirAlumno()
        elif opcion==2:
            mostrarAsignaciones()
        elif opcion==3:
            mostrarAlumnos()
                
def imprimirAlumno():
    if API_KEY is None:
        print("Su Token es incorrecto")
    else:
        course = canvas.get_course(3342) 
        print("Nombre del curso:",course.name+'\n',
              "Fecha de inicio:",course.start_at+'\n',
              "Fecha fin:",course.end_at)    
            
 #####################################################
            #26-10-2018------<01:25>           
def mostrarAsignaciones():
    course = canvas.get_course(3342) 
    assignments = course.get_assignments()
    print(assignments)
    for assignment in assignments:
        print(assignment)

def mostrarAlumnos():
    course = canvas.get_course(3342) 
    students = course.get_users()
    print(students)
    for student in students:
        print(student)
                          
menu()
