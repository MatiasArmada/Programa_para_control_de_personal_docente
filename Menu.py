from Lista import Lista

def menu():
    print("1 -->  Agregar agentes a la colección")
    print("2 -->  Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición")
    print("3 -->  Cantidad de agentes que son docente investigador, y la cantidad de investigadores")
    print("4 -->  Listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.")
    print("5 -->  Solicitar importe extra que cobran los docentes investigadores.")
    print("6 -->  Guardar datos en un archivo nuevo")
    print("7 -->  Ver los datos guardados")

if __name__=='__main__':
    L=Lista()
    L.CargarLista()
    T=True
    while T==True:
        
        menu()
        opcion=int(input("\nElija una opcion: "))
        if opcion == 1:
            print("1 Docente\n2 Personal de apoyo\n3 Investigadores\n4 Docente investigador")
            O=int(input("Ingrese una opcion: "))
            L.agregaragente(O)
           
            
        if opcion == 2:
            O=int(input("Ingrese indice a buscar: "))
            L.Buscarporindice(O)
        
        if opcion == 3:
            
            L.Buscararea()
        
        if opcion == 4:
            L.ordenarporapellido()
        if opcion == 5:
            L.Buscartipoinves()
        if opcion == 6:
            L.CargadeArchivos()
        if opcion == 7:
            L.mostrardatos()
        if opcion == 0:
            T=False

    
    