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
camera = uvage.Camera(800, 600)

start = False #when it's True is when gameplay is displayed
counter = 0 #to keep track of time for automated things
bulletSpeed = 40

'''player'''
player = uvage.from_color(25, 250, "purple", 50, 50) 
playerSpeed = 9

'''health'''
healthBar = uvage.from_color(100, 550, "white", 500, 30)
wordHealth = uvage.from_text(170, 550, "total health", 50, "pink")
healthDecrease = 700 #variable to allow the health bar to decrease
healthRegen = 35
totalHealth = uvage.from_color(0, 550, "red", healthDecrease, 30)

'''weapon'''
bullet1 = uvage.from_color(player.x,player.y, "red", 10, 10)
bullet2 = uvage.from_color(player.x,player.y, "red", 10, 10)
shoot1 = False
shoot2 = False

'''level 1'''
enemy1Damage = 150 #variable to allow the enemy to shrink as it's dealt damage
enemy1 = uvage.from_color(700,250, "blue", enemy1Damage, enemy1Damage)
enemy1Bullet = uvage.from_color(enemy1.x,enemy1.y, "green", 10, 10)
#make a list and forloop for the bullets
enemy1Speed = 10
enemy1Deaths = 0

'''level 2'''
level2 = False
enemy2Damage = 100 #variable to allow the enemy to shrink as it's dealt damage
enemy2 = uvage.from_color(550,250, "blue", enemy2Damage, enemy2Damage)
enemy2Speed = 15
enemy2Deaths = 0
#ADD BULLETS

'''level 3'''
level3 = False
enemy3Damage = 50 #variable to allow the enemy to shrink as it's dealt damage
enemy3 = uvage.from_color(450,250, "blue", enemy3Damage, enemy3Damage)
enemy3Speed = 20
enemy3Deaths = 0

enemies = [enemy1] 
#damage done by a weapon is applicable to all enemies as levels progress

