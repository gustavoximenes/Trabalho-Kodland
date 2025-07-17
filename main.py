import os
import pygame
import pgzrun

# Inicializa pygame
pygame.init()

# Tamanho da janela
WIDTH = 800
HEIGHT = 600

# Física
GRAVITY = 0.5
JUMP_STRENGTH = -10
MOVE_SPEED = 5

ground_y = HEIGHT - 50

# Caminho fixo para a pasta images
IMAGES_PATH = r"C:\Users\Gustavo\Documents\Projeto-Kodland\Python-game\images"

class Hero:
    SCALE = 4  # Aumenta o tamanho do personagem

    def __init__(self):
        self.anim_idle = [self.load_and_scale(f"hero_idle{i}.png") for i in [1, 2]]
        self.anim_run = [self.load_and_scale(f"hero_run{i}.png") for i in [1, 2]]

        self.x = 100
        self.y = ground_y - self.anim_idle[0].get_height() // 2
        self.vel_y = 0
        self.on_ground = False
        self.frame = 0
        self.anim_timer = 0
        self.state = "idle"

    def load_and_scale(self, filename):
        path = os.path.join(IMAGES_PATH, filename)
        print(f"Tentando carregar imagem: {path}")
        img = pygame.image.load(path).convert_alpha()
        w = int(img.get_width() * self.SCALE)
        h = int(img.get_height() * self.SCALE)
        return pygame.transform.scale(img, (w, h))

    def update(self):
        self.move()
        self.apply_gravity()
        self.check_collision()
        self.animate()

    def move(self):
        moving = False
        if keyboard.left:
            self.x -= MOVE_SPEED
            moving = True
        if keyboard.right:
            self.x += MOVE_SPEED
            moving = True

        if keyboard.space and self.on_ground:
            self.vel_y = JUMP_STRENGTH
            self.on_ground = False

        self.state = "run" if moving else "idle"

    def apply_gravity(self):
        self.vel_y += GRAVITY
        self.y += self.vel_y

    def check_collision(self):
        if self.y >= ground_y - self.anim_idle[0].get_height() // 2:
            self.y = ground_y - self.anim_idle[0].get_height() // 2
            self.vel_y = 0
            self.on_ground = True

    def animate(self):
        self.anim_timer += 1
        if self.anim_timer >= 10:
            self.anim_timer = 0
            self.frame = (self.frame + 1) % 2

    def draw(self):
        img = self.anim_idle[self.frame] if self.state == "idle" else self.anim_run[self.frame]
        rect = img.get_rect()
        rect.center = (self.x, self.y)
        screen.surface.blit(img, rect)

# Cria o herói
hero = Hero()

# Carrega e escala o fundo
bg_path = os.path.join(IMAGES_PATH, "background.png")
background_img = pygame.image.load(bg_path).convert()
background_scaled = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

def update():
    hero.update()

def draw():
    screen.surface.blit(background_scaled, (0, 0))  # fundo cobre a tela
    hero.draw()

pgzrun.go()
