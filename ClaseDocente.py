from ClaseAgente import AU
class Docente(AU):
     __clases=''
     __cargo=''
     __cátedra=''
     def __init__(self,AreaV, TipoV, clases, cargo, catedra,cuil, apellido, nombre, sueldoB, antiguedad):
         super().__init__(AreaV, TipoV, clases, cargo, catedra,cuil, apellido, nombre, sueldoB, antiguedad)
         self.__clases=clases
         self.__cargo=cargo
         self.__catedra=catedra
         
     def getcatedra(self):
         return self.__catedra
     def getname(self):
        return super().getname()
     def mostrardatos(self):
         print(f"Clases de Catedra: {self.__clases}")
         print(f"Cargo: {self.__cargo}")
         print(f"Catedra: {self.__catedra}")
         super().mostrardatos()
     def getcarrera(self):
         return self.__clases
     def getapellido(self):
         return super().getapellido()
     def getcargo(self):
         return self.__cargo
     def sueldo(self):
         porcentaje=0
         antiguedad=super().getantiguedad()*0.01
         if self.__cargo=='Simple':
             porcentaje=0.1
         if self.__cargo=='Semiexclusivo':
             porcentaje=0.2
         if self.__cargo=='Exclusivo':
             porcentaje=0.5
         basico=super().getsueldo()
         sueldoA=basico*antiguedad
         sueldoC=basico*porcentaje
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
    