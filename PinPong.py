from pygame import *
from random import randint

win_width = 700
win_height = 500

window = display.set_mode((600, 500))
display.set_caption('PinPong_Game')
window.fill((138, 133, 255))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

players_1 = Player('racket.png', 30 , 200 , 50 ,150 ,4)
players_2 = Player('racket.png', 520 , 200 , 50 ,150 ,4)
ball = GameSprite('ball.png', 200 , 200 , 50 ,50 ,4)

clok = time.Clock()
game = True
finish = False
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False

    if not finish:
        window.fill((138, 133, 255))

        players_1.update_l()
        players_2.update_r()
        players_1.reset()
        players_2.reset()
        ball.reset()



    display.update()



    clok.tick(60)

