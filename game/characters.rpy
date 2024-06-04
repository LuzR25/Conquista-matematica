# PERSONAJES ##################################################################
define juan = Character("Juan Cupul", color="#0011a7")
define prometida = Character("María Dolores", color="#8b6eb9")
define filiberto = Character("Filiberto Tun", color="#155513")
define vendedor = Character("Vendedor ambulante", color="#3d3d3d")

# IMÁGENES ####################################################################
#De los personajes
image protagonista1 = "Juan_Cupul_1.png"
image prometida1 = "Maria_Dolores_1.png"
image filiberto_tun = "Filiberto_1.png"
image spritesheet_juanC = "Personajes/Juan_C_Sprite_Style_Sheets.png"
image spritesheet_novia = "Personajes/Novia_Sprite_Sheet.png"
image spritesheet_fili = "Personajes/Filberto_Style_Sheets_128x128.png"
image spritesheet_hombre = "Personajes/Hombre_Style_Sheets_128x128.png"
image spritesheet_mujer = "Personajes/Mujer_Style_Sheets_128x128.png"
image spritesheet_vendedor = "Personajes/Vendedor_Style_Sheet_128x128.png"

#ANIMACIONES ###################################################################
#* JUAN
image juan_camina_frente_1 = Crop((0, 0, 128, 128), "spritesheet_juanC")
image juan_camina_frente_2 = Crop((128, 0, 128, 128), "spritesheet_juanC")
image juan_camina_frente_3 = Crop((256, 0, 128, 128), "spritesheet_juanC")
image juan_camina_frente_4 = Crop((384, 0, 128, 128), "spritesheet_juanC")

image juan camina frente:
    "juan_camina_frente_1"
    pause 0.3
    "juan_camina_frente_2"
    pause 0.3
    "juan_camina_frente_3"
    pause 0.3
    "juan_camina_frente_4"
    pause 0.3
    repeat

image juan_camina_atras_1 = Crop((0, 128, 128, 128), "spritesheet_juanC")
image juan_camina_atras_2 = Crop((128, 128, 128, 128), "spritesheet_juanC")
image juan_camina_atras_3 = Crop((256, 128, 128, 128), "spritesheet_juanC")
image juan_camina_atras_4 = Crop((384, 128, 128, 128), "spritesheet_juanC")

image juan camina atras:
    "juan_camina_atras_1"
    pause 0.3
    "juan_camina_atras_2"
    pause 0.3
    "juan_camina_atras_3"
    pause 0.3
    "juan_camina_atras_4"
    pause 0.3
    repeat

image juan_camina_izquierda_1 = Crop((0, 256, 128, 128), "spritesheet_juanC")
image juan_camina_izquierda_2 = Crop((128, 256, 128, 128), "spritesheet_juanC")
image juan_camina_izquierda_3 = Crop((256, 256, 128, 128), "spritesheet_juanC")
image juan_camina_izquierda_4 = Crop((384, 256, 128, 128), "spritesheet_juanC")

image juan camina izquierda:
    "juan_camina_izquierda_1"
    pause 0.3
    "juan_camina_izquierda_2"
    pause 0.3
    "juan_camina_izquierda_3"
    pause 0.3
    "juan_camina_izquierda_4"
    pause 0.3
    repeat

image juan_camina_derecha_1 = Crop((0, 384, 128, 128), "spritesheet_juanC")
image juan_camina_derecha_2 = Crop((128, 384, 128, 128), "spritesheet_juanC")
image juan_camina_derecha_3 = Crop((256, 384, 128, 128), "spritesheet_juanC")
image juan_camina_derecha_4 = Crop((384, 384, 128, 128), "spritesheet_juanC")

image juan camina derecha:
    "juan_camina_derecha_1"
    pause 0.3
    "juan_camina_derecha_2"
    pause 0.3
    "juan_camina_derecha_3"
    pause 0.3
    "juan_camina_derecha_4"
    pause 0.3
    repeat

image juan_parado_frente_1 = Crop((0, 512, 128, 128), "spritesheet_juanC")
image juan_parado_frente_2 = Crop((128, 512, 128, 128), "spritesheet_juanC")
image juan_parado_frente_3 = Crop((256, 512, 128, 128), "spritesheet_juanC")
image juan_parado_frente_4 = Crop((384, 512, 128, 128), "spritesheet_juanC")

