init python:
    puntos = 0
    labelFinal = ""
    dialogoRoboAgua = ""
    puntosVictorias=0
    nombreUsuario = ""
    ayudoFili = False
    ayudoVendedor = False
    avatarElegido = ""
    conservaObjeto = False
    aciertos = 0
    errores = 0
    
    def my_save(data):
        #data["nombre_usuario"] = nombreUsuario
        data["puntos_victorias"] = puntosVictorias
        data["ayudo_a_fili"] = ayudoFili
        data["ayudo_a_vendedor"] = ayudoVendedor
        data["conserva_objeto"] = conservaObjeto
        data["avatar_elegido"] = avatarElegido
        data["aciertos"] = aciertos
        data["errores"] = errores

    #config.save_json_callbacks = [ my_save ]
    config.save_json_callbacks.append(my_save)


#Inicio del juego #############################################################
label start:
    play music "audio/fondo.mp3"

    scene fondo_seleccionar_personaje with fade

    "¡Bienvenido/Bienvenida a Conquista matemática!"
    "Esta es una novela visual que presenta parte de la vida de Juan Cupul, ¡un héroe de Tixcacalcupul! 
    (es importante recalcar que no es una representación fiel de su vida, sino una adaptación)."
    "Durante la historia tendrás que tomar decisiones que afectarán el curso de la historia y los personajes."
    "Pero también verás varios ejercicios matemáticos que tendrás que resolver."
    "Si no logras resolverlos con éxito, la historia no avanzará, así que esfuérzate mucho para que puedas
    conocer cuál será el final que te tocará basado en tus decisiones."
    "Y sobre todo, ¡no olvides divertirte!"
    "Como detalle adicional, verás que los personajes se moverán durante la historia.
    Para evitar errores durante esas animaciones, procura no presionar o mover nada 
    hasta que terminen."
    "Por ahora, personaliza un poco tu partida."

    #$ nombreUsuario = renpy.input("Escribe tu nombre")
    $ aciertos = 10
    $ errores = 12

    jump seleccion_avatar_1

label inicio_historia:
    scene interior_casa_juan with fade 

    #Haciendo uso de los nombres de grupo, puedo permitirme declarar la posición
    #de una imagen una sola vez, y si quiero que la imagen se reemplace por otra,
    #la llamo con un show simple y la reemplazará automáticamente.

    show juan parado derecha:
        xpos 0.47
        ypos 0.49
    
    #Con la siguiente instrucción puedo hacer que Juan cambie de animación, 
    #conservando la posición que declaré en la instrucción anterior
    #show juan camina derecha

    #show juan_parado_derecha:
    #    xpos 0.47
    #    ypos 0.49

    show novia parada izquierda:
        xpos 0.53
        ypos 0.49

    #$ nombreUsuario = renpy.input("Escribe tu nombre")

    #Puedo guardar el nombre del usuario por partida y usarlo durante el juego.
    #Debo explorar esa opción
    #$ nombres.append(nombreUsuario)    

    #$ persistent.nombres.append(nombreUsuario)# = nombres

    "Juan Bautista Cupul Tun vive con su prometida María Dolores Canul en una casita 
    en el pueblo Tixcacal."
    "Se la pasan sus días tranquilos, jugando a resolver problemas matemáticos 
    para no perder la práctica en sus habilidades de matemáticas."

    prometida "Te tengo uno bueno."

    menu problema_multiplicacion_6:
        prometida "Participaste en la batalla junto con otros 7 guerreros. 
        Cada uno lanzó 15 flechas durante la batalla. ¿Cuántas flechas lanzaron en total?"
        "7 flechas":
            play sound "error.mp3" volume 4.0
            "Ups, parece que esta respuesta no es la correcta."
            jump abs_multiplicacion_6
        "23 flechas":
            play sound "error.mp3" volume 4.0
            "No te rindas, continúa intentándolo."
            jump abs_multiplicacion_6
        "105 flechas":
            play sound "error.mp3" volume 4.0
            "Vamos, inténtalo otra vez."
            jump abs_multiplicacion_6
        "120 flechas":
            play sound "acierto.mp3"
            "¡Excelente! En este caso hay 8 guerreros (7 guerreros + Juan Cupul) y 
            se multiplica por 15 flechas que lanzó cada uno."
        
    prometida "¡Muy bien, Juan! Aunque todavía te gano por tres aciertos."
    juan "Pero no te dejaré vencerme hoy. Vamos, dime otro."
    
    "Y así se la pasan sus días. Sólo esperando a que llegue la fecha de su boda."

    scene interior_casa_juan with fade 

    show juan parado derecha:
        xpos 1255 ypos 390
    show novia parada izquierda:
        xpos 1465 ypos 390

    juan "¡Espera, espera! Antes de que digas que ya ganaste, dame la oportunidad 
    de un empate."
    prometida "Está bien."

    menu problema_suma_1:
        "Durante la sublevación en 1847, Juan Cupul luchó contra las tropas enemigas durante 
        2 horas y 20 minutos. Si comenzó la lucha a las 9:45 AM, ¿a qué hora terminó?"
        "11:05 AM":
            play sound "error.mp3" volume 4.0
            "¡Casi lo tienes! La respuesta no es correcta, ¿cuál es la operación que se requiere realizar? "
            jump abs_suma_1
        "11:15 AM":
            play sound "error.mp3" volume 4.0
            "Sigue intentado, estoy seguro de que la próxima será la correcta. Observa muy bien tus datos"
            jump abs_suma_1
        "12:05 PM":
            play sound "acierto.mp3"
            "¡Excelente! Has dominado la aritmética del tiempo. Sigue así. "
        "12:25 PM":
            play sound "error.mp3" volume 4.0
            "Ups, parece que esta respuesta no es la correcta. ¡No te rindas, sigue practicando! Recuerda que la hora tiene 60 minutos."
            jump abs_suma_1


    #menu problema_resta_2:
    #    prometida "Tenías 48 litros de agua para un maratón y bebiste 15 litros. 
    #    ¿Cuántos litros de agua te quedan?"
    #    "33 litros":
    #        play sound "acierto.mp3"
    #        "¡Excelente! A Juan Cupul le quedan 33 litros de agua para seguir el maratón."
    #    "34 litros":
    #        play sound "error.mp3" volume 4.0
    #        "¡Vamos, estás cerca! Pero esta vez la respuesta no es la correcta."
    #        jump problema_resta_2
    #    "35 litros":
    #        play sound "error.mp3" volume 4.0
    #        "¡Sigue adelante! Recuerda cuántos litros de agua tenía Juan para su 
    #        maratón y cuántos bebió."
    #        jump problema_resta_2
    #    "63 litros":
    #        play sound "error.mp3" volume 4.0
    #        "¡Puedes descubrir la solución!"
    #        jump problema_resta_2

    juan "¡Sí! Hoy declaramos un empate."
    prometida "Me la debes, te di una oportunidad."
    juan "Está bien. Muchas gracias, María."

    "Pero la amenaza de ataque e invasión al pueblo a causa de los cruzoob estaba tan 
    presente que en el pueblo se tomó la desición de hacer guardia todos los días y a todas 
    horas en una cabaña."
    "Las personas que vigilaban avisarían de los ataques explotando una bomba."
    "A nadie le parecía excesivo ya que estuvieron todos de acuerdo en que era necesario
    estar pendientes por si llegaba algún ataque."
    "Y así pasó el tiempo, hasta el día antes de su boda. Día en el que a Juan le tocaba
    guardia de bombero."

    scene interior_casa_juan with fade 

    show juan parado derecha:
        xpos 400 ypos 600
    show novia parada izquierda:
        xpos 500 ypos 600

    prometida "Buenos días. Veo que apenas te levantas."
    juan "Buenos días. Los preparativos para la boda de mañana me dejaron exhausto."
    prometida "Bueno, no te sobreesfuerces, no queremos que mañana no estés disponible."
    juan "No te preocupes, es lo que menos quiero."
    prometida "Entonces, ¿estás listo para el primer reto de hoy?"
    juan "Completamente listo."

    menu problema_multiplicacion_2:
        prometida "Unos estudiantes investigaban sobre la historia de Juan Cupul; 
        para ello fueron a la sección de Historia en la biblioteca de la escuela. 
        Si hay 4 estanterías y en cada estantería hay 36 libros, ¿cuántos libros hay en la 
        sección de Historia de la biblioteca? "
        "9 libros":
            play sound "error.mp3" volume 4.0
            "Sigue intentando, estoy seguro de que la próxima será la correcta."
            jump problema_multiplicacion_2
        "32 libros":
            play sound "error.mp3" volume 4.0
            "Buen intento, ahora trata con una operación diferente."
            jump problema_multiplicacion_2
        "40 libros":
            play sound "error.mp3" volume 4.0
            "Ups, parece que esta respuesta no es la correcta. ¡No te rindas, sigue practicando!"
            jump problema_multiplicacion_2
        "144 libros":
            play sound "acierto.mp3"
            "¡Felicidades! Para saber el total de libros se multiplican los 36 libros por las 4 
            estanterías que hay en la sección de Historia."

    prometida "Vaya, apenas empieza el día y ya siento que vas a ganarme."
    juan "Yo no estaría tan seguro de eso."
    prometida "Tienes razón, aún hay que ver si yo también empiezo con el pie derecho."
    prometida "Estoy lista para mi ejercicio."
    juan "Tienes 20..."
    filiberto "¡Juan! ¡Juan!"
    juan "Creo que es Filiberto."
    filiberto "¡Juan! ¡Juan!"
    juan "Iré a ver qué necesita."

    jump Filiberto_afuera_casa

    #hide protagonista1
    #with dissolve

label Filiberto_afuera_casa:

    scene afuera_casa_juan with fade 

    show juan parado derecha:
        xpos 0.58
        ypos 0.6

    show fili parado izquierda:
        xpos 0.64
        ypos 0.6

    filiberto "Buenos días, Juan. Sé que estás ocupado por tu boda mañana, pero necesito tu ayuda urgente con algo."
    juan "No te preocupes, Filiberto. Puedes decirme."
    filiberto "Me han pedido que consiga las provisiones para la cabaña donde resguardamos la bomba."
    filiberto "Necesito cosechar verduras y conseguir agua, pero es demasiado el trabajo y nadie me quiere echar una mano."
    filiberto "Si no me ayudas, me tomará todo el día acabar."
    filiberto "¿Puedes ayudarme a conseguir las provisiones?"

    menu:
        "¿Deseas ayudar a Filiberto con las provisiones?"
        "Sí, ayudaré a Filiberto.":
            $ ayudoFili = True
            play sound "audio/seleccion.mp3"
            jump Ayuda_Fili
        "No, deseo ocupar mi tiempo en otra cosa.":
            $ ayudoFili = False
            play sound "audio/seleccion.mp3"
            jump No_ayuda_Fili

