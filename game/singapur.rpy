# abs = Abstracción
# des = Descomposición
# recP = Reconocimiento de patrones
# disAl = Diseño de algoritmos

#* ############################# MULTIPLICACIÓN ###############################
#* Problema 1 de suma 

menu abs_suma_1:
    "¿Cuál es el tema principal del problema?"
    "La cantidad de tropas enemigas":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_suma_1
    "El tiempo que duró la lucha":
        play sound "acierto.mp3"
        "Correcto, el tema principal es el tiempo que duró la lucha."
        jump des_suma_1
    "La fecha de la sublevación":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_suma_1
    "La distancia recorrida por Juan Cupul":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_suma_1

menu des_suma_1:
    "¿Qué datos nos proporciona el problema?"
    "Hora de inicio y duración de la lucha":
        play sound "acierto.mp3"
        "Correcto, los datos proporcionados son la hora de inicio y la duración de la lucha."
        jump recP_suma_1
    "El número de enemigos derrotados":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_suma_1
    "La estrategia utilizada en la lucha":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_suma_1
    "La cantidad de armas utilizadas":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_suma_1

menu recP_suma_1:
    "¿Qué operación necesitamos realizar para encontrar la hora en que terminó la lucha?"
    "Multiplicación":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos añadiendo tiempo a una hora inicial."
        jump recP_suma_1
    "División":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos añadiendo tiempo a una hora inicial."
        jump recP_suma_1
    "Suma":
        play sound "acierto.mp3"
        "Correcto, necesitamos sumar la duración de la lucha a la hora de inicio."
        jump disAl_suma_1
    "Resta":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos añadiendo tiempo a una hora inicial."
        jump recP_suma_1

menu disAl_suma_1:
    "Si la lucha comenzó a las 9:45 AM y duró 2 horas con 20 minutos, ¿cuál es el procedimiento para saber a qué hora terminó?"
    "Sumar la hora de inicio (9:45) con el tiempo que duró la lucha (2:20 horas) y el resultado es 12:05 PM":
        play sound "acierto.mp3"
        "Correcto, sumar 2 horas con 20 minutos a las 9:45 AM da como resultado 12:05 PM."
        jump problema_suma_1
    "Multiplicar la duración de la lucha (2:20 horas) por la hora de inicio (9:45) y el resultado es 11:05 AM":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa nuevamente las operaciones necesarias para sumar tiempo a una hora inicial."
        jump disAl_suma_1
    "Restar la duración de la lucha (2:20 horas) de la hora de inicio (9:45) y el resultado es 7:25 AM":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa nuevamente las operaciones necesarias para sumar tiempo a una hora inicial."
        jump disAl_suma_1
    "Dividir la duración de la lucha (2:20 horas) entre la hora de inicio (9:45) y el resultado es 4:11 PM":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa nuevamente las operaciones necesarias para sumar tiempo a una hora inicial."
        jump disAl_suma_1

#* Problema 2 de suma 
menu abs_suma_2:
    "¿Cuál es el tema principal del problema?"
    "El tiempo total que Juan pasó leyendo mensajes":
        play sound "acierto.mp3"
        "Correcto, el tema principal es el tiempo total que Juan pasó leyendo mensajes."
        jump des_suma_2
    "La urgencia de los mensajes recibidos":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_suma_2
    "La ubicación de la ranchería Poop":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_suma_2
    "La misión de Juan Cupul":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_suma_2

menu des_suma_2:
    "¿Qué datos nos proporciona el problema?"
    "El contenido de los mensajes":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_suma_2
    "La urgencia de cada mensaje":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_suma_2
    "La importancia de la misión de Juan":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_suma_2
    "El tiempo que tomó leer cada mensaje":
        play sound "acierto.mp3"
        "Correcto, los datos proporcionados son el tiempo que tomó leer cada mensaje."
        jump recP_suma_2

menu recP_suma_2:
    "¿Qué operación necesitamos realizar para encontrar el tiempo total que Juan pasó leyendo?"
    "Multiplicación":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos sumando tiempos individuales."
        jump recP_suma_2
    "División":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos sumando tiempos individuales."
        jump recP_suma_2
    "Suma":
        play sound "acierto.mp3"
        "Correcto, necesitamos sumar los tiempos de lectura de los tres mensajes."
        jump disAl_suma_2
    "Resta":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos sumando tiempos individuales."
        jump recP_suma_2

menu disAl_suma_2:
    "Si Juan leyó el primer mensaje en 20 minutos, el segundo en 15 minutos y el 
    tercero en 30 minutos, ¿cuál es el procedimiento para saber el tiempo total de 
    lectura?"
    "Sumar los tiempos de lectura: 20 minutos + 15 minutos + 30 minutos, que da como resultado 1 hora y 5 minutos":
        play sound "acierto.mp3"
        "Correcto, sumar 20 minutos, 15 minutos y 30 minutos da como resultado 1 hora y 5 minutos."
        jump problema_suma_2
    "Multiplicar los tiempos de lectura de los tres mensajes, que da como resultado 1 hora":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa nuevamente las operaciones necesarias para sumar tiempos."
        jump disAl_suma_2
    "Restar el tiempo del primer mensaje del tiempo del tercer mensaje, que da como resultado 45 minutos":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa nuevamente las operaciones necesarias para sumar tiempos."
        jump disAl_suma_2
    "Dividir el tiempo total de lectura entre el número de mensajes, que da como resultado 1 hora y 15 minutos":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa nuevamente las operaciones necesarias para sumar tiempos."
        jump disAl_suma_2

menu abs_suma_5:
    "¿Cuál es el tema principal del problema?"
    "Los tipos de alimentos recolectados por Juan Cupul":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_suma_5
    "La cantidad total de kilogramos de provisiones recolectadas por Juan Cupul":
        play sound "acierto.mp3"
        "Correcto, el tema principal es la cantidad total de kilogramos de provisiones recolectadas por Juan Cupul."
        jump des_suma_5
    "La ubicación de Tixcacalcupul":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_suma_5
    "La hora de recolección de provisiones":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_suma_5

menu des_suma_5:
    "¿Qué datos nos proporciona el problema?"
    "El clima durante la recolección de provisiones":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_suma_5
    "La cantidad de días que Juan Cupul recolectó provisiones":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_suma_5
    "La cantidad de personas en Tixcacalcupul":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_suma_5
    "La cantidad de kilogramos de maíz y la cantidad de kilogramos de frijoles recolectados":
        play sound "acierto.mp3"
        "Correcto, los datos proporcionados son la cantidad de kilogramos de maíz y la cantidad de kilogramos de frijoles recolectados."
        jump recP_suma_5

menu recP_suma_5:
    "¿Qué operación necesitamos realizar para encontrar la cantidad total de kilogramos de provisiones recolectadas por Juan Cupul?"
    "Suma":
        play sound "acierto.mp3"
        "Correcto, necesitamos sumar los kilogramos de maíz y los kilogramos de frijoles recolectados."
        jump disAl_suma_5
    "División":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en la operación que nos permita obtener la suma total de kilogramos de provisiones recolectadas."
        jump recP_suma_5
    "Multiplicación":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en la operación que nos permita obtener la suma total de kilogramos de provisiones recolectadas."
        jump recP_suma_5
    "Resta":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en la operación que nos permita obtener la suma total de kilogramos de provisiones recolectadas."
        jump recP_suma_5

