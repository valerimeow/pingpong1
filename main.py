from pygame import*

window = display.set_mode((700,500))
back = (102, 59, 203) #0-255 0-255 0-255
background = transform.scale(image.load('fon.jpg'),(700,500))



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, w, h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = player_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_p] and self.rect.y > 5:     #[K_UP]  [K_DOWN]
            self.rect.y -= self.speed
        if keys[K_l] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

player_l = Player('racket1.png', 20, 200, 50, 100,10)
player_r = Player('racket.png', 600, 200, 50, 100, 10)
ball = GameSprite('ball.png', 200, 200, 40, 40, 20)

game = True
finish = False

speed_x = 5
speed_y = 5

font.init()
font1 = font.SysFont('Arial', 40)
lose1 = font1.render('проиграл 1 игрок', True, (205, 79, 35))
lose2 = font1.render('проиграл 2 игрок', True, (205, 79, 35))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background,(0,0))
        player_l.reset()
        player_r.reset()
        ball.reset()
        
        player_l.update_l()
        player_r.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(ball, player_l) or sprite.collide_rect(ball, player_r):
            speed_x *= -1
        if ball.rect.y < 5 or ball.rect.y > 450:
            speed_y *= -1
        
        if ball.rect.x < 5:
            window.blit(lose1, (200,200))
            finish = True
        if ball.rect.x > 655:
            window.blit(lose2, (200,200))
            finish = True
    display.update()
    time.delay(60)