label No_ayuda_Fili:
    juan "Lo siento, Filiberto, pero ahora no tengo tiempo para ayudarte." 
    juan "María y yo aún necesitamos revisar unos detalles finales de la boda que no pueden esperar."
    filiberto "Lo entiendo. Ya encontraré a alguien. Nos vemos luego. No se te olvide que hoy nos toca
    hacer guardia."
    juan "Hasta luego, Filiberto."

    hide fili

    jump turno_bombero

######################### Empieza ayuda Fili###################################
label Ayuda_Fili:
    juan "Está bien, Filiberto. No te preocupes, yo te ayudo."
    juan "¿Qué debemos hacer?"
    filiberto "Para empezar, tenemos que ir al huerto que está al oeste y 
    cosechar todo lo que esté listo."
    juan "Entonces vamos. ¡María! ¡Vuelvo en un rato! ¡Voy a ayudar a Juan con algo!"
    prometida "¡Está bien!"

    scene camino_casa_juan
    with fade

    "Juan y Filiberto se ponen a caminar, pero están confundidos y no saben qué camino tomar."

    menu camino_oeste:
        "Si pueden llegar al huerto caminando en línea recta y la casa de Juan 
        está hacia el norte, ¿qué camino deben tomar?"
        "El de arriba":
            play sound "error.mp3" volume 4.0
            "Este es el camino norte, sólo regresarían a la casa de Juan. Intenta de nuevo."
            jump camino_oeste
        "El de la derecha":
            play sound "error.mp3" volume 4.0
            "Casi lo logras, pero este camino lleva al este. Trata de nuevo."
            jump camino_oeste
        "El de la izquierda":
            play sound "acierto.mp3"
            "¡Muy bien! El oeste está a la izquierda."
            jump llegan_a_huerto

label llegan_a_huerto:
    scene A33

    show zanahoria1:
        xpos 260
        ypos 60
    show zanahoria2:
        xpos 435
        ypos 60
    show zanahoria3:
        xpos 610
        ypos 60
    show zanahoria4:
        xpos 260
        ypos 220
    show zanahoria5:
        xpos 435
        ypos 220
    show zanahoria6:
        xpos 610
        ypos 220

    show tomate1:
        xpos 970
        ypos 35
    show tomate2:
        xpos 1120
        ypos 35
    show tomate3:
        xpos 1300
        ypos 35
    show tomate4:
        xpos 1045
        ypos 200
    show tomate5:
        xpos 1210
        ypos 200
    
    show rabanob1:
        xpos 257
        ypos 660
    show rabanob2:
        xpos 432
        ypos 660
    show rabanob3:
        xpos 607
        ypos 660
    show rabanob4:
        xpos 257
        ypos 820
    show rabanob5:
        xpos 432
        ypos 820
    show rabanob6:
        xpos 607
        ypos 820
    
    show rabanor1:
        xpos 990
        ypos 660
    show rabanor2:
        xpos 1160
        ypos 660
    show rabanor3:
        xpos 1330
        ypos 660
    show rabanor4:
        xpos 990
        ypos 820
    show rabanor5:
        xpos 1160
        ypos 820
    show rabanor6:
        xpos 1330
        ypos 820

    show juan parado izquierda:
        xpos 1800
        ypos 430
    show fili parado izquierda:
        xpos 1800
        ypos 530
    
    show juan camina izquierda:
        linear 3 xpos 1300
        
    show fili camina izquierda:
        linear 3 xpos 1300

    pause 3

    show juan parado izquierda:
        xpos 1300
        ypos 430
    show fili parado izquierda:
        xpos 1300
        ypos 530

    "Juan y Filiberto llegaron al huerto. Ahora deben cosechar los cultivos."

    # Movemos a Juan y Fili a los tomates y rábanos blancos
    show juan camina izquierda:
        linear 3 xpos 400
    show fili camina izquierda:
        linear 3 xpos 400
    pause 3
    show juan parado izquierda
    show fili parado izquierda

    "Para poder cosechar, necesitan que los ayudes resolviendo algunos ejercicios."
    
    jump cosechar_verduras_2

label cosechar_verduras_2:

    #* Cosechar las zanahorias
    menu problema_suma_5:
        "Juan Cupul y Filiberto recolectaron cierta cantidad de provisiones para la población 
        de Tixcacal. Si en un día recolectaron 175 kg de maíz y 230 kg de frijoles, 
        ¿cuántos kilogramos de provisiones recolectaron en total?"
        "305 kg":
            play sound "error.mp3" volume 4.0
            "Sigue intentado, estoy seguro de que la próxima será la correcta."
            jump problema_suma_5
        "345 kg":
            play sound "error.mp3" volume 4.0
            "Ups, parece que esta respuesta no es la correcta. ¡No te rindas, sigue practicando!"
            jump problema_suma_5
        "400 kg":
            play sound "error.mp3" volume 4.0
            "¡Casi lo tienes! pero esta vez la respuesta no es la correcta."
            jump problema_suma_5
        "405 kg":
            play sound "acierto.mp3"
            "¡Maravilloso! Parece que Juan y Filiberto saben cómo recolectar la cantidad justa de provisiones."

    # En cada bloque de cosecha se mueve al personaje para que esté a lado de esa
    # verdura, y después de que el usuario presiona Enter, suena "cosechar" y se
    # desaparece la imagen de la verdura.

    "Juan se encarga de cosechar las zanahorias."
    show juan camina atras:
        linear 2 xpos 190 ypos 90
    pause 2
    show juan parado derecha
    "Presiona la tecla Enter para cosechar las zanahorias."
    pause
    play sound "cosechar.mp3" volume 4.0
    hide zanahoria1

    show juan camina derecha:
        linear 1 xpos 365 ypos 90
    pause 1
    show juan parado derecha
    pause
    play sound "cosechar.mp3" volume 4.0
    hide zanahoria2
    
    show juan camina derecha:
        linear 1 xpos 540 ypos 90
    pause 1
    show juan parado derecha
    pause
    play sound "cosechar.mp3" volume 4.0
    hide zanahoria3
    
    show juan camina izquierda:
        linear 2 xpos 190 ypos 250
    pause 2
    show juan parado derecha
    pause
    play sound "cosechar.mp3" volume 4.0
    hide zanahoria4
    
    show juan camina derecha:
        linear 1 xpos 365 ypos 250
    pause 1
    show juan parado derecha
    pause
    play sound "cosechar.mp3" volume 4.0
    hide zanahoria5
    
    show juan camina derecha:
        linear 1 xpos 540 ypos 250
    pause 1
    show juan parado derecha
    pause
    play sound "cosechar.mp3" volume 4.0
    hide zanahoria6

    #* Cosechar los rábanos blancos
    menu problema_suma_2:
        "Juan Cupul recibió 3 mensajes urgentes en la ranchería Poop. Después de leer el 
        primero, pasó 20 minutos. El segundo mensaje le tomó 15 minutos y el tercero, 30 
        minutos. ¿Cuánto tiempo pasó en total antes de continuar su misión?"
        "45 minutos":
            play sound "error.mp3" volume 4.0
            "Sigue intentado, estoy seguro de que la próxima será la correcta."
            jump problema_suma_2
        "1 hora":
            play sound "error.mp3" volume 4.0
            "Ups, parece que esta respuesta no es la correcta. ¡No te rindas, sigue practicando!"
            jump problema_suma_2
        "1 hora y 5 minutos":
            play sound "acierto.mp3"
            "¡Magnífico! La respuesta es correcta."
        "1 hora y 15 minutos":
            play sound "error.mp3" volume 4.0
            "¡Casi lo tienes! pero esta vez la respuesta no es la correcta."
            jump problema_suma_2
        
    "Filiberto se encarga de cosechar los rábanos blancos."
    show fili camina frente:
        linear 2 xpos 187 ypos 650
    pause 2
    show fili parado derecha
    "Presiona la tecla Enter para cosechar los rábanos blancos."
    pause
    play sound "cosechar.mp3" volume 4.0
    hide rabanob1
    
    show fili camina derecha:
        linear 1 xpos 362 ypos 650
    pause 1
    show fili parado derecha
    pause
    play sound "cosechar.mp3" volume 4.0
    hide rabanob2
    
    show fili camina derecha:
        linear 1 xpos 537 ypos 650
    pause 1
    show fili parado derecha
    pause
    play sound "cosechar.mp3" volume 4.0
    hide rabanob3
    
    show fili camina izquierda:
        linear 2 xpos 187 ypos 810
    pause 2
    show fili parado derecha
    pause
    play sound "cosechar.mp3" volume 4.0
    hide rabanob4

    show fili camina derecha:
        linear 1 xpos 362 ypos 810
    pause 1
    show fili parado derecha
    pause
    play sound "cosechar.mp3" volume 4.0
    hide rabanob5

    show fili camina derecha:
        linear 1 xpos 537 ypos 810
    pause 1
    show fili parado derecha
    pause
    play sound "cosechar.mp3" volume 4.0
    hide rabanob6

    # Movemos a Juan y Fili a los tomates y rábanos rojos
    show juan camina derecha:
        linear 3 xpos 900 ypos 90
    show fili camina derecha:
        linear 3 xpos 900 ypos 655
    pause 3
    show juan parado derecha
    show fili parado derecha

    menu problema_resta_4:
        "Juan Cupul tenía 45 provisiones para su expedición y consumió 19. 
        ¿Cuántas provisiones le quedan?"
        "26 provisiones":
            play sound "acierto.mp3"
            "¡Excelente esfuerzo! La respuesta es correcta."
        "28 provisiones":
            play sound "error.mp3" volume 4.0
            "¡Sigue intentándolo, estás en el camino correcto!"
            jump problema_resta_4
        "31 provisiones":
            play sound "error.mp3" volume 4.0
            "¡No te rindas! Piensa en cuántas provisiones tenía Juan al principio y cuántas consumió."
            jump problema_resta_4
        "34 provisiones":
            play sound "error.mp3" volume 4.0
            "¡Sigue intentándolo! La respuesta no es correcta."
            jump problema_resta_4

    #* Cosechar los tomates

    "Juan se encarga de cosechar los tomates."
    "Presiona la tecla Enter para cosechar los tomates."
    pause
    play sound "cosechar.mp3" volume 4.0
    hide tomate1

    show juan camina derecha:
        linear 1 xpos 1050
    pause 1
    show juan parado derecha
    pause
    play sound "cosechar.mp3" volume 4.0
    hide tomate2

    show juan camina derecha:
        linear 1 xpos 1230
    pause 1
    show juan parado derecha
    pause
    play sound "cosechar.mp3" volume 4.0
    hide tomate3

    show juan camina izquierda:
        linear 2 xpos 990 ypos 250
    pause 2
    show juan parado derecha
    pause
    play sound "cosechar.mp3" volume 4.0
    hide tomate4

    show juan camina derecha:
        linear 1 xpos 1140
    pause 1
    show juan parado derecha
    pause
    play sound "cosechar.mp3" volume 4.0
    hide tomate5

    #* Cosechar los rábanos rojos

    menu problema_multiplicacion_1:
        "Juan Cupul se encontraba viajando a una velocidad de 60km por hora para 
        llegar hasta Tixcacal, si viajo durante 3 horas ¿Cuántos kilómetros 
        recorrió en total?"
        "20 kilómetros":
            play sound "error.mp3" volume 4.0
            "Ups, parece que esta respuesta no es la correcta."
            jump problema_multiplicacion_1
        "57 kilómetros":
            play sound "error.mp3" volume 4.0
            "Sigue intentado, estoy seguro de que la próxima será la correcta."
            jump problema_multiplicacion_1
        "63 kilómetros":
            play sound "error.mp3" volume 4.0
            "Inténtalo de nuevo."
            jump problema_multiplicacion_1
        "180 kilómetros":
            play sound "acierto.mp3"
            "Buen trabajo, la respuesta se obtiene de multiplicar la velocidad 
            por el tiempo de viaje, sigue así."
    
    "Filiberto se encarga de cosechar los rábanos rojos."
    "Presiona la tecla Enter para cosechar los rábanos rojos."
    pause
    play sound "cosechar.mp3" volume 4.0
    hide rabanor1

    show fili camina derecha:
        linear 1 xpos 1090
    pause 1
    show fili parado derecha
    pause
    play sound "cosechar.mp3" volume 4.0
    hide rabanor2

    show fili camina derecha:
        linear 1 xpos 1260
    pause 1
    show fili parado derecha
    pause
    play sound "cosechar.mp3" volume 4.0
    hide rabanor3

    show fili camina izquierda:
        linear 2 xpos 920 ypos 810
    pause 2
    show fili parado derecha
    pause
    play sound "cosechar.mp3" volume 4.0
    hide rabanor4

    show fili camina derecha:
        linear 1 xpos 1090
    pause 1
    show fili parado derecha
    pause
    play sound "cosechar.mp3" volume 4.0
    hide rabanor5

    show fili camina derecha:
        linear 1 xpos 1260
    pause 1
    show fili parado derecha
    pause
    play sound "cosechar.mp3" volume 4.0
    hide rabanor6

    # Acercamos a Juan y Filiberto

    show juan camina frente:
        linear 1.5 xpos 1300 ypos 450
    show fili camina atras:
        linear 1.5 xpos 1200 ypos 450
    pause 1.5
    show juan parado izquierda
    show fili parado derecha

    filiberto "Ahora que ya tenemos las verduras, necesitamos ir por agua."
    juan "De acuerdo. Podemos ir por ella al río, pero sería mejor agarrarla de un pozo."
    juan "Vayamos al que está en mi casa."
    filiberto "Regresemos entonces. Sólo hay que dejar esto en la cabaña para no andarlo cargando."

    "Juan y Filiberto dejaron las verduras en la cabaña de los bomberos y se dirigen de vuelta a casa de Juan."

    jump regresar_casaJ_agua
        