menu disAl_suma_5:
    "Si Juan Cupul recolectó 175 kg de maíz y 230 kg de frijoles, ¿cuál es el procedimiento para calcular la cantidad total de kilogramos de provisiones recolectadas?"
    "Multiplicar 175 por 230 kg para obtener 40,250 kg en total":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa nuevamente el proceso de suma para obtener la cantidad total de kilogramos de provisiones recolectadas por Juan Cupul"
        jump disAl_suma_5
    "Restar 175 kg de 230 kg para obtener 55 kg en total":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa nuevamente el proceso de suma para obtener la cantidad total de kilogramos de provisiones recolectadas por Juan Cupul"
        jump disAl_suma_5
    "Sumar 175 y 230 kg para obtener 405 kg en total":
        play sound "acierto.mp3"
        "Correcto, sumar 175 kg y 230 kg da como resultado 405 kg en total."
        jump problema_suma_5
    "Dividir 175 kg entre 230 kg para obtener 0.76 kg en total":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa nuevamente el proceso de suma para obtener la cantidad total de kilogramos de provisiones recolectadas por Juan Cupul"
        jump disAl_suma_5

#* Problema de suma 6
menu abs_suma_6:
    "¿Cuál es el tema principal del problema?"
    "La ubicación de la sublevación":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_suma_6
    "La cantidad total de caballos de Juan Cupul":
        play sound "acierto.mp3"
        "Correcto, el tema principal es la cantidad total de caballos de Juan Cupul."
        
        jump des_suma_6
    "La estrategia de Juan Cupul en la batalla":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_suma_6
    "El número de enemigos enfrentados por Juan Cupul":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_suma_6

menu des_suma_6:
    "¿Qué datos nos proporciona el problema?"
    "El número inicial de caballos, el número de caballos perdidos y el número de caballos ganados":
        play sound "acierto.mp3"
        "Correcto, los datos proporcionados son el número inicial de caballos, el número de caballos perdidos y el número de caballos ganados."
        
        jump recP_suma_6
    "La edad de Juan Cupul":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_suma_6
    "El clima durante la sublevación":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_suma_6
    "El tipo de armas utilizadas por Juan Cupul":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_suma_6

menu recP_suma_6:
    "¿Qué operación necesitamos realizar para encontrar la cantidad total de caballos de Juan Cupul al final?"
    "Multiplicación":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en la operación que nos permita obtener la cantidad total de caballos de Juan Cupul al final."
        jump recP_suma_6
    "División":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en la operación que nos permita obtener la cantidad total de caballos de Juan Cupul al final."
        jump recP_suma_6
    "Suma":
        play sound "acierto.mp3"
        "Correcto, necesitamos sumar los caballos iniciales, los caballos perdidos y los caballos ganados."
        jump disAl_suma_6
    "Resta":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en la operación que nos permita obtener la cantidad total de caballos de Juan Cupul al final."
        jump recP_suma_6

menu disAl_suma_6:
    "Si Juan Cupul tenía 25 caballos al comienzo, perdió 8 caballos y ganó 13 más, ¿cuál es el procedimiento para calcular la cantidad total de caballos al final?"
    "Dividir 25 caballos entre 8 y 13 caballos para obtener 0.96 caballos en total":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa nuevamente el proceso de suma para obtener la cantidad total de caballos de Juan Cupul al final."
        jump disAl_suma_6
    "Restar 25 caballos de 8 y 13 caballos para obtener 4 caballos en total":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa nuevamente el proceso de suma para obtener la cantidad total de caballos de Juan Cupul al final."
        jump disAl_suma_6
    "Multiplicar 25 por 8 y 13 caballos para obtener 3,375 caballos en total":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa nuevamente el proceso de suma para obtener la cantidad total de caballos de Juan Cupul al final."
        jump disAl_suma_6
    "Sumar 25 y 13 caballos, y al resultado restarle los 8 perdidos para obtener 30 caballos en total":
        play sound "acierto.mp3"
        "Correcto, sumar 25 caballos, 8 caballos perdidos y 13 caballos ganados da como resultado 46 caballos en total."
        jump problema_suma_6


#* ############################# MULTIPLICACIÓN ###############################
#* Problema de multiplicación 1

menu abs_mult_1:
    "¿Cuál es el tema principal del problema?"
    "Los kilómetros que recorrió Juan Cupul hasta Tixcacalcupul":
        play sound "acierto.mp3"
        "Correcto, el tema principal es sobre los kilómetros que recorrió Juan Cupul hasta Tixcancalcupul."
        jump des_mult_1
    "Las horas que tardó en recorrer Juan Cupul":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_mult_1
    "El camino hasta llegar a Tixcacalcupul":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_mult_1
    "El destino del viaje que hizo Juan Cupul":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_mult_1

menu des_mult_1:
    "¿Qué datos nos proporciona el problema?"
    "La velocidad en km en los que se desplaza Juan Cupul y el total de horas que tardó":
        play sound "acierto.mp3"
        "Correcto, los datos proporcionados son la velocidad en km en los que se desplaza Juan Cupul y el total de horas que tardó."
        jump recP_mult_1
    "El total de cambio recorrido":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_mult_1
    "Las horas totales de viaje":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_mult_1
    "Los años que tardó en llegar hasta Tixcancalcupul":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_mult_1

menu recP_mult_1:
    "¿Qué operación necesitamos realizar para encontrar la hora en que terminó la lucha?"
    "Multiplicación":
        play sound "acierto.mp3"
        "Correcto, necesitamos multiplicar la velocidad a la que va por la cantidad de horas que tardó en llegar."
        jump disAl_mult_1
    "División":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que necesitamos multiplicar la velocidad a la que va por la cantidad de horas que tardó en llegar."
        jump recP_mult_1
    "Suma":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que necesitamos multiplicar la velocidad a la que va por la cantidad de horas que tardó en llegar."
        jump recP_mult_1
    "Resta":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que necesitamos multiplicar la velocidad a la que va por la cantidad de horas que tardó en llegar."
        jump recP_mult_1

menu disAl_mult_1:
    "Si viajaba a 60 km/h y tardó 3 horas, ¿cuál es el procedimiento para saber los kilómetros que recorrió?"
    "Multiplicar los 60 km de 1 hora por las 3 horas que tardó en total, lo que da de resultado 180 km":
        play sound "acierto.mp3"
        "Correcto, Multiplicar los 60 km de 1 hora por las 3 horas que tardó en total, da de resultado 180 km."
        jump problema_multiplicacion_1
    "Sumar los 60 km más las 3 horas que tardó el viaje y el resultado es 63 km":
        play sound "error.mp3" volume 4.0
        "Incorrecto, intenta realizar otra vez la operación."
        jump disAl_mult_1
    "Restar las 3 horas del viaje a los 60 km que ya recorrió, y el resultado es 57 km":
        play sound "error.mp3" volume 4.0
        "Incorrecto, intenta realizar otra vez la operación."
        jump disAl_mult_1
    "Dividir los 60 km entre las 3 horas de viaje lo que da de resultado 20 km":
        play sound "error.mp3" volume 4.0
        "Incorrecto, intenta realizar otra vez la operación."
        jump disAl_mult_1

#* Problema de multiplicación 2
menu abs_mult_2:
    "¿Cuál es el tema principal del problema?"
    "La cantidad total de libros de las estanterías de la sección de historia":
        play sound "acierto.mp3"
        "Correcto, el tema principal es sobre la cantidad total de libros de las estanterías de la sección de historia."
        jump des_mult_2
    "Los libros de historia":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_mult_2
    "La historia de Juan Cupul":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_mult_2
    "Las estanterías de la biblioteca":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_mult_2

menu des_mult_2:
    "¿Qué datos nos proporciona el problema?"
    "El número total de estanterías y el total de libros por estantería":
        play sound "acierto.mp3"
        "Correcto, los datos proporcionados son el número total de estanterías y el total de libros por estantería."
        jump recP_mult_2
    "La cantidad total de libros de la sección de historia":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_mult_2
    "Los estantes que hay en la biblioteca":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_mult_2
    "Los libros que hay en cada estantería":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_mult_2