image juan parado frente:
    "juan_parado_frente_1"
    pause 0.3
    "juan_parado_frente_2"
    pause 0.3
    "juan_parado_frente_3"
    pause 0.3
    "juan_parado_frente_4"
    pause 0.3
    repeat

image juan_parado_atras_1 = Crop((0, 640, 128, 128), "spritesheet_juanC")
image juan_parado_atras_2 = Crop((128, 640, 128, 128), "spritesheet_juanC")
image juan_parado_atras_3 = Crop((256, 640, 128, 128), "spritesheet_juanC")
image juan_parado_atras_4 = Crop((384, 640, 128, 128), "spritesheet_juanC")

image juan parado atras:
    "juan_parado_atras_1"
    pause 0.3
    "juan_parado_atras_2"
    pause 0.3
    "juan_parado_atras_3"
    pause 0.3
    "juan_parado_atras_4"
    pause 0.3
    repeat

image juan_parado_izquierda_1 = Crop((0, 768, 128, 128), "spritesheet_juanC")
image juan_parado_izquierda_2 = Crop((128, 768, 128, 128), "spritesheet_juanC")
image juan_parado_izquierda_3 = Crop((256, 768, 128, 128), "spritesheet_juanC")
image juan_parado_izquierda_4 = Crop((384, 768, 128, 128), "spritesheet_juanC")

image juan parado izquierda:
    "juan_parado_izquierda_1"
    pause 0.3
    "juan_parado_izquierda_2"
    pause 0.3
    "juan_parado_izquierda_3"
    pause 0.3
    "juan_parado_izquierda_4"
    pause 0.3
    repeat

image juan_parado_derecha_1 = Crop((0, 896, 128, 128), "spritesheet_juanC")
image juan_parado_derecha_2 = Crop((128, 896, 128, 128), "spritesheet_juanC")
image juan_parado_derecha_3 = Crop((256, 896, 128, 128), "spritesheet_juanC")
image juan_parado_derecha_4 = Crop((384, 896, 128, 128), "spritesheet_juanC")

image juan parado derecha:
    "juan_parado_derecha_1"
    pause 0.3
    "juan_parado_derecha_2"
    pause 0.3
    "juan_parado_derecha_3"
    pause 0.3
    "juan_parado_derecha_4"
    pause 0.3
    repeat

#* NOVIA
image novia_camina_frente_1 = Crop((0, 0, 128, 128), "spritesheet_novia")
image novia_camina_frente_2 = Crop((128, 0, 128, 128), "spritesheet_novia")
image novia_camina_frente_3 = Crop((256, 0, 128, 128), "spritesheet_novia")
image novia_camina_frente_4 = Crop((384, 0, 128, 128), "spritesheet_novia")

image novia camina frente:
    "novia_camina_frente_1"
    pause 0.3
    "novia_camina_frente_2"
    pause 0.3
    "novia_camina_frente_3"
    pause 0.3
    "novia_camina_frente_4"
    pause 0.3
    repeat

image novia_camina_atras_1 = Crop((0, 128, 128, 128), "spritesheet_novia")
image novia_camina_atras_2 = Crop((128, 128, 128, 128), "spritesheet_novia")
image novia_camina_atras_3 = Crop((256, 128, 128, 128), "spritesheet_novia")
image novia_camina_atras_4 = Crop((384, 128, 128, 128), "spritesheet_novia")

image novia camina atras:
    "novia_camina_atras_1"
    pause 0.3
    "novia_camina_atras_2"
    pause 0.3
    "novia_camina_atras_3"
    pause 0.3
    "novia_camina_atras_4"
    pause 0.3
    repeat

image novia_camina_izquierda_1 = Crop((0, 256, 128, 128), "spritesheet_novia")
image novia_camina_izquierda_2 = Crop((128, 256, 128, 128), "spritesheet_novia")
image novia_camina_izquierda_3 = Crop((256, 256, 128, 128), "spritesheet_novia")
image novia_camina_izquierda_4 = Crop((384, 256, 128, 128), "spritesheet_novia")

image novia camina izquierda:
    "novia_camina_izquierda_1"
    pause 0.3
    "novia_camina_izquierda_2"
    pause 0.3
    "novia_camina_izquierda_3"
    pause 0.3
    "novia_camina_izquierda_4"
    pause 0.3
    repeat

