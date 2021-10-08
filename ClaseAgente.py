class AU:
    __cuil=''
    __apellido=''
    __nombre=''
    __SB=0
    __anti=''
    def __init__(self, areaV, tipoV,clases, cargo, catedra, C, A, N, S, An):
        self.__cuil=C
        self.__apellido=A
        self.__nombre=N
        self.__SB=S
        self.__anti=An
        #self.mostrardatos()
    def mostrardatos(self):
        print(f"Cuil: {self.__cuil}\nApellido: {self.__apellido}\nNombre: {self.__nombre}")
        print(f"Sueldo: {self.__SB}\nAntiguedad: {self.__anti}")
    def getname(self):
        return self.__nombre
    
    def getapellido(self):
        return self.__apellido
        
    def getantiguedad(self):
        return self.__anti
    def getsueldo(self):
        return self.__SB
    def getcuil(self):
        return self.__cuil
    def vername(self):
        print(self.__nombre)
    def verapellido(self):
        print(self.__apellido)