""" this is the game making tutorial or trial or something like timepass started on 07/02/2024"""
""" this file contains the whole making of the game for just to view the code refer another file"""
import pygame
from sys import exit
from random import randint, choice

pygame.init()

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1 = pygame.image.load('F:\IIITN\Coding\Python\Ash_Dino_Game\dino1.gif').convert_alpha()
        self.image1 = pygame.transform.scale(self.image1,(110,90))
        self.image2 = pygame.image.load('F:\IIITN\Coding\Python\Ash_Dino_Game\dino2.gif').convert_alpha()
        self.image2 = pygame.transform.scale(self.image2,(110,90))
        self.dino_walk = [self.image1,self.image2]
        self.image3 = self.image1
        self.dino_index = 0
        self.image = self.dino_walk[self.dino_index]
        self.rect = self.image.get_rect(topleft = (20,225))
        self.gravity = 0
        self.sound = pygame.mixer.Sound('F:\IIITN\Coding\Python\Ash_Dino_Game\dino_jump_sound.mp3')
        self.sound.set_volume(0.01)
    def dino_input(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]) and self.rect.bottom >= 300:
            self.sound.play()
            self.gravity = -21
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.image3
        else:
            self.dino_index += 0.1
            if self.dino_index >= len(self.dino_walk):
                self.dino_index = 0
            self.image = self.dino_walk[int(self.dino_index)]
    def update(self):
        self.dino_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type == 'single':
            obstacle1 = pygame.image.load('F:\IIITN\Coding\Python\Ash_Dino_Game\obstacle_1.jpeg')
            obstacle1 = pygame.transform.scale(obstacle1,(40,40))
            self.frames = obstacle1
        else:
            obstacle2 = pygame.image.load('F:\IIITN\Coding\Python\Ash_Dino_Game\obstacle_2.jpeg')
            obstacle2 = pygame.transform.scale(obstacle2,(80,40))
            self.frames = obstacle2
        self.image = self.frames
        self.rect = self.image.get_rect(midbottom = (randint(800,1200),300))
    def destroy(self):
        if self.rect.x <= -75:
            self.kill()
    def update(self):
        self.rect.x -= 6
        self.destroy()

# gamemusic
bg_sound = pygame.mixer.Sound('F:\IIITN\Coding\Python\Ash_Dino_Game\Background_music.mp3')
bg_sound.set_volume(0.1)
# bg_sound.play(loops = -1)         
    
# display score
def display_score():
    curr_time = int((pygame.time.get_ticks() - start_time)/100)
    score_surf = test_font.render(f'Score: {curr_time}',True,(64,64,64))
    score_rectangle = score_surf.get_rect(topleft = (650,15))
    # pygame.draw.rect(screen,'#b0eaff',score_rectangle,0,10)
    screen.blit(score_surf,score_rectangle)
    return curr_time

# move obstacle
# def obstacle_movement(obstacle_list):
#     if obstacle_list:
#         for obstacle in obstacle_list:
#             obstacle.right -= 6
#             if obstacle.bottom == 300:
#                 screen.blit(obstacle1_surface,obstacle)
#             else:
#                 screen.blit(obstacle2_surface,obstacle)
#         obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -75]
#         return obstacle_list
#     else:
#         return []

# collisions
# def collisions(player,obstacles):
#     if obstacles:
#         for obstacle in obstacles:
#             if player.colliderect(obstacle):
#                 return False
#     return True

bg_playing = False

def collison_sprite():
    global bg_playing
    if pygame.sprite.spritecollide(dino.sprite, obstacle_group, False):
        obstacle_group.empty()
        endgame_sound = pygame.mixer.Sound('F:\IIITN\Coding\Python\Ash_Dino_Game\game_over_music.wav')
        if bg_playing:
            bg_sound.stop()
            bg_playing = False
        endgame_sound.play()
        pygame.time.delay(1000)
        return False
    else:
        if not bg_playing and game_active:
            bg_sound.play(loops=-1)
            bg_playing = True
        return True


