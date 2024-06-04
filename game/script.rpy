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

    "¡Bienvenido/Bienvenida a Conquista matemática!"
    "Esta es una novela visual que presenta parte de la vida de Juan Cupul, ¡un héroe de Tixcacalcupul!"
    "Durante la historia tendrás que tomar decisiones que afectarán el curso de la historia y los personajes."
    "Pero también verás varios ejercicios matemáticos que tendrás que resolver."
    "Si no logras resolverlos con éxito, la historia no avanzará, así que esfuérzate mucho para que puedas
    conocer cuál será el final que te tocará basado en tus decisiones."
    "Y sobre todo, ¡no olvides divertirte!"
    "Por ahora, personaliza un poco tu partida."

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
            jump cosechar_verduras_2
        "345 kg":
            "Ups, parece que esta respuesta no es la correcta. ¡No te rindas, sigue practicando!"
            jump problema_5
        "400 kg":
            "¡Casi lo tienes! pero esta vez la respuesta no es la correcta."
            jump problema_5
        "305 kg":
            "Sigue intentado, estoy seguro de que la próxima será la correcta."
            jump problema_5

label cosechar_verduras_2:
    "Juan y Filiberto se encargan de cosechar las verduras."
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
            "¡Vuelve a intentarlo, tú puedes! Lee nuevamente el ejercicio. "
            jump problema_division_3
        "7 cubetas":
            "¡Buen trabajo, lo has conseguido! Has logrado ayudar a Juan Cupul."
        "9 cubetas":
            "¡Casi lo tienes, estás cerca! Pero la respuesta no es la correcta."
            jump problema_division_3
        "64 cubetas":
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
            "¡Vuelve a intentarlo, tú puedes!"
            jump problema_resta_6
        "5 partidas":
            "Estás en el camino correcto. Recuerda cuántas partidas de ajedrez jugó Juan en total y cuántas ganó."
            jump problema_resta_6
        "23 partidas":
            "¡Tú puedes hallar la solución!"
            jump problema_resta_6
        "7 partidas":
            "¡Eso es! La respuesta es correcta."

    prometida "No has perdido la práctica. Sigues sin perder tu racha de aciertos."
    juan "Practico mucho gracias a ti."
    juan "Bueno, ya me voy. Nos vemos mañana."

    "Aquí me quedé."

    jump en_la_cabana_bombero

label camino_al_turno:
    scene camino_v_md

    "Juan está de camino a su turno como bombero. Avanza con tranquilidad, sabiendo que va con tiempo
    para llegar puntual."

    show juan parado izquierda:
        xpos 1850
        ypos 520
    
    show juan camina izquierda:
        linear 6 xpos 120

    pause 6

    scene camino_v_osc

    show juan parado izquierda:
        xpos 1850
        ypos 520
    
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

    #! Animación de Juan acercándose

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

    "Por otro lado, podría ser peligroso seguir a este extraño ser a un lugar desconocido a buscar
    quien sabe qué y, de ayudarlo, corre con el riesgo de no llegar a tiempo a su puesto de bombero."

    "Los cruzob podrían atacar en cualquier momento y él necesita estar ahí si eso
    sucede, y no quiere arriesgar su responsabilidad por un desconocido."

    menu:
        "¿Deseas acompañar al vendedor ambulante en su búsqueda, arriesgando llegar tarde a tu
        puesto como bombero y que ocurra un ataque en ese momento?"
        "Sí, quiero acompañar al Vendedor ambulante":
            jump juan_ayuda_ambulante
        "No, no deseo arriesgar la seguridad de Tixcacalcupul":
            jump juan_no_ayuda_ambulante
        

label juan_ayuda_ambulante:
    juan "Está bien. Te ayudaré en tu búsqueda. ¿Qué debo hacer?"

label juan_no_ayuda_ambulante:
    juan "Lo siento, pero tengo algo que hacer justo ahora y no puedo distraerme.
        Tal vez en otro momento."

    vendedor "Pues bien, sólo me queda desearte suerte, Juan Cupul, dado que no nos
            volveremos a encontrar. "
    
    "Y el Vendedor ambulante desaparece."

    #! Animación del vendedor desaparienciendo

    "Juan siente miedo por un segundo, pero se lo quita de encima. Tiene una responsabilidad
    que cumplir."

    juan "Si era un fantasma, no quiero saber."

    #! Animación de Juan yéndose 

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

    "Filiberto se va y Juan se queda solo."

    "Aquí me quedé."

    return



#Que cuendo lleguen a la cabaña no haya agua y aunque ellos no entienden por qué,
#no les queda de otra que ir por más porque la necesitarán para su urno. Lo que ellos
#no saben es que fue una trampa de los atacantes para separarlos porque sabían que
#uno solo tendría que ir por agua porque no podían abandonar su turno































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