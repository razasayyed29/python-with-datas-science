import pgzrun

WIDTH = 1000
HEIGHT = 600
scr = 0

def gamescr(title,bgcolor='gray', info="play the game"):
     screen.fill(bgcolor)
     screen.draw.text(title,center=(WIDTH/2, HEIGHT/2),fontsize=100,color='white',align='center')
     screen.draw.text(info,center=(WIDTH/2, HEIGHT/2+100),fontsize=50,color='white',align='center')
        
def draw():
    if scr ==0:
        gamescr('Amazing game','black','press space to start the game')
    elif scr == 1:
        gamescr(bgcolor='red',title='game is running',)
    elif scr == 2 :
        gamescr('game over',info='go home')

      


        

def update():
    global scr
    if keyboard.space and scr == 0:
        scr=1
    if keyboard.escape and scr == 1:
        scr=2
    if keyboard.space and scr ==2:
        scr=0
    print(scr)         

pgzrun.go()    