image novia_camina_derecha_1 = Crop((0, 384, 128, 128), "spritesheet_novia")
image novia_camina_derecha_2 = Crop((128, 384, 128, 128), "spritesheet_novia")
image novia_camina_derecha_3 = Crop((256, 384, 128, 128), "spritesheet_novia")
image novia_camina_derecha_4 = Crop((384, 384, 128, 128), "spritesheet_novia")

image novia camina derecha:
    "novia_camina_derecha_1"
    pause 0.3
    "novia_camina_derecha_2"
    pause 0.3
    "novia_camina_derecha_3"
    pause 0.3
    "novia_camina_derecha_4"
    pause 0.3
    repeat

image novia_parada_frente_1 = Crop((0, 512, 128, 128), "spritesheet_novia")
image novia_parada_frente_2 = Crop((128, 512, 128, 128), "spritesheet_novia")
image novia_parada_frente_3 = Crop((256, 512, 128, 128), "spritesheet_novia")
image novia_parada_frente_4 = Crop((384, 512, 128, 128), "spritesheet_novia")

image novia parada frente:
    "novia_parada_frente_1"
    pause 0.3
    "novia_parada_frente_2"
    pause 0.3
    "novia_parada_frente_3"
    pause 0.3
    "novia_parada_frente_4"
    pause 0.3
    repeat

image novia_parada_atras_1 = Crop((0, 640, 128, 128), "spritesheet_novia")
image novia_parada_atras_2 = Crop((128, 640, 128, 128), "spritesheet_novia")
image novia_parada_atras_3 = Crop((256, 640, 128, 128), "spritesheet_novia")
image novia_parada_atras_4 = Crop((384, 640, 128, 128), "spritesheet_novia")

image novia parada atras:
    "novia_parada_atras_1"
    pause 0.3
    "novia_parada_atras_2"
    pause 0.3
    "novia_parada_atras_3"
    pause 0.3
    "novia_parada_atras_4"
    pause 0.3
    repeat

image novia_parada_izquierda_1 = Crop((0, 768, 128, 128), "spritesheet_novia")
image novia_parada_izquierda_2 = Crop((128, 768, 128, 128), "spritesheet_novia")
image novia_parada_izquierda_3 = Crop((256, 768, 128, 128), "spritesheet_novia")
image novia_parada_izquierda_4 = Crop((384, 768, 128, 128), "spritesheet_novia")

image novia parada izquierda:
    "novia_parada_izquierda_1"
    pause 0.3
    "novia_parada_izquierda_2"
    pause 0.3
    "novia_parada_izquierda_3"
    pause 0.3
    "novia_parada_izquierda_4"
    pause 0.3
    repeat

image novia_parada_derecha_1 = Crop((0, 896, 128, 128), "spritesheet_novia")
image novia_parada_derecha_2 = Crop((128, 896, 128, 128), "spritesheet_novia")
image novia_parada_derecha_3 = Crop((256, 896, 128, 128), "spritesheet_novia")
image novia_parada_derecha_4 = Crop((384, 896, 128, 128), "spritesheet_novia")

image novia parada derecha:
    "novia_parada_derecha_1"
    pause 0.3
    "novia_parada_derecha_2"
    pause 0.3
    "novia_parada_derecha_3"
    pause 0.3
    "novia_parada_derecha_4"
    pause 0.3
    repeat

#* FILIBERTO
image fili_camina_frente_1 = Crop((0, 0, 128, 128), "spritesheet_fili")
image fili_camina_frente_2 = Crop((128, 0, 128, 128), "spritesheet_fili")
image fili_camina_frente_3 = Crop((256, 0, 128, 128), "spritesheet_fili")
image fili_camina_frente_4 = Crop((384, 0, 128, 128), "spritesheet_fili")

image fili camina frente:
    "fili_camina_frente_1"
    pause 0.3
    "fili_camina_frente_2"
    pause 0.3
    "fili_camina_frente_3"
    pause 0.3
    "fili_camina_frente_4"
    pause 0.3
    repeat

image fili_camina_atras_1 = Crop((0, 128, 128, 128), "spritesheet_fili")
image fili_camina_atras_2 = Crop((128, 128, 128, 128), "spritesheet_fili")
image fili_camina_atras_3 = Crop((256, 128, 128, 128), "spritesheet_fili")
image fili_camina_atras_4 = Crop((384, 128, 128, 128), "spritesheet_fili")