menu recP_mult_2:
    "¿Qué operación necesitamos realizar para encontrar el número total de libros?"
    "Suma":
        play sound "error.mp3" volume 4.0
        "Incorrecto, necesitamos multiplicar el número total de estanterías por el total de libros por estantería."
        jump recP_mult_2
    "División":
        play sound "error.mp3" volume 4.0
        "Incorrecto, necesitamos multiplicar el número total de estanterías por el total de libros por estantería."
        jump recP_mult_2
    "Multiplicación":
        play sound "acierto.mp3"
        "Correcto, necesitamos multiplicar el número total de estanterías por el total de libros por estantería."
        jump disAl_mult_2
    "Resta":
        play sound "error.mp3" volume 4.0
        "Incorrecto, necesitamos multiplicar el número total de estanterías por el total de libros por estantería."
        jump recP_mult_2

menu disAl_mult_2:
    "Si el número total de estanterías es 4 y el total de libros por estantería es de 36, ¿cuál es el procedimiento para calcular el número total de libros?"
    "Multiplicar el número de estanterías (4) por el total de libros por estantería (36), y el resultado es 144 libros":
        play sound "acierto.mp3"
        "Correcto, Multiplicar el número de estanterías (4) por el total de libros por estantería (36), y el resultado es 144 libros."
        jump problema_multiplicacion_2
    "Sumar las 4 estanterías más los 36 libros, que da como resultado 40 libros":
        jump disAl_mult_2
        play sound "error.mp3" volume 4.0
        "Incorrecto, intenta realizar otra vez la operación."
    "Restar a los 36 libros de una estantería el número total de 4 estanterías, lo que da resultado 32 libros":
        jump disAl_mult_2
        play sound "error.mp3" volume 4.0
        "Incorrecto, intenta realizar otra vez la operación."
    "Dividir los 36 libros entre las 4 estanterías, lo que da de resultado 9 libros":
        jump disAl_mult_2
        play sound "error.mp3" volume 4.0
        "Incorrecto, intenta realizar otra vez la operación."


#* Problema de multiplicación 3
menu abs_mult_3:
    "¿Cuál es el tema principal del problema?"
    "El total de zanahorias en la huerta de Antonio":
        play sound "acierto.mp3"
        "Correcto, el tema principal es sobre el total de zanahorias en la huerta de Antonio."
        jump des_mult_3
    "La cantidad de horas que trabajó Antonio":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_mult_3
    "La cosecha de zanahorias":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_mult_3
    "El área de la huerta":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_mult_3

menu des_mult_3:
    "¿Qué datos nos proporciona el problema?"
    "La cantidad de zanahorias por hilera y el total de hileras en la huerta":
        play sound "acierto.mp3"
        "Correcto, los datos proporcionados son la cantidad de zanahorias por hilera y el total de hileras en la huerta."
        jump recP_mult_3
    "La cantidad total de zanahorias":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_mult_3
    "El total de hileras en la huerta":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_mult_3
    "El área de la huerta de Antonio":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_mult_3

menu recP_mult_3:
    "¿Qué operación necesitamos realizar para calcular el total de zanahorias?"
    "Suma":
        play sound "error.mp3" volume 4.0
        "Incorrecto, necesitamos multiplicar el número total de hileras por la cantidad de zanahorias por hilera."
        jump recP_mult_3
    "División":
        play sound "error.mp3" volume 4.0
        "Incorrecto, necesitamos multiplicar el número total de hileras por la cantidad de zanahorias por hilera."
        jump recP_mult_3
    "Multiplicación":
        play sound "acierto.mp3"
        "Correcto, necesitamos multiplicar el número total de hileras por la cantidad de zanahorias por hilera."
        jump disAl_mult_3
    "Resta":
        play sound "error.mp3" volume 4.0
        "Incorrecto, necesitamos multiplicar el número total de hileras por la cantidad de zanahorias por hilera."
        jump recP_mult_3

menu disAl_mult_3:
    "Si hay 8 hileras y en cada hilera hay 25 zanahorias, ¿cuál es el procedimiento para calcular el número total de zanahorias?"
    "Multiplicar el número de hileras (8) por la cantidad de zanahorias por hilera (25), y el resultado es 200 zanahorias":
        play sound "acierto.mp3"
        "Correcto, Multiplicar el número de hileras (8) por la cantidad de zanahorias por hilera (25), y el resultado es 200 zanahorias."
        jump problema_multiplicacion_3
    "Sumar las 8 hileras a las 25 zanahorias, lo que da un total de 33 zanahorias":
        play sound "error.mp3" volume 4.0
        "Incorrecto, intenta realizar otra vez la operación."
        jump disAl_mult_3
    "Restar el número de zanahorias a las hileras y el resultado es 17 zanahorias":
        play sound "error.mp3" volume 4.0
        "Incorrecto, intenta realizar otra vez la operación."
        jump disAl_mult_3
    "Dividir las zanahorias entre las hileras lo que da de resultado 3.125 zanahorias":
        play sound "error.mp3" volume 4.0
        "Incorrecto, intenta realizar otra vez la operación."
        jump disAl_mult_3

#* Problema de multiplicación 4
menu abs_mult_4:
    "¿Cuál es el tema principal del problema?"
    "El número total de camisas fabricadas en la fábrica":
        play sound "acierto.mp3"
        "Correcto, el tema principal es sobre el número total de camisas fabricadas en la fábrica."
        jump des_mult_4
    "La fábrica de camisas":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_mult_4
    "La cantidad de días trabajados":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_mult_4
    "El número de fábricas":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_mult_4

menu des_mult_4:
    "¿Qué datos nos proporciona el problema?"
    "El número de camisas fabricadas por día y el total de días trabajados":
        play sound "acierto.mp3"
        "Correcto, los datos proporcionados son el número de camisas fabricadas por día y el total de días trabajados."
        jump recP_mult_4
    "El total de camisas fabricadas en la fábrica":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_mult_4
    "El número de fábricas y camisas":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_mult_4
    "El total de días que trabajaron":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_mult_4

menu recP_mult_4:
    "¿Qué operación necesitamos realizar para calcular el total de camisas fabricadas?"
    "Multiplicación":
        play sound "acierto.mp3"
        "Correcto, necesitamos multiplicar el número de camisas fabricadas por el total de días trabajados."
        jump disAl_mult_4
    "Suma":
        play sound "error.mp3" volume 4.0
        "Incorrecto, necesitamos multiplicar el número de camisas fabricadas por el total de días trabajados."
        jump recP_mult_4
    "División":
        play sound "error.mp3" volume 4.0
        "Incorrecto, necesitamos multiplicar el número de camisas fabricadas por el total de días trabajados."
        jump recP_mult_4
    "Resta":
        play sound "error.mp3" volume 4.0
        "Incorrecto, necesitamos multiplicar el número de camisas fabricadas por el total de días trabajados."
        jump recP_mult_4

menu disAl_mult_4:
    "Si en un día se fabricaron 50 camisas y trabajaron durante 5 días, ¿cuál es el procedimiento para calcular el número total de camisas?"
    "Multiplicar las 50 camisas fabricadas en un día por los 5 días trabajados, lo que da de resultado 250 camisas":
        play sound "acierto.mp3"
        "Correcto, Multiplicar las 50 camisas fabricadas en un día por los 5 días trabajados da de resultado 250 camisas."
        jump problema_multiplicacion_4
    "Sumar las camisas al número de días trabajados, lo que da de resultado 55 camisas":
        play sound "error.mp3" volume 4.0
        "Incorrecto, intenta realizar otra vez la operación."
        jump disAl_mult_4
    "Restar los días trabajados al número de camisas, lo que da de resultado 45 camisas":
        play sound "error.mp3" volume 4.0
        "Incorrecto, intenta realizar otra vez la operación."
        jump disAl_mult_4
    "Dividir las camisas entre los días trabajados lo que da de resultado 10 camisas":
        play sound "error.mp3" volume 4.0
        "Incorrecto, intenta realizar otra vez la operación."
        jump disAl_mult_4

#* Ejercicio multiplicación 5
menu abs_mult_5:
    "¿Cuál es el tema principal del problema?"
    "El número total de árboles plantados":
        play sound "acierto.mp3"
        "Correcto, el tema principal es sobre el número total de árboles plantados."
        jump des_mult_5
    "El terreno donde se plantaron los árboles":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_mult_5
    "El número de filas de árboles":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_mult_5
    "El tiempo que tardaron en plantar":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_mult_5