### En este label las verduras se cosechan "solas"
label cosechar_verduras:
    "Juan y Filiberto se encargan de cosechar las verduras."
    hide zanahoria1
    pause 0.4
    hide zanahoria2
    pause 0.4
    hide zanahoria3
    pause 0.4
    hide zanahoria4
    pause 0.4
    hide zanahoria5
    pause 0.4
    hide zanahoria6
    pause 0.4
    hide tomate1
    pause 0.4
    hide tomate2
    pause 0.4
    hide tomate3
    pause 0.4
    hide tomate4
    pause 0.4
    hide tomate5
    pause 0.4
    hide rabanob1
    pause 0.4
    hide rabanob2
    pause 0.4
    hide rabanob3
    pause 0.4
    hide rabanob4
    pause 0.4
    hide rabanob5
    pause 0.4
    hide rabanob6
    pause 0.4
    hide rabanor1
    pause 0.4
    hide rabanor2
    pause 0.4
    hide rabanor3
    pause 0.4
    hide rabanor4
    pause 0.4
    hide rabanor5
    pause 0.4
    hide rabanor6
    pause 0.4

    filiberto "Ahora que ya tenemos las verduras, necesitamos ir por agua."
    juan "De acuerdo. Podemos ir por ella al río, pero sería mejor agarrarla de un pozo."
    juan "Vayamos al que está en mi casa."
    filiberto "Regresemos entonces. Sólo hay que dejar esto en la cabaña para no andarlo cargando."

    "Juan y Filiberto dejaron las verduras en la cabaña de los bomberos y se dirigen de vuelta a casa de Juan."

    jump regresar_casaJ_agua

label regresar_casaJ_agua:
    scene afuera_casa_juan

    show juan parado atras:
        xpos 830
        ypos 1000
    show fili parado atras:
        xpos 930
        ypos 1000
    
    show juan camina atras:
        linear 2 ypos 700
        
    show fili camina atras:
        linear 2 ypos 700

    pause 2

    show juan parado derecha:
        xpos 830
        ypos 700
    show fili parado izquierda:
        xpos 930
        ypos 700

    juan "Ya estamos aquí. Llenemos unas cubetas y terminamos."
    filiberto "Está bien."

    "Juan y Filiberto están a punto de recolectar agua del pozo y dejarla en la cabaña de los bomberos."
    "Pero para que ellos puedan hacerlo, debes resolver un problema."
    
    menu problema_division_3:
        "Juan Cupul se encuentra frente a un depósito con 56 litros de agua que 
        debe distribuir en cubetas de 8 litros cada una. ¿Cuántas cubetas necesitará 
        llenar para repartir toda el agua?"
        "7 cubetas":
            play sound "acierto.mp3"
            "¡Buen trabajo, lo has conseguido! Has logrado ayudar a Juan Cupul."
        "9 cubetas":
            play sound "error.mp3" volume 4.0
            "¡Casi lo tienes, estás cerca! Pero la respuesta no es la correcta."
            jump problema_division_3
        "48 cubetas":
            play sound "error.mp3" volume 4.0
            "¡Vuelve a intentarlo, tú puedes! Lee nuevamente el ejercicio. "
            jump problema_division_3
        "64 cubetas":
            play sound "error.mp3" volume 4.0
            "¡Vamos de nuevo!"
            jump problema_division_3
        
    show cubeta1:
        xpos 1140
        ypos 780
    pause 0.4
    show cubeta2:
        xpos 1190
        ypos 780
    pause 0.4
    show cubeta3:
        xpos 1240
        ypos 780
    pause 0.4
    show cubeta4:
        xpos 1290
        ypos 780

    juan "Ya tenemos el agua. Ahora sólo debemos llevarla a la cabaña y habremos terminado."
    filiberto "Muchas gracias por tu ayuda, Juan. Gracias a ti, me ahorré muchas horas de trabajo."
    juan "De nada, Filiberto. Si luego necesitas ayuda con algo más, puedes decirme."
    filiberto "No te preocupes. Por hoy ya fue suficiente, además, mañana te casas."
    filiberto "¿Cómo te sientes? ¿No estás nervioso?"
    juan "Es extraño, pero no. Me siento listo."
    filiberto "Tiene que ser una buena señal. Una señal de que es lo que realmente quieres."
    juan "Eso parece."
    juan "Ya llevemos el agua, antes de que sea tarde."

    hide cubeta1
    hide cubeta2
    hide cubeta3
    hide cubeta4
    hide fili

    jump turno_bombero
######################### Termina ayuda Fili###################################

# Aquí se unen los caminos después de la decisión de ayudar o no a Filiberto
label turno_bombero:

    show juan parado derecha:
        xpos 830
        ypos 700

    show novia parada izquierda:
        xpos 930
        ypos 700

    "Luego de terminar con Filiberto, Juan desayuna y se prepara para su guardia como bombero."

    juan "Ya necesito irme a mi puesto. Hoy me toca hacer guardia con Filiberto."
    prometida "¿Estás seguro? Tu tío José vino en la mañana mientras dormías y me dijo
    que podía ocupar tu lugar."
    juan "Tengo que ir yo. Sé que mañana es nuestra boda, pero es mi responsabilidad ayudar y 
    contribuir como todos."
    juan "Lo siento mucho."
    prometida "No, está bien, yo entiendo. Sólo te pido que no faltes."
    juan "Te prometo que estaré allí. No te voy a fallar."
    prometida "Antes de que te vayas, ¿puedes resolver un reto?"
    juan "Sí, dímelo, estoy listo."

    menu problema_resta_6:
        prometida "Si jugaste 15 partidas de ajedrez y ganaste 8, ¿cuántas partidas perdiste?"
        "2 partidas":
            play sound "error.mp3" volume 4.0
            "¡Vuelve a intentarlo, tú puedes!"
            jump problema_resta_6
        "5 partidas":
            play sound "error.mp3" volume 4.0
            "Estás en el camino correcto. Recuerda cuántas partidas de ajedrez jugó Juan en total y cuántas ganó."
            jump problema_resta_6
        "7 partidas":
            play sound "acierto.mp3"
            "¡Eso es! La respuesta es correcta."
        "23 partidas":
            play sound "error.mp3" volume 4.0
            "¡Tú puedes hallar la solución!"
            jump problema_resta_6

    prometida "No has perdido la práctica. Sigues sin perder tu racha de aciertos."
    juan "Practico mucho gracias a ti."
    juan "Bueno, ya me voy. Nos vemos mañana."

    jump vecina_naranjas

