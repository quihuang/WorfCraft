import re
import os
from datetime import datetime

def validationUser (user):

    lengthUser = user.__len__()
    validate = False

    if lengthUser == 10 : 
        containsNumber = bool(re.search(r'\d', user))
        if (containsNumber == False):
            if user[5] == "@" :
                if user[0] != user[9]:
                    contMas = user.count("+")
                    if contMas == 1 :
                        contK = user.upper().count("K")
                        if contK < 4 :
                            countIdea = user.count("?")
                            countIgual = user.count("=")
                            countAmpersan = user.count("&")
                            if countIdea == 1 or countIgual == 1 or countAmpersan == 1 :
                               validate = True
                               return validate
                            else :
                                return validate   
                        else :
                             return validate
                    else:
                        return validate
                else:
                    return validate
            else:
                return validate
        else:
            return validate
    else:
        return validate

def searchUserExist(user):
    userExistDB = ["juand@vv+=","david@v?+k","frank@k?+k"]
    validateExist = False
    for userDB in userExistDB:
        if userDB.upper() == user.upper():
            validateExist = True
            break

    return validateExist

opcion = 0

def validarNivel(nivel):
    nivelValitdate = False
    if nivel > 0 and nivel < 101 :
        nivelValitdate = True

    return nivelValitdate

def assignmentOfWorld(played,age,level):
    mundo = 0

    if age > 12 and age <= 20 and played.upper() == "NO" :
        mundo = 1
    elif age > 12 and age <= 20 and played.upper() == "SI" and level < 50 :
        mundo = 2
    elif age > 12 and age <= 20 and played.upper() == "SI" and level >= 50 :
        mundo = 3
    elif age > 20 and played.upper() == "NO" :
        mundo = 4
    elif age > 20 and played.upper() == "SI" and level < 50:
        mundo = 5
    elif age > 20 and played.upper() == "SI" and level >= 50:
        mundo = 6

    return mundo

while(opcion != 2) :
    print("\n-------------------------------------")
    print("   Bienvenido a WorldCraft ASCII     ")
    print("-------------------------------------")
    print("1. Registrarse")
    print("2. Salir")

    opcion = int( input("\nIngrese una opción : ") )

    messageError = "\nCDIA inválido"
    messageExit = "\nSaliendo del programa"
    messageInvalidata = "\nLa Opción ingresada es invalida"
    messageUserExist = "\nEl CDIA que ingreso ya esta siendo utilizado"
    messageAgeNotaAllowed = "\nDebes ser mayor de 12 años"
    messageValIncorrecto = "\nEl valor ingresado no cumple con las caracteristicas requeridas"

    if opcion == 1:

        userVerification = False

        while userVerification != True:

            print("\n=================================================================")
            print("Requisitos para tu CDIA : ")
            print("° el CDIA debe ser de 10 letras")
            print("° Solo se permiten letras")
            print("° debe ir siempre el carácter arroba (‘@’) en la posición 6")
            print("° La primera letra no debe coincider con la ultima")
            print("° debe tener por lo menos una vez los carácteres (‘+’,‘?’,‘=’,‘&’)")
            print("° no puede tener mas de 3 veces carácter (‘K’)")
            print("=================================================================")
            
            user = input("\nCree su CDIA : ")
            userVerification = validationUser(user)

            if userVerification :
                validateUserExist = searchUserExist(user)
                if (validateUserExist != True):
                    print("\n-----------------------------------")
                    print("           CDIA CORRECTO             ")
                    print("-------------------------------------")
                    dateOfBirthTemp = input("Digite su fecha de nacimiento en el formato DD/MM/AAAA : ")
                    dateOfBirth = datetime.strptime(dateOfBirthTemp, '%d/%m/%Y')
                    currentDate = datetime.now()
                    age = currentDate.year - dateOfBirth.year
                    if age > 12 :
                         alias = input("\nIngrese un Alias maximo de 5 caracteres sin espacios : ")
                         count = alias.count(" ")
                         len = alias.__len__()
                         if  count == 0 and len < 6 :
                             yesPlay = ""
                             while yesPlay.upper() != "SI" and yesPlay.upper() != "NO":
                                 yesPlay = input("\n¿Ya has jugado WorldCraft ASCII? (Si, No) : ")
                                 if yesPlay.upper() == "SI":
                                     level = int(input("\n¿Hasta que nivel llegaste? (el nivel va desde 1 hasta 100) : "))
                                     nivelValitdate = validarNivel(level)
                                     if nivelValitdate == True:
                                         if age < 16 :
                                            levelUser = level
                                            print(f"\nCDIA : {user} \nAlias: {alias} \nEdad : {age} \nNivel : {levelUser}")
                                         elif age >= 16 :
                                            levelUser = level+2
                                            print(f"\nCDIA : {user} \nAlias: {alias} \nEdad : {age} \nNivel : {levelUser}")
                                     else:
                                         print(messageValIncorrecto)
                                 elif yesPlay.upper() == "NO":
                                     if  age < 16 :
                                        levelUser = 2  
                                        print(f"\nCDIA : {user} \nAlias: {alias} \nEdad : {age} \nNivel : {levelUser}")
                                     elif age >= 16 :
                                        levelUser = 1
                                        print(f"\nCDIA : {user} \nAlias: {alias} \nEdad : {age} \nNivel : {levelUser}")
                                 else: print(messageValIncorrecto)   

                                 mundoAsig = assignmentOfWorld(yesPlay,age,levelUser)  

                                 print(f"\nJugador se te ha asignado el mundo # {mundoAsig}")
                         else:
                             print(messageValIncorrecto)
                    else:
                        print(messageAgeNotaAllowed)
                else:
                    print(messageUserExist)    
            else:
                print(messageError)

    elif opcion == 2:
        os.system("clear")
        print(messageExit)
    else:
        os.system("clear")
        print(messageInvalidata)
