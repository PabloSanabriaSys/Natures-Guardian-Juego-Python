import pygame
from pygame.locals import *
import sys
from models.Mascota import Pet
from models.Cazador import Cazador
import time

pygame.init()

# Configuración de la ventana
coordenadas_ventana = (780, 480)
dis_mov = 50
ventana = pygame.display.set_mode(coordenadas_ventana)
pygame.display.set_caption("Nature's Guardian")
# Cargar una fuente
font_nombre = pygame.font.Font(None, 36)  # Tamaño de fuente 36
font_post = pygame.font.Font(None, 25)  # Tamaño de fuente 28

# Inicializamos fondo
background = pygame.image.load("assets/fondo.jpg").convert()
background = pygame.transform.scale(background, coordenadas_ventana)
background.set_alpha(200)
anterior = background

# Inicializamos la pizza
pizza = pygame.image.load("assets/pizza.png").convert_alpha()
tamanio_p = pizza.get_size()[0] / 10, pizza.get_size()[1] / 10
pizza = pygame.transform.scale(pizza, tamanio_p)
pizza_inicio=700, 100
x_pizza, y_pizza = pizza_inicio
dragging_pizza = False

# Inicializamos la quinsacharaña
kimsa = pygame.image.load("assets/Quimsacharani-transparente.png").convert_alpha()
tamanio_kimsa = kimsa.get_size()[0] / 7, kimsa.get_size()[1] / 7
kimsa = pygame.transform.scale(kimsa, tamanio_kimsa)
kimsa_inicio=700, 160
x_kimsa, y_kimsa = kimsa_inicio
dragging_kimsa = False

# Inicializamos la tuerca
tuerca = pygame.image.load("assets/tuerca.png").convert_alpha()
tamanio_tuerca = tuerca.get_size()[0] / 2.5, tuerca.get_size()[1] /2.5
tuerca = pygame.transform.scale(tuerca, tamanio_tuerca)

# Inicializamos la boton tienda
tienda = pygame.image.load("assets/brn_compras.png").convert_alpha()
tamanio_tienda = tienda.get_size()[0] / 4, tienda.get_size()[1] / 4
tienda = pygame.transform.scale(tienda, tamanio_tienda)

# Inicializamos la vida
salud = pygame.image.load("assets/salud.png").convert_alpha()
tamanio_salud = salud.get_size()[0] / 25, salud.get_size()[1] /25
salud = pygame.transform.scale(salud, tamanio_salud)

# Inicializamos la felicidad
felicidad = pygame.image.load("assets/felicidad.png").convert_alpha()
tamanio_felicidad = felicidad.get_size()[0] / 25, felicidad.get_size()[1] / 25
felicidad = pygame.transform.scale(felicidad, tamanio_felicidad)

# Inicializamos la pizza
ico_pizza = pygame.image.load("assets/pizza_bar.png").convert_alpha()
tamanio_ico_pizza = ico_pizza.get_size()[0] / 25, ico_pizza.get_size()[1] / 25
ico_pizza = pygame.transform.scale(ico_pizza, tamanio_ico_pizza)

# Load animation frames
quir_animation_frames = [
    pygame.image.load("assets/frame1.png"),  # Replace with your image filenames
    pygame.image.load("assets/frame2.png"),
    pygame.image.load("assets/frame3.png")
    # Add more frames as needed
]
frases = [
    pygame.image.load("assets/LETRA_1.png"),
    pygame.image.load("assets/LETRA_2.png"),
    pygame.image.load("assets/LETRA_3.png")
    # Add more frames as needed
]
frame_muerte=pygame.image.load("assets/frame_muerto.png")
# Animation variables
frame_index = 0
frame_delay = 300  # Adjust this value to control animation speed
frame_counter = 0

# Quirquincho
x_quir,y_quir=285, 170
tamanio_quir=200,300
quirquincho = Pet(frases, 'urkupinita', tamanio_quir[0], tamanio_quir[1], quir_animation_frames,frame_muerte)


