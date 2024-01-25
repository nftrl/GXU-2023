

import pygame
import random
import math
import socket
import os

class Scrollscreen(pygame.sprite.Sprite):
    def __init__(self,scrollimg):
        super().__init__()
        img = pygame.image.load(scrollimg).convert_alpha(screen)
        img = pygame.transform.scale(img, (2000,716))
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (0,0)
        self.scrollspeed = -1.5
        self.skibiditoilet = False
    def update(self):
        self.rect.move_ip(self.scrollspeed,0)
        if self.rect.centerx == -1200:
            self.scrollspeed = self.scrollspeed * -1
            self.skibiditoilet = True
        if self.skibiditoilet == True:
            if self.rect.centerx == 0:
                self.scrollspeed = self.scrollspeed * -1
                self.skibiditoilet = False

class Upgrade_Blob(pygame.sprite.Sprite):
    def __init__(self,blobimg,pos):
        super().__init__()
        self.blobimg = blobimg
        img = pygame.image.load(blobimg).convert_alpha(screen)
        img = pygame.transform.scale(img, (200, 200))
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (pos)

    def upgrade1(self):
        global givammo
        global counting
        global startammoammount
        startammoammount += 1
        counting += 1
        if counting == 2:
            givammo += 1
            self.couting = 0

    def upgrade2(self):
        global bulletdmg
        global counting2
        global pirce
        bulletdmg = bulletdmg + 5
        counting2 += 1
        if counting2 == 4:
            pirce += 1
            counting2 = 0

    def upgrade3(self):
        global flowerhp
        global counting3
        global flowerregen
        flowerhp = flowerhp + 50
        counting3 += 1
        if counting3 == 2:
            flowerregen += 10
            counting3 = 0

    def gg(self):
        self.kill()

    def splat(self):
        global ifsplat
        self.blobimg = ("sprites/splat.png")
        img = pygame.image.load(self.blobimg).convert_alpha(screen)
        img = pygame.transform.scale(img, (200, 200))
        self.image = img
        ifsplat = True

class Ammo(pygame.sprite.Sprite):
    def __init__(self,ammoimg):
        super().__init__()
        img = pygame.image.load(ammoimg).convert_alpha(screen)
        img = pygame.transform.scale(img, (200, 200))
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = ((random.randint(1,screen_width)),(random.randint(1,screen_height)))

    def death_is_invevitibel(self):
        self.kill()

class Turret(pygame.sprite.Sprite):
    def __init__(self,time,speed):
        super().__init__()
        img = pygame.image.load("sprites/target.png")
        img = pygame.transform.scale(img, (200, 200))
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width/2-100,screen_height/2-100)
        self.time = time
        self.speed = speed


    def update(self):
        self.time+=1
        if self.time > self.speed * fps:
            (self.rect.center) = targetpos()
            self.time = 0


class Snegl(pygame.sprite.Sprite):
    def __init__(self, sneglimg,dir,spos,stop,dam,hp,bulletdmg):
        # this initialises the class.
        # It does a lot of things in the background
        # that we do not have to worry about :)
        super().__init__()
        #pos
        #speed
        #self.pos,self.speed=functioncall(xxx)
        self.bulletdmg = bulletdmg
        self.hp = hp
        self.dir = dir
        self.spos = spos
        (self.dir,self.spos) = pos()
        # the visual block or image that we see
        img = pygame.image.load(sneglimg)
        img = pygame.transform.scale(img, (170, 170))
        self.image = img
        # used for position
        self.rect = self.image.get_rect()
        self.rect.center = self.spos
        self.stop = stop
        self.dam = dam

    def update(self):

        if self.stop == False:
            self.rect.move_ip(self.dir)

        if self.hp < 1:
            self.kill()
            pygame.mixer.Sound.play(sneglkill_sound)
            spawnammo()

    def slap(self):
        global flowerhp

        flowerhp -= self.dam
        #print(flowerhp)


    def hit(self):
        self.hp = self.hp - self.bulletdmg


