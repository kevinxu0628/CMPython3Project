import pygame
import random
from os import path 
import time


pygame.init()


screen_width = 1280
screen_height = 800

clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("CrIn v1.31")



# bg = pygame.image.load("").convert()


# bg_rect = bg.get_rect(center = (640, 400))


# playerchoice = int(input("select your character...(1-6)"))

# if playerchoice == 1:
player_img = pygame.image.load("merchant 1.png").convert()

# if playerchoice == 2:
#     player_img = pygame.image.load("merchant 2.png").convert()

# if playerchoice == 3:
#     player_img = pygame.image.load("merchant 3.png").convert()

# if playerchoice == 4:
#     player_img = pygame.image.load("merchant 4.png").convert()

# if playerchoice == 5:
#     player_img = pygame.image.load("merchant 5.png").convert()
    
# if playerchoice == 6:
#     player_img = pygame.image.load("merchant 6.png").convert()






enemychoice = ["merchant 1.png", "merchant 2.png", "merchant 3.png", "merchant 4.png", "merchant 5.png", "merchant 6.png"]


woodgraphics = pygame.image.load("wood.png").convert()

watergraphics = pygame.image.load("new water.png").convert()


toggle1graphics= pygame.image.load("IMG_2039.jpg").convert()

white = (255,255,255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (66, 135, 245)
pink = (255, 0, 212)


font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render (text, True, black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)



class Player(pygame.sprite.Sprite):
    def __init__(self):
    #call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        #create an image of the block and fill it with a color
        #this could also be an image loaded from the disk
        #set player image to basket image
        self.image = pygame.transform.scale(player_img, (30, 30))
        #get rid of black outline

        self.image.set_colorkey((0,0,0))


        #Fetch the rectangle object that has the dimensions of the image
        #Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect(center = (screen_width/2, screen_height/2))

        self.x_speed = 0
        self.y_speed = 0


    def update(self):
        self.x_speed = 0
        self.y_speed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.y_speed -= 2
        elif keystate[pygame.K_DOWN]:
            self.y_speed += 2
        elif keystate[pygame.K_LEFT]:
            self.x_speed -= 2
        elif keystate[pygame.K_RIGHT]:
            self.x_speed += 2
        
        if self.rect.right >= screen_width:
            self.rect.right = screen_width
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height


        self.rect.x += self.x_speed 
        self.rect.y += self.y_speed

class Enemy(pygame.sprite.Sprite):
        def __init__(self, enemy_img):
            pygame.sprite.Sprite.__init__(self)
            #need to resize image because it is too large
            self.image = pygame.transform.scale(enemy_img, (30, 30))
            self.image.set_colorkey((0,0,0))

            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(0, 1280)
            self.rect.y = random.randrange(0, 800)
        
        def update(self):
            self.x_speed = 0
            self.y_speed = 0
            dir = random.randint(1,4)
            if dir == 1:
                self.y_speed -= 2
            elif dir == 2:
                self.y_speed += 2
            elif dir == 3:
                self.x_speed -= 12
            elif dir == 4:
                self.x_speed += 12
            
            if self.rect.right >= screen_width:
                self.rect.right = screen_width
            if self.rect.left <= 0:
                self.rect.left = 0
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= screen_height:
                self.rect.bottom = screen_height


            self.rect.x += self.x_speed 
            self.rect.y += self.y_speed


class Wood(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(woodgraphics, (20,20))
        self.image.set_colorkey((0,0,0))

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 1280)
        self.rect.y = random.randrange(0, 800)
        self.count = 0

    def mine(self):
        self.count += 10


class Water(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(watergraphics, (20,20))
        self.image.set_colorkey((0,0,0))

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 1280)
        self.rect.y = random.randrange(0, 800)
        self.count = 0


    def mine(self):
        self.count += 10


class Toggle1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(toggle1graphics, (80,56))
        self.image.set_colorkey((0,0,0))

        self.rect =  self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10


    def inBoundaries(self, pos):
        #check if mouse click happened inside the boundaries of the button 
        if pos[0] > self.rect.x and pos[0] < self.rect.x + 80:
            if pos[1] > self.rect.y and pos[1] < self.rect.y + 56:
                print(pos)
                return True
            return False

TradeMode = Toggle1
# burpButton = Button(blue, 200, 50, 100, 100, "Burp")
# applauseButton = Button(pink, 350, 50, 100, 100, "Applause") 


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
    

enemies = pygame.sprite.Group()
wood = pygame.sprite.Group()
water = pygame.sprite.Group()
toggle1 = pygame.sprite.Group()

# creates random enemies and resources
for i in range(49):
    c = random.randint(0,5)
    enemy_img = pygame.image.load(enemychoice[c]).convert()            

    e = Enemy(enemy_img)
    all_sprites.add(e)
    enemies.add(e)

    wo = Wood()
    all_sprites.add(wo)
    wood.add(wo)

    wa = Water()
    all_sprites.add(wa)
    water.add(wa)

    to = Toggle1()
    all_sprites.add(to)



    


wealth = 0

x = 0

while True:
    clock.tick(60)

    x += 1

    all_sprites.update()
    
    

    


    wood_hits = pygame.sprite.spritecollide(player, wood, False)
    water_hits = pygame.sprite.spritecollide(player, water, False)
    player_hits = wood_hits + water_hits


    for e in enemies:
        enemy_hits = pygame.sprite.spritecollide(e, wood, False)
        enemy_hits = pygame.sprite.spritecollide(e, water, False)
        # print(e)
    print(player_hits)
    print(enemy_hits)


    if x % 3600 == 0:
        wo = Wood()    
        all_sprites.add(wo)
        wood.add(wo)
        wa = Water()
        all_sprites.add(wa)
        water.add(wa)

    for hit in player_hits:
        hit.mine()
        if hit.count >= 6000:
            hit.kill()
            wealth += 5
    
 


    screen.fill((255,255,255))
     #make bg display here 
    all_sprites.draw(screen)

    draw_text(screen, str(wealth), 18, screen_width/2, 10) #call draw_text function here 


    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if TradeMode.inBoundaries(pos): #check if mouse click happened inside of button
                print("button works")