# Pequeña misión en la que María Dolores ofrece regalar naranjas a una vecina si
# esta resuelve un ejercicio
label vecina_naranjas:
    scene afuera_casa_juan

    show caja_naranjas:
        xpos 0.61 ypos 0.6

    show mujer camina atras:
        xpos 880 ypos 1000
        linear 1.5 ypos 850

    pause 1.5

    show mujer parada atras

    vecina "¡Buenas tardes! ¡Vecina! ¡Vecina!"

    show novia parada frente:
        xpos 880 ypos 700

    prometida "¡Hola, Vero! ¿Cómo estás?"
    vecina "Muy bien, María, muy bien. ¿Y cómo estás tú?"
    prometida "Muy bien también, emocionada por mañana."
    vecina "Ah, sí. Tú y el Juanito se casan mañana, qué gusto."
    prometida "Sí, estoy muy feliz, pero dime, ¿en qué te puedo ayudar?"
    vecina "Ay, María, no quisiera molestarte, pero es que necesito unas chinas."
    vecina "Ando cocinando y me acabo de dar cuenta de que no tengo y mi árbol de 
    china no tiene ninguna."
    vecina "¿Me puedes vender unas cuantas de las que tienes?"
    prometida "Claro que sí, pero tengo una mejor idea. Si resuelves bien un ejercicio 
    que te voy a decir, te regalo la caja entera."
    vecina "Ay, María, qué cosas me pides, jajajaja. Ya veo como tú y el Juanito 
    se mantienen entretenidos."
    prometida "Ya sabes que nos encanta resolver problemas matemáticos. Entonces, ¿aceptas?"
    vecina "Está bien, acepto. Será entretenido."

    menu problema_resta_7:
        prometida "Después de la lucha, Juan Cupul tenía 325 balas para sus 
        pistolas. Si usó 150 balas durante la primera parte de la batalla, ¿cuántas 
        balas le quedaron después?"
        "125 balas":
            play sound "error.mp3" volume 4.0
            "Piensa en cuántas balas tenía Juan al principio y cuántas utilizó durante la batalla."
            jump problema_resta_7
        "175 balas":
            play sound "acierto.mp3" 
            "¡Muy bien! Hiciste un maravilloso trabajo, la respuesta es correcta."
        "200 balas":
            play sound "error.mp3" volume 4.0
            "Estás cerca de la respuesta correcta.¡Continúa intentándolo!"
            jump problema_resta_7
        "225 balas":
            play sound "error.mp3" volume 4.0
            "La respuesta es incorrecta, pero ¡tú puedes resolver esto!"
            jump problema_resta_7

    prometida "¡Muy bien, Vero! La caja de naranjas es tuya."
    "María le da la caja de naranjas a Vero."
    hide caja_naranjas

    vecina "Pues muchas gracias, María. Esto fue divertido. La próxima vez regresaré 
    sólo para intentar resolver alguno de tus ejercicios. ¡Nos vemos luego!"
    prometida "¡Adiós!"

    show mujer camina frente:
        linear 2 ypos 1200
    pause 2

    jump camino_al_turno

label camino_al_turno:
    scene camino_v_md

    "Juan está de camino a su turno como bombero. Avanza con tranquilidad, sabiendo que va con tiempo
    para llegar puntual."

    show juan parado izquierda:
        xpos 1850
        ypos 450
    
    show juan camina izquierda:
        linear 6 xpos 0

    pause 6

    scene camino_v_osc

    show vendedor quieto:
        xpos 800
        ypos 400

    show juan parado izquierda:
        xpos 1850
        ypos 450
    
    show juan camina izquierda:
        linear 2 xpos 1600

    pause 2

    show juan parado izquierda:
        xpos 1600

    "Es entonces que ve a este ser extraño al que no reconoce. No siente miedo, pero tampoco le entusiasma
    la idea de acercarse a él."

    "Este ser lo llama y le pide que se acerque."

    vendedor "No temas, muchacho. Acércate, que tengo una misión para ti."

    "Juan duda, pero la intriga lo lleva a caminar a este ser cuyo nombre aún desconoce."

    show juan camina izquierda:
        linear 3 xpos 950 ypos 420

    pause 3

    show juan parado izquierda:
        xpos 950 
        ypos 420

    vendedor "Yo no soy más que un mercader. Me conocen como el Vendedor ambulante."
    vendedor "Como bien sabrás, un vendedor sólo puede mantenerse de las ventas si consigue ofrecer
            a sus clientes los mejores productos."
    vendedor "A mí me encanta ofrecer sólo lo mejor de lo mejor, y resulta que algo que uno de mis
            clientes busca se encuentra aquí, en este pueblo que tú seguramente llamas hogar."
    vendedor "Necesito tu ayuda para encontrarlo, pues poco conozco sobre este lugar en el que 
            me encuentro y en cuanto te he visto, he sabido que eres el indicado."
    vendedor "¿Puedes ayudarme a encontrar lo que busco?"

    "Juan no sabe qué decir, su curiosidad lo hace querer acceder de inmediato, aunque ni siquiera
    sabe qué es lo que el Vendedor ambulante busca."

    "Por otro lado, podría ser peligroso seguir a este extraño a un lugar desconocido a buscar
    quien sabe qué y, de ayudarlo, corre con el riesgo de no llegar a tiempo a su puesto de bombero."

    "Los cruzoob podrían atacar en cualquier momento y él necesita estar ahí si eso
    sucede, y no quiere arriesgar su responsabilidad por un desconocido."

    menu:
        "¿Deseas acompañar al vendedor ambulante en su búsqueda, arriesgando llegar tarde a tu
        puesto como bombero y que ocurra un ataque en ese momento?"
        "Sí, quiero acompañar al Vendedor ambulante":
            play sound "seleccion.mp3"
            $ ayudoVendedor = True
            jump juan_ayuda_ambulante
        "No, no deseo arriesgar la seguridad de Tixcacal":
            play sound "seleccion.mp3"
            $ ayudoVendedor = False
            jump juan_no_ayuda_ambulante
        

##################### Inicia Juan ayuda Vendedor Ambulante #####################
label juan_ayuda_ambulante:
    juan "Está bien. Te ayudaré en tu búsqueda. ¿Qué debo hacer?"

    vendedor "Para encontrar el objeto debemos pasar por un camino que se encuentra siempre oculto y 
            que sólo aparece ante aquellos que se atreven a resolver un acertijo."
    vendedor "Pero antes de eso necesitamos llegar al lugar donde se pide la oportunidad de encontrar 
            el camino."
    vendedor "Lo único que sé sobre ese lugar es que debe haber un árbol enorme, ¿sabes dónde puede estar?"

    juan "Sí, hay un camino aquí que tiene un gran árbol en el centro. No es muy lejos.
        Sígueme."

    vendedor "Muy bien, muchacho. Guía el camino entonces."

    show juan camina derecha:
        linear 4 xpos 1900

    show vendedor quieto:
        linear 5 xpos 1900

    pause 5

    jump en_el_gran_arbol