class Flower(pygame.sprite.Sprite):
    def __init__(self, starting_position,flowerimg):

        # this initialises the class.
        # It does a lot of things in the background
        # that we do not have to worry about :)
        super().__init__()

        # the visual block or image that we see
        self.flowerimg = flowerimg
        img = pygame.image.load(self.flowerimg)
        img = pygame.transform.scale(img, (300, 300))
        self.image = img




        # used for position
        self.rect = self.image.get_rect()
        self.rect.center = starting_position


    def die(self):
        self.kill()

    def imgload(self):
        global flowerhp
        global bildet
        global bildet2
        if flowerhp < 51:
            self.flowerimg = ("sprites/downflower1.png")
            img = pygame.image.load(self.flowerimg)
            img = pygame.transform.scale(img, (300, 300))
            self.image = img
            bildet = True
        if bildet == True:
            if flowerhp > 51:
                self.flowerimg = ("sprites/pixil-frame-0 (6).png")
                img = pygame.image.load(self.flowerimg)
                img = pygame.transform.scale(img, (300, 300))
                self.image = img
                bildet = False
        if flowerhp < 21:
            self.flowerimg = ("sprites/downflower2.png")
            img = pygame.image.load(self.flowerimg)
            img = pygame.transform.scale(img, (300, 300))
            self.image = img
            bildet2 = True
        if bildet2 == True:
            if flowerhp > 21:
                self.flowerimg = ("sprites/downflower1.png")
                img = pygame.image.load(self.flowerimg)
                img = pygame.transform.scale(img, (300, 300))
                self.image = img
                bildet2 = False