# Cazador
caza_animation_frames = [
    pygame.image.load("assets/cazador1.png")
]
x_caza,y_caza=-100, 175
tamanio_caza=250,300
x_maxima=100
caza = Cazador( tamanio_caza[0], tamanio_caza[1], caza_animation_frames,mov_speed=0.05,lp=3)
running = True

tiempo_caza = time.time()
tiempo_balacera = time.time()
tiempo_ini = time.time()
tiempo_mensaje = time.time()

final=True
cont_caza=0

#sonido de fondo
sonido_comer=pygame.mixer.Sound('sonido/sonido_comer.mp3')
sonido_kimsa=pygame.mixer.Sound('sonido/latigo.mp3')
sonido_disparo=pygame.mixer.Sound('sonido/disparo_380.mp3')


pygame.mixer.music.load('sonido/sound_fondo.mp3')
pygame.mixer.music.set_volume(0.04)
pygame.mixer.music.play(-1)




##########################
# Configurar la fuente
font = pygame.font.Font(None, 36)

# Configurar el texto de los créditos
credits = ['','','','','','','CREDITOS', 'DESARROLLADORES:',' Eguino Vazques Leonardo Rene',' Alias: " ENCARGADO "',' Sanabria  Becerra Pablo',' Alias: " OSTEOPOROSIS "', 'DISEÑADORES:',' Alessandra Carrizal Paco',' Alias: " LA ALE "',' URIONA ARTEAGA SERGIO ANDRE',' Alias: " EL CAMBA "','MUSICA: Amilcar Isai Huanaco Triveño',' Alias: "HUANAKIER"',' MUSICA DE CREDITOS: ',' FolklorGuitar ( YouTube )',' ']
text = []

# Cargar las imágenes
image_start = pygame.image.load('assets/title.png')
image_end = pygame.image.load('assets/quir_movimiento_adobe_express.png')

# Agregar la imagen de inicio a la lista de texto
text.append((image_start.get_rect(centerx=320, y=480), image_start))

for i, line in enumerate(credits):
    s = font.render(line, 1, (255, 255, 255))
    r = s.get_rect(centerx=320, y=480 + (i + 2) * 45)
    text.append((r, s))

# Agregar la imagen final a la lista de texto
text.append((image_end.get_rect(centerx=320, y=480 + (len(credits) + 2) * 45), image_end))

for i, line in enumerate(credits):
    s = font.render(line, 1, (255, 255, 255))
    r = s.get_rect(centerx=320, y=480 + (i + 2) * 45)
    text.append((r, s))

# Configurar el mensaje final
final_message = 'Ningun quirquincho fue lastimado en la realizacion de este proyecto      EXCEPTO URKUPIÑITA.......'
final_message_surface = font.render(final_message, 1, (255, 255, 255))
final_message_rect = final_message_surface.get_rect(x=coordenadas_ventana[0], centery=460)

# Record: Eguino - 17 cazadores
def convert_to_grayscale(surface):
    width, height = surface.get_size()
    grayscale_surface = pygame.Surface((width, height))

    for y in range(height):
        for x in range(width):
            pixel_color = surface.get_at((x, y))
            gray_value = sum(pixel_color[:3]) // 3
            grayscale_color = (gray_value, gray_value, gray_value, pixel_color.a)
            grayscale_surface.set_at((x, y), grayscale_color)

    return grayscale_surface

def barra_progreso(pos_x,pos_y,valor_total,valor_actual,bar_color,logo=None):
    background_color = (50, 50, 50)
    # Tamaño de la barra de progreso
    bar_width = 200
    bar_height = 17
    # Valor actual y valor máximo de la barra de progreso

    # Dibujar la barra de fondo
    pygame.draw.rect(ventana, background_color, (pos_x,pos_y, bar_width, bar_height))
    # Calcular la longitud de la barra de progreso basada en el valor actual
    progress_length = int(bar_width * (valor_actual / valor_total))

    # Dibujar la barra de progreso
    pygame.draw.rect(ventana, bar_color, (pos_x,pos_y, progress_length, bar_height))

    # Renderizar el texto en una superficie
    text_post = font_post.render(str(valor_actual), True, (255, 255, 255))
    # Dibujar la superficie con el texto en la ventana
    ventana.blit(text_post, (pos_x+bar_width+10,pos_y))
    if logo:
        ventana.blit(logo, (pos_x-25,pos_y-2))
