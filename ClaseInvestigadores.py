from ClaseAgente import AU
class Investigadores(AU):
    __area_de_investigacion=''
    __tipo_de_investigacion=''
    def __init__(self, areaV, tipoV,clases, cargo, catedra,cuil, apellido, nombre, sueldoB, antiguedad):
        self.__area_de_investigacion=areaV
        self.__tipo_de_investigacion=tipoV
        super().__init__(areaV, tipoV, clases, cargo, catedra,cuil, apellido, nombre, sueldoB, antiguedad)
    def getname(self):
        return super().getname()
    def mostrardatos(self):
        print(f"Area de investigacion: {self.__area_de_investigacion}")
        print(f"Tipo de investigacion: {self.__tipo_de_investigacion}")
        super().mostrardatos()
    def getarea(self):
        return self.__area_de_investigacion
    def getapellido(self):
        return super().getapellido()
    def sueldo(self):
        antiguedad=super().getantiguedad()*0.01
        basico=super().getsueldo()
        sueldoA=basico*antiguedad
        SueldoT=sueldoA+basico
        return SueldoT
    def getcuil(self):
        return super().getcuil()
    def gettipo(self):
        return self.__tipo_de_investigacion
    def mostrarD(self):
        Sueldo=self.sueldo()
        print("Nombre: ")
        super().vername()
        print("Apellido: ")
        super().verapellido()
        print(f"Tipo de agente: Personal de apoyo, Sueldo: {Sueldo}")