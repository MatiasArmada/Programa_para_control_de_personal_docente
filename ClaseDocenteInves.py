from ClaseDocente import Docente
from ClaseInvestigadores import Investigadores
class DocenteInves(Investigadores, Docente):
    __categoría_programa_investi='' 
    __importe_extra_doceinvesti=''
    def __init__(self, areaV, tipoV, clases, cargo, catedra, categoria, importe, cuil, apellido, nombre, sueldoB, antiguedad):
        super().__init__(areaV, tipoV,clases, cargo, catedra, cuil, apellido, nombre, sueldoB, antiguedad)
        self.__categoría_programa_investi=categoria
        self.__importe_extra_doceinvesti=importe
    def getname(self):
        return super().getname()
    def mostrardatos(self):
        print(f"Categoria del programa de investigacion: {self.__categoría_programa_investi}")
        print(f"Importe extra por docencia e investigacion: {self.__importe_extra_doceinvesti}")
        super().mostrardatos()
    def getcarreraD(self):
        return super().getcarrera()
    def getarea(self):
        return super().getarea()
    def getapellido(self):
        return super().getapellido()
    def getsueldo(self):
        return super().getsueldo()
    def getantiguedad(self):
        return super().getantiguedad()
    def sueldo(self):
        porcentaje=0
        antiguedad=self.getantiguedad()*0.01
        if super().getcargo()=='Simple':
            porcentaje=0.1
        if super().getcargo()=='Semiexclusivo':
            porcentaje=0.2
        if super().getcargo()=='Exclusivo':
            porcentaje=0.5
        basico=self.getsueldo()
        sueldoA=basico*antiguedad
        sueldoC=basico*porcentaje
        SueldoT=basico+sueldoA+sueldoC
        SueldoT=SueldoT+float(self.__importe_extra_doceinvesti)
        return SueldoT
    def getimportex(self):
        print(self.__importe_extra_doceinvesti)
        return self.__importe_extra_doceinvesti
    def mostrarD(self):
        Sueldo=self.sueldo()
        print("Nombre: ")
        super().vername()
        print("Apellido: ")
        super().verapellido()
        print(f"Tipo de agente: Personal de apoyo, Sueldo: {Sueldo}")
    def getcuil(self):
        return super().getcuil()
    def getcategoria(self):
        return self.__categoría_programa_investi
    def getcatedra(self):
        return super().getcatedra()
    def getcargo(self):
        return super().getcargo()
    def gettipo(self):
        return super().gettipo()
    def getarea(self):
        return super().getarea()