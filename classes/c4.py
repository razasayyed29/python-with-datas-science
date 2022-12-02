from pgzero.actor import Actor

class Myactor (Actor):
    speedx = 5
    speedy = 5

    def __init__(self, image, pos=..., anchor=...,speed=0, **kwargs):
        super().__init__(image, pos, anchor, **kwargs)
        self.speedx = self.speedy = speed


    def move(self):
        self.x += self.speedx
        self.y += self.speedy
print(filter(lambda i:not i.startswith('__')or not i.startwith('__'),dir(Myactor)))
#Actor= Myactor('ironman',(100,100), speed=5)        



print(dir(Myactor))