menu des_mult_5:
    "¿Qué datos nos proporciona el problema?"
    "El número de árboles por fila y el total de filas plantadas":
        play sound "acierto.mp3"
        "Correcto, los datos proporcionados son el número de árboles por fila y el total de filas plantadas."
        jump recP_mult_5
    "El total de árboles plantados":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_mult_5
    "El número total de filas":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_mult_5
    "El área del terreno plantado":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_mult_5

menu recP_mult_5:
    "¿Qué operación necesitamos realizar para calcular el número total de árboles plantados?"
    "Multiplicación":
        play sound "acierto.mp3"
        "Correcto, necesitamos multiplicar el número de árboles por fila por el total de filas plantadas."
        jump disAl_mult_5
    "Suma":
        play sound "error.mp3" volume 4.0
        "Incorrecto, necesitamos multiplicar el número de árboles por fila por el total de filas plantadas."
        jump recP_mult_5
    "División":
        play sound "error.mp3" volume 4.0
        "Incorrecto, necesitamos multiplicar el número de árboles por fila por el total de filas plantadas."
        jump recP_mult_5
    "Resta":
        play sound "error.mp3" volume 4.0
        "Incorrecto, necesitamos multiplicar el número de árboles por fila por el total de filas plantadas."
        jump recP_mult_5

menu disAl_mult_5:
    "Si se plantaron 30 árboles por fila y había 6 filas, ¿cuál es el procedimiento para calcular el número total de árboles?"
    "Multiplicar los 30 árboles por fila por las 6 filas plantadas, lo que da un total de 180 árboles plantados":
        play sound "acierto.mp3"
        "Correcto, Multiplicar los 30 árboles por fila por las 6 filas plantadas da un total de 180 árboles."
        jump problema_multiplicacion_5
    "Sumar los árboles a las filas, lo que da como resultado 36 árboles plantados":
        play sound "error.mp3" volume 4.0
        "Incorrecto, intenta realizar otra vez la operación."
        jump disAl_mult_5
    "Restar el número de filas a los árboles plantados lo que da de resultado 24 árboles plantados":
        play sound "error.mp3" volume 4.0
        "Incorrecto, intenta realizar otra vez la operación."
        jump disAl_mult_5
    "Dividir el número de árboles por fila entre el total de filas, lo que da de resultado 5 árboles plantados":
        play sound "error.mp3" volume 4.0
        "Incorrecto, intenta realizar otra vez la operación."
        jump disAl_mult_5

#* Problema de multiplicación 6
menu abs_multiplicacion_6:
    "¿Cuál es el tema principal del problema?"
    "La cantidad de flechas lanzadas por Juan Cupul y los otros 7 guerreros durante la batalla":
        play sound "acierto.mp3"
        jump des_multiplicacion_6
        "Correcto, el tema principal es sobre la cantidad de flechas lanzadas por Juan Cupul y otros 7 guerreros durante la batalla."
    "La cantidad de heridos en batalla":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa bien en lo que se está preguntando en el problema."
        jump abs_multiplicacion_6
    "Cantidad de armamento llevado al campo de batalla":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa bien en lo que se está preguntando en el problema."
        jump abs_multiplicacion_6
    "La cantidad de enemigos registrados ":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa bien en lo que se está preguntando en el problema."
        jump abs_multiplicacion_6

menu des_multiplicacion_6:
    "¿Qué datos nos proporciona el problema?"
    "La cantidad de personas que lanzaron flechas y la cantidad de flechas que lanzó cada uno":
        play sound "acierto.mp3"
        "Correcto, los datos proporcionados son: la cantidad de personas que lanzaron flechas y la cantidad de flechas que lanzó cada uno."
        jump recP_multiplicacion_6
    "La cantidad de guerreros enemigos  ":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_multiplicacion_6
    "El número total de flechas que se lanzaron durante la batalla":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_multiplicacion_6
    "La cantidad de flechas que sobraron después de la batalla":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_multiplicacion_6

menu recP_multiplicacion_6:
    "¿Qué operación necesitamos realizar para encontrar el número de aliados que invitó Juan Cupul para la reunión?"
    "Suma":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que necesitamos multiplicar el número total de guerreros contando a Juan Cupul por 15 flechas que lanzó cada uno."
        jump recP_multiplicacion_6
    "División":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que necesitamos multiplicar el número total de guerreros contando a Juan Cupul por 15 flechas que lanzó cada uno."
        jump recP_multiplicacion_6
    "Multiplicación":
        play sound "acierto.mp3"
        "Correcto, necesitamos multiplicar el número total de guerreros contando a Juan Cupul por 15 flechas que lanzó cada uno."
        jump disAl_multiplicacion_6
    "Resta":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que necesitamos multiplicar el número total de guerreros contando a Juan Cupul por 15 flechas que lanzó cada uno."
        jump recP_multiplicacion_6

menu disAl_multiplicacion_6:
    "Si el número de guerreros es 8 y la cantidad de flechas es de 15 ¿cuál es el procedimiento para calcular el total de flechas lanzadas durante la batalla?"
    "Multiplicar el número guerreros (8) por el total de flechas que lanzó cada uno (15), y el resultado es de 120 flechas":
        play sound "acierto.mp3"
        "Correcto, al multiplicar el número de mesas (4) por el total de sillas en cada mesa (8) obtenemos que el resultado es de 32 aliados invitados a la reunión."
        jump problema_multiplicacion_6
    "Sumar el total de guerreros (8) más las 15 flechas lanzadas, lo que da 23 flechas":
        play sound "error.mp3" volume 4.0
        "Incorrecto, intenta realizar otra vez la operación."
        jump disAl_multiplicacion_6
    "Restar a las 15 flechas el total de guerreros (8), lo que da de resultado 7 flechas":
        play sound "error.mp3" volume 4.0
        "Incorrecto, intenta realizar otra vez la operación."
        jump disAl_multiplicacion_6
    "Dividir las 15 flechas entre el total de guerreros (8), lo que da de resultado 1.875 flechas":
        play sound "error.mp3" volume 4.0
        "Incorrecto, intenta realizar otra vez la operación."
        jump disAl_multiplicacion_6


#* ################################ DIVISIÓN ##################################
#* Problema de división 1
menu abs_division_1:
    "¿Cuál es el tema principal del problema?"
    "La cantidad de machetes que Juan Cupul debe dar a cada campesino":
        play sound "acierto.mp3"
        "Correcto, el tema principal son los machetes que tienen que repartirse."
        jump des_division_1
    "Los machetes totales que Juan Cupul tiene.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_division_1
    "Los campesinos de la comunidad":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_division_1
    "El uso que le darán a los machetes":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_division_1

menu des_division_1:
    "¿Qué datos nos proporciona el problema?"
    "Los machetes que tiene Juan Cupul y el número de campesinos":
        play sound "acierto.mp3"
        "Correcto, los datos proporcionados son los machetes que tiene Juan Cupul y el número de campesinos."
        jump recP_division_1
    "El número de vecinos que tiene Juan Cupul":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_division_1
    "Cantidad de campesinos de todo el pueblo":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_division_1
    "La cantidad de machetes utilizados":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_division_1

menu recP_division_1:
    "¿Qué operación necesitamos realizar para encontrar la cantidad de machetes que Juan Cupul debe dar a cada campesino?"
    "División.":
        play sound "acierto.mp3"
        "Correcto, necesitamos dividir la cantidad de machetes entre el total de campesinos."
        jump disAl_division_1
    "Multiplicación.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos repartiendo los machetes entre los campesinos."
        jump recP_division_1
    "Suma.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos repartiendo los machetes entre los campesinos."
        jump recP_division_1
    "Resta.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos repartiendo los machetes entre los campesinos."
        jump recP_division_1

