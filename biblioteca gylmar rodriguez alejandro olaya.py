class Libro:
    def __init__(self, id_libro, titulo_libro, autor_libro):
        self.id_libro = id_libro
        self.titulo = titulo_libro
        self.autor = autor_libro
    
    def __str__(self):
        return f"ID: {self.id_libro} Título: {self.titulo} Autor: {self.autor}"

class Estudiante:
    def __init__ (self, id_estudiante, nombres_estudiante, apellidos_estudiante):
        self.id_estudiante = id_estudiante
        self.nombres_estudiante = nombres_estudiante
        self.apellidos_estudiante = apellidos_estudiante

    def __str__(self):
        return f"ID: {self.id_estudiante} Nombres: {self.nombres_estudiante} Apellidos: {self.apellidos_estudiante}"

class Prestamo:
    def __init__ (self, libro, estudiante, fecha_prestamo):
        self.libro = libro
        self.estudiante = estudiante
        self.fechaprestamo = fecha_prestamo
        self.fechadevolucion = None

    def __str__(self):
        
        fecha_devolucion = self.fecha_devolucion if self.fecha_devolucion is not None else "Libro prestado sin devolución"
        return f"""   Préstamo   
                Libro: {self.libro.titulo}
                Estudiante: {self.estudiante.nombres.estudiante}
                Fecha de préstamo: {self.fechaprestamo}"
                Fecha devolución: {fecha_devolucion}"
                """
    
class Biblioteca:
    def __init__ (self):
        self.libros = []
        self.estudiantes = []
        self.prestamos = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
    
    def buscar_libro(self, id_buscar_libro):
        
        for libro in self.libros:
            if libro.id_libro == id_buscar_libro:
                return libro # libro encontrado
        return None
    
    def buscar_estudiante(self, id_buscar_estudiante):
        
        for estudiante in self.estudiantes:
            if estudiante.id_estudiante == id_buscar_estudiante:
                return estudiante # estudiante encontrado
        return None

    def realizar_prestamo(self, id_libro, id_estudiante):
        libro_prestamo = self.buscar_libro(id_libro)
        estudiante_prestamo = self.buscar_estudiante(id_estudiante)

        if libro_prestamo is None or estudiante_prestamo is None:
            print("No existe el libro o el estudiante, no se puede realizar el préstamo.")
            return
        
        fecha_prestamo = input("digite la fecha de préstamo del libro: ")

#apartado de "nuevos prestamos para crear el prestamo en la biblioteca"

        nuevo_prestamo = Prestamo(libro_prestamo, estudiante_prestamo, fecha_prestamo)
        self.prestamos.append(nuevo_prestamo)
        
        print("   Préstamo éxitoso")
        print(f"Libro: {libro_prestamo.titulo}")
        print(f"Estudiante: {estudiante_prestamo.nombres_estudiante} {estudiante_prestamo.apellidos_estudiante}")
        print(f"Fecha de préstamo {fecha_prestamo}")
    
    def devolucion(self, id_libro):
        print("  Buscando préstamo  ")
        prestamo_devuelto = None

        for prestamo in self.prestamos:
                if prestamo.libro.id_libro == id_libro and prestamo.fechadevolucion is None:
                    prestamo_devuelto = prestamo
                    break

        if prestamo_devuelto is None:
            print(f"No se encontró el préstamo para el libro de ID: {id_libro}")
            return
        
        fecha_devolucion = input(f"Préstamo encontrado, ingrese la fecha de devolución para el libro '{prestamo_devuelto.libro.titulo}': ")
        prestamo_devuelto.fechadevolucion = fecha_devolucion

        print("    Devolución éxitosa   ")
        print(f"   Libro:   '{prestamo_devuelto.libro.titulo}'")
        print(f"   Fecha de devolución:   {fecha_devolucion}")

    def mostrar_libros(self):
        print("\n   Catálogo de libros   ")
        if not self.libros:
            print("No hay libros registrados.")
        for libro in self.libros:
            print(libro)

    def mostrar_estudiantes(self):
        print("   Lista de estudiantes   ")
        if not self.estudiantes:
            print("No hay estudiantes registrados")
        for estudiante in self.estudiantes:
            print(estudiante)

    def mostrar_prestamos(self):
        print("   Historial de préstamos   ")
        if not self.prestamos:
            print("No hay préstamos registrados")
        for prestamo in self.prestamos:
            print(prestamo)

if __name__ == "__main__":
    
    #prueba de agregar libros para la biblioteca
    biblioteca = Biblioteca()
    biblioteca.agregar_libro(Libro("ID001", "Don quijote de la mancha", "Miguel de Cervantes Saavedra"))
    biblioteca.agregar_libro(Libro("ID002","Historia de dos ciudades", "Charles Dickens"))
    biblioteca.agregar_libro(Libro("ID003","El señor de los anillos", "J.R.R. Tolkien"))
    biblioteca.agregar_libro(Libro("ID004","El principito", "Saint-Exupéry"))
    biblioteca.agregar_libro(Libro("ID005","Harry potter y la piedra filosofal", "J.K. Rowling"))

#prueba de agregar estudiantes biblioteca

    biblioteca.agregar_estudiante(Estudiante("ID001","Gylmar", "Rodriguez"))
    biblioteca.agregar_estudiante(Estudiante("ID002","Alejandro", "Olaya"))
    

    while True:
        print("\n     Biblioteca     ")
        print("1. Realizar Préstamo")
        print("2. Registrar devolución")
        print("3. Mostrar libros")
        print("4. Mostrar estudiantes")
        print("5. Historial de prestamos")
        print("6. Registrar estudiantes")
        print("0. Salir del programa")
        
        opcion= input("ingrese una opción del (1-5) de lo contrario use (0) para salir: ")

        if opcion == "1":
            print("\n Nuevo préstamo")
            id_libro = input("Introduce el ID del libro: ")
            id_estudiante = input("Introduce el ID del estudiante: ")
            biblioteca.realizar_prestamo(id_libro, id_estudiante)

        elif opcion == "2":
            print("\n Registrar devolución")
            id_libro_devuelto = input("Ingrese el ID del libro que se devuelve: ")
            biblioteca.devolucion(id_libro_devuelto)
        
        elif opcion == "3":
            biblioteca.mostrar_libros()
        
        elif opcion == "4":
            biblioteca.mostrar_estudiantes()

        elif opcion == "5":
            biblioteca.mostrar_prestamos()
        
        elif opcion == "6":
            print("\n Registro de nuevo estudiante")
            id_nuevo = input("Ingrese el ID del estudiante: ")
            nombres_nuevos = input("Ingrese los nombres del estudiante: ")
            apellidos_nuevos = input("Ingrese los apellidos del estudiante: ")

            nuevo_estudiante = Estudiante(id_nuevo, nombres_nuevos, apellidos_nuevos)
            biblioteca.agregar_estudiante(nuevo_estudiante)

            print(f"\n Estudiante {nombres_nuevos} {apellidos_nuevos} registrado con éxito, ID del estudiante: {id_nuevo}")

        
        elif opcion == "0":
            break
        
        else:
            print("Opción no válida, intente de nuevo")


