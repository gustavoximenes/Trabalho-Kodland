import math
import pygame
from pygame import Rect
import pgzrun

WIDTH = 800
HEIGHT = 600

# Constantes de física
GRAVITY = 0.5
JUMP_STRENGTH = -10
MOVE_SPEED = 5

# Plataforma (chão)
ground = Rect(0, HEIGHT - 50, WIDTH, 50)

# Herói
class Hero:
    def __init__(self):
        # Apenas 2 frames para cada animação
        self.anim_idle = ["hero_idle1", "hero_idle2"]
        self.anim_run = ["hero_run1", "hero_run2"]
        self.actor = Actor(self.anim_idle[0])
        self.actor.pos = (100, HEIGHT - 100)
        self.vel_y = 0
        self.on_ground = False
        self.frame = 0
        self.anim_timer = 0
        self.state = "idle"  # ou "run"

    def update(self):
        self.move()
        self.apply_gravity()
        self.check_collision()
        self.animate()

    def move(self):
        moving = False
        if keyboard.left:
            self.actor.x -= MOVE_SPEED
            moving = True
        if keyboard.right:
            self.actor.x += MOVE_SPEED
            moving = True

        if keyboard.space and self.on_ground:
            self.vel_y = JUMP_STRENGTH
            self.on_ground = False

        self.state = "run" if moving else "idle"

    def apply_gravity(self):
        self.vel_y += GRAVITY
        self.actor.y += self.vel_y

    def check_collision(self):
        if self.actor.y >= ground.top - self.actor.height // 2:
            self.actor.y = ground.top - self.actor.height // 2
            self.vel_y = 0
            self.on_ground = True

    def animate(self):
        self.anim_timer += 1
        if self.anim_timer >= 10:  # troca de frame a cada 10 ticks
            self.anim_timer = 0
            self.frame = (self.frame + 1) % 2  # só dois quadros por animação

            if self.state == "idle":
                self.actor.image = self.anim_idle[self.frame]
            elif self.state == "run":
                self.actor.image = self.anim_run[self.frame]

    def draw(self):
        self.actor.draw()

# Instância do herói
hero = Hero()

def update():
    hero.update()

def draw():
    screen.clear()

    # Redimensiona e desenha o fundo para cobrir toda a tela
    bg_scaled = pygame.transform.scale(images.background, (WIDTH, HEIGHT))
    screen.surface.blit(bg_scaled, (0, 0))

    hero.draw()

pgzrun.go()