label en_el_gran_arbol:
    scene gran_arbol

    show juan camina derecha:
        xpos 0 ypos 400
        linear 2.5 xpos 220

    pause 2.5

    show juan parado derecha
    
    juan "Listo, ya estamos a..."

    show juan parado izquierda
    pause 1

    "El vendedor ambulante, que supuestamente venía detrás de Juan, ya no está."

    show juan parado atras
    pause 1

    show juan parado frente
    pause 1

    show juan parado derecha

    "Juan voltea para todos lados, pero no lo encuentra."

    play sound "vendedor_efecto.mp3"

    show vendedor quieto with hpunch:
        xpos 310 ypos 390

    show juan camina derecha:
        linear 0.05 xpos 180
    
    show juan parado derecha

    vendedor "Sí, naturalmente más eficiente que caminar todo el tramo."
    juan "Casi me matas de un susto, ¿por qué hiciste eso?"
    vendedor "Me he cansado de seguirte a medio camino, así que me detuve a descansar 
            por un rato y luego me he transportado a dónde te encontrabas en ese momento,
            que es aquí."
    vendedor "¿Verdad que ha sido de lo más impresionante?"
    juan "Impresionante no es la palabra que yo usaría, más bien ruidoso."
    vendedor "Pequeños defectos para una magia tan maravillosa."
    juan "Ya estamos aquí, ¿qué debemos hacer ahora?"
    vendedor "Ahora debemos llamar a los dioses y pedirles que nos muestren el camino."
    juan "¿Y cómo hacemos eso?"
    vendedor "Primero necesitamos una vela."

    show vela:
        xpos 550 ypos 500

    juan "¿No te parece peligroso poner una vela tan cerca del árbol? Sobre todo una tan grande.
        Creo que mido casi lo mismo que esa vela."

    vendedor "Silencio, muchacho. Necesito calma y concentranción."

    "Juan se mantiene callado mientras ve al vendedor ambulante hacer absolutamente nada."
    "Pareciera estar pensando en algo, así que sólo puede asumir que el vendedor se está 
    comunicando con alguien usando esos desconocidos poderes suyos."

    vendedor "Los dioses me están haciendo varias preguntas, pero no sé qué responder, necesito tu ayuda."

    menu problema_division_1:
        vendedor "Juan Cupul tiene 36 machetes y los tiene que repartir entre 6 campesinos de la comunidad. 
        ¿Cuántos machetes le debe dar a cada campesino?"
        "4 machetes":
            play sound "error.mp3" volume 4.0
            "¡Casi lo tienes, estás cerca! Pero la respuesta no es la correcta."
            jump problema_division_1
        "5 machetes":
            play sound "error.mp3" volume 4.0
            "¡Vamos de nuevo!"
            jump problema_division_1
        "6 machetes":
            play sound "acierto.mp3"
            "¡Excelente, ahí lo tienes! Juan Cupul debe dar 6 machetes a cada campesino."
        "30 machetes":
            play sound "error.mp3" volume 4.0
            "¡Vuelve a intentarlo, tú puedes!"
            jump problema_division_1
    
    menu problema_division_2:
        vendedor "Durante la cosecha de tomates Juan Cupul recolecta 72 kilos y se los 
        quiere regalar a 9 familias que viven cerca de su casa, ¿cuántos kilos de tomate 
        le regalará a cada familia?"
        "7 kilos":
            play sound "error.mp3" volume 4.0
            "¡Casi lo tienes, estás cerca! Pero la respuesta no es la correcta."
            jump problema_division_2
        "8 kilos":
            play sound "acierto.mp3"
            "¡Excelente, lo has conseguido! Juan Cupul le regalara 8 kilos de tomate a cada familia."
        "13 kilos":
            play sound "error.mp3" volume 4.0
            "¡Vuelve a intentarlo, tú puedes!"
            jump problema_division_2
        "63 kilos":
            play sound "error.mp3" volume 4.0
            "¡Vamos de nuevo!"
            jump problema_division_2
    
    menu problema_division_4:
        vendedor "Juan Cupul está ayudando a sus vecinos a prepararse para el invierno. 
                Han cortado 60 troncos de árboles y desean dividirlos igualmente entre 5 hogares. 
                ¿Cuántos troncos recibirá cada hogar?"
        "8 troncos":
            play sound "error.mp3" volume 4.0
            "¡Vamos de nuevo!"
            jump problema_division_4
        "11 troncos":
            play sound "error.mp3" volume 4.0
            "¡Casi lo tienes, estás cerca! Pero la respuesta no es la correcta."
            jump problema_division_4
        "12 troncos":
            play sound "acierto.mp3"
            "¡Buen trabajo, lo has conseguido! Has apoyado mucho a Juan Cupul."
        "55 troncos":
            play sound "error.mp3" volume 4.0
            "¡Vuelve a intentarlo, tú puedes!"
            jump problema_division_4

    vendedor "Muchas gracias, muchacho. Dame un segundo más."
    vendedor "Ya está."

    scene arboles_doblado with hpunch
    play sound "audio/vendedor_efecto.mp3"

    show gallina_1 quieta:
        xpos 350 ypos 600

    show vendedor quieto:
        xpos 310 ypos 390

    show juan parado derecha:
        xpos 180 ypos 400

    "De la nada, ya están en otro lugar."

    vendedor "Espero te encuentres bien, muchacho, la transportación inmediata suele sentar
            muy mal la primera vez."

    juan "Estoy bien, sólo... No vuelvas a hacerlo."
    vendedor "Eso no puedo prometerlo. ¡Ah, mira! Ahí está. Es perfecta."

    "Lo único que Juan ve es a una gallina haciendo nada en el camino."

    vendedor "Es exactamente lo que necesitaba."
    juan "¿Lo que estabas buscando era una gallina?"
    vendedor "No cualquier gallina, muchacho. Mira este maravilloso ejemplar haciendo 
            cosas que ninguna otra gallina puede hacer."
    
    show gallina_1 come

    juan "Esa gallina está comiendo. Como cualquier otra."
    vendedor "Hay que saber diferenciar al diamante del zafiro, muchacho. Este es un 
            ejemplar muy especial y procederé a añadirlo a mi cesta de inmediato."

    show cesta:
        xpos 360 ypos 390
    pause 1
    hide gallina_1 come
    show gallina_1 quieta:
        xpos 350 ypos 600
        linear 1.5 xpos 440 ypos 535
    pause 2
    hide gallina_1 quieta

    vendedor "Bien, ya tengo lo que buscaba. Muchas gracias por tu ayuda."
    juan "De nada, la experiencia ha sido muy... interesante."
    vendedor "Por tu ayuda, me tomaré la libertad de obsequiarte algo."

    show calavera:
        xpos 250 ypos 500

    "Una calavera gigante con una vela encendida encima es lo que aparece ante Juan."

    vendedor "No cometas el error de confundir al diamante con zafiro, muchacho. 
            Esta no es una calavera ordinaria."
    vendedor "Tiene el poder de despertar al ser vivo de tu elección de cualquier 
            tipo de sueño. Cuídala bien. La necesitarás en el futuro."
    
    menu:
        "El vendedor ambulante le ha obsequiado un objeto mágico a Juan Cupul. Si lo 
        aceptas, se añadirá a tu inventario y podrás usarlo en un momento específico
        de la historia en el futuro. ¿Deseas conservar el obsequio del vendedor ambulante?"
        "Sí, quiero quedármelo.":
            play sound "seleccion.mp3"
            $ conservaObjeto = True
            pause 1.0
            hide calavera
            jump acepta_objeto
        "No, no creo necesitarlo.":
            play sound "seleccion.mp3"
            jump no_acepta_objeto

label acepta_objeto:
    juan "Muchas gracias. La voy a cuidar muy bien."
    jump adios_vendedor

label no_acepta_objeto:
    juan "Agradezco el gesto, pero no creo que necesitar un objeto mágico. Será mejor que 
        lo conserves tú."
    vendedor "Es tu decisión, muchacho."
    hide calavera
    jump adios_vendedor

label adios_vendedor:
    vendedor "Pues bien, yo me despido. Ya no nos volveremos a ver, pero sin duda alguna 
            conservaré un buen recuerdo sobre ti."

    hide cesta
    hide vendedor quieto with hpunch
    play sound "vendedor_efecto.mp3"

    juan "No me acostumbraría jamás a eso."

    show juan camina frente:
        linear 3 ypos 1000
    pause 3

    jump en_la_cabana_bombero

#################### Termina Juan ayuda Vendedor Ambulante ####################

label juan_no_ayuda_ambulante:
    juan "Lo siento, pero tengo algo que hacer justo ahora y no puedo distraerme.
        Tal vez en otro momento."

    vendedor "Pues bien, sólo me queda desearte suerte, muchacho, dado que no nos
            volveremos a encontrar. "
    
    "Y el Vendedor ambulante desaparece."

    hide vendedor quieto with wipeup

    "Juan siente miedo por un segundo, pero se lo quita de encima. Tiene una responsabilidad
    que cumplir."

    juan "Si era un fantasma, no quiero saber."

    show juan camina izquierda:
        linear 3.5 xpos 0

    pause 3.5

    jump en_la_cabana_bombero

label en_la_cabana_bombero:
    scene cabana_bombero

    show fili parado derecha:
        xpos 520
        ypos 410
    
    show juan parado izquierda:
        xpos 1850
        ypos 520
    
    show juan camina izquierda:
        linear 6 xpos 620 ypos 410

    pause 6

    show juan parado izquierda:
        xpos 610
        ypos 410

    filiberto "Juan, qué bueno que llegaste. Tenemos un problema."
    juan "¿Un problema? ¿Qué pasó?"

    python:
        if ayudoFili == True:
            dialogoRoboAgua = "El agua que obtuvimos del pozo de tu casa ya no está. Desaparecieron las cubetas."
        else:
            dialogoRoboAgua = "Las cubetas con agua que dejé antes de irme a desayunar ya no están."

    filiberto "[dialogoRoboAgua]"
    juan "¿Estás seguro? ¿No será que alguien vino y las movió de lugar? 
        ¿Buscaste en toda la cabaña?"
    filiberto "Sí, en toda la cabaña y alrededor de ella. No hay rastros del agua."
    filiberto "No tiene sentido que desapareciera. Somos los únicos que deberían estar aquí hoy."
    juan "Es extraño, pero no podemos descartar que alguien pasara y se la llevara, aunque no estoy
        seguro de por qué."
    filiberto "¿Y si llegaron los cruzoob y se la llevaron?"
    juan "Podría ser. Pero, de ser así, no habrían desperdiciado la oportunidad de atacar si pudieron
        tomarse el tiempo de robarse el agua."
    filiberto "Hay algo que no está bien aquí, Juan."
    juan "Por ahora, lo único que podemos hacer es no abandonar nuestro puesto. Si de verdad van a atacar,
        hay que asegurarnos de avisar a los demás."
    filiberto "De acuerdo, iré por más agua entonces. Voy al río, no me tardo."

    show fili camina derecha:
        linear 3 xpos 1900

    pause 3

    hide fili camina derecha

    show juan parado derecha

    "Filiberto se va y Juan se queda solo."

    jump maria_alimenta_animales


#! Hay un problema con el guardado de los datos de las partidas. La primera vez
#! que esos datos se guardan, se mantienen bien y todo. Pero si te sales de una
#! partida, la guardas, cierras la app, la vuelves a abrir, cargas esa partida
#! de nuevo y sobreescribes tu nuevo avance en la misma ranura, los datos 
#! anteriomente guardados se pierden. No sé por qué, pero eso es lo que sucede. 
#! Probablemente por eso tenía problemas para enseñar el nombre antes cuando 
#! intentaba crear la pantalla para mostrar los datos de la partida. 
#! Tengo que averiguar cómo resolver eso o buscar una alternativa para ese 
#! guardado dinámico de datos porque me está causando muchos problemas.

