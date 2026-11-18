import pgzrun,random,pyautogui

print(pyautogui.size())
WIDTH,HEIGHT=pyautogui.size()

score=0
speed=2
lives=3
gamestate='start'
instructions=['this game is space invader rip off','press space to start','use A and D or left and right keys to move your rocket and doge the enemies']
player=Actor('rocket (player)')
player.pos=WIDTH/2,HEIGHT-200
heart=Actor('star1.png')
enemies=[]
bullets=[]
def draw():
    screen.blit('bg.jpg',(0,0))
    player.draw()
    for i in enemies:
        i.draw()
    for i in bullets:
        i.draw()
    if gamestate == 'start':
        yp=100
        for i in instructions:
            l=len(i)*10
            screen.draw.text(i,center=(WIDTH//2-l//2,yp))
            yp=yp+50
    for i in range(lives):
        heart.draw()
        heart.pos=50+(i*50),50

def update():
    global gamestate,score,lives 
    if gamestate != 'play' and keyboard.space:
        gamestate='play'
    elif gamestate == 'play':
        if keyboard.left or keyboard.a and player.x >50:
            player.x-=10

        if keyboard.right or keyboard.d and player.x < WIDTH-50:                                                                                                                  
            player.x+=10
        for i in enemies:
            i.y += 10
            if player.colliderect(i):
                if lives>0:
                    lives=lives-1
                    enemies.remove(i)
                else:
                    gamestate='end'
            if i.y > HEIGHT:
                enemies.remove(i)
                continue
            for b in bullets:
                if b.colliderect(i):
                    enemies.remove(i)
                    bullets.remove(b)
                    break


        for i in bullets:
            i.y-=10
            if i.y < 0:
                bullets.remove(i)
    

def create_enemies():
    if gamestate == 'play':
        enemy=Actor('player.png')
        enemy.pos=random.randint(50,WIDTH-50),-50
        enemies.append(enemy)


def on_key_down(key):
    if key == keys.SPACE and len(bullets) < 6 and gamestate == 'play':
        bullet=Actor("playerbullet.png")
        bullet.pos = player.x,player.y-100
        bullets.append(bullet)
    



clock.schedule_interval(create_enemies,1)
pgzrun.go()