
class Asiento:
    def __init__(self, color, precio, registro):

        self.color = color
        self.precio = precio
        self.registro = registro
    
        def cambiarColor(self, colorcambio):
            if (colorcambio in ["rojo","verde","amarillo","negro","blanco"]):
                self.color = colorcambio
        
        def CantidadAsientos (self, numeroasiento):
            return numeroasiento
        
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, numero):
        self.registro = numero

    def asignarTipo(self, Tipomotor):
        l=["Electrico", "Gasolina"]
        if Tipomotor in l:
            self.tipo = Tipomotor
        else:
            print("Tipo invalido")

class Auto:
    CantidadAutos=0
    def __init__(self, modelo, precio, asientos, marca, motor, registro,): 
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        

    def cantidadAsientos(self, numero):
        self.cantidadCreados =numero

    def verificarintegridad(self, integridad):