# animations
# def dino_animation():
#     global dino_surface, dino_index
#     if dino_rect.bottom < 300:
#         dino_surface = dino1_surface
#     else:
#         dino_index += 0.1
#         if dino_index >= len(dino_walk):
#             dino_index = 0
#         dino_surface = dino_walk[int(dino_index)]

# print("hello")

# font
test_font = pygame.font.Font('F:\IIITN\Coding\Python\Ash_Dino_Game\Rainyhearts.ttf',50)

# setting up screen
screen = pygame.display.set_mode((900,500)) # set_mode((width,height))
pygame.display.set_caption('Ash_Dino_Game')
# setting up out clock
clock = pygame.time.Clock()
start_time = 0

# gamename
gamename = test_font.render('Ash_Dino_Game',True,(64,64,64))
gamename_rect = gamename.get_rect(center = (450,300))
message_font = pygame.font.Font(None,30)

game_active = False

# ground surface
ground_surface = pygame.Surface((900,200)) # pygame.Surface((width,height))
ground_surface.fill('Green')

#sky surface
sky_surface = pygame.image.load('F:\IIITN\Coding\Python\Ash_Dino_Game\Sky_Background.jpg').convert_alpha() # convert is used to make the game run faster but it adds background to the image so we use convert_alpha(it doesn't add background to the image)
sky_surface = pygame.transform.scale(sky_surface,(900,300))

# score font surface
# score_font = pygame.font.Font('F:\IIITN\Coding\Python\Ash_Dino_Game\Rainyhearts.ttf',50) # .Font(font_type,font_size)
# score_surface = score_font.render('Score',True,(64,64,64)) # .render(text,Anti Aliasing,color)
# score_rect = score_surface.get_rect(topleft = (750,15))

# # dino surface
# dino1_surface = pygame.image.load('F:\IIITN\Coding\Python\Ash_Dino_Game\dino1.gif').convert_alpha()
# dino1_surface = pygame.transform.scale(dino1_surface,(110,90))
# dino_rect = dino1_surface.get_rect(topleft = (20,225))
# dino2_surface = pygame.image.load('F:\IIITN\Coding\Python\Ash_Dino_Game\dino2.gif').convert_alpha()
# dino2_surface = pygame.transform.scale(dino2_surface,(110,90))
# dino_rect = dino2_surface.get_rect(topleft = (20,225))
# dino_walk = [dino1_surface,dino2_surface]
# dino_index = 0
# dino_surface = dino_walk[int(dino_index)]

# Groups
dino = pygame.sprite.GroupSingle()
dino.add(Dino())
obstacle_group = pygame.sprite.Group()

# obstacle surface
# obstacle1_surface = pygame.image.load('F:\IIITN\Coding\Python\Ash_Dino_Game\obstacle_1.jpeg')
# obstacle1_surface = pygame.transform.scale(obstacle1_surface,(40,40))
# # obstacle1_rect = obstacle1_surface.get_rect(bottomright = (800,300))
# obstacle2_surface = pygame.image.load('F:\IIITN\Coding\Python\Ash_Dino_Game\obstacle_2.jpeg')
# obstacle2_surface = pygame.transform.scale(obstacle2_surface,(80,40))
# # obstacle2_rect = obstacle2_surface.get_rect(bottomright = (800,300))
# obstacle_rect_list = []
# timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1800)

# gravity
# gravity = -21

# dino_x = 0
# dino_y = 225