menu disAl_division_1:
    "Si el número total de machetes es 36 y se quiere repartir entre 6 campesinos de la comunidad, ¿cuál es el procedimiento para saber cuántos machetes le tocará a cada campesino?"
    "Dividir el total de machetes (36) entre el número de campesinos (6) y el resultado es 6.":
        play sound "acierto.mp3"
        "Correcto, dividir el total de machetes (36) entre los campesinos (6) da como resultado 6 machetes para cada campesino."
        jump 
    "Restar al total de machetes (36) el número de campesinos (6) y el resultado es 30.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, divide nuevamente los machetes entre los campesinos."
        jump disAl_division_1
    "Multiplicar los campesinos (6) por el total de machetes (36) y el resultado es 216.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, divide nuevamente los machetes entre los campesinos."
        jump disAl_division_1
    "Sumar los machetes (36) más el número de campesinos (6) y el resultado es 42.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, divide nuevamente los machetes entre los campesinos."
        jump disAl_division_1

#* Problema división 2
menu abs_division_2:
    "¿Cuál es el tema principal del problema?"
    "La cantidad de tomates que Juan Cupul deberá regalar a cada familia.":
        play sound "acierto.mp3"
        "Correcto, el tema principal son los tomates que le tocará a cada familia."
        jump des_division_2
    "Los vecinos que viven cerca de Juan Cupul.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_division_2
    "La cosecha de verduras de la comunidad.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_division_2
    "La cantidad de vecinos que no comen tomates.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_division_2

menu des_division_2:
    "¿Qué datos nos proporciona el problema?"
    "La cantidad total de tomates que se cosechó y el número de familias.":
        play sound "acierto.mp3"
        "Correcto, los datos proporcionados son el total de tomates que se cosechó y el número de familias."
        jump recP_division_2
    "Las verduras que Juan Cupul recolectó.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_division_2
    "El número de familias que consumen tomate.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_division_2
    "Cantidad de familias del pueblo.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_division_2

menu recP_division_2:
    "¿Qué operación necesitamos realizar para encontrar la cantidad de tomates que Juan Cupul debe dar a cada familia?"
    "División.":
        play sound "acierto.mp3"
        "Correcto, necesitamos dividir la cantidad de tomates entre el total de familias."
        jump disAl_division_2
    "Multiplicación.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos repartiendo los tomates entre las familias."
        jump recP_division_2
    "Suma.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos repartiendo los tomates entre las familias."
        jump recP_division_2
    "Resta.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos repartiendo los tomates entre las familias."
        jump recP_division_2

menu disAl_division_2:
    "Si el número total de tomates es de 72 kilos y se quiere repartir entre 9 familias de la comunidad, ¿cuál es el procedimiento para saber cuántos kilos de tomate le tocará a cada familia?"
    "Dividir el total de tomates (72) entre el número de familias (9) y el resultado es 8.":
        play sound "acierto.mp3"
        "Correcto, dividir 72 kilos de tomate entre las 9 familias da como resultado 8."
        jump 
    "Restar al total de tomates (72) el número de familias (9) y el resultado es 63.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, divide nuevamente los kilos de tomate entre las familias."
        jump disAl_division_2
    "Sumar los tomates (72) más el número de familias (9) y el resultado es 81.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, divide nuevamente los kilos de tomate entre las familias."
        jump disAl_division_2
    "Multiplicar las familias (9) por el total de tomates (72) y el resultado es 648.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, divide nuevamente los kilos de tomate entre las familias."
        jump disAl_division_2

#* Problema división 3
menu abs_division_3:
    "¿Cuál es el tema principal del problema?"
    "Cantidad de cubetas que se necesitan para repartir el agua que se tiene.":
        play sound "acierto.mp3"
        "Correcto, el tema principal son las cubetas que se necesitan para repartir el agua."
        jump des_division_3
    "Los problemas del servicio de agua.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_division_3
    "Cantidad de litros de agua de la comunidad.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_division_3
    "El agua que tienen las familias.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_division_3

menu des_division_3:
    "¿Qué datos nos proporciona el problema?"
    "La cantidad de agua que hay en el depósito y los litros que pondrá en cada cubeta.":
        play sound "acierto.mp3"
        "Correcto, los datos proporcionados son los litros de agua en el depósito y los que irán en cada cubeta."
        jump recP_division_3
    "La cantidad de agua que hay en el río.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_division_3
    "El número de cubetas que hay por casa.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_division_3
    "Cantidad de vecinos que no tienen agua y necesitan.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_division_3

menu recP_division_3:
    "¿Qué operación necesitamos realizar para encontrar la cantidad de cubetas que se necesitan?"
    "División.":
        play sound "acierto.mp3"
        "Correcto, necesitamos dividir la cantidad total de agua que hay en el depósito entre la cantidad de litros que se quiere en cada cubeta."
        jump disAl_division_3
    "Multiplicación.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos dividiendo el agua en cubetas de 8 litros cada una."
        jump recP_division_3
    "Suma.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos dividiendo el agua en cubetas de 8 litros cada una."
        jump recP_division_3
    "Resta.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos dividiendo el agua en cubetas de 8 litros cada una."
        jump recP_division_3

menu disAl_division_3:
    "Si el número total de litros de agua es 56 y se quiere repartir en cubetas con 8 litros en cada una, ¿cuál es el procedimiento para saber cuántas cubetas se necesitan para repartir toda el agua?"
    "Dividir los litros de agua del depósito (56) entre el número de litros que va en cada cubeta (8) y el resultado es 7.":
        play sound "acierto.mp3"
        "Correcto, dividir los litros de agua del depósito (56) entre el número de litros que va en cada cubeta (8) ayuda a saber que son 7 las cubetas que se necesitan para sacar toda el agua."
        jump disAl_division_3
    "Sumar los litros de agua del depósito (56) más el número de litros que va en cada cubeta (8) y el resultado es 63.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, divide nuevamente los litros de agua del depósito entre los que irían en cada cubeta."
        jump disAl_division_3
    "Restar a los litros de agua del depósito (56) los litros que van en cada cubeta (8) y el resultado es 48.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, divide nuevamente los litros de agua del depósito entre los que irían en cada cubeta."
        jump disAl_division_3
    "Multiplicar los litros de agua del depósito (56) por el número de litros que va en cada cubeta (8) y el resultado es 448.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, divide nuevamente los litros de agua del depósito entre los que irían en cada cubeta."
        jump disAl_division_3

#* Problema división 4
menu abs_division_4:
    "¿Cuál es el tema principal del problema?"
    "La cantidad de troncos que le deberá tocar a cada hogar.":
        play sound "acierto.mp3"
        "Correcto, el tema principal son los troncos que Juan Cupul debe darle a cada hogar."
        jump des_division_4
    "La escasez de troncos.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_division_4
    "Los hogares que no tienen madera.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_division_4
    "Los troncos que Juan Cupul tiene en su parcela.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_division_4

menu des_division_4:
    "¿Qué datos nos proporciona el problema?"
    "La cantidad de troncos totales y el número de hogares que recibirán dichos troncos.":
        play sound "acierto.mp3"
        "Correcto, los datos proporcionados son la cantidad de troncos totales y el número de hogares que lo recibirán."
        jump recP_division_4
    "La cantidad de troncos que hay en la parcela y se quieren vender.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_division_4
    "Cantidad de vecinos que necesitan troncos.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_division_4
    "El precio que tiene cada tronco y el número de vecinos que quieren comprar.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_division_4

menu recP_division_4:
    "¿Qué operación necesitamos realizar para encontrar la cantidad de troncos que recibirá cada hogar?"
    "División.":
        play sound "acierto.mp3"
        "Correcto, necesitamos dividir la cantidad total de troncos entre el número de hogares que los recibirán."
        jump disAl_division_4
    "Suma.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos dividiendo los troncos entre los hogares que existen cerca de la casa de Juan Cupul."
        jump recP_division_4
    "Multiplicación.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos dividiendo los troncos entre los hogares que existen cerca de la casa de Juan Cupul."
        jump recP_division_4
    "Resta.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos dividiendo los troncos entre los hogares que existen cerca de la casa de Juan Cupul."
        jump recP_division_4