mostrar_facto=False
mostrando=False
principal=True
indice_m=None
mostrar_creditos=False
tiempo_muerte=0
while True:
    if principal:
        for e in pygame.event.get():

            if e.type == QUIT:
                pygame.quit()
                sys.exit()

            # mover pizza
            elif e.type == MOUSEBUTTONDOWN:

                mouse_x, mouse_y = pygame.mouse.get_pos()
                pizza_rect = pizza.get_rect(topleft=(x_pizza, y_pizza))
                kimsa_rect = kimsa.get_rect(topleft=(x_kimsa, y_kimsa))
                # Detectamos la pizza con el click
                if pizza_rect.collidepoint(mouse_x, mouse_y):
                    dragging_pizza = True
                    offset_x = mouse_x - x_pizza
                    offset_y = mouse_y - y_pizza

                # Detectamos la quisacharaña con el click
                elif kimsa_rect.collidepoint(mouse_x, mouse_y):
                    dragging_kimsa = True
                    offset_x = mouse_x - x_kimsa
                    offset_y = mouse_y - y_kimsa

            elif e.type == MOUSEBUTTONUP :
                #detectamos si la pizza esta en el
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if quirquincho.is_alive() and dragging_pizza and x_quir <= mouse_x <= x_quir + tamanio_quir[0] and y_quir <= mouse_y <= y_quir + tamanio_quir[1]:
                    x_pizza, y_pizza=pizza_inicio
                    quirquincho.eat(20)
                    sonido_comer.play(0)

                # detectamos si la quisacharaña esta en el cazador
                elif  quirquincho.is_alive() and dragging_kimsa and x_quir <= mouse_x <= x_quir + tamanio_quir[0] and y_quir <= mouse_y <= y_quir + tamanio_quir[1]:
                    x_kimsa, y_kimsa=kimsa_inicio
                    quirquincho.take_damage(20)
                    sonido_kimsa.play(0)
                    if not quirquincho.is_alive():
                        background = convert_to_grayscale(background)

                elif  quirquincho.is_alive() and y_quir <= mouse_y <= y_quir + tamanio_quir[1] and x_quir <= mouse_x <= x_quir + tamanio_quir[0]:
                    quirquincho.pet_him(20)


                elif caza.is_alive() and dragging_kimsa and x_caza <= mouse_x <= x_caza + tamanio_caza[0] and y_caza <= mouse_y <= y_caza + tamanio_caza[1]:
                    x_kimsa, y_kimsa=kimsa_inicio
                    sonido_kimsa.play(0)
                    caza.take_damage(1)
                    if not caza.is_alive():
                        cont_caza += 1

                dragging_pizza = False
                dragging_kimsa=False

            elif e.type == KEYDOWN:
                if e.key == K_b:
                    anterior = background
                    background = convert_to_grayscale(background)
                elif e.key == K_c:
                    background = anterior
                elif e.key == K_p:
                    principal=False
                    pygame.mixer.music.load('sonido/sound_sad.mp3')
                    pygame.mixer.music.set_volume(1)
                    pygame.mixer.music.play(-1)
        #Verificamos muerte Quirquincho
        if not quirquincho.is_alive() and final:
            background = convert_to_grayscale(background)
            tiempo_muerte=time.time()
            mostrar_creditos=True
            final=False
        #Verificamos Muerte Cazador


        #Rebajamos felicidad y comida
        if (time.time() - tiempo_ini >=7):
            tiempo_ini=time.time()
            quirquincho.reduce_food(5)
            quirquincho.reduce_hap(15)
            quirquincho.handle_health()




        #Reiniciamos el cazador
        if (time.time() - tiempo_caza >= 10 and not caza.is_alive()):
            tiempo_caza = time.time()
            # Cazador
            x_caza = -100
            caza = Cazador(tamanio_caza[0], tamanio_caza[1], caza_animation_frames, mov_speed=caza.mov_speed+0.01, lp=caza.max_lp+0.5)

        #Se deja de ver el Mensaje
        if(time.time() - tiempo_mensaje >= 7 and not mostrando):
            mostrar_facto=True
            indice_m=quirquincho.display_fact()
            mostrando = True

        if (time.time() - tiempo_mensaje >=12):
            mostrar_facto = False
            mostrando=False
            tiempo_mensaje = time.time()

        #Movemos al cazador
        if (x_caza <= x_maxima and caza.is_alive()):
            x_caza += caza.get_mov_speed()
            tiempo_balacera = time.time()
        elif x_caza > x_maxima and caza.is_alive() and quirquincho.is_alive():
            if time.time() - tiempo_balacera >= 1:
                quirquincho.take_damage(5)
                tiempo_balacera=time.time()
                sonido_disparo.play(0)

        if mostrar_creditos:
            if time.time()-tiempo_muerte>=5:
                principal = False
                pygame.mixer.music.load('sonido/sound_sad.mp3')
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play(-1)

        if dragging_pizza:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            x_pizza = mouse_x - offset_x
            y_pizza = mouse_y - offset_y
        elif dragging_kimsa:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            x_kimsa = mouse_x - offset_x
            y_kimsa = mouse_y - offset_y

        #cambio de frame
        frame_counter +=1
        if frame_counter >= frame_delay:
            frame_counter = 0
            frame_index = (frame_index + 1) % len(quirquincho.frames)
        # ventana
        ventana.fill((0, 0, 0))


        #Fondo
        ventana.blit(background, (0, 0))
        # Renderizar el texto en una superficie
        text_surface = font_nombre.render("Urkupiñita", True, (255, 255, 255))
        text_puntaje = font_nombre.render("Cazadores: "+str(cont_caza), True, (255, 255, 255))
        # Dibujar la superficie con el texto en la ventana
        ventana.blit(text_surface, (20, 20))
        ventana.blit(text_puntaje, (500, 20))
        # quiquincho
        #pygame.draw.rect(ventana, (255, 0, 0), (x_quir, y_quir, tamanio_quir[0], tamanio_quir[1]), 2)
        if quirquincho.is_alive():
            quirquincho.draw_element(ventana, (x_quir,y_quir), frame_index)
        else:
            quirquincho.draw_kill(ventana,0)

        # cazador
        if caza.is_alive() and quirquincho.is_alive():
            caza.draw_element(ventana, (x_caza, y_caza), 0)
        #pygame.draw.rect(ventana, (255, 0, 0), (x_caza, y_caza, tamanio_caza[0], tamanio_caza[1]), 2)

        # pizza
        ventana.blit(pizza, (x_pizza, y_pizza))
        # kimsa
        ventana.blit(kimsa, (x_kimsa, y_kimsa))
        #tuerca
        ventana.blit(tuerca,(700,10))
        # tienda
        ventana.blit(tienda, (680, 380))
        #Mensaje
        if (mostrar_facto and quirquincho.is_alive() and indice_m):
            ventana.blit(indice_m, (300, 20))


        barra_progreso(30, 50,quirquincho.max_lp, quirquincho.lp,(255,0,0),logo=salud)
        barra_progreso(30, 75, quirquincho.max_food, quirquincho.food, (255, 255, 0),logo=ico_pizza)
        barra_progreso(30, 100, quirquincho.max_hap, quirquincho.hap, (0, 255, 0),logo=felicidad)
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        ventana.fill((0, 0, 0))

        for r, s in text:
            if r != text[-1][0]:
                r.move_ip(0, -1)
            ventana.blit(s, r)

        if text[-2][0].y < -text[-2][0].height:
            final_message_rect.move_ip(-1, 0)
            if final_message_rect.x < -final_message_surface.get_width():
                final_message_rect.x = coordenadas_ventana[0]
            ventana.blit(final_message_surface, final_message_rect)

        # if text[-2][0].y < -text[-2][0].height:
        #     break

        pygame.display.flip()
        pygame.time.wait(10)
    pygame.display.flip()