score_now = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): # to exit from game and avoid infinite loop
            pygame.quit()
            exit()
            
        # this is the event method to get the position of mouse
        # if event.type == pygame.MOUSEMOTION: # events can also use MOUSEBUTTONUP and MOUSEBUTTONDOWN
        #     if dino_rect.collidepoint(event.pos): # this is how you can use event method to determine mouse position
        #         print("collide")
        
        if game_active:
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE) and dino.sprite.rect.bottom >= 200:
                    gravity = -21
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_active = True      
                    # obstacle1_rect.x -= 150
                    start_time = pygame.time.get_ticks()
        
        if event.type == obstacle_timer and game_active:
            obstacle_group.add(Obstacle(choice(['single','double','single'])))
            # if randint(0,2):
            #     obstacle_rect_list.append(obstacle1_surface.get_rect(bottomright = (randint(800,1200),300)))
            # else:
            #     obstacle_rect_list.append(obstacle2_surface.get_rect(bottomright = (randint(800,1200),301)))
                
    if game_active:
        # placing order of surfaces matters
        # sky surface placed
        screen.blit(sky_surface,(0,0))

        # score surface placed
        # pygame.draw.rect(screen,'#c0e8ec',score_rect)
        # pygame.draw.rect(screen,'#b0eaff',score_rect,0,10)
        # screen.blit(score_surface,score_rect)
        score_now = display_score()

        # ground surface placed
        screen.blit(ground_surface,(0,300)) # .blit(surface,position)

        # code for placing obstacle1 surface
        # obstacle1_rect.right -= 6
        # if obstacle1_rect.right <= 0:
        #     obstacle1_rect.right = 900
        # screen.blit(obstacle1_surface,obstacle1_rect)
        
        # obstacle movement
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # moving dino without fitting it in rectangle
        # dino_x += 4
        # if(dino_x == 900):
        #     dino_x = 0

        # code for placing and moving dino surface
        # dino_rect.left += 4
        # if dino_rect.left==900:
        #     dino_rect.left = 0
        
        # gravity += 1
        # dino_rect.y += gravity
        # if dino_rect.bottom > 300:
        #     dino_rect.bottom = 300
        # dino_animation()
        # screen.blit(dino_surface,dino_rect)
        dino.draw(screen)
        dino.update()
        obstacle_group.draw(screen)
        obstacle_group.update()

        # checking rectangle-wise collision
        # if dino_rect.colliderect(obstacle1_rect):
        #     print("collision")

        # checking point-wise collision
        # mouse_pos = pygame.mouse.get_pos() # used to get the position of mouse
        # if dino_rect.collidepoint(mouse_pos):
        #     # print("collision")
        #     print(pygame.mouse.get_pressed()) # gives the info that which key on mouse is pressed in the boolean format (left,center,right)

        # # to do some event if some key is pressed
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]: # key for space
        #     print("jmpp")

        # game over
        # if dino_rect.colliderect(obstacle1_rect):
        #     game_active = False
        # game_active = collisions(dino_rect,obstacle_rect_list)
        game_active = collison_sprite()
    else:
        # obstacle_rect_list.clear()
        # dino_rect.topleft = (20,225)
        # gravity = 0
        screen.fill((50,205,50))
        dino_endgame = pygame.image.load('F:\IIITN\Coding\Python\Ash_Dino_Game\dino.png').convert_alpha()
        dino_endgame = pygame.transform.rotozoom(dino_endgame,0,1)
        dino_rectangle = dino_endgame.get_rect(center = (450,175))
        screen.blit(dino_endgame,dino_rectangle)
        screen.blit(gamename,gamename_rect)
        if score_now:
            gamemessage = message_font.render('Press ENTER to RUN again',False,(64,64,64))
            gamemessage_rect = gamemessage.get_rect(center = (450,400))
            endscore = message_font.render(f'Score: {score_now}',True,(64,64,64))
            endscore_rect = endscore.get_rect(center = (450,360))
            screen.blit(endscore,endscore_rect)
        else:
            gamemessage = message_font.render('Press ENTER to RUN',False,(64,64,64))
            gamemessage_rect = gamemessage.get_rect(center = (450,350))
        screen.blit(gamemessage,gamemessage_rect)
        
    pygame.display.update() # this updates the screen again and again else it would be only the black screen
    clock.tick(60) # this is the timer that at what rate program should run