menu disAl_division_4:
    "Si el número total de troncos es 60 y se quiere repartir en 5 hogares, ¿cuál es el procedimiento para saber cuántos troncos le debe tocar a cada hogar?"
    "Dividir los troncos (60) entre el número de hogares (5) lo que da como resultado 12.":
        play sound "acierto.mp3"
        "Correcto, dividir la cantidad de troncos (60) entre la de los hogares (5) ayuda a conocer que son 12 los troncos que le tocará a cada hogar."
        jump disAl_division_4
    "Restar los troncos (60) menos el número de hogares (5) lo que da como resultado 55.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, divide nuevamente la cantidad de troncos entre los hogares que se les quiere dar."
        jump disAl_division_4
    "Sumar los troncos (60) más el número de hogares (5) lo que da como resultado 65.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, divide nuevamente la cantidad de troncos entre los hogares que se les quiere dar."
        jump disAl_division_4
    "Multiplicar los troncos (60) por el número de hogares (5) lo que da como resultado 300.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, divide nuevamente la cantidad de troncos entre los hogares que se les quiere dar."
        jump disAl_division_4

#* Problema división 5
menu abs_division_5:
    "¿Cuál es el tema principal del problema?"
    "La cantidad de semillas que se tienen que vender por día.":
        play sound "acierto.mp3"
        "Correcto, el tema principal son los paquetes de semilla que le tocará a cada agricultor."
        jump des_division_5
    "La feria agrícola que habrá en el pueblo.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_division_5
    "Los tipos de semillas que Juan Cupul vende.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_division_5
    "Los paquetes de semilla que le tocará a cada agricultor.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_division_5

menu des_division_5:
    "¿Qué datos nos proporciona el problema?"
    "La cantidad de paquetes de semillas que tiene Juan Cupul y el número de agricultores.":
        play sound "acierto.mp3"
        "Correcto, los datos proporcionados son la cantidad de paquetes de semillas que tiene Juan Cupul y el número de agricultores."
        jump recP_division_5
    "La cantidad de semillas que tiene cada paquete.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_division_5
    "Cantidad de agricultores que asistieron a la feria agrícola.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_division_5
    "El precio que tiene cada paquete.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_division_5

menu recP_division_5:
    "¿Qué operación necesitamos realizar para encontrar la cantidad de paquetes que Juan Cupul debe darle a cada agricultor?"
    "División.":
        play sound "acierto.mp3"
        "Correcto, necesitamos dividir la cantidad total de paquetes de semilla entre el número de agricultores."
        jump disAl_division_5
    "Suma.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos dividiendo los paquetes de semilla entre el número de agricultores."
        jump recP_division_5
    "Multiplicación.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos dividiendo los paquetes de semilla entre el número de agricultores."
        jump recP_division_5
    "Resta.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos dividiendo los paquetes de semilla entre el número de agricultores."
        jump recP_division_5

menu disAl_division_5:
    "Si el número total de paquetes de semilla es 45 y se quiere repartir entre 9 agricultores, ¿cuál es el procedimiento para saber cuántos paquetes le debe dar Juan Cupul a cada agricultor?"
    "Dividir los paquetes de semilla (45) entre el número de agricultores (9) lo que da como resultado 5.":
        play sound "acierto.mp3"
        "Correcto, dividir la cantidad de paquetes de semilla (45) entre el número de agricultores (9) ayuda a conocer que son 5 los paquetes que le tocará a cada agricultor."
        jump 
    "Restar a los paquetes de semilla (45) el número de agricultores (9) lo que da como resultado 36.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, divide nuevamente la cantidad de paquetes de semilla entre el número de agricultores que se les quiere dar."
        jump disAl_division_5
    "Sumar los paquetes de semilla (45) más el número de agricultores (9) lo que da como resultado 54.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, divide nuevamente la cantidad de paquetes de semilla entre el número de agricultores que se les quiere dar."
        jump disAl_division_5
    "Multiplicar los paquetes de semilla (45) por número de agricultores (9) lo que da como resultado 405.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, divide nuevamente la cantidad de paquetes de semilla entre el número de agricultores que se les quiere dar."
        jump disAl_division_5

#* Problema división 6
menu abs_division_6:
    "¿Cuál es el tema principal del problema?"
    "Las horas que recibe cada guerrero de entrenamiento.":
        play sound "acierto.mp3"
        "Correcto, el tema principal son las horas que recibe cada guerrero de entrenamiento."
        jump des_division_6
    "Los entrenamientos que hace el guerrero en un semana.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_division_6
    "Los guerreros que se necesitan en el combate.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_division_6
    "El uso del tiempo en el combate.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_division_6

menu des_division_6:
    "¿Qué datos nos proporciona el problema?"
    "El número de guerreros y la cantidad de horas que Juan Cupul tiene.":
        play sound "acierto.mp3"
        "Correcto, los datos proporcionados son el número de guerreros y la cantidad de horas que Juan Cupul tiene."
        jump recP_division_6
    "El número de guerreros que tiene Juan Cupul.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_division_6
    "Cantidad de horas que tarda un combate.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_division_6
    "Las horas de trabajo de los guerreros.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_division_6

menu recP_division_6:
    "¿Qué operación necesitamos realizar para encontrar la cantidad de horas de entrenamiento que Juan Cupul debe dar a cada guerrero?"
    "División.":
        play sound "acierto.mp3"
        "Correcto, necesitamos dividir la cantidad de horas entre el total de guerreros."
        jump disAl_division_6
    "Multiplicación.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos asignando el número de horas de entrenamiento para cada guerrero."
        jump recP_division_6
    "Suma.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos asignando el número de horas de entrenamiento para cada guerrero."
        jump recP_division_6
    "Resta.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos asignando el número de horas de entrenamiento para cada guerrero."
        jump recP_division_6

menu disAl_division_6:
    "Si el número total de horas de entrenamiento es de 45 y se quiere dar la misma cantidad de tiempo entre 15 guerreros, ¿cuál es el procedimiento para saber cuántas horas de entrenamiento le tocará a cada guerrero?"
    "Dividir las horas de entrenamiento totales (45) entre el número de guerreros (15) y el resultado es 3.":
        play sound "acierto.mp3"
        "Correcto, dividir el total de horas de entrenamiento (45) entre los guerreros (15) da como resultado 3 horas de entrenamiento para cada guerrero."
        jump 
    "Restar al total de horas de entrenamiento (45) el número de guerreros (15) y el resultado es 30.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, divide nuevamente los machetes entre los campesinos."
        jump disAl_division_6
    "Sumar las horas de entrenamiento totales (45) más el número de guerreros (15) y el resultado es 60.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, divide nuevamente los machetes entre los campesinos."
        jump disAl_division_6
    "Multiplicar el número de guerreros (15) por el total de horas de entrenamiento (45) y el resultado es 675.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, divide nuevamente los machetes entre los campesinos."
        jump disAl_division_6



# Problema Resta 1
menu abs_resta_1:
    "¿Cuál es el tema principal del problema?"
    "El número de enemigos derrotados.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_resta_1
    "La cantidad de espadas restantes.":
        play sound "acierto.mp3"
        "Correcto, el tema principal es la cantidad de espadas restantes."
        jump des_resta_1
    "La fecha de la batalla.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_resta_1
    "La duración de la batalla.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, piensa en lo que se está preguntando en el problema."
        jump abs_resta_1

