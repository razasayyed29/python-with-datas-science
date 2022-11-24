import pgzrun

HEIGHT = 600
WIDTH = 1200

p = Actor('ironman (2)',center=(WIDTH//2, HEIGHT//2))

def draw():
    screen.fill('white')
    p.draw()

def p_move():
    '''function to move player'''
    if keyboard.left:
        p.x -= 3
        p.angle = 10
    elif keyboard.right:
        p.x += 3
    if keyboard.up:
        p.y -=3
    if keyboard.down:
        p.y +=3
def update():
      p_move()  #function call

pgzrun.go()    