image fili camina atras:
    "fili_camina_atras_1"
    pause 0.3
    "fili_camina_atras_2"
    pause 0.3
    "fili_camina_atras_3"
    pause 0.3
    "fili_camina_atras_4"
    pause 0.3
    repeat

image fili_camina_izquierda_1 = Crop((0, 256, 128, 128), "spritesheet_fili")
image fili_camina_izquierda_2 = Crop((128, 256, 128, 128), "spritesheet_fili")
image fili_camina_izquierda_3 = Crop((256, 256, 128, 128), "spritesheet_fili")
image fili_camina_izquierda_4 = Crop((384, 256, 128, 128), "spritesheet_fili")

image fili camina izquierda:
    "fili_camina_izquierda_1"
    pause 0.3
    "fili_camina_izquierda_2"
    pause 0.3
    "fili_camina_izquierda_3"
    pause 0.3
    "fili_camina_izquierda_4"
    pause 0.3
    repeat

image fili_camina_derecha_1 = Crop((0, 384, 128, 128), "spritesheet_fili")
image fili_camina_derecha_2 = Crop((128, 384, 128, 128), "spritesheet_fili")
image fili_camina_derecha_3 = Crop((256, 384, 128, 128), "spritesheet_fili")
image fili_camina_derecha_4 = Crop((384, 384, 128, 128), "spritesheet_fili")

image fili camina derecha:
    "fili_camina_derecha_1"
    pause 0.3
    "fili_camina_derecha_2"
    pause 0.3
    "fili_camina_derecha_3"
    pause 0.3
    "fili_camina_derecha_4"
    pause 0.3
    repeat

image fili_parado_frente_1 = Crop((0, 512, 128, 128), "spritesheet_fili")
image fili_parado_frente_2 = Crop((128, 512, 128, 128), "spritesheet_fili")
image fili_parado_frente_3 = Crop((256, 512, 128, 128), "spritesheet_fili")
image fili_parado_frente_4 = Crop((384, 512, 128, 128), "spritesheet_fili")

image fili parado frente:
    "fili_parado_frente_1"
    pause 0.3
    "fili_parado_frente_2"
    pause 0.3
    "fili_parado_frente_3"
    pause 0.3
    "fili_parado_frente_4"
    pause 0.3
    repeat

image fili_parado_atras_1 = Crop((0, 640, 128, 128), "spritesheet_fili")
image fili_parado_atras_2 = Crop((128, 640, 128, 128), "spritesheet_fili")
image fili_parado_atras_3 = Crop((256, 640, 128, 128), "spritesheet_fili")
image fili_parado_atras_4 = Crop((384, 640, 128, 128), "spritesheet_fili")

image fili parado atras:
    "fili_parado_atras_1"
    pause 0.3
    "fili_parado_atras_2"
    pause 0.3
    "fili_parado_atras_3"
    pause 0.3
    "fili_parado_atras_4"
    pause 0.3
    repeat

image fili_parado_izquierda_1 = Crop((0, 768, 128, 128), "spritesheet_fili")
image fili_parado_izquierda_2 = Crop((128, 768, 128, 128), "spritesheet_fili")
image fili_parado_izquierda_3 = Crop((256, 768, 128, 128), "spritesheet_fili")
image fili_parado_izquierda_4 = Crop((384, 768, 128, 128), "spritesheet_fili")

image fili parado izquierda:
    "fili_parado_izquierda_1"
    pause 0.3
    "fili_parado_izquierda_2"
    pause 0.3
    "fili_parado_izquierda_3"
    pause 0.3
    "fili_parado_izquierda_4"
    pause 0.3
    repeat

image fili_parado_derecha_1 = Crop((0, 896, 128, 128), "spritesheet_fili")
image fili_parado_derecha_2 = Crop((128, 896, 128, 128), "spritesheet_fili")
image fili_parado_derecha_3 = Crop((256, 896, 128, 128), "spritesheet_fili")
image fili_parado_derecha_4 = Crop((384, 896, 128, 128), "spritesheet_fili")

image fili parado derecha:
    "fili_parado_derecha_1"
    pause 0.3
    "fili_parado_derecha_2"
    pause 0.3
    "fili_parado_derecha_3"
    pause 0.3
    "fili_parado_derecha_4"
    pause 0.3
    repeat

