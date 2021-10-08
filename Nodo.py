class Nodo:
    __Persona=None
    __siguiente=None
    def __init__(self, Persona):
        self.__Persona=Persona
        self.__siguiente=None
    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente
    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__Persona
    def P(self):
        print(self.__Persona.getname())