""" this is the game made using python's pygame library and it is similar to chrome dino game, to view it's learning process you can view another file"""
"""also would like to share that this game got deleted and recovered from chatgpt (thanks)"""
"""it is completed on 13/02/2024"""

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
        if (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]) and self.rect.bottom >= 200:
            self.sound.play()
            self.gravity = -15
    
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

bg_sound = pygame.mixer.Sound('F:/IIITN/Coding/Python/Ash_Dino_Game/Background_music.mp3')
bg_sound.set_volume(0.1)

def display_score():
    curr_time = int((pygame.time.get_ticks() - start_time)/100)
    score_surf = test_font.render(f'Score: {curr_time}',True,(64,64,64))
    score_rectangle = score_surf.get_rect(topleft = (650,15))
    screen.blit(score_surf,score_rectangle)
    return curr_time

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

test_font = pygame.font.Font('F:\IIITN\Coding\Python\Ash_Dino_Game\Rainyhearts.ttf',50)

screen = pygame.display.set_mode((900,500))
pygame.display.set_caption('Ash_Dino_Game')
clock = pygame.time.Clock()
start_time = 0

gamename = test_font.render('Ash_Dino_Game',True,(64,64,64))
gamename_rect = gamename.get_rect(center = (450,300))
message_font = pygame.font.Font(None,30)

game_active = False

ground_surface = pygame.Surface((900,200))
ground_surface.fill('Green')

sky_surface = pygame.image.load('F:\IIITN\Coding\Python\Ash_Dino_Game\Sky_Background.jpg').convert_alpha()
sky_surface = pygame.transform.scale(sky_surface,(900,300))

dino = pygame.sprite.GroupSingle()
dino.add(Dino())
obstacle_group = pygame.sprite.Group()

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

score_now = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE) and dino.sprite.rect.bottom >= 200:
                    gravity = -21
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_active = True
                    start_time = pygame.time.get_ticks()
        
        if event.type == obstacle_timer and game_active:
            obstacle_group.add(Obstacle(choice(['single','double','single'])))
                
    if game_active:
        screen.blit(sky_surface,(0,0))
        score_now = display_score()
        screen.blit(ground_surface,(0,300))
        dino.draw(screen)
        dino.update()
        obstacle_group.draw(screen)
        obstacle_group.update()
        game_active = collison_sprite()
    else:
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
        
    pygame.display.update()
    clock.tick(60)