import os
import pygame
import pgzrun

# Inicializa pygame
pygame.init()

WIDTH = 800
HEIGHT = 600

GRAVITY = 0.5
JUMP_STRENGTH = -10
MOVE_SPEED = 5

# Caminho fixo para imagens
IMAGES_PATH = r"C:\Users\Gustavo\Documents\Projeto-Kodland\Python-game\images"

# Retângulo de colisão do chão
GROUND_RECT = pygame.Rect(0, 472, WIDTH, HEIGHT - 472)

class Hero:
    SCALE = 3

    def __init__(self):
        self.anim_idle = [self.load_and_scale(f"hero_idle{i}.png") for i in [1, 2]]
        self.anim_run = [self.load_and_scale(f"hero_run{i}.png") for i in [1, 2]]

        self.x = 100
        self.image_height = self.anim_idle[0].get_height()
        self.y = GROUND_RECT.top - self.image_height // 2
        self.vel_y = 0
        self.on_ground = False
        self.frame = 0
        self.anim_timer = 0
        self.state = "idle"
        self.facing_right = True  # Direção inicial

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
            self.facing_right = False
        if keyboard.right:
            self.x += MOVE_SPEED
            moving = True
            self.facing_right = True

        if keyboard.space and self.on_ground:
            self.vel_y = JUMP_STRENGTH
            self.on_ground = False

        self.state = "run" if moving else "idle"

    def apply_gravity(self):
        self.vel_y += GRAVITY
        self.y += self.vel_y

    def check_collision(self):
        bottom_y = self.y + self.image_height // 2
        if bottom_y >= GROUND_RECT.top:
            self.y = GROUND_RECT.top - self.image_height // 2
            self.vel_y = 0
            self.on_ground = True
        else:
            self.on_ground = False

    def animate(self):
        self.anim_timer += 1
        if self.anim_timer >= 10:
            self.anim_timer = 0
            self.frame = (self.frame + 1) % 2

    def draw(self):
        img_list = self.anim_idle if self.state == "idle" else self.anim_run
        img = img_list[self.frame]
        if not self.facing_right:
            img = pygame.transform.flip(img, True, False)  # Inverte a imagem horizontalmente
        rect = img.get_rect()
        rect.center = (self.x, self.y)
        screen.surface.blit(img, rect)

hero = Hero()

# Carrega e escala o fundo
bg_path = os.path.join(IMAGES_PATH, "background.png")
background_img = pygame.image.load(bg_path).convert()
background_scaled = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

def update():
    hero.update()

def draw():
    screen.surface.blit(background_scaled, (0, 0))
    hero.draw()
    

pgzrun.go()
