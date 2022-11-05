from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, speed, x, y, w, h, img):
        super().__init__()
        self.image = transform.scale(image.load())
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

class paddle(GameSprite):
    def L_paddle(self):
        #keys = key.get pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed
    
    def R_paddle(self):
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed

#class ball(GameSprite):
    #direction = "left"
    #def update(self):
        #if self.direction ==