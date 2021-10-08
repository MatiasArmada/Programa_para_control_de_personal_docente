import json
data = {}
data['personal']= []

data['personal'].append(
    {
     "Cuil": "456654",
     "Apellido": "Julius",
     "Nombre": "Marta",
     "Sueldo_basico": 5000,
     "Antiguedad": 3,
     "Clases": "POO",
     "Cargo": "Docente",
     "Catedra": "Programacion"
    })
data['personal'].append({
     "Cuil": "456654",
     "Apellido": "Selor",
     "Nombre": "Maria",
     "Sueldo_basico": 5000,
     "Antiguedad": 3,
     "Clases": "POO",
     "Cargo": "Docente investigador",
     "Catedra": "Programacion",
     "area_de_investigacion":"Migracion de datos",
     "tipo_de_investigacion":"Educacional",
     "categoria_programa_investi":"III",
     "Importex":200
    })
data['personal'].append({
      "Cuil": "456654",
     "Apellido": "Bogado",
     "Nombre": "Andrea",
     "Sueldo_basico": 5000,
     "Antiguedad": 3,
     "Categoria": "10"
    })




with open('personal.json', 'w') as file:
    json.dump(data, file, indent=4)
file.close()