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
import random
camera = uvage.Camera(800, 600)

'''things left to code: 
y axis enemy
and LOTS AND LOTS OF BULLETS!!!
game overing on different levels
also add instructions
also fix the changing to red color
also make it so that if the player runs into enemy player gets hurt
also prly adjust speed of movement but idk'''

start = False #when it's True is when gameplay is displayed
counter = 0 #to keep track of time for automated things
bulletSpeed = 40 #you're gonna need to make variations on this btw

'''player'''
player = uvage.from_color(25, 250, "purple", 50, 50) 
playerSpeed = 20
canMove = True

'''health'''
healthBar = uvage.from_color(100, 550, "white", 500, 30)
wordHealth = uvage.from_text(170, 550, "total health", 50, "pink")
healthDecrease = 700 #variable to allow the health bar to decrease
healthRegen = 35
totalHealth = uvage.from_color(0, 550, "red", healthDecrease, 30)

'''weapon 1'''
bullet1 = uvage.from_color(player.x,player.y, "red", 10, 10)
bullet2 = uvage.from_color(player.x,player.y, "red", 10, 10)
shoot1 = False
shoot2 = False

'''weapon 2'''
stillBullet = uvage.from_color(player.x,player.y, "yellow", 10, 10)
stillBulletspeed = 30

'''level 1'''
enemy1Damage = 150 #variable to allow the enemy to shrink as it's dealt damage
enemy1 = uvage.from_color(700,250, "blue", enemy1Damage, enemy1Damage)
enemy1Bullet = uvage.from_color(enemy1.x,enemy1.y, "green", 10, 10)
E1Bullet2 = uvage.from_color(enemy1.x,enemy1.y, "green", 10, 10)
E1Bullet3 = uvage.from_color(enemy1.x,enemy1.y, "green", 10, 10)
E1Bullet4 = uvage.from_color(enemy1.x,enemy1.y, "green", 10, 10)
enemy1Bullets = [enemy1Bullet, E1Bullet2, E1Bullet3, E1Bullet4]
enemy1Speed = 10
enemy1Deaths = 0

'''level 2'''
level2 = False
enemy2Damage = 100 #variable to allow the enemy to shrink as it's dealt damage
enemy2 = uvage.from_color(550,900, "blue", enemy2Damage, enemy2Damage)
enemy2Speed = 15
enemy2Deaths = 0
#ADD BULLETS

'''level 3'''
level3 = False
enemy3Damage = 50 #variable to allow the enemy to shrink as it's dealt damage
enemy3 = uvage.from_color(450,900, "blue", enemy3Damage, enemy3Damage)
enemy3Speed = 20
enemy3Deaths = 0

'''weapon 3'''
laserOn = False
laserWidth = 1
laser = uvage.from_color(player.x + laserWidth/2 ,player.y, "pink", laserWidth, 10)
laserTimer = -1
Tracker = False
enemies = [enemy1, enemy2, enemy3]
randomEnemy = random.choice(enemies)
laserBar = uvage.from_color(60, 500, "white", 120, 30)
wordLaser = uvage.from_text(60, 500, "laser recharge", 23, "red")
laserDecrease = 200
laserRegen = uvage.from_color(60, 500, "pink", laserDecrease, 30)         

