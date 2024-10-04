from pygame import *
from random import randint
window = display.set_mode((700,500))
display.set_caption('Шутер')

background = transform.scale(image.load(r'C:\Users\Alena.k.mur.AcerNotebook\Downloads\image\backfor.jpg'),(700,500))

game = True
finish = False
clock = time.Clock()
FPS = 60
lost = 0

speed_x = 4
speed_y = 4
font.init()
font1 = font.Font(None,45)
lose1 = font1.render('Player 1 Lose!',True,(100,100,100))
lose2 = font1.render('Player 2 Lose!',True,(100,100,100))
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,high,width):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(high,width))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y  < 450:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed





player_sprite = Player(r'C:\Users\Alena.k.mur.AcerNotebook\Downloads\image\player.jpg',30,250,8,50,60)
player_sprite2 = Player(r'C:\Users\Alena.k.mur.AcerNotebook\Downloads\image\player.jpg',620,250,4,50,60)
enemy = GameSprite(r'C:\Users\Alena.k.mur.AcerNotebook\Downloads\image\ball.jpg',randint(50,630),randint(50,450,),4,40,40)
while game:

    for i in event.get():
        if i.type == QUIT:
            game = False

    if finish != True:
        enemy.rect.x += speed_x
        enemy.rect.y += speed_y
        if enemy.rect.y>500-40 or enemy.rect.y<0:
            speed_y *= -1
        if sprite.collide_rect(player_sprite,enemy) or sprite.collide_rect(player_sprite2,enemy):
            speed_x *= -1
        window.blit(background,(0,0))
        if enemy.rect.x <0:
            finish =True
            window.blit(lose1,(350,250))
        if enemy.rect.x >700-40:
            finish=True
            window.blit(lose2,(350,250))
        player_sprite.reset()
        player_sprite.update_l()
        player_sprite2.reset()
        player_sprite2.update_r()
        enemy.reset()


    display.update()
    clock.tick(FPS)