# A class that represents a player in the game
class Player(pygame.sprite.Sprite):
    def __init__(self, starting_position, keys, speed):

        # this initialises the class.
        # It does a lot of things in the background
        # that we do not have to worry about :)
        super().__init__()

        # the visual block or image that we see
        img = pygame.image.load("sprites/pixil-frame-0 (2).png")
        img = pygame.transform.scale(img, (200, 200))
        self.image = img
        # used for position
        self.rect = self.image.get_rect()
        self.rect.center = starting_position





        # movement chars and speed
        (self.up, self.down, self.left, self.right) = keys # unpack keys
        self.speed = speed


    def update(self, ks):

        if ks[self.up]:
            self.rect.move_ip(0, -self.speed)
        if ks[self.down]:
            self.rect.move_ip(0, self.speed)
        if ks[self.left]:
            self.rect.move_ip(-self.speed, 0)
        if ks[self.right]:
            self.rect.move_ip(self.speed, 0)


        if ks[pygame.K_UP]:
            self.rect.move_ip(0, -self.speed)
        if ks[pygame.K_DOWN]:
            self.rect.move_ip(0, self.speed)
        if ks[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if ks[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        #self.rect.centerx = self.x
        #self.rect.centery = self.y

        if self.rect.centerx > screen_width:
            self.rect.centerx -= 20
        if self.rect.centerx < 0:
            self.rect.centerx += 20

        if self.rect.centery < 0:
            self.rect.centery += 20
        if self.rect.centery > screen_height:
            self.rect.centery -= 20

class Bullet(pygame.sprite.Sprite):
    def __init__(self,bulletpirce):
        super().__init__()

        self.bulletpirce = bulletpirce

        img = pygame.image.load("sprites/shot2.png").convert_alpha(screen)
        img = pygame.transform.scale(img, (20, 20))
        self.image = img
        self.rect = self.image.get_rect()

        (self.mousex, self.mousey) = mousepos
        (self.playerx, self.playery) = playerpos
        self.playerx += 20
        self.playery -= 20
        self.mousex += 20
        self.mousey -= 20
        self.rect.center = (self.playerx,self.playery)

        self.x = (self.mousex - self.playerx)
        self.y = (self.mousey - self.playery)

        self.soon_r = self.x * self.x + self.y * self.y
        self.r = math.sqrt(float(self.soon_r))
        self.dx = float(self.x/self.r)
        self.dy = float(self.y / self.r)

        self.dx *= 5
        self.dy *= 5

        #self.diry = float(self.mousey - self.playery) / float(self.mousex - self.playerx)

    def update(self):
        self.playerx += 20
        self.playery -= 20
        self.mousex += 20
        self.mousey -= 20
        #if self.xde > 0:
            #self.x = -1
            #self.diry = self.diry * -1
        #else:
            #self.x = 1

        self.rect.centery += self.dy
        self.rect.centerx += self.dx

    def koopa_trooper_ostehaps_fiskefille_selvmord(self):
        self.kill()


# Global variables
fps = 60

screen_width = 800
screen_height = 716

color_background = (200,200,200)
color_player = (255,255,255)

flowerhp = 100
startflowerhp = 100
atc = False
i = 0
sek = 0
ting = 0
ting2 = 0
turretsize = 200
shot = False
shotbullet = True
i2 = 0
i4 = 0
sneglhp = 20
how_many_snegls_udrabstegn = 2
bulletdmg = 10
startammoammount = 6
ammoamount = startammoammount
ammoamountspawn = 3
fromammoamountspawn = 2
ifsplat = False
h = True
wavesurvived= 1
waveend = False
wavestart = True
spawn = True
sneglamount = 5
snegldmg = 10
blubpos1 = (screen_width/2 - 200,screen_height/2 + 200)
blubpos2 = (screen_width/2 + 200,screen_height/2 + 200)
blubpos3 = (screen_width/2,screen_height/2 + 200)
blubid = 0
readyforupgrade = True
counting = 0
counting2 = 0
counting3 = 0
bulletcanhit = True
pirce = 1
flowerregen = 0
bildet = False
bildet2 = False
givammo = 1
sneglspeed = 1
j = False
fjolletvariabel = True
pygame.font.init()
hostname = socket.gethostname()
desmasjovetal = socket.gethostbyname(hostname)
font = pygame.font.SysFont('Comic Sans MS', 50)
color = (0, 0, 0)
color2 = (232, 200, 0)
color3 = (255, 0, 0)
color4 = (0,255,255)
textpos4 = (screen_width / 2 - 100, screen_height / 2 - 100)
textpos5 = (screen_width / 2 - 150, screen_height / 2 - 150)
textpos6 = (screen_width / 2 - 100, screen_height / 2 - 200)
textpos7 = (screen_width / 2 - 150, screen_height / 2 + 200)
gameover = "gameover"
messagedif = random.randint(1,15)
textpos3 = (100, screen_height / 2 - 50)

messages = {1: "bliv bedre", 2: "Skill issue", 3: "get good", 4: "du lort", 5: "du værre end min mormor",
            6: "bad game", 7: "bruh", 8: "kom ikke igen", 9: "nej.", 10: "du er bare dårlig",
            11: "bad played", 12: "jeg skuffet", 13: "gg          " + desmasjovetal,
            14: "slå din computer no balls", 15: "you suck ass"}
ggmessage = messages[(messagedif)]
newhighscore = False
hj = font.render(str(gameover), True, color3)
ja = font.render(str(ggmessage), True, color)
jmanden = font.render(str("NEW HIGHSCORE!"), True, color4)
menu = True

def placepic(pic,x,y,size_x,size_y):
    img = pygame.image.load(pic).convert_alpha(screen)
    img = pygame.transform.scale(img, (size_x, size_y))
    screen.blit(img, (x, y))

def spawnsnegl():

    snegl = Snegl("sprites/pixil-frame-0 (3).png", (1, 1), (200, 200), False, snegldmg,sneglhp,bulletdmg)
    snegls.add(snegl)
    all_sprites.add(snegl)
    all_snegls.add(snegl)

def spawnammo():
    i3 = 0
    spawnammoamount = random.randint(fromammoamountspawn,ammoamountspawn)
    while i3 < spawnammoamount:
        i3 += 1
        ammo = Ammo("sprites/ammo.png")
        ammos.add(ammo)
        all_sprites.add(ammo)


def pos():
    ranposdis = random.randint(1,6)
    ranposlir = {1: "L", 2: "R", 3: "TL", 4: "TR", 5: "BL", 6: "BR"}
    ranpos = ranposlir[(ranposdis)]

    if ranpos == "L":
        sranpos = (0, screen_height / 2)
        di = (sneglspeed, 0)
    elif ranpos == "R":
        sranpos = (screen_width, screen_height / 2)
        di = (-sneglspeed, 0)
    elif ranpos == "TL":
        sranpos = (0, 0)
        di = (sneglspeed, sneglspeed)
    elif ranpos == "TR":
        sranpos = (screen_width, 0)
        di = (-sneglspeed, sneglspeed)
    elif ranpos == "BL":
        di = (sneglspeed, -sneglspeed)
        sranpos = (0, screen_height)
    elif ranpos == "BR":
        di = (-sneglspeed, -sneglspeed)
        sranpos = (screen_width, screen_height)
    return di,sranpos


def targetpos():

    chose = random.randint(1,8)
    poslir = {1:(screen_width/2+turretsize/2,screen_height/2),
              2:(screen_width/2+turretsize/2,screen_height/2+turretsize/2),
              3:(screen_width/2+turretsize/2,screen_height/2-turretsize/2),
              4:(screen_width/2,screen_height/2-turretsize/2),

              5:(screen_width/2-turretsize/2,screen_height/2),
              6:(screen_width/2-turretsize/2,screen_height/2+turretsize/2),
              7:(screen_width/2-turretsize/2,screen_height/2-turretsize/2),
              8:(screen_width/2,screen_height/2+turretsize/2)}
    pos = poslir[(chose)]
    return pos

def sneglupgrade():
    global sneglhp
    global sneglspeed
    global how_many_snegls_udrabstegn
    choseupgarde = random.randint(1,3)
    if choseupgarde == 1:
        sneglhp = sneglhp + 10
        how_many_snegls_udrabstegn = how_many_snegls_udrabstegn + 1
    if choseupgarde == 2:
        sneglspeed = sneglspeed + 0.5
        how_many_snegls_udrabstegn = how_many_snegls_udrabstegn + 1
    if choseupgarde == 2:
        how_many_snegls_udrabstegn = how_many_snegls_udrabstegn + 2


def wave(snelgamo):
    global ting
    global spawn
    global ting2
    global readyforupgrade
    if ting == snelgamo:
        spawn = False
        ting2 = 0
        ting = 0

    if spawn == True:
        ting2 += 1

        if ting2 == fps/2:
            ting += 1
            ting2 = 0
            spawnsnegl()
            readyforupgrade = True

def wave_joeheim_end():
    blub1 = Upgrade_Blob("sprites/blub bullet.png", blubpos1)
    blub2 = Upgrade_Blob("sprites/blub dmg.png", blubpos2)
    blub3 = Upgrade_Blob("sprites/blub flower hp.png", blubpos3)
    blub1s.add(blub1)
    blub2s.add(blub2)
    blub3s.add(blub3)
    blubs.add(blub1)
    blubs.add(blub2)
    blubs.add(blub3)
    all_sprites.add(blub1)
    all_sprites.add(blub2)
    all_sprites.add(blub3)






# Initialising pygame instance
pygame.init()
#sounds
sneglkill_sound = pygame.mixer.Sound("sounds/hitHurt.wav")
levelup_sound = pygame.mixer.Sound("sounds/pickupCoin.wav")
shoot_sound = pygame.mixer.Sound("sounds/laserShoot.wav")
blubsplat_sound = pygame.mixer.Sound("sounds/very-loud-splat-88998.mp3")
sneglmomse_sound =pygame.mixer.Sound("sounds/nom-nom-nom_gPJiWn4.mp3")
gameover_sound =pygame.mixer.Sound("sounds/wah-wah-sad-trombone-6347.mp3")
sneglhit_sound =pygame.mixer.Sound("sounds/punch-140236.mp3")
reload_sound =pygame.mixer.Sound("sounds/1911-reload-6248.mp3")
pygame.mixer.music.load('sounds/video-game-music-loop-27629.mp3')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

# Set up the drawing window
screen = pygame.display.set_mode((screen_width, screen_height))

# Sprites
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
flowers = pygame.sprite.Group()
snegls = pygame.sprite.Group()
all_snegls = pygame.sprite.Group()
turrets = pygame.sprite.Group()
bullets = pygame.sprite.Group()
ammos = pygame.sprite.Group()
blubs = pygame.sprite.Group()
blub1s = pygame.sprite.Group()
blub2s = pygame.sprite.Group()
blub3s = pygame.sprite.Group()
menusprites = pygame.sprite.Group()

player1 = Player((screen_width/2, screen_height/2-50), (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d), 7)
players.add(player1)
all_sprites.add(player1)


flower = Flower((screen_width/2, screen_height/2-50),"sprites/pixil-frame-0 (6).png")
flowers.add(flower)
all_sprites.add(flower)


snegl = Snegl("sprites/pixil-frame-0 (3).png",(1,1),(200,200),False,snegldmg,sneglhp,bulletdmg)
snegls.add(snegl)
all_sprites.add(snegl)
all_snegls.add(snegl)


#turret = Turret(0,1)
#turrets.add(turret)
#all_sprites.add(turret)

blub1 = Upgrade_Blob("sprites/blub bullet.png", blubpos1)
blub2 = Upgrade_Blob("sprites/blub dmg.png", blubpos2)
blub3 = Upgrade_Blob("sprites/blub flower hp.png", blubpos3)

ammo = Ammo("sprites/ammo.png")

scrollscreen = Scrollscreen("sprites/scorllscreen.png")

pygame.mouse.set_visible(False)


# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill(color_background)


    if menu:
        screen.blit(scrollscreen.image, (scrollscreen.rect.centerx,scrollscreen.rect.centery))
        scrollscreen.update()
        placepic("sprites/titel.png",screen_width/2-250,screen_height/2-300,500,500)
        pressstart = font.render(str("press space to start"), True, color)
        textpos4 = (screen_width/2-225, screen_height/2+20)
        screen.blit(pressstart, textpos4)
        if not os.path.exists('highscore.txt'):
            with open('highscore.txt', 'w') as f:
                f.write("0")
        with open('highscore.txt', 'r') as f:
            skibidihighscore = f.read()
        skibidi = font.render(str("highscore: " + str(skibidihighscore)), True, color)

        screen.blit(skibidi,textpos7)

        ks = pygame.key.get_pressed()
        if ks[pygame.K_SPACE]:
            menu = False

    else:
        mousepos = pygame.mouse.get_pos()
        (mousex,mousey) = mousepos



        playerpos = player1.rect.center
        placepic("sprites/background.png",0,0,screen_width,screen_height-50)


        # Fill the background


        # get key presses
        ks = pygame.key.get_pressed()
        i += 1



        collided = pygame.sprite.groupcollide(snegls, flowers, dokilla=False, dokillb=False,collided=pygame.sprite.collide_mask)
        for snegl in collided:
            for flower in collided[snegl]:
                snegl.stop = True

                while i > fps:
                    snegl.slap()
                    pygame.mixer.Sound.play(sneglmomse_sound)
                    flower.imgload()
                    i = 0
#----------------------------------DEATH---------------------------------------
        if flowerhp < 1:
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(gameover_sound)
            highscore = 1000000000000000000
            if not os.path.exists('highscore.txt'):
                with open('highscore.txt', 'w') as f:
                    f.write("0")
            with open('highscore.txt', 'r') as f:
                prehighscore = f.read()
                if not prehighscore:
                    prehighscore = 0
                highscore = int(prehighscore)
            if highscore < int(wavesurvived):
                with open('highscore.txt', 'w') as f:
                    wavesurvived = str(wavesurvived)
                    f.write(wavesurvived)
                    highscoremessage = wavesurvived
                    newhighscore = True


            flower.die()

            if newhighscore == True:
                screen.blit(jmanden,textpos6)

            screen.blit(ja, textpos3)

            screen.blit(hj, textpos4)

            player1.kill()
            for sprite in snegls:
                if isinstance(sprite, Snegl):
                    sprite.kill()
            readyforupgrade = False

        collided = pygame.sprite.groupcollide(snegls, bullets, dokilla=False, dokillb=False,collided=pygame.sprite.collide_mask)
        collided_bullets = []
        for snegl in collided:
            for bullet in collided[snegl]:
                collided_bullets.append(bullet)
                if bullet.bulletpirce >= 1:
                    if bulletcanhit == True:
                        snegl.hit()
                        pygame.mixer.Sound.play(sneglhit_sound)
                        bulletcanhit = False
                        bullet.bulletpirce -= 1


        for bullet in bullets:
            if bullet in collided_bullets:
                continue
            bulletcanhit = True
            if bullet.bulletpirce < 1:
                bullet.koopa_trooper_ostehaps_fiskefille_selvmord()

        collided = pygame.sprite.groupcollide(players, ammos, dokilla=False, dokillb=False,collided=pygame.sprite.collide_mask)
        for player1 in collided:
            for ammo in collided[player1]:
                pygame.mixer.Sound.play(reload_sound)
                ammoamount = ammoamount + givammo
                ammo.death_is_invevitibel()

        collided = pygame.sprite.groupcollide(players, blub1s, dokilla=False, dokillb=False,collided=pygame.sprite.collide_mask)
        for player1 in collided:
            for blub1 in collided[player1]:
                blub1.splat()
                blub3.gg()
                blub2.gg()
                blubid = 1


        collided = pygame.sprite.groupcollide(players, blub2s, dokilla=False, dokillb=False,collided=pygame.sprite.collide_mask)
        for player1 in collided:
            for blub2 in collided[player1]:
                blub2.splat()
                blub1.gg()
                blub3.gg()
                blubid = 2

        collided = pygame.sprite.groupcollide(players, blub3s, dokilla=False, dokillb=False,collided=pygame.sprite.collide_mask)
        for player1 in collided:
            for blub3 in collided[player1]:
                blub3.splat()
                blub1.gg()
                blub2.gg()
                blubid = 3






        wave(how_many_snegls_udrabstegn)

        i2 = i2 + 1

        if ammoamount > 0:

            if shotbullet == True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    bullet = Bullet(pirce)
                    bullets.add(bullet)
                    all_sprites.add(bullet)
                    ammoamount = ammoamount - 1
                    shotbullet = False
                    pygame.mixer.Sound.play(shoot_sound)
                    i2 = 0

            if i2 > fps/3:
                shotbullet = True

        if readyforupgrade == True:
            if not all_snegls:
                waveend = True
                readyforupgrade = False

        if h == True:
            if waveend == True:
                blub1 = Upgrade_Blob("sprites/blub bullet.png", blubpos1)
                blub2 = Upgrade_Blob("sprites/blub dmg.png", blubpos2)
                blub3 = Upgrade_Blob("sprites/blub flower hp.png", blubpos3)
                blub1s.add(blub1)
                blub2s.add(blub2)
                blub3s.add(blub3)
                blubs.add(blub1)
                blubs.add(blub2)
                blubs.add(blub3)
                all_sprites.add(blub1)
                all_sprites.add(blub2)
                all_sprites.add(blub3)


                h = False



        if ifsplat == True:
            if fjolletvariabel == True:
                pygame.mixer.Sound.play(blubsplat_sound)
            fjolletvariabel = False
            wave(how_many_snegls_udrabstegn)
            i4 += 1
            if i4 > fps * 2:
                fjolletvariabel = True
                wavesurvived += 1
                pygame.mixer.Sound.play(levelup_sound)
                if blubid == 1:
                    blub1.upgrade1()
                if blubid == 2:
                    blub1.upgrade2()
                if blubid == 3:
                    blub1.upgrade3()
                sneglupgrade()
                blub1.gg()
                blub2.gg()
                blub3.gg()
                wavestart = True
                ting = 0
                spawn = True
                waveend = False
                for sprite in ammos:
                    if isinstance(sprite, Ammo):
                        sprite.kill()
                ammoamount = startammoammount
                flower.imgload()
                flowerhp += flowerregen
                h = True
                ifsplat = False
                i4 = 0






        bullets.update()
        # update sprites
        players.update(ks)
        #img = pygame.image.load("C:\Users\mart92b0\PycharmProjects\tower\sprites\pixil-frame-0 (2).png")
        #screen.blit(img, (0, 0))
        #turrets.update()
        snegls.update()
        # draw sprites on the screen
        all_sprites.draw(screen)
        wavecounder = font.render(str(wavesurvived), True, color)
        textpos1 = (screen_width / 2, 50)
        screen.blit(wavecounder, textpos1)

        placepic("sprites/ammo_place.png", -110, -20, 300, 300)

        ammocounder = font.render(str(ammoamount), True, color2)
        textpos2 = (30,100)
        screen.blit(ammocounder, textpos2)

        placepic("sprites/curser.png", mousex, mousey, 20, 20)


        #placepic("sprites/pixil-frame-0 (8).png", screen_width / 2 -150, screen_height / 2 -150, 300, 300)

        # execute the drawing to the screen
    pygame.display.flip()

        # handle fps
    clock.tick(fps)


# Done! Time to quit.
pygame.quit()
