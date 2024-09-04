import turtle

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
        self.tortuga = turtle.Turtle()  # Crea una instancia de la tortuga para dibujar

    def dibujar(self):
        for _ in range(4):
            self.tortuga.forward(self.lado)
            self.tortuga.right(90)  # Gira la tortuga 90 grados a la derecha

    def mostrar(self):
        turtle.done()  # Finaliza y mantiene la ventana abierta

# Solicitar entrada del usuario
lado = int(input("Ingresa la longitud de un lado del cuadrado: "))

# Crear instancia de la clase con la longitud del lado
cuadrado = Cuadrado(lado)

# Dibujar el cuadrado
cuadrado.dibujar()

# Mostrar el dibujo
cuadrado.mostrar()