# Misión en la que María Dolores "alimenta" a los animales después de que el 
# resuelve correctamente tres ejercicios
label maria_alimenta_animales:
    scene corral_animales

    show novia parada frente:
        xpos 895 ypos 400

    show puerquito1 quieto:
        xpos 200 ypos 300
    show puerquito2 quieto:
        xpos 277 ypos 600
    show puerquito3 quieto:
        xpos 375 ypos 400

    show gallina_1 quieta:
        xpos 1350 ypos 400
    show gallina_2:
        xpos 1500 ypos 450
    show gallina_3:
        xpos 1780 ypos 600
    show gallina_4:
        xpos 1700 ypos 350
    show pollito:
        xpos 1730 ypos 350
    show pavo:
        xpos 1350 ypos 650

    "María Dolores aprovecha el tiempo en el que no está Juan para cuidar de sus 
    animales."

    prometida "Muy bien. Es hora de alimentarlos."

    "María quiere alimentar a sus animales. Para que ella pueda alimentar a los 
    cochinos, las gallinas y el pavo, debes resolver tres ejercicios."

    menu problema_division_5:
        "En la feria agrícola, Juan Cupul obtuvo 45 paquetes de semillas. Quiere 
        distribuirlos de manera igualitaria entre 9 agricultores de la comunidad. 
        ¿Cuántos paquetes de semillas recibirá cada agricultor?"
        "4 paquetes":
            play sound "error.mp3" volume 4.0
            "¡Casi lo tienes, estás cerca! pero la respuesta no es la correcta."
            jump problema_division_5
        "5 paquetes":
            play sound "acierto.mp3" 
            "¡Muy bien, lo has conseguido!"
        "28 paquetes":
            play sound "error.mp3" volume 4.0
            "¡Vamos de nuevo!"
            jump problema_division_5
        "36 paquetes":
            play sound "error.mp3" volume 4.0
            "¡Vuelve a intentarlo, tú puedes! Lee nuevamente el ejercicio."
            jump problema_division_5

    menu problema_multiplicacion_4:
        "Después de la batalla que se dio en Tixcacal se empezó a recolectar despensa 
        para los heridos; cada día se juntó 1 caja de mercancía y en cada una 
        había 14 bolsas de frijol. ¿Cuántas bolsas de frijol se juntaron a la semana?"
        "2 bolsas de frijol":
            play sound "error.mp3" volume 4.0
            "Sigue practicando, cada intento te acerca más al éxito."
            jump problema_multiplicacion_4
        "7 bolsas de frijol":
            play sound "error.mp3" volume 4.0
            "No te desanimes, sigue intentándolo."
            jump problema_multiplicacion_4
        "21 bolsas de frijol":
            play sound "error.mp3" volume 4.0
            "Ups, parece que esta respuesta no es la correcta."
            jump problema_multiplicacion_4
        "98 bolsas de frijol":
            play sound "acierto.mp3"
            "Muy bien, se multiplica el total de días de la semana (7) por las 
            14 bolsas de frijol que se juntó en cada uno de esos días. "

    menu problema_multiplicacion_5:
        "Para armar una estrategia de batalla Juan Cupul organizó una reunión con 
        sus aliados, para ello acomodó 4 mesas y en cada mesa colocó 8 sillas. ¿A 
        cuántos aliados invitó Juan Cupul para la reunión?"
        "2 aliados":
            play sound "error.mp3" volume 4.0
            "Sigue practicando, cada intento te acerca más al éxito."
            jump problema_multiplicacion_5
        "4 aliados":
            play sound "error.mp3" volume 4.0
            "Vamos, inténtalo otra vez."
            jump problema_multiplicacion_5
        "12 aliados":
            play sound "error.mp3" volume 4.0
            "Ups, parece que esta respuesta no es la correcta."
            jump problema_multiplicacion_5
        "32 aliados":
            play sound "acierto.mp3"
            "Lo estás resolviendo muy bien, la respuesta se obtiene multiplicando 
            el número de mesas (4) por la cantidad de sillas que va en cada mesa (8)."

    "María alimenta a los cochinos, las gallinas y los pavos."

    show gallina_1 come

    prometida "¿De verdad? ¿Sólo Paquita quiere comer?"

    show puerquito1 revolcado
    show puerquito3 revolcado

    prometida "Bien, yo ya hice mi parte."

    show novia camina atras:
        linear 1.5 ypos 0
    pause 1.5

    jump comprar_super_gallina

# María recorre un largo camino para encontrar al Vendedor ambulante y comprar 
# una supuesta gallina mágica
label comprar_super_gallina:
    scene afuera_casa_juan

    show novia parada frente:
        xpos 895 ypos 700
    
    "María Dolores está saliendo de su casa de nuevo, luego de haber alimentado 
    a sus animales."

    "Escuchó en el camino de regreso a unas personas hablando de un vendedor 
    que ofrece objetos mágicos a un buen precio. Velas que nunca se apagan, 
    gallinas que te vuelven súper fuerte si las comes en caldo, un gato que te 
    traerá suerte en el amor."

    "Ella está decidida a comprar esa gallina para Juan."

    prometida "Bien, es hora de encontrar a ese vendedor."

    show novia camina frente:
        linear 1.5 ypos 1000
    pause 1.5

    # Primera bifurcación
    scene A10

    show novia camina frente:
        xpos 895 ypos 0
        linear 1.5 ypos 480
    pause 1.5
    show novia parada frente

    prometida "Ahora, ¿a dónde se supone que debo ir?"

    "Las personas habían mencionado que encontrar el camino al vendedor era 
    complicado porque te confundes y pierdes mucho mientras lo buscas. "
    "Lo único que mencionaron que sí fue de ayuda fue que se puede encontrar un 
    letrero de una pócima cuando ya estás en el camino correcto."

    prometida "¿Derecha...?"
    show novia parada derecha
    prometida "¿... O frente?"
    show novia parada frente

    "María Dolores intenta concentrarse para escoger el camino correcto."

    prometida "Bien, lo más fácil sería dejarlo al azar, pero no quiero estar 
    dando vueltas todo el día."

    "Ayuda a María Dolores contestando correctamente un ejercicio cada que ella 
    necesite cambiar de dirección hasta que encuentre el camino al vendedor."

    menu problema_suma_4:
        "Durante la lucha en 1847, Juan Cupul salvó a 40 niños y 25 ancianos. Si 
        cada anciano representa 2 unidades y cada niño representa 1 unidad, 
        ¿cuántas unidades en total salvó Juan Cupul?"
        "65":
            play sound "error.mp3" volume 4.0
            "Sigue intentado, estoy seguro de que la próxima será la correcta."
            jump problema_suma_4
        "80":
            play sound "error.mp3" volume 4.0
            "Ups, parece que esta respuesta no es la correcta. ¡No te rindas, sigue practicando!"
            jump problema_suma_4
        "90":
            play sound "acierto.mp3"
            "¡Buen trabajo! La respuesta es correcta."
        "100":
            play sound "error.mp3" volume 4.0
            "¡Casi lo tienes! pero esta vez la respuesta no es la correcta."
            jump problema_suma_4

    prometida "Hacia el frente, tiene que ser hacia el frente."
    
    show novia camina frente:
        linear 2 ypos 1000
    pause 2
    
    # Segunda "bifurcación"
    scene A16

    show novia camina frente:
        xpos 895 ypos 0
        linear 1.5 ypos 450
    pause 1.5
    show novia parada frente

    prometida "¿Debería regresar o ir a la derecha?"

    menu problema_suma_6:
        "Juan Cupul tenía 25 caballos al comienzo de la sublevación. Después de 
        un enfrentamiento, perdió 8 caballos y ganó 13 más en una escaramuza 
        posterior. ¿Cuántos caballos tenía Juan Cupul al final?"
        "25 caballos":
            play sound "error.mp3" volume 4.0
            "Sigue intentado, estoy seguro de que la próxima será la correcta."
            jump problema_suma_6
        "30 caballos":
            play sound "acierto.mp3"
            "¡Espectacular! Parece que Juan Cupul tiene una manada impresionante de 
            caballos a su disposición."
        "34 caballos":
            play sound "error.mp3" volume 4.0
            "¡Casi lo tienes! pero esta vez la respuesta no es la correcta."
            jump problema_suma_4
        "35 caballos":
            play sound "error.mp3" volume 4.0
            "Ups, parece que esta respuesta no es la correcta. ¡No te rindas, sigue practicando!"
            jump problema_suma_4
    
    prometida "A la derecha."

    show novia camina derecha:
        linear 2 xpos 1600
    pause 2

    # Tercera bifurcación
    scene A15
    
    show novia camina derecha:
        xpos 0 ypos 480
        linear 2 xpos 880
    pause 2
    show novia parada derecha

    menu problema_resta_3:
        "Juan Cupul cosechó 63 tomates en su campo y después regaló 25 a sus 
        vecinos. ¿Cuántos tomates le quedaron a Juan después de regalar algunos?"
        "3 tomates":
            play sound "error.mp3" volume 4.0
            "¡Puedes encontrar la respuesta!"
            jump problema_resta_3
        "14 tomates":
            play sound "error.mp3" volume 4.0
            "Vuelve a intentarlo, ¡tú puedes!"
            jump problema_resta_3
        "38 tomates":
            play sound "acierto.mp3"
            "¡Tienes esto! La respuesta es correcta."
        "88 tomates":
            play sound "error.mp3" volume 4.0
            "¡Estás haciendo un gran trabajo! Imagina cuántos tomates tenía Juan 
            en total y cuántos decidió regalar."
            jump problema_resta_3

    show novia camina frente:
        linear 2 ypos 1000
    pause 2

    # Cuarta "bifurcación"
    scene arboles_doblado

    show novia camina frente:
        xpos 900 ypos 0
        linear 1.5 ypos 430
    pause 1.5
    show novia parada frente

    prometida "No estoy segura de esto, ¿debería regresar?"

    menu problema_resta_5:
        "Juan Cupul tenía 60 tablones para construir un puente y usó 27. ¿Cuántos tablones le quedan?"
        "31 tablones":
            play sound "error.mp3" volume 4.0
            "¡Sigue adelante, estás en el buen camino!"
            jump problema_resta_5
        "33 tablones":
            play sound "acierto.mp3"
            "¡Hiciste un buen trabajo, has llegado a la respuesta correcta!"
        "35 tablones":
            play sound "error.mp3" volume 4.0
            "Intenta recordar cuántos tablones tenía Juan para construir el puente 
            y cuántos utilizó."
            jump problema_resta_5
        "37 tablones":
            play sound "error.mp3" volume 4.0
            "¡Tú puedes hacerlo, sigue intentando!"
            jump problema_resta_5

    prometida "No tiene caso regresar, ya llegué hasta aquí."

    show novia camina izquierda:
        linear 1.8 xpos 200
    pause 1.8
    show novia camina frente:
        linear 2 ypos 1000
    pause 2

    # Encuentra el letrero
    scene A12

    show novia camina frente:
        xpos 895 ypos 0
        linear 1.5 ypos 300
    pause 1.5
    show novia parada frente

    prometida "¡El letrero! ¡Este es el camino correcto!"

    show novia camina frente:
        linear 1.5 ypos 1000
    pause 1.5

    # Llega con el Vendedor ambulante
    scene A14

    show vendedor quieto:
        xpos 1220 ypos 670

    show novia camina frente:
        xpos 200 ypos 0
        linear 1.5 ypos 355
    pause 1.5
    show novia parada frente

    prometida "¡Llegué!"

    # Camina al puesto del Vendedor ambulante
    show novia camina frente:
        linear 1.5 ypos 900
    pause 1.5
    show novia camina derecha:
        linear 2.5 xpos 1220
    pause 2.5
    show novia camina atras:
        linear 0.5 ypos 800
    pause 0.5
    show novia parada atras

    prometida "Buenas tardes."
    vendedor "Buenas tardes, señorita. Soy el Vendedor ambulante. Pídame lo 
                que quiera, vendo de todo. ¿Qué puedo ofrecerle?"
    prometida "Escuché que usted vende una gallina que puede hacerte muy fuerte 
                si se come en caldo."
    vendedor "Y así es."

    python:
        labelGallina = ""
        if ayudoVendedor:
            labelGallina = "tiene_gallina"
        else:
            labelGallina = "no_tiene_gallina"

    jump expression labelGallina

