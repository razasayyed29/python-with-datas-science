import pgzrun

HEIGHT = 600
WIDTH = 1200

p = Actor('ironman (2)',center=(WIDTH//2, HEIGHT//2))


def draw():
    screen.fill('white')
    screen.draw.text(title,(10,10),frontsize=30, color='black')
    p.draw()

def p_move():
    '''function to move player'''
    def handle_boundary():
    if p.x > WIDTH:
        p.x = 0
    if p.x < 0:
        p.x=WIDTH
    if p.y > HEIGHT:
        p.y = 0
    if p.y < 0:
        p.y = HEIGHT                        

def update():
    p_move()  #function call

pgzrun.go()    