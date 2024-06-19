init python:
    puntos = 0
    labelFinal = ""
    puntosVictorias=0
    nombreUsuario = ""
    ayudoFili = False
    avatarElegido = ""
    conservaObjeto = False
    
    def my_save(data):
        data["nombre_usuario"] = nombreUsuario
        data["puntos_victorias"] = puntosVictorias
        data["ayudo_a_fili"] = ayudoFili
        data["conserva_objeto"] = conservaObjeto
        data["avatar_elegido"] = avatarElegido

    config.save_json_callbacks = [ my_save ]


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
    "Por ahora, personaliza un poco tu partida."

    $ nombreUsuario = renpy.input("Escribe tu nombre")

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
        "¿Deseas ayudar a Filiberto con las provisiones?"
        "Sí, ayudaré a Filiberto.":
            play sound "audio/seleccion.mp3"
            jump Ayuda_Fili
            $ ayudoFili = True
        "No, deseo ocupar mi tiempo en otra cosa.":
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

    #! Subir volumen del audio de error porque no se escucha con la canción de fondo encima

    menu camino_oeste:
        "Si pueden llegar al huerto caminando en línea recta y la casa de Juan está hacia el norte, ¿qué camino deben tomar?"
        "El de arriba":
            play sound "error.mp3" volume 4.0
            "Este es el camino norte, sólo regresarían a la casa de Juan. Intenta de nuevo."
            jump camino_oeste
        "El de la izquierda":
            play sound "acierto.mp3"
            "¡Muy bien! El oeste está a la izquierda."
            jump llegan_a_huerto
        "El de la derecha":
            play sound "error.mp3" volume 4.0
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
            play sound "acierto.mp3"
            "¡Maravilloso! Parece que Juan y Filiberto saben cómo recolectar la cantidad justa de provisiones."
            jump cosechar_verduras_2
        "345 kg":
            play sound "error.mp3" volume 4.0
            "Ups, parece que esta respuesta no es la correcta. ¡No te rindas, sigue practicando!"
            jump problema_5
        "400 kg":
            play sound "error.mp3" volume 4.0
            "¡Casi lo tienes! pero esta vez la respuesta no es la correcta."
            jump problema_5
        "305 kg":
            play sound "error.mp3" volume 4.0
            "Sigue intentado, estoy seguro de que la próxima será la correcta."
            jump problema_5