# El Vendedor ambulante sí tiene la gallina (Juan sí lo ayudó)
label tiene_gallina:
    vendedor "Es tu día de suerte, porque justo hoy encontré una con la ayuda de 
    un amable muchacho."
    prometida "Excelente, pues me la llevo."

    "María le paga al Vendedor ambulante y él envía la gallina a su casa."

    play sound "vendedor_efecto.mp3"

    "María se asusta al oír una explosión."

    prometida "¡¿Qué fue eso?! ¡Nos atacan!"
    vendedor "No se preocupe, señorita. He sido yo. Envié a la gallina a su casa 
                usando mi magia de transportación inmediata."
    prometida "¿O sea que la gallina ya está en mi casa?"
    vendedor "Así es. En su jardín delantero, si debo ser específico."
    prometida "Pues ¡muchas gracias!"
    vendedor "A ti, señorita. Si regresas otro día, te prometo que te regalaré 
                un vestido que jamás se ensucia y tampoco se rompe."
    prometida "Es muy amable, me aseguraré de volver, ¡hasta pronto!"
    vendedor "¡Nos vemos!"

    show novia camina frente:
        linear 0.5 ypos 900
    pause 0.5
    show novia camina izquierda:
        linear 2.5 xpos 400
    pause 2
    
    jump fili_desaperece

# El Vendedor ambulante no tiene la gallina (Juan no lo ayudó)
label no_tiene_gallina:
    vendedor "Lamentablemente, hoy no tengo ninguna en mi maravilloso inventario.
            No soy capaz de hallarlas solo y nadie en mi camino estuvo dispuesto 
            a ayudarme."
    prometida "Es una lástima. Vine hasta aquí sólo por esa gallina."
    vendedor "Me siento muy apenado, señorita. Le diré algo. Le prometo conseguir 
            una de esas gallinas especiales para la próxima semana, y como bono 
            por las molestias, le regalaré un vestido que jamás se ensucia o se rompe."
    prometida "¿En serio?"
    vendedor "Lo prometo y juro en este momento ante la presencia de nuestros dioses 
            que nos vigilan desde lo más alto."
    prometida "De acuerdo. Acepto entonces. Volveré la próxima semana."
    vendedor "Nos vemos hasta entonces."
    prometida "Hasta luego."

    show novia camina frente:
        linear 0.5 ypos 900
    pause 0.5
    show novia camina izquierda:
        linear 2.5 xpos 400
    pause 2
    
    jump fili_desaperece

# Filiberto va en busca del agua, pero lo noquean cuando encuentra el río
label fili_desaperece:
    scene camino_v_osc

    "Filiberto camina con prisa, esperando obtener el agua lo más pronto posible."
    "Tiene la rara sensación de que algo no va bien. No es normal que cuatro cubetas 
    de agua desaparezcan así como así."
    
    show fili camina derecha:
        xpos 0
        ypos 450
    
    show fili camina derecha:
        linear 3 xpos 1850

    pause 3

    scene casa_naranja

    show fili camina derecha:
        xpos 100
        ypos 400
    
    show fili camina derecha:
        linear 2 xpos 900

    pause 2

    show fili parado derecha

    "Llega a una chopcalle y, de repente, siente que no sabe por dónde ir."

    filiberto "¿Cuál era el camino? ¿Cuál era el camino?"

    show fili parado atras
    pause 1.5
    show fili parado frente
    pause 1.5
    show fili parado derecha

    filiberto "He vivido aquí toda mi vida y de la nada no sé cuál es el camino."

    "Filiberto se desespera, no entendiendo por qué no se acuerda."

    filiberto "Bien, pues escogeré al azar. Lo peor que puede pasar es que tenga que regresar 
    y tomar el otro camino."

    filiberto "De tín marín de..."

    "Filiberto está escogiendo al azar. Ayúdalo a que el camino elegido sea el correcto 
    resolviendo exitosamente el siguiente ejercicio."

    menu problema_suma_3:
        "Durante la 'Guerra de Castas', Juan Cupul caminó 2 horas y 40 minutos para llegar 
        al frente de batalla. Si comenzó su marcha a las 6:20 AM, ¿a qué hora llegó?"
        "8:00 AM":
            play sound "error.mp3" volume 4.0
            "¡Casi lo tienes! Pero esta vez la respuesta no es la correcta."
            jump problema_suma_3
        "8:20 AM":
            play sound "error.mp3" volume 4.0
            "Sigue intentando, estoy de que la próxima será la correcta."
            jump problema_suma_3
        "9:00 AM":
            play sound "acierto.mp3"
            "¡Fantástico! Parece que Juan Cupul tiene un buen ritmo para llegar a tiempo 
            a la batalla."
        "9:40 AM":
            play sound "error.mp3" volume 4.0
            "Ups, parece que esta respuesta no es la correcta. ¡No te rindas, sigue practicando!"
            jump problema_suma_3

    filiberto "... pégale, pégale que ella fue."
    pause 0.1
    show fili parado frente

    filiberto "Bien, el camino de abajo será."

    show fili camina frente:
        linear 3 ypos 1000
    
    pause 3

    #Fili llega al río
    scene puente_rio

    show fili camina frente:
        xpos 0.46 ypos 0
        linear 1 ypos 180
    pause 1
    show fili parado frente

    filiberto "¡Eso es todo!"
    filiberto "Ahora a conseguir esa agua."

    show fili camina frente:
        linear 2 ypos 500
    pause 2
    show fili parado frente

    cruzob "¿A dónde vas tan apurado? ¿Cuál es la prisa?"

    show fili parado atras
    filiberto "¡¿Quién anda ahí?!"

    "Filiberto, ya ansioso a causa de la desaparición del agua, sabe que esa persona 
    no tiene, en absoluto, buenas intenciones."

    cruzob "¿Por qué no intentas adivinar?"
    filiberto "¡No tengo tiempo para juegos! ¡Sal ya!"

    # Cruzob "sale" del árbol
    show hombre camina derecha:
        xpos 0.35 ypos 50
        linear 1 xpos 0.46
    pause 1
    show hombre parado frente

    cruzob "Un gusto conocerte, Filiberto, aunque no para ti."

    "El cruzoob no duda. Corre a Filiberto y lo noquea en un segundo."

    # Cruzob avanza hasta Fili
    show hombre camina frente:
        linear 1 ypos 470
    pause 1
    show hombre parado frente
    hide fili parado atras

    # Fili en posición de morido
    show fili_parado_atras_2:
        xpos 0.46 ypos 500
        linear 0.1 rotate 90
    
    cruzob "Espero que tu primo tenga un poco más de resistencia que tú, Fili."
    cruzob "Es hasta vergonzoso lo fácil que fue."
    jump ataque


label ataque:
    scene cabana_bombero with fade
    show juan parado derecha:
        xpos 610 ypos 410

    "Juan no tiene nada qué hacer en este momento, más que vigilar."
    "Pasa mucho tiempo, pero Filiberto no regresa."

    show hombre camina derecha:
        xpos 0 ypos 800
        linear 1 xpos 100
    pause 1.0
    show hombre parado derecha

    juan "¿Qué habrá sucedido con Filiberto? Si no iba tan lejos."

    "Juan se enoja, pensando que Filiberto lo ha abandonado para relajarse un rato."

    juan "Si quería descansar, como mínimo me pudo haber avisado."

    "Para distraerse, analiza lo que ocurrió con el agua."

    juan "Es muy sospechoso que el agua desapareciera."
    
    show hombre camina derecha:
        linear 1 xpos 200
    pause 1.0
    show hombre parado derecha

    juan "Mientras más lo analizo, menos sentido tiene."

    show hombre camina derecha:
        linear 1 xpos 300
    pause 1.0
    show hombre parado derecha

    juan "Aunque, si yo fuera un cruzoob, intentaría..."

    show hombre camina derecha:
        linear 1 xpos 485
    pause 1.0
    show hombre parado atras

    play music "audio/pelea.mp3"

    cruzob "¿Separar a tu enemigo? Sí, nosotros pensamos exactamente igual."

    show juan parado frente

    show hombre camina atras:
        linear 3 xpos 610 ypos 490
    pause 3
    show hombre parado atras

    cruzob "Te estarás preguntando dónde está tu primo. Mi compañero le hizo una 
            visita mientras iba por el agua. No te preocupes. No le ha hecho 
            mucho daño. Todavía."
    cruzob "Lo dejó inconsciente, y ahora me toca a mí encargarme de ti en lo 
            que los demás llegan."

    "El primer impulso de Juan es saltar para alcanzar la bomba y avisar de que 
    hay cruzoob en el pueblo."

    show juan camina derecha

    show hombre camina atras:
        linear 0.5 xpos 655 ypos 410
    pause 0.5

    show hombre camina izquierda:
        linear 0.5 xpos 640
    
    show juan camina derecha:
        linear 1 xpos 550

    pause 1

    show juan parado derecha
    show hombre parado izquierda

    cruzob "Ni se te ocurra tocar esa bomba, Juan Cupul. "
    cruzob "Lo que tú debes hacer justo ahora es enfrentarte a mí, no avisarle nada a nadie."

    "Juan sabe que necesita vencer a este cruzoob si quiere alcanzar la bomba."

    juan "Pues hay que acabar con esto rápido."

    menu:
        "Durante la sublevación en 1847, Juan Cupul luchó contra las tropas enemigas durante 
        2 horas y 20 minutos. Si comenzó la lucha a las 9:45 AM, ¿a qué hora terminó?"
        "11:05 AM":
            play sound "error.mp3" volume 4.0
            "No hay segundas oportunidades en el campo de batalla."
        "11:15 AM":
            play sound "error.mp3" volume 4.0
            "No hay segundas oportunidades en el campo de batalla."
        "12:05 PM":
            play sound "acierto.mp3"
            "¡Muy bien! Juan ha ganado un punto en la batalla."
            $ puntos = puntos + 1
        "12:25 PM":
            play sound "error.mp3" volume 4.0
            "No hay segundas oportunidades en el campo de batalla."
        
    menu:
        "Para la batalla que se aproximaba Juan Cupul decidió armar 5 escuadrones con 10 
        soldados en cada una y de esta manera enfrentar a los enemigos ¿Cuántos soldados 
        fueron en total los que apoyaron en la batalla?"
        "2 soldados":
            play sound "error.mp3" volume 4.0
            "Fallaste, así que Juan también."
        "5 soldados":
            play sound "error.mp3" volume 4.0
            "Fallaste, así que Juan también."
        "15 soldados":
            play sound "error.mp3" volume 4.0
            "Fallaste, así que Juan también."
        "50 soldados":
            play sound "acierto.mp3"
            "¡Excelente! Tal vez Juan pueda vencer al cruzoob."
            $ puntos = puntos + 1
    
    "Juan Cupul está enseñando técnicas de combate a 15 guerreros en su pueblo. 
        Quiere asegurarse de que todos reciban la misma cantidad de entrenamiento, 
        así que divide el tiempo de entrenamiento igualmente entre ellos. "
        
    menu:
        "Si tiene 45 horas de entrenamiento, ¿cuántas horas recibe cada guerrero?"
        "2 horas":
            play sound "error.mp3" volume 4.0
            "Juan se ha equivocado porque tú te equivocaste."
        "3 horas":
            play sound "acierto.mp3"
            "¡Eso es todo! Juan puede triunfar."
            $ puntos = puntos + 1
        "356 horas":
            play sound "error.mp3" volume 4.0
            "Juan se ha equivocado porque tú te equivocaste."
        "1675 horas":
            play sound "error.mp3" volume 4.0
            "Juan se ha equivocado porque tú te equivocaste."

    menu:
        "Juan Cupul tenía 25 espadas y perdió 9 en una batalla. ¿Cuántas espadas le quedan?"
        "14 espadas":
            play sound "error.mp3" volume 4.0
            "Juan podría no vencer, lo has guiado mal."
        "16 espadas":
            play sound "acierto.mp3"
            "¡Triunfaste, y Juan también!"
            $ puntos = puntos + 1
        "18 espadas":
            play sound "error.mp3" volume 4.0
            "Juan podría no vencer, lo has guiado mal."
        "34 espadas":
            play sound "error.mp3" volume 4.0
            "Juan podría no vencer, lo has guiado mal."

    
    python:
        if puntos <= 2:
            if conservaObjeto == True:
                labelFinal = "usar_objeto"
            else:
                labelFinal = "perdiste"
        else:
                labelFinal = "juan_triunfa"

    jump expression labelFinal