def tick():
    global start
    global counter
    global bulletSpeed
    
    global player
    global playerSpeed
    
    global totalHealth 
    global healthRegen
    global healthDecrease
    
    global bullet1
    global bullet2
    global shoot1 
    global shoot2

    global enemy1Damage
    global enemy1
    global enemy1Bullet
    global enemy1Speed
    global enemy1Deaths

    global enemy2Damage 
    global enemy2
    global enemy2Speed
    global enemy2Deaths
    
    global enemy3Damage
    global enemy3
    global enemy3Speed
    global enemy3Deaths
    
    global enemies
    global level2
    global level3
    
    camera.clear("black")
    counter+=1
    
    if uvage.is_pressing("return"):
        start = True  
    
    elif start == False:
        title = uvage.from_text(400, 300, "cs 1111 game", 100, "purple")
        hitEnter = uvage.from_text(400, 400, "hit enter to play", 50, "orange")
        camera.draw(title)
        camera.draw(hitEnter)
    
    if start == True:       
        '''player mobility'''
        if uvage.is_pressing("right arrow"): 
            player.x += playerSpeed
            if 800 < player.x: 
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
            if 600 < player.y: 
                player.y -= playerSpeed
        
        '''enemies' mobility'''
        enemy1.y += enemy1Speed 
        if 0 > enemy1.y or enemy1.y > 600:
            enemy1Speed = -1*enemy1Speed
                
        if level2 == True or level3 == True:  
            enemy2.y += enemy2Speed 
            if 0 > enemy2.y or enemy2.y > 600:
                enemy2Speed = -1*enemy2Speed 
            camera.draw(enemy2)
        
        if level3 == True:
            enemy3.y += enemy3Speed 
            if 0 > enemy3.y or enemy3.y > 600:
                enemy3Speed = -1*enemy3Speed 
            camera.draw(enemy3) 
        
        enemy1Bullet.x -= bulletSpeed
        #4 bulletsviisble on screen
        
        if enemy1Bullet.touches(player): #enemy bullet dealing damage on player
            enemy1Bullet = uvage.from_color(enemy1.x,enemy1.y, "green", 10, 10)
            totalHealth.size = [healthDecrease - 70, 30]
            healthDecrease = healthDecrease - 70
            
        elif healthDecrease <= 0: #player dies and game ends
            enemy1Bullet.x = 0
            enemy1.y = 0 
            gameOver = uvage.from_text(400, 300, "game over", 100, "red")
            hitEnter = uvage.from_text(400, 400, "hit enter to start over", 50, "orange")        
            camera.draw(player)
            camera.draw(enemy1)
            camera.draw(healthBar)
            camera.draw(totalHealth)
            camera.draw(wordHealth)
            camera.draw(gameOver)    
            camera.draw(hitEnter) 
            if uvage.is_pressing("return"): #restarting the game
                healthDecrease = 700
                enemy1Damage = 100
                counter = 0
                player = uvage.from_color(25, 250, "purple", 50, 50) 
                totalHealth = uvage.from_color(0, 550, "red", healthDecrease, 30)
                enemy1 = uvage.from_color(700, 250, "blue", enemy1Damage, enemy1Damage)
        
        elif enemy1Bullet.touches(bullet1) or enemy1Bullet.touches(bullet2): #player bullet can deflect enemy bullet
            enemy1Bullet = uvage.from_color(enemy1.x,enemy1.y, "green", 10, 10)
        elif counter%45 == 0:
            enemy1Bullet = uvage.from_color(enemy1.x,enemy1.y, "green", 10, 10)
    
        '''weapon 1'''
 
        if uvage.is_pressing("w"): #how player can shoot
            shoot1 = True
        if shoot1 == True:
            player.color = "red" #WHY DOESNT THIS ONE WORK
            bullet1.x += bulletSpeed
            for enemy in enemies:
                if bullet1.touches(enemy):
                    shoot1 = False
            if bullet1.x > 800:
                shoot1 = False          
        else:
            bullet1 = uvage.from_color(player.x,player.y, "red", 10, 10)
        
        if bullet1.x > player.x+300 and uvage.is_pressing("w"):
                shoot2 = True
        if shoot2 == True:
            player.color = "red"
            bullet2.x += bulletSpeed
            for enemy in enemies:
                if bullet2.touches(enemy):
                    shoot2 = False
            if bullet2.x > 800:
                shoot2 = False     
        else:
            bullet2 = uvage.from_color(player.x,player.y, "red", 10, 10) 
            player.color = "purple"

        '''if bullet hits enemy1'''
        if bullet1.touches(enemy1) or bullet2.touches(enemy1): #how player can defeat enemies and gain back health
            enemy1.size = [enemy1Damage - 10, enemy1Damage - 10]
            enemy1Damage = enemy1Damage - 10
            if healthDecrease < 700:
                totalHealth.size = [healthDecrease + healthRegen, 30]
                healthDecrease = healthDecrease + healthRegen
            else:
                pass
            if enemy1Damage <= 50:
                dead = uvage.from_text(enemy1.x, enemy1.y, "dead", 50,"red")
                enemy1Damage = 150
                '''keeps track of beating level 1'''
                enemy1Deaths +=1
                camera.draw(dead)
                if enemy1.y < 600:
                    enemy1 = uvage.from_color(700,enemy1.y+150, "blue", enemy1Damage, enemy1Damage)
                elif enemy1.y > 600:
                    enemy1 = uvage.from_color(700,enemy1.y-150, "blue", enemy1Damage, enemy1Damage)
    
        '''if bullet hits enemy2'''
        if level2 == True or level3 == True:
            if bullet1.touches(enemy2) or bullet2.touches(enemy2): #how player can defeat enemies and gain back health
                enemy2.size = [enemy2Damage - 5, enemy2Damage - 5]
                enemy2Damage = enemy2Damage - 5
                if healthDecrease < 700:
                    totalHealth.size = [healthDecrease + healthRegen, 30]
                    healthDecrease = healthDecrease + healthRegen
                else:
                    pass
                if enemy2Damage <= 30:
                    dead = uvage.from_text(enemy2.x, enemy2.y, "dead", 50,"red")
                    enemy2Damage = 100
                    enemy2Deaths +=1
                    camera.draw(dead)
                    if enemy2.y < 600:
                        enemy2 = uvage.from_color(550,enemy2.y+150, "blue", enemy2Damage, enemy2Damage)
                    elif enemy2.y > 600:
                        enemy2 = uvage.from_color(550,enemy2.y-150, "blue", enemy2Damage, enemy2Damage)
        
        '''if bullet hits enemy3'''
        if level3 == True:
            if bullet1.touches(enemy3) or bullet2.touches(enemy3): #how player can defeat enemies and gain back health
                enemy3.size = [enemy3Damage - 5, enemy3Damage - 5]
                enemy3Damage = enemy3Damage - 5
                if healthDecrease < 700:
                    totalHealth.size = [healthDecrease + healthRegen, 30]
                    healthDecrease = healthDecrease + healthRegen
                else:
                    pass
                if enemy3Damage <= 20:
                    dead = uvage.from_text(enemy3.x, enemy3.y, "dead", 50,"red")
                    enemy3Damage = 50
                    enemy3Deaths +=1
                    camera.draw(dead)
                    if enemy3.y < 600:
                        enemy3 = uvage.from_color(450,enemy3.y+150, "blue", enemy3Damage, enemy3Damage)
                    elif enemy3.y > 600:
                        enemy3 = uvage.from_color(45,enemy3.y-150, "blue", enemy3Damage, enemy3Damage)
        
        camera.draw(bullet1)
        camera.draw(bullet2)                        
        camera.draw(player)
        camera.draw(enemy1Bullet)
        camera.draw(enemy1)

        '''beat level 1 by killing 4 of enemy 1'''
        if level2 == False and level3 == False:
            if enemy1Deaths >= 4: 
                enemy1Bullet.x = -10
                beatlevel1 = uvage.from_text(400, 300, "level 1 complete", 100, "green")
                hitEnter = uvage.from_text(400, 400, "hit enter to play level 2", 50, "orange")        
                camera.draw(beatlevel1)    
                camera.draw(hitEnter)
                
                if uvage.is_pressing("return"): #going to level 2
                    enemy1Deaths = 0
                    level2 = True
                    enemies.append(enemy2)
                    healthRegen = 17.5
                    healthDecrease = 700
                    enemy1Damage = 150
                    player = uvage.from_color(25, 250, "purple", 50, 50)
                    enemy1 = uvage.from_color(700,250, "blue", enemy1Damage, enemy1Damage)
                    totalHealth = uvage.from_color(0, 550, "red", healthDecrease, 30)
                    camera.draw(enemy2)
                    #add second enemy and also make another bool evaluator to like "turn on" a second weapon 
                    #in second weapon ahve instructions appear that go away after u press the button
            
        '''beat level 2 by killing 2 of each enemy'''
        if level2 == True:
            if enemy1Deaths >= 2 and enemy2Deaths >= 2:
                enemy1Bullet.x = -10
                #do the same thing to enemy 2 bullets
                beatlevel2 = uvage.from_text(400, 300, "level 2 complete", 100, "green")
                hitEnter = uvage.from_text(400, 400, "hit enter to play level 3", 50, "orange")        
                camera.draw(beatlevel2)    
                camera.draw(hitEnter)
                
                if uvage.is_pressing("return"): #going to level 3
                    enemy1Deaths = 0
                    enemy2Deaths = 0
                    level2 = False
                    level3 = True
                    enemies.append(enemy3)
                    healthRegen = 0
                    healthDecrease = 700
                    enemy1Damage = 150
                    enemy2Damage = 100
                    player = uvage.from_color(25, 250, "purple", 50, 50)
                    enemy1 = uvage.from_color(700,250, "blue", enemy1Damage, enemy1Damage)
                    enemy2 = uvage.from_color(550,250, "blue", enemy2Damage, enemy2Damage)
                    totalHealth = uvage.from_color(0, 550, "red", healthDecrease, 30)
                    camera.draw(enemy3)
        
        '''beat level 3 by surviving and killing 2 of each enemy'''
        if level3 == True:
            if enemy3Deaths >= 2:
                if enemy1Deaths >= 2 and enemy2Deaths >= 2:
                    enemy1Bullet.x = -10
                    #do the same thing to enemy 2 and 3 bullets 
                    #stop y axis thingy too btw
                    beatlevel3 = uvage.from_text(400, 300, "you win!", 100, "green")
                    hitEnter = uvage.from_text(400, 400, "hit enter to start over", 50, "orange")        
                    camera.draw(beatlevel3)    
                    camera.draw(hitEnter)
                    
                    if uvage.is_pressing("return"): #returns to the beginning of the game
                        enemy1Deaths = 0
                        enemy2Deaths = 0
                        enemy3Deaths = 0
                        level2 = False
                        level3 = False
                        enemies.clear()
                        enemies = [enemy1]
                        healthRegen = 35
                        healthDecrease = 700
                        enemy1Damage = 150
                        enemy2Damage = 100
                        enemy3Damage = 50
                        player = uvage.from_color(25, 250, "purple", 50, 50)
                        enemy1 = uvage.from_color(700,250, "blue", enemy1Damage, enemy1Damage)
                        totalHealth = uvage.from_color(0, 550, "red", healthDecrease, 30)
                        #DOUBLE CHECK THIS CODE

            
                

            
        camera.draw(healthBar)
        camera.draw(totalHealth)
        camera.draw(wordHealth)
        
    
    camera.display()
 
uvage.timer_loop(30, tick)