label cosechar_verduras_2:
    "Juan y Filiberto se encargan de cosechar las verduras."
    "Presiona la tecla Enter para cosechar las verduras."
    hide zanahoria1
    pause
    hide zanahoria2
    pause
    hide zanahoria3
    pause
    hide zanahoria4
    pause
    hide zanahoria5
    pause
    hide zanahoria6
    pause
    hide tomate1
    pause
    hide tomate2
    pause
    hide tomate3
    pause
    hide tomate4
    pause
    hide tomate5
    pause
    hide rabanob1
    pause
    hide rabanob2
    pause
    hide rabanob3
    pause
    hide rabanob4
    pause
    hide rabanob5
    pause
    hide rabanob6
    pause
    hide rabanor1
    pause
    hide rabanor2
    pause
    hide rabanor3
    pause
    hide rabanor4
    pause
    hide rabanor5
    pause
    hide rabanor6
    pause

    filiberto "Ahora que ya tenemos las verduras, necesitamos ir por agua."
    juan "De acuerdo. Podemos ir por ella al río, pero sería mejor agarrarla de un pozo."
    juan "Vayamos al que está en mi casa."
    filiberto "Regresemos entonces. Sólo hay que dejar esto en la cabaña para no andarlo cargando."

    "Juan y Filiberto dejaron las verduras en la cabaña de los bomberos y se dirigen de vuelta a casa de Juan."

    jump regresar_casaJ_agua
        
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
        "48 cubetas":
            play sound "error.mp3" volume 4.0
            "¡Vuelve a intentarlo, tú puedes! Lee nuevamente el ejercicio. "
            jump problema_division_3
        "7 cubetas":
            play sound "acierto.mp3"
            "¡Buen trabajo, lo has conseguido! Has logrado ayudar a Juan Cupul."
        "9 cubetas":
            play sound "error.mp3" volume 4.0
            "¡Casi lo tienes, estás cerca! Pero la respuesta no es la correcta."
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
        "23 partidas":
            play sound "error.mp3" volume 4.0
            "¡Tú puedes hallar la solución!"
            jump problema_resta_6
        "7 partidas":
            play sound "acierto.mp3"
            "¡Eso es! La respuesta es correcta."

    prometida "No has perdido la práctica. Sigues sin perder tu racha de aciertos."
    juan "Practico mucho gracias a ti."
    juan "Bueno, ya me voy. Nos vemos mañana."

    #jump en_la_cabana_bombero
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

    "Los cruzob podrían atacar en cualquier momento y él necesita estar ahí si eso
    sucede, y no quiere arriesgar su responsabilidad por un desconocido."

    menu:
        "¿Deseas acompañar al vendedor ambulante en su búsqueda, arriesgando llegar tarde a tu
        puesto como bombero y que ocurra un ataque en ese momento?"
        "Sí, quiero acompañar al Vendedor ambulante":
            play sound "seleccion.mp3"
            jump juan_ayuda_ambulante
        "No, no deseo arriesgar la seguridad de Tixcacalcupul":
            play sound "seleccion.mp3"
            jump juan_no_ayuda_ambulante
        

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
        "6 machetes":
            play sound "acierto.mp3"
            "¡Excelente, ahí lo tienes! Juan Cupul debe dar 6 machetes a cada campesino."
        "30 machetes":
            play sound "error.mp3" volume 4.0
            "¡Vuelve a intentarlo, tú puedes!"
            jump problema_division_1
        "5 machetes":
            play sound "error.mp3" volume 4.0
            "¡Vamos de nuevo!"
            jump problema_division_1
    
    menu problema_division_2:
        vendedor "Durante la cosecha de tomates Juan Cupul recolecta 72 kilos y se los 
        quiere regalar a 9 familias que viven cerca de su casa, ¿cuántos kilos de tomate 
        le regalará a cada familia?"
        "8 kilos":
            play sound "acierto.mp3"
            "¡Excelente, lo has conseguido! Juan Cupul le regalara 8 kilos de tomate a cada familia."
        "13 kilos":
            play sound "error.mp3" volume 4.0
            "¡Vuelve a intentarlo, tú puedes!"
            jump problema_division_2
        "7 kilos":
            play sound "error.mp3" volume 4.0
            "¡Casi lo tienes, estás cerca! Pero la respuesta no es la correcta."
            jump problema_division_2
        "63 kilos":
            play sound "error.mp3" volume 4.0
            "¡Vamos de nuevo!"
            jump problema_division_2
    
    menu problema_division_4:
        vendedor "Juan Cupul está ayudando a sus vecinos a prepararse para el invierno. 
                Han cortado 60 troncos de árboles y desean dividirlos igualmente entre 5 hogares. 
                ¿Cuántos troncos recibirá cada hogar?"
        "12 troncos":
            play sound "acierto.mp3"
            "¡Buen trabajo, lo has conseguido! Has apoyado mucho a Juan Cupul."
        "55 troncos":
            play sound "error.mp3" volume 4.0
            "¡Vuelve a intentarlo, tú puedes!"
            jump problema_division_4
        "11 troncos":
            play sound "error.mp3" volume 4.0
            "¡Casi lo tienes, estás cerca! Pero la respuesta no es la correcta."
            jump problema_division_4
        "8 troncos":
            play sound "error.mp3" volume 4.0
            "¡Vamos de nuevo!"
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

    vendedor "Espero te encuentres bien, muchacho, la trasnportación inmediata suele sentar
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
    filiberto "El agua que trajimos del pozo de tu casa ya no está."
    juan "¿Estás seguro? ¿No será que alguien vino y la movió de lugar? 
        ¿Buscaste en toda la cabaña?"
    filiberto "Sí, en toda la cabaña y alrededor de ella. No hay rastros del agua."
    filiberto "No tiene sentido que desapareciera. Somos los únicos que deberían estar aquí hoy."
    juan "Es extraño, pero no podemos descartar que alguien pasara y se la llevara, aunque no estoy
        seguro de por qué."
    filiberto "¿Y si llegaron los cruzob y se la llevaron?"
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

    juan "Aunque, si yo fuera un cruzob, intentaría..."

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

    cruzob "Te estarás preguntando dónde está tu primo. Mis compañeros le hicieron una 
            visita mientras iba por el agua. No te preocupes. No le han hecho mucho daño.
            Todavía."
    cruzob "Lo dejaron inconsciente, y ahora me toca a mí encargarme de ti."

    "El primer impulso de Juan es saltar para alcanzar la bomba y avisar de que hay cruzob en 
    el pueblo."

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

    "Juan sabe que necesita vencer a este cruzob si quiere alcanzar la bomba."

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
        "50 soldados":
            play sound "acierto.mp3"
            "¡Excelente! Tal vez Juan pueda vencer al cruzob."
            $ puntos = puntos + 1
        "2 soldados":
            play sound "error.mp3" volume 4.0
            "Fallaste, así que Juan también."
        "15 soldados":
            play sound "error.mp3" volume 4.0
            "Fallaste, así que Juan también."
        "5 soldados":
            play sound "error.mp3" volume 4.0
            "Fallaste, así que Juan también."
    
    "Juan Cupul está enseñando técnicas de combate a 15 guerreros en su pueblo. 
        Quiere asegurarse de que todos reciban la misma cantidad de entrenamiento, 
        así que divide el tiempo de entrenamiento igualmente entre ellos. "
        
    menu:
        "Si tiene 45 horas de entrenamiento, ¿cuántas horas recibe cada guerrero?"
        "2 horas":
            play sound "error.mp3" volume 4.0
            "Juan se ha equivocado porque tú te equivocaste."
        "1675 horas":
            play sound "error.mp3" volume 4.0
            "Juan se ha equivocado porque tú te equivocaste."
        "356 horas":
            play sound "error.mp3" volume 4.0
            "Juan se ha equivocado porque tú te equivocaste."
        "3 horas":
            play sound "acierto.mp3"
            "¡Eso es todo! Juan puede triunfar."
            $ puntos = puntos + 1

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
    "Juan logra vencer al cruzob."
    
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

    juan "Listo, ahora todos saben que hay cruzob en el pueblo."

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
            de los cruzob que me vigilaban, pero los demás están atacando el pueblo."
    juan "Vamos, vamos."

    show juan camina derecha:
        linear 2 xpos 1850
    show fili camina derecha:
        linear 2 xpos 1850 ypos 620

    pause 2.0
    hide juan camina derecha
    hide fili camina derecha

    "Gracias a que Juan logró vencer al cruzob y explotó la bomba, avisaron al pueblo a tiempo."
    "Juan y Filiberto apoyaron a la gente de su hogar a combatir a los cruzob invasores y los vencieron 
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
    dar el aviso lo suficientemente antes como para que Tixcacalcupul se defendiera
    con éxito."
    "Tixcacalcupul venció a los cruzob."
    "Juan y María Dolores pudieron casarse al día siguiente :)."
    jump despedida_final

label perdiste:
    "Has perdido la batalla contra el cruzob, te han vencido."
    hide hombre parado izquierda
    hide juan parado derecha
    "Lamentablemente, los cruzob invadieron Tixcacalcupul porque Juan nunca avisó 
    del ataque y Filiberto no despertó a tiempo para ir a ayudarlo."
    "Los cruzob decidieron secuestrar a Juan para que viera cómo hacían trizas su hogar."
    "Al final, simplemente se deshicieron de Juan. "
    "Juan no pudo casarse con María Dolores al día siguiente :(."
    jump despedida_final

label despedida_final:
    play music "fondo3.mp3"
    scene fondo_final
    "Esto ha sido todo, ¡muchas gracias por jugar Conquista matemática!"

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