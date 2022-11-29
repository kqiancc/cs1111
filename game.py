# Katherine Chacon Cai rst3nk
# Victoria Spitzer fky7tb

# Description of game:
# A bird's eye view arena shooter game where the player shoots enemies from a 2D perspective.
# There are 3 levels, and the player gets different weapons. If the enemy hurts the player,
# they lose health. If the player hurts the enemy, they get some health back. If the player
# runs out of health, they die. The aim of the game is to make it through all 3 levels.

# 3 basic features:
# User Input - to control the character and shoot, the player uses the keyboard.
# Game Over - if the player runs out of health, they die and have to start over again.
# Graphics/Images - images for the different levels and the character and enemies.

# 4 additional features:
# Sprite Animation - the enemies and character are animated and can move around.
# Enemies - if the enemies hit the player, the player loses health and can die from this
# Health Bar - health bars for the player and some enemies, player will lose when health bar is at 0
# Multiple levels - there are 3 levels for the player to get through

#rst3nk - Katherine Chacon Cai

#rst3nk - Katherine Chacon Cai

import uvage
camera = uvage.Camera(1000, 1000)

player = uvage.from_color(25, 250, "purple", 50, 50) 
bullet = uvage.from_color(player.x,player.y, "red", 10, 10)
healthBar = uvage.from_color(100, 950, "white", 500, 30)
wordHealth = uvage.from_text(170, 950, "total health", 50, "pink")
m = 700
totalHealth = uvage.from_color(0, 950, "red", m, 30)
n = 100
enemy = uvage.from_color(900,250, "blue", n, n)
enemyBullet = uvage.from_color(enemy.x,enemy.y, "green", 10, 10)
playerSpeed = 9
bulletSpeed = 20
enemySpeed = 10
counter = 0
level1deaths = 0

def tick():
    global playerSpeed
    global bulletSpeed
    global bullet
    global n
    global enemySpeed
    global enemyBullet
    global counter
    global totalHealth
    global m 
    global gameOver
    global enemy
    global player
    global level1deaths
    
    camera.clear("black")
    counter+=1
        
    '''player mobility'''
    if uvage.is_pressing("right arrow"): 
        player.x += playerSpeed
        if 1000 < player.x: 
            player.x -= playerSpeed
    elif uvage.is_pressing("left arrow"): 
        player.x -= playerSpeed 
        if 0 > player.x:
            player.x += playerSpeed
    elif uvage.is_pressing("up arrow"): 
        player.y -= playerSpeed
        if 0 > player.y: 
            player.y += playerSpeed
    elif uvage.is_pressing("down arrow"): 
        player.y += playerSpeed
        if 1000 < player.y: 
            player.y -= playerSpeed
    
    '''enemy mobility and bullet'''
    enemy.y += enemySpeed 
    if 0 > enemy.y or enemy.y > 1000:
        enemySpeed = -1*enemySpeed  
    
    enemyBullet.x -= bulletSpeed
    
    if enemyBullet.touches(player): #enemy bullet dealing damage on player
        enemyBullet = uvage.from_color(enemy.x,enemy.y, "green", 10, 10)
        totalHealth.size = [m-70, 30]
        m = m-70
        
    elif m <= 0: #player dies and game ends
        enemyBullet.x = 0
        enemy.y = 0 
        gameOver = uvage.from_text(500, 500, "game over", 100, "red")
        hitEnter = uvage.from_text(500, 600, "hit enter to start over", 50, "orange")        
        camera.draw(player)
        camera.draw(enemy)
        camera.draw(healthBar)
        camera.draw(totalHealth)
        camera.draw(wordHealth)
        camera.draw(gameOver)    
        camera.draw(hitEnter) 
        if uvage.is_pressing("return"): #restarting the game
            m = 700
            n = 100
            counter = 0
            player = uvage.from_color(25, 250, "purple", 50, 50) 
            totalHealth = uvage.from_color(0, 950, "red", m, 30)
            enemy = uvage.from_color(900,250, "blue", n, n)
    
    elif enemyBullet.touches(bullet): #player bullet can deflect enemy bullet
        enemyBullet = uvage.from_color(enemy.x,enemy.y, "green", 10, 10)
    elif counter%60 == 0:
        enemyBullet = uvage.from_color(enemy.x,enemy.y, "green", 10, 10)
        
    if uvage.is_pressing("space"): #how player can shoot
        bullet.x += bulletSpeed
    else: 
        bullet = uvage.from_color(player.x,player.y, "red", 10, 10)
    
    if bullet.touches(enemy): #how player can defeat enemies and gain back health
        enemy.size = [n-10,n-10]
        n = n-10
        if m < 700:
            totalHealth.size = [m+35, 30]
            m = m+35
        else:
            pass
        if n <= 30:
            dead = uvage.from_text(enemy.x, enemy.y, "dead", 50,"red")
            n = 100
            level1deaths +=1
            camera.draw(dead)
            if level1deaths < 4: 
                 if enemy.y <800:
                    enemy = uvage.from_color(900,enemy.y+200, "blue", n, n)
                 elif enemy.y >800:
                    enemy = uvage.from_color(900,enemy.y-200, "blue", n, n)
            else:
                pass
    
    if level1deaths >= 4: 
        '''beat level 1 by killing a certain number of enemies 
        (idk i picked a random number for now)'''
        enemyBullet.x = 0
        enemy.y = 0 
        beatlevel1 = uvage.from_text(500, 500, "level 1 complete", 100, "green")
        hitEnter = uvage.from_text(500, 600, "hit enter to play level 2", 50, "orange")        
        camera.draw(player)
        camera.draw(enemy)
        camera.draw(healthBar)
        camera.draw(totalHealth)
        camera.draw(wordHealth)
        camera.draw(beatlevel1)    
        camera.draw(hitEnter)
         
        if uvage.is_pressing("return"): #going to level 2
            level1deaths = 0
            player = uvage.from_color(25, 250, "purple", 50, 50)
            #idk what level 2's set up is yet   
                 
    camera.draw(bullet)                        
    camera.draw(player)
    camera.draw(enemyBullet)
    camera.draw(enemy)
    camera.draw(healthBar)
    camera.draw(totalHealth)
    camera.draw(wordHealth)
    camera.display()
 
uvage.timer_loop(30, tick)