label juan_triunfa:
    "Juan logra vencer al cruzoob."
    
    hide hombre parado izquierda with moveouttop

    juan "Es hora de explotar la bomba."

    "Juan enciende la bomba y corre a protegerse."

    show juan camina frente:
        linear 1 xpos 485 ypos 800
    
    pause 1

    show juan camina izquierda:
        linear 0.7 xpos 110

    pause 0.7

    show juan parado derecha
    pause 1.0

    play sound "audio/explosion.mp3"

    scene cabana_vacio with hpunch
    show cabana_milpa:
        xpos 50 ypos 150

    show juan parado derecha:
        xpos 110 ypos 800

    juan "Listo, ahora todos saben que hay cruzoob en el pueblo."

    show fili parado izquierda:
        xpos 1840 ypos 520
    
    filiberto "¡Juan! ¡Juan!"

    juan "¡Aquí estoy!"

    show juan camina derecha:
        linear 1.5 xpos 485
    
    pause 1.5

    show juan camina atras:
        linear 1.5 xpos 655 ypos 410

    show fili camina izquierda:
        linear 1.5 xpos 755 ypos 410

    pause 1.5

    show juan parado derecha
    show fili parado izquierda

    filiberto "Escuché que lograste explotar la bomba, ¿todo bien?"
    juan "Sí, todo bien. ¿Y tú? Me dijeron que te dejaron inconsciente."
    filiberto "No tengo nada. Vamos, hay que correr y ayudar. Afortunadamente me libré 
            de los cruzoob que me vigilaban, pero los demás están atacando el pueblo."
    juan "Vamos, vamos."

    show juan camina derecha:
        linear 2 xpos 1850
    show fili camina derecha:
        linear 2 xpos 1850 ypos 620

    pause 2.0
    hide juan camina derecha
    hide fili camina derecha

    "Gracias a que Juan logró vencer al cruzoob y explotó la bomba, avisaron al pueblo a tiempo."
    "Juan y Filiberto apoyaron a la gente de su hogar a combatir a los cruzoob invasores y los vencieron 
    en poco tiempo."
    "Juan y María Dolores se pudieron casar al día siguiente :)."

    jump despedida_final



menu usar_objeto:
    "Has perdido la batalla, ¿deseas usar el obsequio del vendedor ambulante para despertar 
    a Filiberto de la inconsciencia y así él llegue a tiempo a rescatarte?"
    "Sí, que mi primo me ayude":
        play sound "seleccion.mp3"
        "Muy bien, has decidido aceptar la ayuda de Filiberto."
        jump fili_ayuda
    "No, prefiero perder a ser rescatado":
        play sound "seleccion.mp3"
        jump perdiste

label fili_ayuda:
    show fili parado izquierda:
        xpos 1830 ypos 520
    
    filiberto "¡Juan! ¡Juan!"
    show hombre parado derecha

    filiberto "¡Oye! ¡Tú! Deja a mi primo en paz."

    show fili camina izquierda:
        linear 2 xpos 650 ypos 410

    pause 2.0
    hide hombre parado derecha with moveoutleft

    show fili parado izquierda

    filiberto "¿Estás bien, Juan?"
    juan "No, pero lo estaré. Ahora no hay tiempo que perder. Encendamos la bomba."

    show juan camina frente:
        linear 1 xpos 485 ypos 800
    show fili camina frente:
        linear 1 xpos 535 ypos 800
    pause 1

    show juan camina izquierda:
        linear 0.7 xpos 110
    
    show fili camina izquierda:
        linear 0.7 xpos 210

    pause 0.7

    show juan parado derecha
    show fili parado derecha
    
    play sound "audio/explosion.mp3"

    scene cabana_vacio with hpunch
    show cabana_milpa:
        xpos 50 ypos 150

    show juan parado derecha:
        xpos 110 ypos 800
    
    show fili parado derecha:
        xpos 210 ypos 800

    juan "Ya está, ahora todos saben que estamos bajo ataque."
    show fili parado izquierda
    filiberto "Pues hay que apurarnos, hay que ir a ayudar."

    "Juan y Fili corren para ir a ayudar a su pueblo."

    hide juan parado derecha
    hide fili parado izquierda

    "Gracias a que Filiberto despertó justo a tiempo para rescatar a Juan, lograron 
    dar el aviso lo suficientemente antes como para que Tixcacal se defendiera
    con éxito."
    "Tixcacal venció a los cruzoob."
    "Juan y María Dolores pudieron casarse al día siguiente :)."
    jump despedida_final

label perdiste:
    "Has perdido la batalla contra el cruzoob, te han vencido."
    hide hombre parado izquierda
    hide juan parado derecha
    "Lamentablemente, los cruzoob invadieron Tixcacal porque Juan nunca avisó 
    del ataque y Filiberto no despertó a tiempo para ir a ayudarlo."
    "Los cruzoob decidieron llevarse a Juan para que viera cómo hacían trizas su hogar."
    "Juan no pudo casarse con María Dolores al día siguiente :(."
    jump despedida_final

label despedida_final:
    play music "fondo3.mp3"
    scene fondo_final
    "Esto ha sido todo, ¡muchas gracias por leer Conquista matemática!"

    "Tu progreso se mantendrá en el mismo punto de la última vez que guardaste partida."
    "Si quieres guardar tu progreso para quedarte en el final, este es el momento."
    "Presiona Enter para terminar la partida y regresar al menú."
    pause

    return




























label Juan_irse_Dolores:
    hide filiberto_tun with dissolve

    show juan parado izquierda:
        xpos 0.51
        ypos 0.59

    show novia parada derecha:
        xpos 0.47
        ypos 0.59
    
    "Juan le explica a Dolores lo que sucede."

    prometida "Ya veo. Entonces eso es lo que pasó."
    juan "Lo siento. Sé que mañana es importante."
    prometida "No te preocupes. Sé lo importante que es esto. Ve, yo te estaré esperando aquí."
    juan "¡Gracias!"
    prometida "Cuando te sientas cansado, puedes volver aquí y te diré lo que necesites."
    juan "Nos vemos luego. Regresaré. Te lo prometo."
    prometida "Nos vemos."

    hide novia with dissolve

    "Juan se dirige a la casa de milpa que está al Oeste."
    #"Juan debe dirigirse a la casa de milpa que está al Oeste."

    #jump juan_milpa_oeste
    #jump ubicar_afuera_casa
    #jump mapa_6
    jump ir_milpa_oeste

label ir_milpa_oeste:
    scene camino_casa_juan
    with fade
    pause 0.5

    scene A4
    with fade
    pause 0.5

    scene A3
    with fade
    pause 0.5

    scene A2
    with fade
    pause 0.5

    scene A33
    with fade
    pause 0.5

    scene A35
    with fade
    pause 0.5

    show protagonista1:
        xpos 0.5
        ypos 0.5

    "Juan ve una estatua y se acerca a ella."
    "Su aparación le resulta extraña, sin importar que Filiberto ya le hubiera comentado. 
    Estaba claro que había problemas."
    "Cuando la toca —tal como Filiberto le indicó que hiciera—, la estatua le habla."

    estatua "Tienes que demostrar ser digno de la información que te ayudará a salvar a tu pueblo. 
    Y para lograrlo, tienes que contestar correctamente la siguiente pregunta."

    menu problema1_suma:
        "Durante la sublevación en 1847, Juan Cupul luchó contra las tropas enemigas 
        durante 2 horas y 20 minutos. Si comenzó la lucha a las 9:45 AM, ¿a qué hora terminó?"
        "11:05 AM":
            "¡Respuesta incorrecta!"
            jump problema1_suma
        "11:15 AM":
            "¡Respuesta incorrecta!"
            jump problema1_suma
        "12:05 AM":
            "¡Respuesta correcta!"
        "12:25 AM":
            "¡Respuesta incorrecta!"
            jump problema1_suma
    
    estatua "Muy bien, Juan Cupul. Has demostrado ser digno. Ahora escucha con atención."

    pause

    return