menu des_resta_1:
    "¿Qué datos nos proporciona el problema?"
    "Hora de inicio y duración de la batalla":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump recP_resta_1
    "El número de enemigos derrotados":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_resta_1
    "La cantidad de espadas iniciales y las espadas perdidas":
        play sound "acierto.mp3"
        "Correcto, los datos proporcionados son la cantidad de espadas iniciales y las espadas perdidas."
        jump recP_resta_1
    "La estrategia utilizada en la batalla":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa los datos que se mencionan en el problema."
        jump des_resta_1

menu recP_resta_1:
    "¿Qué operación necesitamos realizar para encontrar la cantidad de espadas restantes?"
    "Multiplicación.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos restando la cantidad de espadas perdidas de la cantidad inicial."
        jump recP_resta_1
    "División.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos restando la cantidad de espadas perdidas de la cantidad inicial."
        jump recP_resta_1
    "Suma.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, recuerda que estamos restando la cantidad de espadas perdidas de la cantidad inicial."
        jump recP_resta_1
    "Resta.":
        play sound "acierto.mp3"
        "Correcto, necesitamos restar la cantidad de espadas perdidas de la cantidad inicial."
        jump disAl_resta_1

menu disAl_resta_1:
    "Si Juan Cupul tenía 25 espadas y perdió 9 en una batalla, ¿cuál es el procedimiento para saber cuántas espadas le quedan?"
    "Sumar la cantidad de espadas iniciales (25) con la cantidad de espadas perdidas (9) y el resultado es 34.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa nuevamente las operaciones necesarias para restar espadas perdidas de la cantidad inicial."
        jump disAl_resta_1
    "Multiplicar la cantidad de espadas iniciales (25) por la cantidad de espadas perdidas (9) y el resultado es 16.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa nuevamente las operaciones necesarias para restar espadas perdidas de la cantidad inicial."
        jump disAl_resta_1
    "Restar la cantidad de espadas perdidas (9) de la cantidad de espadas iniciales (25) y el resultado es 16.":
        play sound "acierto.mp3"
        "Correcto, restar 9 espadas de las 25 espadas iniciales da como resultado 16 espadas."
        jump 
    "Dividir la cantidad de espadas iniciales (25) entre la cantidad de espadas perdidas (9) y el resultado es 14.":
        play sound "error.mp3" volume 4.0
        "Incorrecto, revisa nuevamente las operaciones necesarias para restar espadas perdidas de la cantidad inicial."
        jump disAl_resta_1

#* Resta 2
menu abs_resta_2:
    "¿Cuál es el tema principal del problema?"
    "La cantidad de agua restante":
        "Correcto, el tema principal es la cantidad de agua restante."
    "La distancia del maratón":
        "Incorrecto, piensa en lo que se está preguntando en el problema."
    "El tiempo del maratón":
        "Incorrecto, piensa en lo que se está preguntando en el problema."
    "La cantidad de calorías quemadas":
        "Incorrecto, piensa en lo que se está preguntando en el problema."

menu des_resta_2:
    "¿Qué datos nos proporciona el problema?"
    "La cantidad inicial de agua y la cantidad de agua bebida":
        "Correcto, los datos proporcionados son la cantidad inicial de agua y la cantidad de agua bebida."
    "La duración del maratón":
        "Incorrecto, revisa los datos que se mencionan en el problema."
    "La velocidad de Juan":
        "Incorrecto, revisa los datos que se mencionan en el problema."
    "La cantidad de calorías quemadas":
        "Incorrecto, revisa los datos que se mencionan en el problema."

menu recP_resta_2:
    "¿Qué operación necesitamos realizar para encontrar la cantidad de agua restante?"
    "Multiplicación":
        "Incorrecto, recuerda que estamos restando la cantidad de agua bebida de la cantidad inicial."
    "División":
        "Incorrecto, recuerda que estamos restando la cantidad de agua bebida de la cantidad inicial."
    "Suma":
        "Incorrecto, recuerda que estamos restando la cantidad de agua bebida de la cantidad inicial."
    "Resta":
        "Correcto, necesitamos restar la cantidad de agua bebida de la cantidad inicial."

Retroalimentación:
A, B, C) Incorrecto, recuerda que estamos restando la cantidad de agua bebida de la cantidad inicial.
D) Correcto, necesitamos restar la cantidad de agua bebida de la cantidad inicial.

menu disAl_resta_2:
    "Si Juan Cupul tenía 48 litros de agua y bebió 15 litros, ¿cuál es el procedimiento para saber cuántos litros de agua le quedan?"
    "Restar la cantidad de agua bebida (15) de la cantidad de agua inicial (48) y el resultado es 33":
        "Correcto, restar 15 litros de los 48 litros iniciales da como resultado 33 litros."
    "Sumar la cantidad de agua inicial (48) con la cantidad de agua bebida (15) y el resultado es 63":
        "Incorrecto, revisa nuevamente las operaciones necesarias para restar la cantidad de agua bebida de la cantidad inicial."
    "Multiplicar la cantidad de agua inicial (48) por la cantidad de agua bebida (15) y el resultado es 35":
        "Incorrecto, revisa nuevamente las operaciones necesarias para restar la cantidad de agua bebida de la cantidad inicial."
    "Dividir la cantidad de agua inicial (48) entre la cantidad de agua bebida (15) y el resultado es 34":
        "Incorrecto, revisa nuevamente las operaciones necesarias para restar la cantidad de agua bebida de la cantidad inicial."



*Problema resta 3*
menu:
    "¿Cuál es el tema principal del problema?"
La cantidad de tomates regalados.
La cantidad de tomates restantes.
La cantidad de vecinos de Juan.
La cantidad de tomates cosechados.

Retroalimentación:
B) Correcto, el tema principal es la cantidad de tomates restantes.
A, C, D) Incorrecto, piensa en lo que se está preguntando en el problema.

menu:
    "¿Qué datos nos proporciona el problema?"
La cantidad de tomates cosechados y la cantidad de tomates regalados.
El número de vecinos.
La distancia del campo de tomates.
La cantidad de tiempo para cosechar los tomates.

Retroalimentación:
A) Correcto, los datos proporcionados son la cantidad de tomates cosechados y la cantidad de tomates regalados.
B, C, D) Incorrecto, revisa los datos que se mencionan en el problema.

menu:
    "¿Qué operación necesitamos realizar para encontrar la cantidad de tomates restantes?"
Resta.
Multiplicación.
División.
Suma.

Retroalimentación:
B, C, D) Incorrecto, recuerda que estamos restando la cantidad de tomates regalados de la cantidad inicial.
A) Correcto, necesitamos restar la cantidad de tomates regalados de la cantidad inicial.

menu:
    "Si Juan Cupul cosechó 63 tomates y regaló 25, ¿cuál es el procedimiento para saber cuántos tomates le quedaron?"
Sumar la cantidad de tomates cosechados (63) con la cantidad de tomates regalados (25) y el resultado es 88.
Multiplicar la cantidad de tomates cosechados (63) por la cantidad de tomates regalados (25) y el resultado es 3.
Dividir la cantidad de tomates cosechados (63) entre la cantidad de tomates regalados (25) y el resultado es 14.
Restar la cantidad de tomates regalados (25) de la cantidad de tomates cosechados (63) y el resultado es 38.

Retroalimentación:
D) Correcto, restar 25 tomates de los 63 tomates cosechados da como resultado 38 tomates.
A, B, C) Incorrecto, revisa nuevamente las operaciones necesarias para restar la cantidad de tomates regalados de la cantidad inicial.

*Problema resta 4*
menu:
    "¿Cuál es el tema principal del problema?"
La cantidad de provisiones consumidas.
La cantidad de provisiones restantes.
La duración de la expedición.
La cantidad de provisiones iniciales.

Retroalimentación:
B) Correcto, el tema principal es la cantidad de provisiones restantes.
A, C, D) Incorrecto, piensa en lo que se está preguntando en el problema.

menu:
    "¿Qué datos nos proporciona el problema?"
La cantidad de provisiones iniciales y la cantidad de provisiones consumidas.
La duración de la expedición.
El número de personas en la expedición.
La cantidad de tiempo para consumir las provisiones.

