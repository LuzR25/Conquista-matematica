#* Screens con la selección de los avatares
screen avatares_1():
    imagebutton:
        idle "fondo_seleccionar_personaje"
        action Jump("seleccion_avatar_1") #*El label que quiero que se vea
    
    imagebutton:
        idle "derecha"
        hover "derecha_hover"
        action Jump("seleccion_avatar_2")
        xpos 1550
        ypos 570
    
    imagebutton:
        idle "avatar1"
        hover "avatar1_hover"
        action Jump("elegi_A1")
        xpos 600
        ypos 100

    imagebutton:
        idle "avatar2"
        hover "avatar2_hover"
        action Jump("elegi_A2")
        xpos 600
        ypos 500
    
    imagebutton:
        idle "avatar3"
        hover "avatar3_hover"
        action Jump("elegi_A3")
        xpos 1100
        ypos 100

    imagebutton:
        idle "avatar4"
        hover "avatar4_hover"
        action Jump("elegi_A4")
        xpos 1100
        ypos 500

screen avatares_2():
    imagebutton:
        idle "fondo_seleccionar_personaje"
        action Jump("seleccion_avatar_2") #*El label que quiero que se vea
    
    imagebutton:
        idle "derecha"
        hover "derecha_hover"
        action Jump("seleccion_avatar_3")
        xpos 1550
        ypos 570
    
    imagebutton:
        idle "izquierda"
        hover "izquierda_hover"
        action Rollback()#ShowMenu("seleccion_avatar_1")
        xpos 150
        ypos 570
    
    imagebutton:
        idle "avatar5"
        hover "avatar5_hover"
        action Jump("elegi_A5")
        xpos 600
        ypos 100

    imagebutton:
        idle "avatar6"
        hover "avatar6_hover"
        action Jump("elegi_A6")
        xpos 600
        ypos 500
    
    imagebutton:
        idle "avatar7"
        hover "avatar7_hover"
        action Jump("elegi_A7")
        xpos 1100
        ypos 100

    imagebutton:
        idle "avatar8"
        hover "avatar8_hover"
        action Jump("elegi_A8")
        xpos 1100
        ypos 500

screen avatares_3():
    imagebutton:
        idle "fondo_seleccionar_personaje"
        action Jump("seleccion_avatar_3") #*El label que quiero que se vea
    
    imagebutton:
        idle "derecha"
        hover "derecha_hover"
        action Jump("seleccion_avatar_4")
        xpos 1550
        ypos 570
    
    imagebutton:
        idle "izquierda"
        hover "izquierda_hover"
        action Rollback()
        xpos 150
        ypos 570
    
    imagebutton:
        idle "avatar9"
        hover "avatar9_hover"
        action Jump("elegi_A9")
        xpos 600
        ypos 100

    imagebutton:
        idle "avatar10"
        hover "avatar10_hover"
        action Jump("elegi_A10")
        xpos 600
        ypos 500
    
    imagebutton:
        idle "avatar11"
        hover "avatar11_hover"
        action Jump("elegi_A11")
        xpos 1100
        ypos 100

    imagebutton:
        idle "avatar12"
        hover "avatar12_hover"
        action Jump("elegi_A12")
        xpos 1100
        ypos 500

screen avatares_4():
    imagebutton:
        idle "fondo_seleccionar_personaje"
        action Jump("seleccion_avatar_4") #*El label que quiero que se vea
    
    imagebutton:
        idle "derecha"
        hover "derecha_hover"
        action Jump("seleccion_avatar_5")
        xpos 1550
        ypos 570
    
    imagebutton:
        idle "izquierda"
        hover "izquierda_hover"
        action Rollback()
        xpos 150
        ypos 570
    
    imagebutton:
        idle "avatar13"
        hover "avatar13_hover"
        action Jump("elegi_A13")
        xpos 600
        ypos 100

    imagebutton:
        idle "avatar14"
        hover "avatar14_hover"
        action Jump("elegi_A14")
        xpos 600
        ypos 500
    
    imagebutton:
        idle "avatar15"
        hover "avatar15_hover"
        action Jump("elegi_A15")
        xpos 1100
        ypos 100

    imagebutton:
        idle "avatar16"
        hover "avatar16_hover"
        action Jump("elegi_A16")
        xpos 1100
        ypos 500

screen avatares_5():
    imagebutton:
        idle "fondo_seleccionar_personaje"
        action Jump("seleccion_avatar_5") #*El label que quiero que se vea
    
    imagebutton:
        idle "derecha"
        hover "derecha_hover"
        action Jump("seleccion_avatar_6")
        xpos 1550
        ypos 570
    
    imagebutton:
        idle "izquierda"
        hover "izquierda_hover"
        action Rollback()
        xpos 150
        ypos 570
    
    imagebutton:
        idle "avatar17"
        hover "avatar17_hover"
        action Jump("elegi_A17")
        xpos 600
        ypos 100

    imagebutton:
        idle "avatar18"
        hover "avatar18_hover"
        action Jump("elegi_A18")
        xpos 600
        ypos 500
    
    imagebutton:
        idle "avatar19"
        hover "avatar19_hover"
        action Jump("elegi_A19")
        xpos 1100
        ypos 100

    imagebutton:
        idle "avatar20"
        hover "avatar20_hover"
        action Jump("elegi_A20")
        xpos 1100
        ypos 500

