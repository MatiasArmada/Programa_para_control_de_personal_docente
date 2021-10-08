from Zope import Zope
from zope.interface import implementer
from ClaseInvestigadores import Investigadores
from ClaseDocente import Docente
from ClaseDocenteInves import DocenteInves
from ClasePersonalApoyo import PersonalApoyo
from Nodo import Nodo
import json
@implementer(Zope)
class Lista:
    __Comienzo=None
    def __init__(self):
        self.__Comienzo=None
    def agregarnodo(self, persona):
        nodo = Nodo(persona)
        nodo.setSiguiente(self.__Comienzo)
        self.__Comienzo=nodo
    def mostrarElemento(self):
        aux = self.__Comienzo
        while aux!=None:
            dato=aux.getDato()
            dato.mostrarD()
            
            aux=aux.getSiguiente()
    def CargarLista(self):
        with open('personal.json') as file:
            
            data = json.load(file)
            for personal in data['personal']:
                cuil=personal['Cuil']
                apellido=personal['Apellido']
                nombre=personal['Nombre']
                SueldoB=personal['Sueldo_basico']
                antiguedad=personal['Antiguedad']
                if 'Clases' in personal: #Docente
                    clases=personal['Clases']
                    cargo=personal['Cargo']
                    catedra=personal['Catedra']
                    if 'area_de_investigacion' in personal:
                        pass
                    else:
                        areaV=0
                        tipoV=0
                        D=Docente(areaV, tipoV, clases, cargo, catedra, cuil, apellido, nombre, SueldoB, antiguedad)
                        self.agregarnodo(D)
                        print("cargo un docente")
                if 'Categoria' in personal:#Personal de apoyo
                    categoria=personal['Categoria']
                    clases=0
                    cargo=0
                    catedra=0
                    areaV=0
                    tipoV=0
                    P=PersonalApoyo(categoria,areaV, tipoV, clases, cargo, catedra, cuil, apellido, nombre, SueldoB, antiguedad)
                    self.agregarnodo(P)
                if 'area_de_investigacion' in personal:#Investigador
                    areaV=personal['area_de_investigacion']
                    tipoV=personal['tipo_de_investigacion']
                    if 'categoria_programa_investi' in personal:
                        pass
                    else:
                        clases=0
                        cargo=0
                        catedra=0
                        I=Investigadores(areaV, tipoV, clases, cargo, catedra, cuil, apellido, nombre, SueldoB, antiguedad)
                        self.agregarnodo(I)
                if 'categoria_programa_investi' in personal:#Investigador, docentes y agente universitario
                    imp=personal['Importex']
                    categoriap=personal['categoria_programa_investi']
                    DI=DocenteInves(areaV, tipoV, clases, cargo, catedra, categoriap, imp, cuil, apellido, nombre, SueldoB, antiguedad)
                    self.agregarnodo(DI)
                    print("CARGO UN DOCENTE I")
        #file.close()

    def agregaragente(self, O):                    
        cuil=input("Ingrese el cuil: ")
        apellido= input("Ingrese el apellido: ")
        nombre= input("Ingrese el nombre: ")
        SueldoB=float(input("Ingrese el sueldo basisco: "))
        antiguedad=0
        if O==1:
            areaV=0
            tipoV=0
            clases=input("Ingrese la carrera donde dicta clases: ")
            cargo=input("Ingrese el cargo: ")
            catedra=input("Ingrese la catedra: ")
            D=Docente(areaV, tipoV,clases, cargo, catedra, cuil, apellido, nombre, SueldoB, antiguedad)
            self.agregarnodo(D)
        if O==2:
            clases=0
            cargo=0
            catedra=0
            areaV=0
            tipoV=0
            categoria=input("Ingrese la categoria: ")
            P=PersonalApoyo(categoria,areaV, tipoV, clases, cargo, catedra, cuil, apellido, nombre, SueldoB, antiguedad)
            self.agregarnodo(P)
        if O==3:
            clases=0
            cargo=0
            catedra=0
            areaV=input("Ingrese el area de investigacion: ")
            tipoV=input("Ingrese el tipo de investigacion: ")
            I=Investigadores(areaV, tipoV, clases, cargo, catedra, cuil, apellido, nombre, SueldoB, antiguedad)
            self.agregarnodo(I)
        if O==4:
            clases=input("Ingrese la carrera donde dicta clases: ")
            cargo=input("Ingrese el cargo: ")
            catedra=input("Ingrese la catedra: ")
            areaV=input("Ingrese el area de investigacion: ")
            tipoV=input("Ingrese el tipo de investigacion: ")
            categoria=input("Ingrese la categoría del programa de investigacion: ")
            importe=input("Ingrese el importe extra por docencia e investigacion: ")
            DI=DocenteInves(areaV, tipoV, clases, cargo, catedra, categoria, importe, cuil, apellido, nombre, SueldoB, antiguedad)
            self.agregarnodo(DI)
    def Buscarporindice(self, I):
        T=True
        j=1
        aux = self.__Comienzo
        while j<=I and T==True:
            if j==I:
                T=False
            else:
                aux=aux.getSiguiente()
                j=j+1
    def Buscarcarrera(self):
        L=Lista()
        nombre=input("Ingrese el nombre de la carrera: ")
        aux = self.__Comienzo
        while aux!=None:
            if type(aux.getDato()) == DocenteInves:
                dato=aux.getDato()
                if nombre == dato.getcarreraD():
                    L.agregarnodo(dato)
            aux=aux.getSiguiente()
        if L!=None:
            L.ordenarpornombre()
        
    def ordenarpornombre(self):
        T=False
        while T==False:
            T=True
            aux=self.__Comienzo
        
            aux2=self.__Comienzo.getSiguiente()
            #print("LALA")
            while aux2!=None:
                if aux2!=None:
                    dato=aux.getDato()
                    dato2=aux2.getDato()
                    nombre1=dato.getname()
                    nombre2=dato2.getname()
                    #print("LALA")
                    if nombre1>nombre2:
                        aux.setSiguiente(aux2.getSiguiente())
                        aux2.setSiguiente(aux)
                        T=False
                        if aux==self.__Comienzo:
                            self.__Comienzo=aux2
                            ant=self.__Comienzo        
                        else:
                            ant.setSiguiente(aux2)
                            ant=aux2
                    aux=aux2
                    aux2=aux.getSiguiente()
        self.mostrarElemento()
    def Buscararea(self):
        DI=0
        I=0
        nombre=input("Ingrese el nombre del area de investigacion: ")
        aux = self.__Comienzo
        while aux!=None:
            if type(aux.getDato()) == DocenteInves:
                dato=aux.getDato()
                if nombre == dato.getarea():
                    DI=DI+1
            if type(aux.getDato()) == Investigadores:
                dato=aux.getDato()
                if nombre == dato.getarea():
                    I=I+1
            aux=aux.getSiguiente()
        print(f"La cantidad de investigadores que trabajan en el area {nombre} son: {I}")
        print(f"La cantidad de docentes investigadores que trabajan en el area {nombre} son: {DI}")
    
    def mostrardatos(self):
        aux = self.__Comienzo
        while aux!=None:
            dato=aux.getDato()
            dato.mostrardatos()
            aux=aux.getSiguiente()
        
    def ordenarporapellido(self):
        ant=self.__Comienzo
        T=False
        while T==False:
            T=True
            aux=self.__Comienzo
        
            aux2=self.__Comienzo.getSiguiente()
            #print("LALA")
            while aux2!=None:
                if aux2!=None:
                    dato=aux.getDato()
                    dato2=aux2.getDato()
                    nombre1=dato.getapellido()
                    nombre2=dato2.getapellido()
                    #print("LALA")
                    if nombre1>nombre2:
                        aux.setSiguiente(aux2.getSiguiente())
                        aux2.setSiguiente(aux)
                        T=False
                        if aux==self.__Comienzo:
                            self.__Comienzo=aux2
                            ant=self.__Comienzo        
                        else:
                            ant.setSiguiente(aux2)
                            ant=aux2
                    aux=aux2
                    aux2=aux.getSiguiente()
        self.mostrarElemento()
    def Buscartipoinves(self):
        importeT=0
        print("Apellido\n Nombre\n Importe")
        nombre=input("Ingrese categoria de investigacion: ")
        aux = self.__Comienzo
        while aux!=None:
            if type(aux.getDato()) == DocenteInves:
                dato=aux.getDato()
                if nombre == dato.getcategoria():
                    importeT=importeT+dato.getimportex()
                    print(f"{dato.getname()}\n {dato.getapellido()}\n {dato.getimportex()}")
            aux=aux.getSiguiente()
        print(f"Dinero que la Secretaría de Investigación debe solicitar al Ministerio: {importeT}")

    def CargadeArchivos(self):
        data = {}
        data['personal'] = []
        aux = self.__Comienzo
        dato=aux.getDato()
        while aux!=None:
            if type(aux.getDato())==Investigadores:
                data['personal'].append(
                    {
                    "Cuil":dato.getcuil(),
                    "Apellido":dato.getapellido(),
                    "Nombre":dato.getname(),
                    "Sueldo_basico":dato.getsueldo(),
                    "Antiguedad":dato.getantiguedad(),
                    "area_de_investigacion":dato.getarea(),
                    "tipo_de_investigacion":dato.gettipo()
                    })
            if type(aux.getDato()) == Docente :
                data['personal'].append(
                    {
                    "Cuil":dato.getcuil(),
                    "Apellido":dato.getapellido(),
                    "Nombre":dato.getname(),
                    "Sueldo_basico":dato.getsueldo(),
                    "Antiguedad":dato.getantiguedad(),
                    "Catedra":dato.getcatedra(),
                    "Clases":dato.getcarrera(),
                    "Cargo":dato.getcargo()
                    })
            if type(aux.getDato())==DocenteInves:
                data['personal'].append(
                    {
                    "Cuil":dato.getcuil(),
                    "Apellido":dato.getapellido(),
                    "Nombre":dato.getname(),
                    "Sueldo_basico":dato.getsueldo(),
                    "Antiguedad":dato.getantiguedad(),
                    "Clases":dato.getcarreraD(),
                    "Cargo":dato.getcargo(),
                    "Catedra":dato.getcatedra(),
                    "area_de_investigacion":dato.getarea(),
                    "tipo_de_investigacion":dato.gettipo(),
                    "categoria_programa_investi":dato.getcategoria(),
                    "Importex":dato.getimportex()
                    })
            if type(aux.getDato())==PersonalApoyo:
                 data['personal'].append(
                    {
                    "Cuil":dato.getcuil(),
                    "Apellido":dato.getapellido(),
                    "Nombre":dato.getname(),
                    "Sueldo_basico":dato.getsueldo(),
                    "Antiguedad":dato.getantiguedad(),
                    "Categoria":dato.getcategoria()
                    })
            aux=aux.getSiguiente()
            if aux != None:
                dato=aux.getDato()
        with open('personal.json', 'w') as file:
            json.dump(data, file, indent=4)
        file.close()