import pygame

SCREENSIZE = (800, 600)
TITLE = "Tuto Pygame"
FPS = 60
PLAYER_VEL = 10

TILESIZE = 32
 
LIGHTGREY = (110,110,110)
YELLOW = (255,255,0)
BLACK = (0,0,0)
LIGHTSEAGREEN = (32,178,170)
MAROON = (128,0,0)
CORAL = (255,127,80)
LIGHTSTEALBLUE = (176,196,222)
FORESTGREEN = (34,139,34)

BGCOLOR = FORESTGREEN

class Player(pygame.sprite.Sprite):
    
    # constructeur de la classe
    def __init__(self, x, y):
        super().__init__()
        self.image_right = pygame.image.load("assets/perso_right.png")
        self.image_left = pygame.image.load("assets/perso_left.png")
        self.image = self.image_right
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, direction):
        if direction == "R" and self.rect.right < SCREENSIZE[0]:
            self.image = self.image_right
            self.rect.x += PLAYER_VEL
        elif direction == "L" and self.rect.left > 0:
            self.image = self.image_left
            self.rect.x -= PLAYER_VEL
        elif direction == "D" and self.rect.bottom < SCREENSIZE[1]:
            self.image = self.image_right
            self.rect.y += PLAYER_VEL
        elif direction == "U" and self.rect.top > 0:
            self.image = self.image_right
            self.rect.y -= PLAYER_VEL


class Game(object):
    
    # Constructeur de la classe  
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def closeWindow(self):
        if self.playing:
            self.playing = False
        self.running = False
        
    def events(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.closeWindow()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    self.closeWindow()
            elif keys[pygame.K_RIGHT]:
                self.player.move("D")
            elif keys[pygame.K_LEFT]:
                self.player.move("Q")
            elif keys[pygame.K_DOWN]:
                self.player.move("S")
            elif keys[pygame.K_UP]:
                self.player.move("Z")
                    
    def update(self):
        self.all_sprites.update()
   
    def draw(self):
        # couleur de fond d'écran
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        pygame.display.update()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(SCREENSIZE[0] / 2, SCREENSIZE[1] / 2)
        self.all_sprites.add(self.player)
        
# programme principal
game = Game()
game.new()
while game.running:
    game.run()
pygame.quit()