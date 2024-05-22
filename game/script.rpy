init python:
    puntosVictorias=0
    nombreUsuario = ""
    ayudoFili = False
    avatarElegido = ""
    
    def my_save(data):
        data["nombre_usuario"] = nombreUsuario
        data["puntos_victorias"] = puntosVictorias
        data["ayudo_a_fili"] = ayudoFili
        data["avatar_elegido"] = avatarElegido

    config.save_json_callbacks = [ my_save ]


#Inicio del juego #############################################################
label start:
    play music "audio/fondo.mp3"

    scene fondo_seleccionar_personaje with fade

    $ nombreUsuario = renpy.input("Escribe tu nombre")

    #jump seleccionar_avatar_1
    jump seleccion_avatar_1


#scene narracion with fade
#pause

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

    

    prometida "Buenos días. Veo que apenas te levantas."
    juan "Buenos días. Los preparativos para la boda de mañana me dejaron exhausto."
    prometida "Bueno, no te sobreesfuerces, no queremos que mañana no estés disponible."
    juan "No te preocupes, es lo que menos quiero."
    prometida "Bueno, ve afuera que Filiberto ha venido y dice que quiere hablar contigo."
    juan "Ya voy, debe ser importante."

    jump Filiberto_afuera_casa

    #hide protagonista1
    #with dissolve

    #hide prometida1
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
        "¿Deseas ayudar a Filiberto con las provisiones? Esta decisión te afectará más adelante."
        "Sí, ayudaré a Filiberto.":
            jump Ayuda_Fili
            $ ayudoFili = True
        "No, deseo ocupar mi tiempo en otra cosa.":
            jump No_ayuda_Fili

label No_ayuda_Fili:
    juan "Lo siento, Filiberto, pero ahora no tengo tiempo para ayudarte." 
    juan "María y yo aún necesitamos revisar unos detalles finales de la boda que no pueden esperar."
    filiberto "Lo entiendo. Ya encontraré a alguien. Nos vemos luego. No se te olvide que hoy nos toca
    hacer guardia."
    juan "Hasta luego, Filiberto."

    "Hasta aquí llegué."

    return

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
        "Si pueden llegar al huerto caminando en línea recta y la casa de Juan está hacia el norte, ¿qué camino deben tomar?"
        "El de arriba":
            "Este es el camino norte, sólo regresarían a la casa de Juan. Intenta de nuevo."
            jump camino_oeste
        "El de la izquierda":
            "¡Muy bien! El oeste está a la izquierda."
            jump llegan_a_huerto
        "El de la derecha":
            "Casi lo logras, pero este camino lleva al este. Trata de nuevo."
            jump camino_oeste

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

    "Para poder cosechar, necesitan saber cuánta comida recolectarán al final. 
    Ayúdalos a calcularlo."


    menu problema_5:
        "Juan Cupul y Filiberto recolectaron cierta cantidad de provisiones para la población 
        de Tixcacalcupul. Si en un día recolectaron 175 kg de maíz y 230 kg de frijoles, 
        ¿cuántos kilogramos de provisiones recolectaron en total?"
        "405 kg":
            "¡Maravilloso! Parece que Juan y Filiberto saben cómo recolectar la cantidad justa de provisiones."
            jump cosechar_verduras
        "345 kg":
            "Ups, parece que esta respuesta no es la correcta. ¡No te rindas, sigue practicando!"
            jump problema_5
        "400 kg":
            "¡Casi lo tienes! pero esta vez la respuesta no es la correcta."
            jump problema_5
        "305 kg":
            "Sigue intentado, estoy seguro de que la próxima será la correcta."
            jump problema_5
        
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

    "Me detuve aquí."

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