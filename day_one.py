import pygame
import random
# from objects import Grumpy, Pipe, Base, Score

# Initialize pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH, SCREEN_HEIGHT = 288, 512
DISPLAY_HEIGHT = int(0.80 * SCREEN_HEIGHT)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Set up the clock
clock = pygame.time.Clock()
FPS = 30

# Define colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load backgrounds
bg1 = pygame.image.load('Assets/background-day.png')
bg2 = pygame.image.load('Assets/background-night.png')

# Choose a random background
background = random.choice([bg1, bg2])

# Load assets
pipe_images = [pygame.image.load('Assets/pipe-green.png'), pygame.image.load('Assets/pipe-red.png')]
gameover_img = pygame.image.load('Assets/gameover.png')
flappybird_img = pygame.image.load('Assets/flappybird.png')
flappybird_img = pygame.transform.scale(flappybird_img, (200, 80))

# Load sounds
die_sound = pygame.mixer.Sound('Sounds/die.wav')
hit_sound = pygame.mixer.Sound('Sounds/hit.wav')
point_sound = pygame.mixer.Sound('Sounds/point.wav')
swoosh_sound = pygame.mixer.Sound('Sounds/swoosh.wav')
wing_sound = pygame.mixer.Sound('Sounds/wing.wav')

class Bird:
	def __init__(self, win):
		self.win = win

		self.im_list = []
		bird_color = random.choice(['red', 'blue', 'yellow'])
		for i in range(1,4):
			img =  pygame.image.load(f'Assets/Grumpy/{bird_color}{i}.png')
			self.im_list.append(img)
		
		self.reset()
		
	def update(self):
		# gravity
		self.vel += 0.3
		if self.vel >= 8:
			self.vel = 8
		if self.rect.bottom <= 0.80 * SCREEN_HEIGHT:
			self.rect.y += int(self.vel)

# Set initial game variables
base_height = 0.80 * SCREEN_HEIGHT
speed = 0
game_started = False
game_over = False
restart = False
score = 0
start_screen = True
pipe_pass = False
pipe_frequency = 1600

# Main game loop
running = True
while running:
    screen.blit(background, (0, 0))
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
