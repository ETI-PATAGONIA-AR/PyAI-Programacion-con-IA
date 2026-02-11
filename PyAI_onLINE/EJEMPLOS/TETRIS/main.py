import pygame
import random

pygame.init()

# Definir colores
negro = (0, 0, 0)
blanco = (255, 255, 255)
gris = (128, 128, 128)

# Definir tamaño de la pantalla
ancho_pantalla = 400
alto_pantalla = 500
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

# Definir título de la ventana
pygame.display.set_caption("Tetris")

# Definir tamaño de los bloques
tamaño_bloque = 20

# Definir figuras
figuras = [
    [[1, 1],
     [1, 1]],

    [[1, 1, 1, 1]],

    [[1, 1, 0],
     [0, 1, 1]],

    [[0, 1, 1],
     [1, 1, 0]],

    [[1, 1, 1],
     [0, 1, 0]],

    [[1, 1, 1],
     [1, 0, 0]],

    [[1, 1, 1],
     [0, 0, 1]]
]

# Definir clase para los bloques
class Bloque:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dibujar(self):
        pygame.draw.rect(pantalla, blanco, (self.x * tamaño_bloque, self.y * tamaño_bloque, tamaño_bloque, tamaño_bloque))

# Definir clase para las figuras
class Figura:
    def __init__(self, x, y, figura):
        self.x = x
        self.y = y
        self.figura = figura
        self.bloques = []

        for i in range(len(figura)):
            for j in range(len(figura[i])):
                if figura[i][j] == 1:
                    self.bloques.append(Bloque(x + j, y + i))

    def dibujar(self):
        for bloque in self.bloques:
            bloque.dibujar()

    def mover_abajo(self):
        self.y += 1
        for bloque in self.bloques:
            bloque.y += 1

    def mover_derecha(self):
        self.x += 1
        for bloque in self.bloques:
            bloque.x += 1

    def mover_izquierda(self):
        self.x -= 1
        for bloque in self.bloques:
            bloque.x -= 1

    def girar(self):
        self.figura = [list(reversed(x)) for x in zip(*self.figura)]
        self.bloques = []
        for i in range(len(self.figura)):
            for j in range(len(self.figura[i])):
                if self.figura[i][j] == 1:
                    self.bloques.append(Bloque(self.x + j, self.y + i))

# Definir clase para el juego
class Juego:
    def __init__(self):
        self.figura_actual = Figura(5, 0, random.choice(figuras))
        self.bloques_fijos = []
        self.pausado = False
        self.iniciado = False
        self.timer = 0
        self.bajar_rapido = False

    def dibujar(self):
        pantalla.fill(negro)
        if self.iniciado:
            self.figura_actual.dibujar()
            for bloque in self.bloques_fijos:
                bloque.dibujar()
        else:
            font = pygame.font.Font(None, 36)
            texto = font.render("Presiona ENTER para iniciar", True, blanco)
            pantalla.blit(texto, (ancho_pantalla // 2 - texto.get_width() // 2, alto_pantalla // 2 - texto.get_height() // 2))
        pygame.display.flip()

    def actualizar(self):
        if self.iniciado and not self.pausado:
            self.timer += 1
            if self.bajar_rapido:
                if self.timer >= 7:
                    self.timer = 0
                    self.figura_actual.mover_abajo()
                    if self.choca_con_bloques_fijos() or self.choca_con_piso():
                        self.figura_actual.y -= 1
                        for bloque in self.figura_actual.bloques:
                            bloque.y -= 1
                        self.bloques_fijos.extend(self.figura_actual.bloques)
                        self.figura_actual = Figura(5, 0, random.choice(figuras))
            else:
                if self.timer >= 30:
                    self.timer = 0
                    self.figura_actual.mover_abajo()
                    if self.choca_con_bloques_fijos() or self.choca_con_piso():
                        self.figura_actual.y -= 1
                        for bloque in self.figura_actual.bloques:
                            bloque.y -= 1
                        self.bloques_fijos.extend(self.figura_actual.bloques)
                        self.figura_actual = Figura(5, 0, random.choice(figuras))
            self.eliminar_lineas_completas()

    def choca_con_bloques_fijos(self):
        for bloque in self.figura_actual.bloques:
            for bloque_fijo in self.bloques_fijos:
                if bloque.x == bloque_fijo.x and bloque.y == bloque_fijo.y:
                    return True
        return False

    def choca_con_piso(self):
        for bloque in self.figura_actual.bloques:
            if bloque.y >= alto_pantalla // tamaño_bloque:
                return True
        return False

    def eliminar_lineas_completas(self):
        lineas_completas = []
        for y in range(alto_pantalla // tamaño_bloque):
            linea_completa = True
            for x in range(ancho_pantalla // tamaño_bloque):
                bloque_encontrado = False
                for bloque in self.bloques_fijos:
                    if bloque.x == x and bloque.y == y:
                        bloque_encontrado = True
                        break
                if not bloque_encontrado:
                    linea_completa = False
                    break
            if linea_completa:
                lineas_completas.append(y)
        for linea in lineas_completas:
            for bloque in self.bloques_fijos:
                if bloque.y == linea:
                    self.bloques_fijos.remove(bloque)
            for bloque in self.bloques_fijos:
                if bloque.y < linea:
                    bloque.y += 1

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_a:
                    self.figura_actual.mover_izquierda()
                    if self.choca_con_bloques_fijos() or self.choca_con_pared_izquierda():
                        self.figura_actual.mover_derecha()
                elif evento.key == pygame.K_d:
                    self.figura_actual.mover_derecha()
                    if self.choca_con_bloques_fijos() or self.choca_con_pared_derecha():
                        self.figura_actual.mover_izquierda()
                elif evento.key == pygame.K_s:
                    self.bajar_rapido = True
                elif evento.key == pygame.K_SPACE:
                    self.figura_actual.girar()
                elif evento.key == pygame.K_p:
                    self.pausado = not self.pausado
                elif evento.key == pygame.K_RETURN:
                    self.iniciado = True
                elif evento.key == pygame.K_q:
                    pygame.quit()
                    quit()
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_s:
                    self.bajar_rapido = False

    def choca_con_pared_izquierda(self):
        for bloque in self.figura_actual.bloques:
            if bloque.x < 0:
                return True
        return False

    def choca_con_pared_derecha(self):
        for bloque in self.figura_actual.bloques:
            if bloque.x >= ancho_pantalla // tamaño_bloque:
                return True
        return False

# Crear juego
juego = Juego()

# Bucle principal
while True:
    juego.dibujar()
    juego.actualizar()
    juego.manejar_eventos()
    pygame.time.delay(10)