#* HOMBRE
image hombre_camina_frente_1 = Crop((0, 0, 128, 128), "spritesheet_hombre")
image hombre_camina_frente_2 = Crop((128, 0, 128, 128), "spritesheet_hombre")
image hombre_camina_frente_3 = Crop((256, 0, 128, 128), "spritesheet_hombre")
image hombre_camina_frente_4 = Crop((384, 0, 128, 128), "spritesheet_hombre")

image hombre camina frente:
    "hombre_camina_frente_1"
    pause 0.3
    "hombre_camina_frente_2"
    pause 0.3
    "hombre_camina_frente_3"
    pause 0.3
    "hombre_camina_frente_4"
    pause 0.3
    repeat

image hombre_camina_atras_1 = Crop((0, 128, 128, 128), "spritesheet_hombre")
image hombre_camina_atras_2 = Crop((128, 128, 128, 128), "spritesheet_hombre")
image hombre_camina_atras_3 = Crop((256, 128, 128, 128), "spritesheet_hombre")
image hombre_camina_atras_4 = Crop((384, 128, 128, 128), "spritesheet_hombre")

image hombre camina atras:
    "hombre_camina_atras_1"
    pause 0.3
    "hombre_camina_atras_2"
    pause 0.3
    "hombre_camina_atras_3"
    pause 0.3
    "hombre_camina_atras_4"
    pause 0.3
    repeat

image hombre_camina_izquierda_1 = Crop((0, 256, 128, 128), "spritesheet_hombre")
image hombre_camina_izquierda_2 = Crop((128, 256, 128, 128), "spritesheet_hombre")
image hombre_camina_izquierda_3 = Crop((256, 256, 128, 128), "spritesheet_hombre")
image hombre_camina_izquierda_4 = Crop((384, 256, 128, 128), "spritesheet_hombre")

image hombre camina izquierda:
    "hombre_camina_izquierda_1"
    pause 0.3
    "hombre_camina_izquierda_2"
    pause 0.3
    "hombre_camina_izquierda_3"
    pause 0.3
    "hombre_camina_izquierda_4"
    pause 0.3
    repeat

image hombre_camina_derecha_1 = Crop((0, 384, 128, 128), "spritesheet_hombre")
image hombre_camina_derecha_2 = Crop((128, 384, 128, 128), "spritesheet_hombre")
image hombre_camina_derecha_3 = Crop((256, 384, 128, 128), "spritesheet_hombre")
image hombre_camina_derecha_4 = Crop((384, 384, 128, 128), "spritesheet_hombre")

image hombre camina derecha:
    "hombre_camina_derecha_1"
    pause 0.3
    "hombre_camina_derecha_2"
    pause 0.3
    "hombre_camina_derecha_3"
    pause 0.3
    "hombre_camina_derecha_4"
    pause 0.3
    repeat

image hombre_parado_frente_1 = Crop((0, 512, 128, 128), "spritesheet_hombre")
image hombre_parado_frente_2 = Crop((128, 512, 128, 128), "spritesheet_hombre")
image hombre_parado_frente_3 = Crop((256, 512, 128, 128), "spritesheet_hombre")
image hombre_parado_frente_4 = Crop((384, 512, 128, 128), "spritesheet_hombre")

image hombre parado frente:
    "hombre_parado_frente_1"
    pause 0.3
    "hombre_parado_frente_2"
    pause 0.3
    "hombre_parado_frente_3"
    pause 0.3
    "hombre_parado_frente_4"
    pause 0.3
    repeat

image hombre_parado_atras_1 = Crop((0, 640, 128, 128), "spritesheet_hombre")
image hombre_parado_atras_2 = Crop((128, 640, 128, 128), "spritesheet_hombre")
image hombre_parado_atras_3 = Crop((256, 640, 128, 128), "spritesheet_hombre")
image hombre_parado_atras_4 = Crop((384, 640, 128, 128), "spritesheet_hombre")

image hombre parado atras:
    "hombre_parado_atras_1"
    pause 0.3
    "hombre_parado_atras_2"
    pause 0.3
    "hombre_parado_atras_3"
    pause 0.3
    "hombre_parado_atras_4"
    pause 0.3
    repeat

