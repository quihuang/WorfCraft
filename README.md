# **PROYECTO WORLD CRAFT ASCII : PARTE 1**

## **Contexto**

implementar un programa que permita veriﬁcar los datos de un
aspirante a jugador del juego y asignarle un nivel de inicio.

## **Identificación del problema**

**Objetivo**

Realizar una veriﬁcación para evaluar la posibilidad de que una persona pueda ingresar como nuevo jugador del WorldCraft ASCII, para ello se solicita el CDIA (código de identiﬁcación ASCII) del aspirante. 

una vez validado se debe asignar un mundo al jugador dependiendo de su edad, si a jugado antes y su nivel.

**Interesados**

Jugadores - Usuario.

**Restriciones**

Este CDIA es una cadena de 10 caracteres que debe cumplir con las siguientes restricciones y las cuales deben ser validadas por el programa una vez se ingresa:

* Se debe veriﬁcar que el CDIA sea de tipo str exclusivamente y sin dígitos numéricos.
* En la posición 6 de la cadena del CDIA debe ir siempre el
carácter arroba (‘@’)
* El carácter en la primera posición y el carácter en la última posición del CDIA deben ser diferentes.
* El CDIA debe contener en cualquier posición de la cadena el
carácter arroba (‘+’)
* El código CDIA no debe contener más de 3 veces la letra ’k’
* El CDIA debe tener al menos uno de los siguientes símbolos
(‘?’,’=’,’&’)

Si el CDIA no cumple con alguna de estas reglas se debe presentar el mensaje “CDIA inválido”

Una vez se ha validado que efectivamente el código CDIA no
corresponde con el de otro jugador ya inscrito, se le deben hacer las siguientes preguntas:

* caracteres del código CDIA que sean letras minúsculas a
mayúsculas.
A continuación, se presenta un ejemplo del uso de la función de
búsqueda de un CDIA.
* Fecha de Nacimiento (en formato DD/MM/AAAA)
 *  (la edad del jugador debe ser mayor a 12 años y debes  
calcularla)
* Si la edad es correcta debes preguntar los siguientes datos
 * Alias del jugador (Una cadena de caracteres de una
longitud mínima de 5 y sin espacios)
 * ¿Ya has jugado WorldCraft ASCII? (Si, No)
 * Si ya ha jugado antes debe preguntarle:
     ¿Hasta que nivel llegaste?  (el nivel va desde 1 hasta 100)
Si la edad del jugador es menor a 16 y no ha jugado antes debe ser
enviado el nivel 2 del juego, si ya ha jugado debe ser enviado al
mismo nivel que tenía.


## **Definir el problema**

**Información que conozco**

Para que el programa pueda funcionar se requieren los siguientes parametros :

* CDIA
* Edad
* Si a jugado o no
* Alias
* nivel (en caso de haber jugado)

Tambien se requieren datos de ejecución :

* Fecha de nacimiento en formato (DD/MM/AAAA) ingresado por el usuario
* Fecha actual (Calculada por el sistema)

Contamos con los requisitos expecificos para el desarrollo de las condiciones y asignaciones del mundo para cada jugador.

Cuando un nuevo jugador es admitido al WorldCraft ASCII se le debe asignar un Mundo para iniciar a jugar de acuerdo a las siguientes reglas:
* Mundo 1: jugadores entre 12 y 20 años que no han jugado antes.
* Mundo 2: jugadores entre 12 y 20 años que ya han jugado antes
y su nivel actual es menor a 50.
* Mundo 3: jugadores entre 12 y 20 años que ya han jugado antes
y su nivel actual es mayor o igual a 50.
* Mundo 4: jugadores mayores a 20 años que no han jugado antes
* Mundo 5: jugadores mayores a 20 años que ya han jugado antes
y su nivel actual es menor a 50.
* Mundo 5: jugadores mayores a 20 años que ya han jugado antes y su nivel actual es mayor o igual a 50.
 
El programa debe tener una función que reciba la edad (ya
calculada) del nuevo jugador, la respuesta si ha jugado antes y su nivel, con estos datos debe retornar el mundo que le corresponde al
jugador. 

## **Explorar**

Se realizara un programa en python donde como estrategia se implementaran los conocimientos obtenidos en clases junto a buenas practicas aprendidas a lo largo del programa.


## **Actuar**

Se realiza la logica del programa analizando el problema y ejecutando el paso a paso del metodo ideal para poder saber con claridad lo que se desarrollo.

se aplican conocimientos de condicionales, ciclos ,operadores, funciones y librerias.

## **Lograr**

Se desarrolla el reto de manera exitosa cumpliento con los requerimientos del mismo.
