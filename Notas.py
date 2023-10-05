from datetime import datetime

class Carrera:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

class Alumno:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = []

    def agregar_nota(self, carrera, semestre, asignatura, seccion, valor):
        nota = Nota(self, carrera, semestre, asignatura, seccion, valor)
        self.notas.append(nota)

class Semestre:
    def __init__(self, nivel, inicio_semestre, fin_semestre):
        self.nivel = nivel
        self.inicio_semestre = datetime.strptime(inicio_semestre, "%d/%m/%Y")
        self.fin_semestre = datetime.strptime(fin_semestre, "%d/%m/%Y")

class Nota:
    def __init__(self, alumno, carrera, semestre, asignatura, seccion, valor):
        self.alumno = alumno
        self.carrera = carrera
        self.semestre = semestre
        self.asignatura = asignatura
        self.seccion = seccion
        self.valor = valor

class Profesor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Asignatura:
    def __init__(self, nombre):
        self.nombre = nombre

class Seccion:
    def __init__(self, nombre, paralelo):
        self.nombre = nombre
        self.paralelo = paralelo

carrera = Carrera("Ingeniería Software")
alumno = Alumno("Ricardo", "Coque")
inicio_semestre = "01/08/2023"
fin_semestre = "31/12/2023"
semestre = Semestre("Cuarto Nivel", inicio_semestre, fin_semestre)
asignatura = Asignatura("Poo")
seccion = Seccion("Matutina","A1")
profesor = Profesor("Daniel", "Vera")

# Agregar notas directamente al alumno
alumno.agregar_nota(carrera, semestre, asignatura, seccion, 15)
alumno.agregar_nota(carrera, semestre, asignatura, seccion, 15)
alumno.agregar_nota(carrera, semestre, asignatura, seccion, 15)
alumno.agregar_nota(carrera, semestre, asignatura, seccion, 15)
alumno.agregar_nota(carrera, semestre, asignatura, seccion, 20)


# Presentar Información por Pantalla alumno
print('='*40)
print("Carrera:", carrera.nombre)
print("Alumno:", alumno.nombre, alumno.apellido)
print("Semestre:", semestre.nivel)
print("Inicio del Semestre:", semestre.inicio_semestre)
print("Fin del Semestre:", semestre.fin_semestre)
print("Asignatura:", asignatura.nombre)
print("Sección:", seccion.nombre, seccion.paralelo)
print("Profesor:", profesor.nombre, profesor.apellido)
print("Notas:")
for i, nota in enumerate(alumno.notas, start=1):
    if i == len(alumno.notas):
        nombre_nota = "EXA"
    else:
        nombre_nota = f"N{i}"
    
    print(f"  - {nombre_nota}: {nota.valor}")
print('='*40)