def tick():
    global start
    global counter
    global bulletSpeed
    
    global player
    global playerSpeed
    global canMove
    
    global totalHealth 
    global healthRegen
    global healthDecrease
    
    global bullet1
    global bullet2
    global shoot1 
    global shoot2
    
    global stillBullet
    global stillBulletspeed

    global laser
    global laserTimer
    global Tracker
    global laserOn
    global laserWidth
    global enemies
    global randomEnemy
    global laserBar
    global wordLaser
    global laserDecrease
    global laserRegen
    
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
    
    global level2
    global level3
    
    camera.clear("black")
    counter+=1
    
    if uvage.is_pressing("return"): #leaving title screen
        start = True  
    
    elif start == False:
        title = uvage.from_text(400, 300, "cs 1111 game", 100, "purple")
        hitEnter = uvage.from_text(400, 400, "hit enter to play", 50, "orange")
        camera.draw(title)
        camera.draw(hitEnter)
    
    if start == True:       
        '''player mobility'''
        if canMove == True:
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
        
        enemy1.y += enemy1Speed #enemy 1 is ther from the start
        if 0 > enemy1.y or enemy1.y > 600:
            enemy1Speed = -1*enemy1Speed
                
        if level2 == True or level3 == True: #2nd enemy appears in level 2 
            enemy2.y += enemy2Speed 
            if 0 > enemy2.y or enemy2.y > 600:
                enemy2Speed = -1*enemy2Speed 
            camera.draw(enemy2)
        
        if level3 == True: #third enemy appears in level 3
            enemy3.y += enemy3Speed 
            if 0 > enemy3.y or enemy3.y > 600:
                enemy3Speed = -1*enemy3Speed 
            camera.draw(enemy3) 
        
        '''CURRENT WORK IN PROGRESS HERE'''
        
        # for bullet in enemy1Bullets:
        #     bullet.x -= bulletSpeed
        #     if bullet.touches(player): #enemy bullet dealing damage on player
        #         bullet = uvage.from_color(enemy1.x,enemy1.y, "green", 10, 10)
        #         totalHealth.size = [healthDecrease - 70, 30]
        #         healthDecrease = healthDecrease - 70
        #     #4 bulletsviisble on screen
        # #     elif enemy1Bullet.touches(bullet1) or enemy1Bullet.touches(bullet2): #player bullet can deflect enemy bullet
        # # #     enemy1Bullet = uvage.from_color(enemy1.x,enemy1.y, "green", 10, 10)
        #     elif counter%45 == 0:
        #         bullet = uvage.from_color(enemy1.x,enemy1.y, "green", 10, 10)
        
        #THIS NEEDS TO BE FIXED TOO BTW
        #ORIGINAL CODE DO NOT TOUCH!!!!!
        enemy1Bullet.x -= bulletSpeed
        
        '''enemy bullet dealing damage'''

        if enemy1Bullet.touches(player): #enemy bullet dealing damage on player
            enemy1Bullet = uvage.from_color(enemy1.x,enemy1.y, "green", 10, 10)
            totalHealth.size = [healthDecrease - 70, 30]
            healthDecrease = healthDecrease - 70
            
        elif healthDecrease <= 0: #if player dies in level 1
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
    
    
    
        '''weapon 1''' #WHY DOESNT IT TURN RED WITH THE FIRST BULLET PLS
        
        '''first bullet of weapon 1'''
        if uvage.is_pressing("w"): #how player can shoot
            shoot1 = True
        if shoot1 == True:
            bullet1.x += bulletSpeed
            player.color = "red" #WHY DOESNT THIS WORK IM GONNA CRY
            if bullet1.touches(enemy1):
                shoot1 = False
            if level2 == True or level3 == True:
                if bullet1.touches(enemy2):
                    shoot1 = False
            if level3 == True:
                if bullet1.touches(enemy3):
                    shoot1 = False
            if bullet1.x > 800:
                shoot1 = False          
        else:
            bullet1 = uvage.from_color(player.x,player.y, "red", 10, 10)
            player.color = "purple"
            
        '''second bullet of weapon 1'''
        if bullet1.x > player.x+300 and uvage.is_pressing("w"):
            shoot2 = True
        elif shoot2 == True:
            player.color = "red"
            bullet2.x += bulletSpeed
            if bullet2.touches(enemy1):
                shoot2 = False
            if level2 == True or level3 == True:
                if bullet2.touches(enemy2):
                    shoot2 = False
            if level3 == True:
                if bullet2.touches(enemy3):
                    shoot1 = False
            if bullet2.x > 800:
                shoot2 = False     
        else:
            bullet2 = uvage.from_color(player.x,player.y, "red", 10, 10) 
            player.color = "purple"
        
        '''if weapon 1 hits enemy1'''
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
                enemy1Deaths +=1 
                camera.draw(dead)
                if enemy1.y < 600:
                    enemy1 = uvage.from_color(700,enemy1.y+150, "blue", enemy1Damage, enemy1Damage)
                elif enemy1.y > 600:
                    enemy1 = uvage.from_color(700,enemy1.y-150, "blue", enemy1Damage, enemy1Damage)
    
        '''if weapon 1 hits enemy2'''
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
        
        '''if weapon 1 hits enemy3'''
        if level3 == True:
            if bullet1.touches(enemy3) or bullet2.touches(enemy3): #how player can defeat enemies and gain back health
                enemy3.size = [enemy3Damage - 2.5, enemy3Damage - 2.5]
                enemy3Damage = enemy3Damage - 2.5
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
                        enemy3 = uvage.from_color(450,enemy3.y-150, "blue", enemy3Damage, enemy3Damage)
    
    
    
        ''' weapon 2'''
        if level2 == True or level3 == True:
            if uvage.is_pressing("a"):    
                player.color = "yellow" 
                stillBullet.x += stillBulletspeed
                canMove = False #can't move when using weapon 2
            else:
                stillBullet = uvage.from_color(player.x,player.y, "yellow", 10, 10)
                canMove = True
        else:
            stillBullet = uvage.from_color(player.x,player.y, "yellow", 10, 10)
        
        '''if weapon 2 hits enemy1'''
        if stillBullet.touches(enemy1):
            stillBullet = uvage.from_color(player.x,player.y, "yellow", 10, 10)
            enemy1.size = [enemy1Damage/2, enemy1Damage/2]
            enemy1Damage = enemy1Damage/2
            if healthDecrease < 700:
                totalHealth.size = [healthDecrease + healthRegen, 30]
                healthDecrease = healthDecrease + healthRegen
            else:
                pass
            if enemy1Damage <= 50:
                dead = uvage.from_text(enemy1.x, enemy1.y, "dead", 50,"red")
                enemy1Damage = 150
                enemy1Deaths +=1
                camera.draw(dead)
                if enemy1.y < 600:
                    enemy1 = uvage.from_color(700,enemy1.y+150, "blue", enemy1Damage, enemy1Damage)
                elif enemy1.y > 600:
                    enemy1 = uvage.from_color(700,enemy1.y-150, "blue", enemy1Damage, enemy1Damage)
                
        '''if weapon 2 hits enemy2'''
        if level2 == True or level3 == True:
            if stillBullet.touches(enemy2):
                stillBullet = uvage.from_color(player.x,player.y, "yellow", 10, 10)
                enemy2.size = [enemy2Damage/2, enemy2Damage/2]
                enemy2Damage = enemy2Damage/2
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
                    
        '''if weapon 2 hits enemy3'''   
        if level3 == True:
            if stillBullet.touches(enemy3):
                stillBullet = uvage.from_color(player.x,player.y, "yellow", 10, 10)
                enemy3.size = [enemy3Damage/2, enemy3Damage/2]
                enemy3Damage = enemy3Damage/2
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
                        enemy3 = uvage.from_color(450,enemy3.y-150, "blue", enemy3Damage, enemy3Damage)
        
        
        
        '''weapon 3'''    
        if level3 == True:
                       
            if Tracker == True: #tracks laser recharge
                laserTimer +=1
                if laserTimer <= 120:
                    laserDecrease += 1
                laserRegen = uvage.from_color(60, 500, "pink", laserDecrease, 30)         
                camera.draw(laserBar)
                camera.draw(laserRegen)
                camera.draw(wordLaser)
                
            if Tracker == True and laserTimer >= 120: #makes laser function
                if uvage.is_pressing("d"):
                    randomEnemy = random.choice(enemies)
                    laserOn = True
                    laserWidth = randomEnemy.x-player.x
                    laserTimer = 0
                    laserDecrease = 0
                    laserRegen = uvage.from_color(60, 500, "pink", laserDecrease, 30)         
            
            elif uvage.is_pressing("d") and laserTimer < 0: #for 1st use of laser
                randomEnemy = random.choice(enemies)
                laserOn = True
                laserWidth = randomEnemy.x-player.x
                Tracker = True
                laserTimer = 0
                laserDecrease = 0
                laserRegen = uvage.from_color(60, 500, "pink", laserDecrease, 30)         
                      
            if laserOn == True:
                laser = uvage.from_color(player.x + laserWidth/2 ,player.y, "pink", laserWidth, 10)
                camera.draw(laser)                    
                if counter%1 == 0:
                    laserOn = False

                '''if weapon 3 hits enemy1'''
                if laser.touches(enemy1):
                    enemy1.size = [enemy1Damage - 5, enemy1Damage - 5]
                    enemy1Damage = enemy1Damage - 5
                    if healthDecrease < 700:
                        totalHealth.size = [healthDecrease + healthRegen, 30]
                        healthDecrease = healthDecrease + healthRegen
                    else:
                        pass
                    if enemy1Damage <= 50:
                        dead = uvage.from_text(enemy1.x, enemy1.y, "dead", 50,"red")
                        enemy1Damage = 150
                        enemy1Deaths +=1 #keeps track of beating level 1
                        camera.draw(dead)
                        if enemy1.y < 600:
                            enemy1 = uvage.from_color(700,enemy1.y+150, "blue", enemy1Damage, enemy1Damage)
                        elif enemy1.y > 600:
                            enemy1 = uvage.from_color(700,enemy1.y-150, "blue", enemy1Damage, enemy1Damage)    
                
                '''if weapon 3 hits enemy2'''
                if laser.touches(enemy2):
                    enemy2.size = [enemy2Damage - 2.5, enemy2Damage - 2.5]
                    enemy2Damage = enemy2Damage - 2.5
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

                '''if weapon 3 hits enemy3'''
                if laser.touches(enemy3):
                    enemy3.size = [enemy3Damage - 1.25, enemy3Damage - 1.25]
                    enemy3Damage = enemy3Damage - 1.25
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
                        enemy3 = uvage.from_color(450,enemy3.y-150, "blue", enemy3Damage, enemy3Damage)
        
        camera.draw(bullet1)
        camera.draw(bullet2) 
        camera.draw(stillBullet)                     
        camera.draw(player)
        camera.draw(enemy1Bullet)
        camera.draw(enemy1)
        camera.draw(enemy2)
        camera.draw(enemy3)

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
                    healthRegen = 17.5
                    healthDecrease = 700
                    enemy1Damage = 150
                    player = uvage.from_color(25, 250, "purple", 50, 50)
                    enemy1 = uvage.from_color(700,250, "blue", enemy1Damage, enemy1Damage)
                    enemy2 = uvage.from_color(550,250, "blue", enemy2Damage, enemy2Damage)
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
                    healthRegen = 0
                    healthDecrease = 700
                    enemy1Damage = 150
                    enemy2Damage = 100
                    player = uvage.from_color(25, 250, "purple", 50, 50)
                    enemy1 = uvage.from_color(700,250, "blue", enemy1Damage, enemy1Damage)
                    enemy2 = uvage.from_color(550,250, "blue", enemy2Damage, enemy2Damage)
                    enemy3 = uvage.from_color(450,250, "blue", enemy3Damage, enemy3Damage)
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
                        healthRegen = 35
                        healthDecrease = 700
                        enemy1Damage = 150
                        enemy2Damage = 100
                        enemy3Damage = 50
                        player = uvage.from_color(25, 250, "purple", 50, 50)
                        enemy1 = uvage.from_color(700,250, "blue", enemy1Damage, enemy1Damage)
                        enemy2 = uvage.from_color(550,900, "blue", enemy2Damage, enemy2Damage)
                        enemy3 = uvage.from_color(450,900, "blue", enemy3Damage, enemy3Damage)
                        totalHealth = uvage.from_color(0, 550, "red", healthDecrease, 30)
                                    
        camera.draw(healthBar)
        camera.draw(totalHealth)
        camera.draw(wordHealth)
        
    
    camera.display()
 
uvage.timer_loop(30, tick)