image hombre_parado_izquierda_1 = Crop((0, 768, 128, 128), "spritesheet_hombre")
image hombre_parado_izquierda_2 = Crop((128, 768, 128, 128), "spritesheet_hombre")
image hombre_parado_izquierda_3 = Crop((256, 768, 128, 128), "spritesheet_hombre")
image hombre_parado_izquierda_4 = Crop((384, 768, 128, 128), "spritesheet_hombre")

image hombre parado izquierda:
    "hombre_parado_izquierda_1"
    pause 0.3
    "hombre_parado_izquierda_2"
    pause 0.3
    "hombre_parado_izquierda_3"
    pause 0.3
    "hombre_parado_izquierda_4"
    pause 0.3
    repeat

image hombre_parado_derecha_1 = Crop((0, 896, 128, 128), "spritesheet_hombre")
image hombre_parado_derecha_2 = Crop((128, 896, 128, 128), "spritesheet_hombre")
image hombre_parado_derecha_3 = Crop((256, 896, 128, 128), "spritesheet_hombre")
image hombre_parado_derecha_4 = Crop((384, 896, 128, 128), "spritesheet_hombre")

image hombre parado derecha:
    "hombre_parado_derecha_1"
    pause 0.3
    "hombre_parado_derecha_2"
    pause 0.3
    "hombre_parado_derecha_3"
    pause 0.3
    "hombre_parado_derecha_4"
    pause 0.3
    repeat

#* MUJER
image mujer_camina_frente_1 = Crop((0, 0, 128, 128), "spritesheet_mujer")
image mujer_camina_frente_2 = Crop((128, 0, 128, 128), "spritesheet_mujer")
image mujer_camina_frente_3 = Crop((256, 0, 128, 128), "spritesheet_mujer")
image mujer_camina_frente_4 = Crop((384, 0, 128, 128), "spritesheet_mujer")

image mujer camina frente:
    "mujer_camina_frente_1"
    pause 0.3
    "mujer_camina_frente_2"
    pause 0.3
    "mujer_camina_frente_3"
    pause 0.3
    "mujer_camina_frente_4"
    pause 0.3
    repeat

image mujer_camina_atras_1 = Crop((0, 128, 128, 128), "spritesheet_mujer")
image mujer_camina_atras_2 = Crop((128, 128, 128, 128), "spritesheet_mujer")
image mujer_camina_atras_3 = Crop((256, 128, 128, 128), "spritesheet_mujer")
image mujer_camina_atras_4 = Crop((384, 128, 128, 128), "spritesheet_mujer")

image mujer camina atras:
    "mujer_camina_atras_1"
    pause 0.3
    "mujer_camina_atras_2"
    pause 0.3
    "mujer_camina_atras_3"
    pause 0.3
    "mujer_camina_atras_4"
    pause 0.3
    repeat

image mujer_camina_izquierda_1 = Crop((0, 256, 128, 128), "spritesheet_mujer")
image mujer_camina_izquierda_2 = Crop((128, 256, 128, 128), "spritesheet_mujer")
image mujer_camina_izquierda_3 = Crop((256, 256, 128, 128), "spritesheet_mujer")
image mujer_camina_izquierda_4 = Crop((384, 256, 128, 128), "spritesheet_mujer")

image mujer camina izquierda:
    "mujer_camina_izquierda_1"
    pause 0.3
    "mujer_camina_izquierda_2"
    pause 0.3
    "mujer_camina_izquierda_3"
    pause 0.3
    "mujer_camina_izquierda_4"
    pause 0.3
    repeat

image mujer_camina_derecha_1 = Crop((0, 384, 128, 128), "spritesheet_mujer")
image mujer_camina_derecha_2 = Crop((128, 384, 128, 128), "spritesheet_mujer")
image mujer_camina_derecha_3 = Crop((256, 384, 128, 128), "spritesheet_mujer")
image mujer_camina_derecha_4 = Crop((384, 384, 128, 128), "spritesheet_mujer")

image mujer camina derecha:
    "mujer_camina_derecha_1"
    pause 0.3
    "mujer_camina_derecha_2"
    pause 0.3
    "mujer_camina_derecha_3"
    pause 0.3
    "mujer_camina_derecha_4"
    pause 0.3
    repeat