Retroalimentación:
A) Correcto, los datos proporcionados son la cantidad de provisiones iniciales y la cantidad de provisiones consumidas.
B, C, D) Incorrecto, revisa los datos que se mencionan en el problema.

menu:
    "¿Qué operación necesitamos realizar para encontrar la cantidad de provisiones restantes?"
Multiplicación.
División.
Suma.
Resta.

Retroalimentación:
A, B, C) Incorrecto, recuerda que estamos restando la cantidad de provisiones consumidas de la cantidad inicial.
D) Correcto, necesitamos restar la cantidad de provisiones consumidas de la cantidad inicial.

menu:
    "Si Juan Cupul tenía 45 provisiones y consumió 19, ¿cuál es el procedimiento para saber cuántas provisiones le quedan?"
Sumar la cantidad de provisiones iniciales (45) con la cantidad de provisiones consumidas (19) y el resultado es 64.
Restar la cantidad de provisiones consumidas (19) de la cantidad de provisiones iniciales (45) y el resultado es 26.
Multiplicar la cantidad de provisiones iniciales (45) por la cantidad de provisiones consumidas (19) y el resultado es 34.
Dividir la cantidad de provisiones iniciales (45) entre la cantidad de provisiones consumidas (19) y el resultado es 28.

Retroalimentación:
B) Correcto, restar 19 provisiones de las 45 provisiones iniciales da como resultado 26 provisiones.
A, C, D) Incorrecto, revisa nuevamente las operaciones necesarias para restar la cantidad de provisiones consumidas de la cantidad inicial.

*Problema resta 5*
menu:
    "¿Cuál es el tema principal del problema?"
La cantidad de tablones utilizados.
La cantidad de tablones restantes.
La duración de la construcción del puente.
La cantidad de tablones iniciales.

Retroalimentación:
B) Correcto, el tema principal es la cantidad de tablones restantes.
A, C, D) Incorrecto, piensa en lo que se está preguntando en el problema.

menu:
    "¿Qué datos nos proporciona el problema?"
La cantidad de tablones iniciales y la cantidad de tablones utilizados.
La duración de la construcción del puente.
El número de trabajadores.
La cantidad de tiempo para utilizar los tablones.

Retroalimentación:

A) Correcto, los datos proporcionados son la cantidad de tablones iniciales y la cantidad de tablones utilizados.
B, C, D) Incorrecto, revisa los datos que se mencionan en el problema.
menu:
    "¿Qué operación necesitamos realizar para encontrar la cantidad de tablones restantes?"
Multiplicación.
División.
Resta.
Suma.

Retroalimentación:
A, B, D) Incorrecto, recuerda que estamos restando la cantidad de tablones utilizados de la cantidad inicial.
C) Correcto, necesitamos restar la cantidad de tablones utilizados de la cantidad inicial.

menu:
    "Si Juan Cupul tenía 60 tablones y usó 27, ¿cuál es el procedimiento para saber cuántos tablones le quedan?"
Sumar la cantidad de tablones iniciales (60) con la cantidad de tablones utilizados (27) y el resultado es 87.
Multiplicar la cantidad de tablones iniciales (60) por la cantidad de tablones utilizados (27) y el resultado es 33.
Dividir la cantidad de tablones iniciales (60) entre la cantidad de tablones utilizados (27) y el resultado es 31.
Restar la cantidad de tablones utilizados (27) de la cantidad de tablones iniciales (60) y el resultado es 33.

Retroalimentación:
D) Correcto, restar 27 tablones de los 60 tablones iniciales da como resultado 33 tablones.
A, B, C) Incorrecto, revisa nuevamente las operaciones necesarias para restar la cantidad de tablones utilizados de la cantidad inicial.

*Problema resta 6*
menu:
    "¿Cuál es el tema principal del problema?"
La cantidad de partidas ganadas.
La cantidad de partidas perdidas.
El tiempo dedicado a cada partida.
El número de oponentes.

Retroalimentación:
B) Correcto, el tema principal es la cantidad de partidas perdidas.
A, C, D) Incorrecto, piensa en lo que se está preguntando en el problema.

menu:
    "¿Qué datos nos proporciona el problema?"
La cantidad de partidas jugadas y la cantidad de partidas ganadas.
La duración de cada partida.
La cantidad de tiempo dedicada a las partidas.
La cantidad de oponentes.

Retroalimentación:
A) Correcto, los datos proporcionados son la cantidad de partidas jugadas y la cantidad de partidas ganadas.
B, C, D) Incorrecto, revisa los datos que se mencionan en el problema.

menu:
    "¿Qué operación necesitamos realizar para encontrar la cantidad de partidas perdidas?"
Resta.
Multiplicación.
División.
Suma.

Retroalimentación:
B, C, D) Incorrecto, recuerda que estamos restando la cantidad de partidas ganadas de la cantidad total de partidas jugadas.
A) Correcto, necesitamos restar la cantidad de partidas ganadas de la cantidad total de partidas jugadas.

menu:
    "Si Juan Cupul jugó 15 partidas y ganó 8, ¿cuál es el procedimiento para saber cuántas partidas perdió?"
 Sumar la cantidad de partidas jugadas (15) con la cantidad de partidas ganadas (8) y el resultado es 23.
Multiplicar la cantidad de partidas jugadas (15) por la cantidad de partidas ganadas (8) y el resultado es 2.
Restar la cantidad de partidas ganadas (8) de la cantidad de partidas jugadas (15) y el resultado es 7.
Dividir la cantidad de partidas jugadas (15) entre la cantidad de partidas ganadas (8) y el resultado es 5.

Retroalimentación:
C) Correcto, restar 8 partidas ganadas de las 15 partidas jugadas da como resultado 7 partidas perdidas.
A, B, D) Incorrecto, revisa nuevamente las operaciones necesarias para restar la cantidad de partidas ganadas de la cantidad total de partidas jugadas.

*Problema resta 7*
menu:
    "¿Cuál es el tema principal del problema?"
La cantidad de balas utilizadas.
La duración de la batalla.
El tipo de pistolas utilizadas.
La cantidad de balas restantes.

Retroalimentación:
D) Correcto, el tema principal es la cantidad de balas restantes.
A, B, C) Incorrecto, piensa en lo que se está preguntando en el problema.

menu:
    "¿Qué datos nos proporciona el problema?"
La cantidad de balas iniciales y la cantidad de balas utilizadas.
La duración de la batalla.
El tipo de armas utilizadas.
La cantidad de enemigos.

Retroalimentación:
A) Correcto, los datos proporcionados son la cantidad de balas iniciales y la cantidad de balas utilizadas.
B, C, D) Incorrecto, revisa los datos que se mencionan en el problema.

menu:
    "¿Qué operación necesitamos realizar para encontrar la cantidad de balas restantes?"
Multiplicación.
Resta.
División.
Suma.

Retroalimentación:
A, C, D Incorrecto, recuerda que estamos restando la cantidad de balas utilizadas de la cantidad inicial.
B) Correcto, necesitamos restar la cantidad de balas utilizadas de la cantidad inicial.

menu:
    "Si Juan Cupul tenía 325 balas y usó 150, ¿cuál es el procedimiento para saber cuántas balas le quedaron?"
Restar la cantidad de balas utilizadas (150) de la cantidad de balas iniciales (325) y el resultado es 175.
Sumar la cantidad de balas iniciales (325) con la cantidad de balas utilizadas (150) y el resultado es 475.
Multiplicar la cantidad de balas iniciales (325) por la cantidad de balas utilizadas (150) y el resultado es 200.
Dividir la cantidad de balas iniciales (325) entre la cantidad de balas utilizadas (150) y el resultado es 225.

Retroalimentación:
A) Correcto, restar 150 balas de las 325 balas iniciales da como resultado 175 balas.
B, C, D) Incorrecto, revisa nuevamente las operaciones necesarias para restar la cantidad de balas utilizadas de la cantidad inicial.