screen avatares_6():
    imagebutton:
        idle "fondo_seleccionar_personaje"
        action Jump("seleccion_avatar_6") #*El label que quiero que se vea
    
    imagebutton:
        idle "izquierda"
        hover "izquierda_hover"
        action Rollback()
        xpos 150
        ypos 570
    
    imagebutton:
        idle "avatar21"
        hover "avatar21_hover"
        action Jump("elegi_A21")
        xpos 600
        ypos 100

#* Labels que muestran esas screens
label seleccion_avatar_1:
    show screen avatares_1
    "Elige un avatar."
    pause

label seleccion_avatar_2:
    show screen avatares_2
    "Elige un avatar."
    pause

label seleccion_avatar_3:
    show screen avatares_3
    "Elige un avatar."
    pause

label seleccion_avatar_4:
    show screen avatares_4
    "Elige un avatar."
    pause

label seleccion_avatar_5:
    show screen avatares_5
    "Elige un avatar."
    pause

label seleccion_avatar_6:
    show screen avatares_6
    "Elige un avatar."
    pause

#* Labels para los avatares elegidos
label elegi_A1:
    hide screen avatares_1
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 1"

    show avatar1 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."

    jump inicio_historia

label elegi_A2:
    hide screen avatares_1
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 2"

    show avatar2 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."

    jump inicio_historia

label elegi_A3:
    hide screen avatares_1
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 3"

    show avatar3 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."

    jump inicio_historia

label elegi_A4:
    hide screen avatares_1
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 4"

    show avatar4 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."

    jump inicio_historia

label elegi_A5:
    hide screen avatares_1
    hide screen avatares_2
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 5"

    show avatar5 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."

    jump inicio_historia

label elegi_A6:
    hide screen avatares_1
    hide screen avatares_2
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 6"

    show avatar6 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."

    jump inicio_historia

label elegi_A7:
    hide screen avatares_1
    hide screen avatares_2
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 7"

    show avatar7 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."

    jump inicio_historia

label elegi_A8:
    hide screen avatares_1
    hide screen avatares_2
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 8"

    show avatar8 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."

    jump inicio_historia

label elegi_A9:
    hide screen avatares_1
    hide screen avatares_2
    hide screen avatares_3
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 9"
    show avatar9 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."

    jump inicio_historia

label elegi_A10:
    hide screen avatares_1
    hide screen avatares_2
    hide screen avatares_3
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 10"

    show avatar10 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."

    jump inicio_historia

label elegi_A11:
    hide screen avatares_1
    hide screen avatares_2
    hide screen avatares_3
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 11"

    show avatar11 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."

    jump inicio_historia

label elegi_A12:
    hide screen avatares_1
    hide screen avatares_2
    hide screen avatares_3
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 12"
    show avatar12 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."

    jump inicio_historia

label elegi_A13:
    hide screen avatares_1
    hide screen avatares_2
    hide screen avatares_3
    hide screen avatares_4
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 13"

    show avatar13 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."

    jump inicio_historia

label elegi_A14:
    hide screen avatares_1
    hide screen avatares_2
    hide screen avatares_3
    hide screen avatares_4
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 14"

    show avatar14 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."

    jump inicio_historia

label elegi_A15:
    hide screen avatares_1
    hide screen avatares_2
    hide screen avatares_3
    hide screen avatares_4
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 15"

    show avatar15 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."

    jump inicio_historia

label elegi_A16:
    hide screen avatares_1
    hide screen avatares_2
    hide screen avatares_3
    hide screen avatares_4
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 16"
    show avatar16 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."

    jump inicio_historia

label elegi_A17:
    hide screen avatares_1
    hide screen avatares_2
    hide screen avatares_3
    hide screen avatares_4
    hide screen avatares_5
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 17"
    show avatar17 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."

    jump inicio_historia

label elegi_A18:
    hide screen avatares_1
    hide screen avatares_2
    hide screen avatares_3
    hide screen avatares_4
    hide screen avatares_5
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 18"

    show avatar18 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."

    jump inicio_historia

label elegi_A19:
    hide screen avatares_1
    hide screen avatares_2
    hide screen avatares_3
    hide screen avatares_4
    hide screen avatares_5
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 19"

    show avatar19 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."

    jump inicio_historia

label elegi_A20:
    hide screen avatares_1
    hide screen avatares_2
    hide screen avatares_3
    hide screen avatares_4
    hide screen avatares_5
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 20"

    show avatar20 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."
    
    jump inicio_historia

label elegi_A21:
    hide screen avatares_1
    hide screen avatares_2
    hide screen avatares_3
    hide screen avatares_4
    hide screen avatares_5
    hide screen avatares_6
    scene fondo_seleccionar_personaje

    $ avatarElegido = "Avatar 21"

    show avatar21 at center:
        #xpos 800
        ypos 550
    
    "¡Ya has elegido un avatar! Ahora iniciemos la historia ;)."

    jump inicio_historia