image mujer_parada_frente_1 = Crop((0, 512, 128, 128), "spritesheet_mujer")
image mujer_parada_frente_2 = Crop((128, 512, 128, 128), "spritesheet_mujer")
image mujer_parada_frente_3 = Crop((256, 512, 128, 128), "spritesheet_mujer")
image mujer_parada_frente_4 = Crop((384, 512, 128, 128), "spritesheet_mujer")

image mujer parada frente:
    "mujer_parada_frente_1"
    pause 0.3
    "mujer_parada_frente_2"
    pause 0.3
    "mujer_parada_frente_3"
    pause 0.3
    "mujer_parada_frente_4"
    pause 0.3
    repeat

image mujer_parada_atras_1 = Crop((0, 640, 128, 128), "spritesheet_mujer")
image mujer_parada_atras_2 = Crop((128, 640, 128, 128), "spritesheet_mujer")
image mujer_parada_atras_3 = Crop((256, 640, 128, 128), "spritesheet_mujer")
image mujer_parada_atras_4 = Crop((384, 640, 128, 128), "spritesheet_mujer")

image mujer parada atras:
    "mujer_parada_atras_1"
    pause 0.3
    "mujer_parada_atras_2"
    pause 0.3
    "mujer_parada_atras_3"
    pause 0.3
    "mujer_parada_atras_4"
    pause 0.3
    repeat

image mujer_parada_izquierda_1 = Crop((0, 768, 128, 128), "spritesheet_mujer")
image mujer_parada_izquierda_2 = Crop((128, 768, 128, 128), "spritesheet_mujer")
image mujer_parada_izquierda_3 = Crop((256, 768, 128, 128), "spritesheet_mujer")
image mujer_parada_izquierda_4 = Crop((384, 768, 128, 128), "spritesheet_mujer")

image mujer parada izquierda:
    "mujer_parada_izquierda_1"
    pause 0.3
    "mujer_parada_izquierda_2"
    pause 0.3
    "mujer_parada_izquierda_3"
    pause 0.3
    "mujer_parada_izquierda_4"
    pause 0.3
    repeat

image mujer_parada_derecha_1 = Crop((0, 896, 128, 128), "spritesheet_mujer")
image mujer_parada_derecha_2 = Crop((128, 896, 128, 128), "spritesheet_mujer")
image mujer_parada_derecha_3 = Crop((256, 896, 128, 128), "spritesheet_mujer")
image mujer_parada_derecha_4 = Crop((384, 896, 128, 128), "spritesheet_mujer")

image mujer parada derecha:
    "mujer_parada_derecha_1"
    pause 0.3
    "mujer_parada_derecha_2"
    pause 0.3
    "mujer_parada_derecha_3"
    pause 0.3
    "mujer_parada_derecha_4"
    pause 0.3
    repeat

#* VENDEDOR
image vendedor_quieto_1 = Crop((0, 0, 128, 128), "spritesheet_vendedor")
image vendedor_quieto_1 = Crop((128, 0, 128, 128), "spritesheet_vendedor")
image vendedor_quieto_3 = Crop((256, 0, 128, 128), "spritesheet_vendedor")
image vendedor_quieto_4 = Crop((384, 0, 128, 128), "spritesheet_vendedor")
image vendedor_quieto_5 = Crop((512, 0, 128, 128), "spritesheet_vendedor")
image vendedor_quieto_6 = Crop((640, 0, 128, 128), "spritesheet_vendedor")
image vendedor_quieto_7 = Crop((768, 0, 128, 128), "spritesheet_vendedor")
image vendedor_quieto_8 = Crop((896, 0, 128, 128), "spritesheet_vendedor")
image vendedor_quieto_9 = Crop((1024, 0, 128, 128), "spritesheet_vendedor")
image vendedor_quieto_10 = Crop((1152, 0, 128, 128), "spritesheet_vendedor")

image vendedor quieto:
    "vendedor_quieto_1"
    pause 0.3
    "vendedor_quieto_2"
    pause 0.3
    "vendedor_quieto_3"
    pause 0.3
    "vendedor_quieto_4"
    pause 0.3
    "vendedor_quieto_5"
    pause 0.3
    "vendedor_quieto_6"
    pause 0.3
    "vendedor_quieto_7"
    pause 0.3
    "vendedor_quieto_8"
    pause 0.3
    "vendedor_quieto_9"
    pause 0.3
    "vendedor_quieto_10"
    pause 0.3