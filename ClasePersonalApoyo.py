from ClaseAgente import AU
categoria1=[1,2,3,4,5,6,7,8,9,10]
categoria2=[11,12,13,14,15,16,17,18,19,20]
class PersonalApoyo(AU):
    __categoria=''
    def __init__(self, categoria,areaV, tipoV, clases, cargo, catedra, cuil, apellido, nombre, sueldoB, antiguedad):
        self.__categoria=categoria
        super().__init__(areaV, tipoV, clases, cargo, catedra,cuil, apellido, nombre, sueldoB, antiguedad)
    def getname(self):
        return super().getname()
    def getcategoria(self):
        return self.__categoria
    def mostrardatos(self):
        print(f"Categoria: {self.__categoria}")

        super().mostrardatos()
    def getapellido(self):
        return super().getapellido()
    def sueldo(self):
        porcentaje=0
        antiguedad=super().getantiguedad()*0.01
        if self.__categoria in categoria1:
            porcentaje=0.1
        if self.__categoria in categoria2:
            porcentaje=0.2
        if self.__categoria == 21 or self.__categoria == 22:
            porcentaje=0.3
        por=porcentaje
        basico=super().getsueldo()
        sueldoA=basico*antiguedad
        sueldoC=basico*por
        SueldoT=basico+sueldoA+sueldoC
        return SueldoT
    def getcuil(self):
        return super().getcuil()
    def mostrarD(self):
        Sueldo=self.sueldo()
        print("Nombre: ")
        super().vername()
        print("Apellido: ")
        super().verapellido()
        print(f"Tipo de agente: Personal de apoyo, Sueldo: {Sueldo}")
        