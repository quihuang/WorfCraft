import re
from datetime import datetime

 #1144213155 - 94417272 - 0332423123
 # 2022-05-21 22:22


def buscar_CDIA(CDIA):
    #Lista de usuarios CDIA
    lista = ["juand@vv+=","david@v?+k","prueba"]

texto = "juknkzm1+j"

#Obtener la cantidad de elementos de un texto
x = texto.__len__()

#Convertir a mayusculas
texto = texto.upper()

print("Cantidad de elementos: ", x)

print(texto[0])
print(texto[1])
print(texto[2])
print(texto[3])
print(texto[4])
#print(texto[9])
print("---------------------------")

for x in texto:
    print(x)

#Busco si existe un numero en el texto
contieneNumero = bool(re.search(r'\d', texto))
print( contieneNumero )

if texto[5] == "@" :
    print("Valida")
else:
    print("no Valido")

contieneMas = bool(re.search(r'\+', texto))
print(contieneMas)

conteoMas = texto.count("+")
print(conteoMas)

conteoK = texto.count("K")
print(conteoK)

contieneMas = bool(re.search(r'\?', texto)) or bool(re.search(r'\=', texto)) or bool(re.search(r'\&', texto))
print(contieneMas)

#Pedir la fecha de nacimiento
fecha_nacimiento_temp = input("Digite su fecha de nacimiento en el formato DD/MM/AAAA: ")
fecha_nacimiento = datetime.strptime(fecha_nacimiento_temp, '%d-%m-%Y')
print(fecha_nacimiento)

fecha_actual = datetime.now()
print(fecha_actual)

edad = fecha_actual.year - fecha_nacimiento.year
print(edad)



[
    {
     "Tipo Documento":"CC",
     "Numero Documento":"1144213155",
     "Nombres":"Franklin German",
     "Apellidos":"Quihuang Garzon",
     "Fecha de nacimiento":"1999-12-08",
     "RH":"O+",
     "Correo":"quihuang2017@gmail.com",
     "Numero de telefono":"3205282231"
    },
    {
     "Tipo Documento":"TI",
     "Numero Documento":"94417272",
     "Nombres":"Pepito",
     "Apellidos":"Perez",
     "Fecha de nacimiento":"2011-02-02",
     "RH":"O+",
     "Correo":"pepitopez@hotmail.es",
     "Numero de telefono":"454323234"
    },
    {
     "Tipo Documento":"PA",
     "Numero Documento":"0332423123",
     "Nombres":"Victor Alfonso",
     "Apellidos":"Zapata Ocampo",
     "Fecha de nacimiento":"2002-08-30",
     "RH":"A+",
     "Correo":"victor@gmail.com",
     "Numero de telefono":"123434254"
    }
]