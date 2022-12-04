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

# rst3nk - Katherine Chacon Cai

# rst3nk - Katherine Chacon Cai

import uvage
import random

camera = uvage.Camera(800, 600)

'''things left to code: 
add images
also fix the changing to red color'''
'''turn  this on!!! player runs into enemy player gets hurt
also fix up comments'''

start = False  # when it's True is when gameplay is displayed
counter = 0  # to keep track of time for automated things
gameplay = True

'''player'''
player = uvage.from_image(25, 250, "player.png")
playerSpeed = 20
canMove = True
totalenemyDeaths = 0
bulletSpeed = 40

'''health'''
healthBar = uvage.from_color(100, 550, "white", 500, 30)
wordHealth = uvage.from_text(170, 550, "total health", 50, "pink")
healthDecrease = 700  # variable to allow the health bar to decrease
healthRegen = 70
totalHealth = uvage.from_color(0, 550, "red", healthDecrease, 30)

'''weapon 1'''
bullet1 = uvage.from_color(player.x, player.y, "red", 10, 10)
bullet2 = uvage.from_color(player.x, player.y, "red", 10, 10)
shoot1 = False
shoot2 = False

'''weapon 2'''
stillBullet = uvage.from_color(player.x, player.y, "yellow", 10, 10)
stillBulletspeed = 30

'''level 1'''
enemy1Damage = 150  # variable to allow the enemy to shrink as it's dealt damage
enemy1 = uvage.from_image(700, 250, "enemy1.png")
e1bulletSpeed = 30
e1Bullet1 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)
e1Bullet2 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)
e1Bullet3 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)
e1Bullet4 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)
e1Bullet1moves = False
e1Bullet2moves = False
e1Bullet3moves = False
e1Bullet4moves = False
enemy1Speed = 10
enemy1Deaths = 0

'''level 2'''
level2 = False
enemy2Damage = 100  # variable to allow the enemy to shrink as it's dealt damage
enemy2 = uvage.from_image(550, 900, "enemy2.png")
enemy2Speed = 15
enemy2Deaths = 0
e2bulletSpeed = 40
e2Bullet1 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)
e2Bullet2 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)
e2Bullet3 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)
e2Bullet4 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)
e2Bullet1moves = False
e2Bullet2moves = False
e2Bullet3moves = False
e2Bullet4moves = False

'''level 3'''
level3 = False
enemy3Damage = 50  # variable to allow the enemy to shrink as it's dealt damage
enemy3 = uvage.from_image(450, 900, "enemy3.png")
enemy3Speed = 20
enemy3Deaths = 0
e3bulletSpeed = 50
e3Bullet1 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)
e3Bullet2 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)
e3Bullet3 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)
e3Bullet4 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)
e3Bullet1moves = False
e3Bullet2moves = False
e3Bullet3moves = False
e3Bullet4moves = False

'''weapon 3'''
laserOn = False
laserWidth = 1
laser = uvage.from_color(player.x + laserWidth / 2, player.y, "pink", laserWidth, 10)
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
    global gameplay

    global player
    global playerSpeed
    global canMove
    global totalenemyDeaths

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
    global enemy1Speed
    global enemy1Deaths
    global e1Bullet1
    global e1Bullet2
    global e1Bullet3
    global e1Bullet4
    global e1Bullet1moves
    global e1Bullet2moves
    global e1Bullet3moves
    global e1Bullet4moves
    global e1bulletSpeed

    global enemy2Damage
    global enemy2
    global enemy2Speed
    global enemy2Deaths
    global e2Bullet1
    global e2Bullet2
    global e2Bullet3
    global e2Bullet4
    global e2Bullet1moves
    global e2Bullet2moves
    global e2Bullet3moves
    global e2Bullet4moves
    global e2bulletSpeed

    global enemy3Damage
    global enemy3
    global enemy3Speed
    global enemy3Deaths
    global e3bulletSpeed
    global e3Bullet1
    global e3Bullet2
    global e3Bullet3
    global e3Bullet4
    global e3Bullet1moves
    global e3Bullet2moves
    global e3Bullet3moves
    global e3Bullet4moves

    global level2
    global level3

    camera.clear("black")
    counter += 1

    if uvage.is_pressing("return"):  # leaving title screen
        start = True

    elif start == False:
        title = uvage.from_text(400, 300, "cs 1111 game", 100, "purple")
        hitEnter = uvage.from_text(400, 400, "hit enter to play", 50, "orange")
        instructions1 = uvage.from_text(400, 450, "press w for weapon 1 and use arrows to move", 30, "pink")
        instructions2 = uvage.from_text(400, 480, "kill four enemies to move on to level 2", 30, "pink")
        camera.draw(instructions1)
        camera.draw(instructions2)
        camera.draw(title)
        camera.draw(hitEnter)

    if start == True:

        displayDeaths = uvage.from_text(650, 550, "total deaths: " + str(totalenemyDeaths), 50, "pink")

        camera.draw(bullet1)
        camera.draw(bullet2)
        camera.draw(stillBullet)
        camera.draw(player)
        camera.draw(enemy2)
        camera.draw(enemy3)
        camera.draw(healthBar)
        camera.draw(totalHealth)
        camera.draw(wordHealth)

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
        if gameplay == True:
            enemy1.y += enemy1Speed  # enemy 1 is ther from the start
            if 0 > enemy1.y or enemy1.y > 600:
                enemy1Speed = -1 * enemy1Speed

            if level2 == True or level3 == True:  # 2nd enemy appears in level 2
                enemy2.y += enemy2Speed
                if 0 > enemy2.y or enemy2.y > 600:
                    enemy2Speed = -1 * enemy2Speed
                camera.draw(enemy2)

            if level3 == True:  # third enemy appears in level 3
                enemy3.y += enemy3Speed
                if 0 > enemy3.y or enemy3.y > 600:
                    enemy3Speed = -1 * enemy3Speed
                camera.draw(enemy3)

        '''enemy1 bullets and damage'''

        if gameplay == True:

            # enemy 1 bullet 1 movement
            if enemy1.y == 100:
                e1Bullet1moves = True

            if e1Bullet1moves == False:
                e1Bullet1 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)
            elif e1Bullet1moves == True:
                camera.draw(e1Bullet1)
                e1Bullet1.x -= e1bulletSpeed
            if e1Bullet1.x <= 0:
                e1Bullet1 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)

            # enemy 1 bullet 1 dealing damage
            if e1Bullet1.touches(player):
                e1Bullet1 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)
                totalHealth.size = [healthDecrease - 35, 30]
                healthDecrease = healthDecrease - 35

            # player bullet can deflect enemy bullet
            if e1Bullet1.touches(bullet1) or e1Bullet1.touches(bullet2):
                e1Bullet1 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)
            elif e1Bullet1.touches(stillBullet):
                e1Bullet1 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)

            '''enemy 1 bullet 2 movement'''
            if enemy1.y == 200:
                e1Bullet2moves = True

            if e1Bullet2moves == False:
                e1Bullet2 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)
            elif e1Bullet2moves == True:
                camera.draw(e1Bullet2)
                e1Bullet2.x -= e1bulletSpeed
            if e1Bullet2.x <= 0:
                e1Bullet2 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)

            # enemy 1 bullet 2 dealing damage
            if e1Bullet2.touches(player):
                e1Bullet2 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)
                totalHealth.size = [healthDecrease - 35, 30]
                healthDecrease = healthDecrease - 35

            # player bullet can deflect enemy bullet
            if e1Bullet2.touches(bullet1) or e1Bullet2.touches(bullet2):
                e1Bullet2 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)
            elif e1Bullet2.touches(stillBullet):
                e1Bullet2 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)

            '''enemy 1 bullet 3 movement'''
            if enemy1.y == 300:
                e1Bullet3moves = True

            if e1Bullet3moves == False:
                e1Bullet3 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)
            elif e1Bullet3moves == True:
                camera.draw(e1Bullet3)
                e1Bullet3.x -= e1bulletSpeed
            if e1Bullet3.x <= 0:
                e1Bullet3 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)

            # enemy 1 bullet 3 dealing damage
            if e1Bullet3.touches(player):
                e1Bullet3 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)
                totalHealth.size = [healthDecrease - 35, 30]
                healthDecrease = healthDecrease - 35

            # player bullet can deflect enemy bullet
            if e1Bullet3.touches(bullet1) or e1Bullet3.touches(bullet2):
                e1Bullet3 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)
            elif e1Bullet3.touches(stillBullet):
                e1Bullet3 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)

            '''enemy 1 bullet 4 movement'''  # idk i don't think we need four bullets for e1
            if enemy1.y == 400:
                e1Bullet4moves = True

            if e1Bullet4moves == False:
                e1Bullet4 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)
            elif e1Bullet4moves == True:
                camera.draw(e1Bullet4)
                e1Bullet4.x -= e1bulletSpeed
            if e1Bullet4.x <= 0:
                e1Bullet4 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)

            # enemy 1 bullet 2 dealing damage
            if e1Bullet4.touches(player):
                e1Bullet4 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)
                totalHealth.size = [healthDecrease - 35, 30]
                healthDecrease = healthDecrease - 35

            # player bullet can deflect enemy bullet
            if e1Bullet4.touches(bullet1) or e1Bullet4.touches(bullet2):
                e1Bullet4 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)
            elif e1Bullet4.touches(stillBullet):
                e1Bullet4 = uvage.from_color(enemy1.x, enemy1.y, "green", 10, 10)

        camera.draw(enemy1)

        '''enemy2 bullets and damage'''
        if level2 == True or level3 == True:
            if gameplay == True:

                # enemy 2 bullet 1 movement
                if enemy2.y == 100:
                    e2Bullet1moves = True

                if e2Bullet1moves == False:
                    e2Bullet1 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)
                elif e2Bullet1moves == True:
                    camera.draw(e2Bullet1)
                    e2Bullet1.x -= e2bulletSpeed
                if e2Bullet1.x <= 0:
                    e2Bullet1 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)

                # enemy 2 bullet 1 dealing damage
                if e2Bullet1.touches(player):
                    e2Bullet1 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)
                    totalHealth.size = [healthDecrease - 35, 30]
                    healthDecrease = healthDecrease - 35

                # player bullet can deflect enemy bullet
                if e2Bullet1.touches(bullet1) or e2Bullet1.touches(bullet2):
                    e2Bullet1 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)
                elif e2Bullet1.touches(stillBullet):
                    e2Bullet1 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)

                '''enemy 2 bullet 2 movement'''
                if enemy2.y == 200:
                    e2Bullet2moves = True

                if e2Bullet2moves == False:
                    e2Bullet2 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)
                elif e2Bullet2moves == True:
                    camera.draw(e2Bullet2)
                    e2Bullet2.x -= e2bulletSpeed
                if e2Bullet2.x <= 0:
                    e2Bullet2 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)

                # enemy 1 bullet 2 dealing damage
                if e2Bullet2.touches(player):
                    e2Bullet2 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)
                    totalHealth.size = [healthDecrease - 35, 30]
                    healthDecrease = healthDecrease - 35

                # player bullet can deflect enemy bullet
                if e2Bullet2.touches(bullet1) or e2Bullet2.touches(bullet2):
                    e2Bullet2 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)
                elif e2Bullet2.touches(stillBullet):
                    e2Bullet2 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)

                '''enemy 1 bullet 3 movement'''
                if enemy2.y == 300:
                    e2Bullet3moves = True

                if e2Bullet3moves == False:
                    e2Bullet3 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)
                elif e2Bullet3moves == True:
                    camera.draw(e2Bullet3)
                    e2Bullet3.x -= e2bulletSpeed
                if e2Bullet3.x <= 0:
                    e2Bullet3 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)

                # enemy 1 bullet 3 dealing damage
                if e2Bullet3.touches(player):
                    e2Bullet3 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)
                    totalHealth.size = [healthDecrease - 35, 30]
                    healthDecrease = healthDecrease - 35

                # player bullet can deflect enemy bullet
                if e2Bullet3.touches(bullet1) or e2Bullet3.touches(bullet2):
                    e2Bullet3 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)
                elif e2Bullet3.touches(stillBullet):
                    e2Bullet3 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)

                '''enemy 1 bullet 4 movement'''  # idk i don't think we need four bullets for e1
                if enemy2.y == 400:
                    e2Bullet4moves = True

                if e2Bullet4moves == False:
                    e2Bullet4 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)
                elif e2Bullet4moves == True:
                    camera.draw(e2Bullet4)
                    e2Bullet4.x -= e2bulletSpeed
                if e2Bullet4.x <= 0:
                    e2Bullet4 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)

                # enemy 1 bullet 2 dealing damage
                if e2Bullet4.touches(player):
                    e2Bullet4 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)
                    totalHealth.size = [healthDecrease - 35, 30]
                    healthDecrease = healthDecrease - 35

                # player bullet can deflect enemy bullet
                if e2Bullet4.touches(bullet1) or e2Bullet4.touches(bullet2):
                    e2Bullet4 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)
                elif e2Bullet4.touches(stillBullet):
                    e2Bullet4 = uvage.from_color(enemy2.x, enemy2.y, "green", 10, 10)

            camera.draw(enemy2)

        if level3 == True and gameplay == True:

            # enemy 3 bullet 1 movement
            if enemy3.y >= 100:
                e3Bullet1moves = True

            if e3Bullet1moves == False:
                e3Bullet1 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)
            elif e3Bullet1moves == True:
                camera.draw(e3Bullet1)
                e3Bullet1.x -= e3bulletSpeed
            if e3Bullet1.x <= 0:
                e3Bullet1 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)

            # enemy 3 bullet 1 dealing damage
            if e3Bullet1.touches(player):
                e3Bullet1 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)
                totalHealth.size = [healthDecrease - 35, 30]
                healthDecrease = healthDecrease - 35

            # player bullet can deflect enemy bullet
            if e3Bullet1.touches(bullet1) or e3Bullet1.touches(bullet2):
                e3Bullet1 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)
            elif e3Bullet1.touches(stillBullet):
                e3Bullet1 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)

            '''enemy 3 bullet 2 movement'''
            if enemy3.y >= 200:
                e3Bullet2moves = True

            if e3Bullet2moves == False:
                e3Bullet2 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)
            elif e3Bullet2moves == True:
                camera.draw(e3Bullet2)
                e3Bullet2.x -= e3bulletSpeed
            if e3Bullet2.x <= 0:
                e3Bullet2 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)

            # enemy 3 bullet 2 dealing damage
            if e3Bullet2.touches(player):
                e3Bullet2 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)
                totalHealth.size = [healthDecrease - 35, 30]
                healthDecrease = healthDecrease - 35

            # player bullet can deflect enemy bullet
            if e3Bullet2.touches(bullet1) or e3Bullet2.touches(bullet2):
                e3Bullet2 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)
            elif e3Bullet2.touches(stillBullet):
                e3Bullet2 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)

            '''enemy 3 bullet 3 movement'''
            if enemy3.y >= 300:
                e3Bullet3moves = True

            if e3Bullet3moves == False:
                e3Bullet3 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)
            elif e3Bullet3moves == True:
                camera.draw(e3Bullet3)
                e3Bullet3.x -= e3bulletSpeed
            if e3Bullet3.x <= 0:
                e3Bullet3 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)

            # enemy 3 bullet 3 dealing damage
            if e3Bullet3.touches(player):
                e3Bullet3 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)
                totalHealth.size = [healthDecrease - 35, 30]
                healthDecrease = healthDecrease - 35

            # player bullet can deflect enemy bullet
            if e3Bullet3.touches(bullet1) or e3Bullet3.touches(bullet2):
                e3Bullet3 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)
            elif e3Bullet3.touches(stillBullet):
                e3Bullet3 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)

            '''enemy 3 bullet 4 movement'''  # idk i don't think we need four bullets for e1
            if enemy3.y >= 400:
                e3Bullet4moves = True

            if e3Bullet4moves == False:
                e3Bullet4 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)
            elif e3Bullet4moves == True:
                camera.draw(e3Bullet4)
                e3Bullet4.x -= e3bulletSpeed
            if e3Bullet4.x <= 0:
                e3Bullet4 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)

            # enemy 3 bullet 2 dealing damage
            if e3Bullet4.touches(player):
                e3Bullet4 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)
                totalHealth.size = [healthDecrease - 35, 30]
                healthDecrease = healthDecrease - 35

            # player bullet can deflect enemy bullet
            if e3Bullet4.touches(bullet1) or e3Bullet4.touches(bullet2):
                e3Bullet4 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)
            elif e3Bullet4.touches(stillBullet):
                e3Bullet4 = uvage.from_color(enemy3.x, enemy3.y, "green", 10, 10)

            camera.draw(enemy3)

        '''player health'''
        if healthDecrease <= 0:  # if player dies
            gameplay = False
            gameOver = uvage.from_text(400, 300, "game over", 100, "red")
            hitEnter = uvage.from_text(400, 400, "hit enter to start over", 50, "orange")
            camera.draw(player)
            camera.draw(gameOver)
            camera.draw(hitEnter)
            if uvage.is_pressing("return"):  # restarting the game
                gameplay = True
                enemy1Deaths = 0
                enemy2Deaths = 0
                enemy3Deaths = 0
                totalenemyDeaths = 0
                level2 = False
                level3 = False
                healthRegen = 70
                healthDecrease = 700
                enemy1Damage = 150
                enemy2Damage = 100
                enemy3Damage = 50
                player = uvage.from_image(25, 250, "player.png")
                enemy1 = uvage.from_image(700, 250, "enemy1.png")
                enemy2 = uvage.from_image(550, 900, "enemy2.png")
                enemy3 = uvage.from_image(450, 900, "enemy3.png")
                totalHealth = uvage.from_color(0, 550, "red", healthDecrease, 30)

        '''player can't touch enemy'''
        '''okay so imma leave this off rn for the sake
        of testing but i'll uncomment it for actual gameplay'''
        # for enemy in enemies:
        #     if player.touches(enemy):
        #         totalHealth.size = [healthDecrease - 70, 30]
        #         healthDecrease = healthDecrease - 70

        '''weapon 1'''
        '''first bullet of weapon 1'''

        if uvage.is_pressing("w"):  # how player can shoot
            shoot1 = True

        if shoot1 == True:
            bullet1.x += bulletSpeed
            player = uvage.from_image(player.x, player.y, "player belted.png")
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
            bullet1 = uvage.from_color(player.x, player.y, "red", 10, 10)

        '''second bullet of weapon 1'''
        if bullet1.x > player.x + 300 and uvage.is_pressing("w"):
            shoot2 = True
        elif shoot2 == True:
            player = uvage.from_image(player.x, player.y, "player belted.png")
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
            bullet2 = uvage.from_color(player.x, player.y, "red", 10, 10)

        '''if weapon 1 hits enemy1'''
        if bullet1.touches(enemy1) or bullet2.touches(enemy1):  # how player can defeat enemies and gain back health
            enemy1.size = [enemy1Damage - 10, enemy1Damage - 10]
            enemy1Damage = enemy1Damage - 10
            if healthDecrease < 700:
                totalHealth.size = [healthDecrease + healthRegen, 30]
                healthDecrease = healthDecrease + healthRegen
            else:
                pass
            if enemy1Damage <= 50:
                dead = uvage.from_text(enemy1.x, enemy1.y, "dead", 50, "red")
                enemy1Damage = 150
                enemy1Deaths += 1
                totalenemyDeaths += 1
                camera.draw(dead)
                if enemy1.y < 600:
                    enemy1 = uvage.from_image(700, enemy1.y + 150, "enemy1.png")
                elif enemy1.y > 600:
                    enemy1 = uvage.from_image(700, enemy1.y - 150, "enemy1.png")

        '''if weapon 1 hits enemy2'''
        if level2 == True or level3 == True:
            if bullet1.touches(enemy2) or bullet2.touches(enemy2):  # how player can defeat enemies and gain back health
                enemy2.size = [enemy2Damage - 5, enemy2Damage - 5]
                enemy2Damage = enemy2Damage - 5
                if healthDecrease < 700:
                    totalHealth.size = [healthDecrease + healthRegen, 30]
                    healthDecrease = healthDecrease + healthRegen
                else:
                    pass
                if enemy2Damage <= 30:
                    dead = uvage.from_text(enemy2.x, enemy2.y, "dead", 50, "red")
                    enemy2Damage = 100
                    enemy2Deaths += 1
                    totalenemyDeaths += 1
                    camera.draw(dead)
                    if enemy2.y < 600:
                        enemy2 = uvage.from_image(550, enemy2.y + 150, "enemy2.png")
                    elif enemy2.y > 600:
                        enemy2 = uvage.from_image(550, enemy2.y - 150, "enemy2.png")

        '''if weapon 1 hits enemy3'''
        if level3 == True:
            if bullet1.touches(enemy3) or bullet2.touches(enemy3):  # how player can defeat enemies and gain back health
                enemy3.size = [enemy3Damage - 2.5, enemy3Damage - 2.5]
                enemy3Damage = enemy3Damage - 2.5
                if healthDecrease < 700:
                    totalHealth.size = [healthDecrease + healthRegen, 30]
                    healthDecrease = healthDecrease + healthRegen
                else:
                    pass
                if enemy3Damage <= 20:
                    dead = uvage.from_text(enemy3.x, enemy3.y, "dead", 50, "red")
                    enemy3Damage = 50
                    enemy3Deaths += 1
                    totalenemyDeaths += 1
                    camera.draw(dead)
                    if enemy3.y < 600:
                        enemy3 = uvage.from_image(450, enemy3.y + 150, "enemy3.png")
                    elif enemy3.y > 600:
                        enemy3 = uvage.from_image(450, enemy3.y - 150, "enemy3.png")

        ''' weapon 2'''
        if level2 == True or level3 == True:
            if uvage.is_pressing("a"):
                player = uvage.from_image(player.x, player.y, "player grounded.png")
                stillBullet.x += stillBulletspeed
                canMove = False  # can't move when using weapon 2
            else:
                stillBullet = uvage.from_color(player.x, player.y, "yellow", 10, 10)
                canMove = True
        else:
            stillBullet = uvage.from_color(player.x, player.y, "yellow", 10, 10)

        '''if weapon 2 hits enemy1'''
        if stillBullet.touches(enemy1):
            stillBullet = uvage.from_color(player.x, player.y, "yellow", 10, 10)
            enemy1.size = [enemy1Damage / 2, enemy1Damage / 2]
            enemy1Damage = enemy1Damage / 2
            if healthDecrease < 700:
                totalHealth.size = [healthDecrease + healthRegen, 30]
                healthDecrease = healthDecrease + healthRegen
            else:
                pass
            if enemy1Damage <= 50:
                dead = uvage.from_text(enemy1.x, enemy1.y, "dead", 50, "red")
                enemy1Damage = 150
                enemy1Deaths += 1
                totalenemyDeaths += 1
                camera.draw(dead)
                if enemy1.y < 600:
                    enemy1 = uvage.from_image(700, enemy1.y + 150, "enemy1.png")
                elif enemy1.y > 600:
                    enemy1 = uvage.from_image(700, enemy1.y - 150, "enemy1.png")

        '''if weapon 2 hits enemy2'''
        if level2 == True or level3 == True:
            if stillBullet.touches(enemy2):
                stillBullet = uvage.from_color(player.x, player.y, "yellow", 10, 10)
                enemy2.size = [enemy2Damage / 2, enemy2Damage / 2]
                enemy2Damage = enemy2Damage / 2
                if healthDecrease < 700:
                    totalHealth.size = [healthDecrease + healthRegen, 30]
                    healthDecrease = healthDecrease + healthRegen
                else:
                    pass
                if enemy2Damage <= 30:
                    dead = uvage.from_text(enemy2.x, enemy2.y, "dead", 50, "red")
                    enemy2Damage = 100
                    enemy2Deaths += 1
                    totalenemyDeaths += 1
                    camera.draw(dead)
                    if enemy2.y < 600:
                        enemy2 = uvage.from_image(550, enemy2.y + 150, "enemy2.png")
                    elif enemy2.y > 600:
                        enemy2 = uvage.from_image(550, enemy2.y - 150, "enemy2.png")

        '''if weapon 2 hits enemy3'''
        if level3 == True:
            if stillBullet.touches(enemy3):
                stillBullet = uvage.from_color(player.x, player.y, "yellow", 10, 10)
                enemy3.size = [enemy3Damage / 2, enemy3Damage / 2]
                enemy3Damage = enemy3Damage / 2
                if healthDecrease < 700:
                    totalHealth.size = [healthDecrease + healthRegen, 30]
                    healthDecrease = healthDecrease + healthRegen
                else:
                    pass
                if enemy3Damage <= 20:
                    dead = uvage.from_text(enemy3.x, enemy3.y, "dead", 50, "red")
                    enemy3Damage = 50
                    enemy3Deaths += 1
                    totalenemyDeaths += 1
                    camera.draw(dead)
                    if enemy3.y < 600:
                        enemy3 = uvage.from_image(450, enemy3.y + 150, "enemy3.png")
                    elif enemy3.y > 600:
                        enemy3 = uvage.from_image(450, enemy3.y - 150, "enemy3.png")

        '''weapon 3'''
        if level3 == True:

            if Tracker == True:  # tracks laser recharge
                laserTimer += 1
                if laserTimer <= 120:
                    laserDecrease += 1
                laserRegen = uvage.from_color(60, 500, "pink", laserDecrease, 30)
                camera.draw(laserBar)
                camera.draw(laserRegen)
                camera.draw(wordLaser)

            if Tracker == True and laserTimer >= 120:  # makes laser function
                if uvage.is_pressing("d"):
                    randomEnemy = random.choice(enemies)
                    laserOn = True
                    laserWidth = randomEnemy.x - player.x
                    laserTimer = 0
                    laserDecrease = 0
                    laserRegen = uvage.from_color(60, 500, "pink", laserDecrease, 30)

            elif uvage.is_pressing("d") and laserTimer < 0:  # for 1st use of laser
                randomEnemy = random.choice(enemies)
                laserOn = True
                laserWidth = randomEnemy.x - player.x
                Tracker = True
                laserTimer = 0
                laserDecrease = 0
                laserRegen = uvage.from_color(60, 500, "pink", laserDecrease, 30)

            if laserOn == True:
                laser = uvage.from_color(player.x + laserWidth / 2, player.y, "pink", laserWidth, 10)
                camera.draw(laser)
                if counter % 1 == 0:
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
                        dead = uvage.from_text(enemy1.x, enemy1.y, "dead", 50, "red")
                        enemy1Damage = 150
                        enemy1Deaths += 1
                        totalenemyDeaths += 1  # keeps track of beating level 1
                        camera.draw(dead)
                        if enemy1.y < 600:
                            enemy1 = uvage.from_image(700, enemy1.y + 150, "enemy1.png")
                        elif enemy1.y > 600:
                            enemy1 = uvage.from_image(700, enemy1.y - 150, "enemy1.png")

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
                    dead = uvage.from_text(enemy2.x, enemy2.y, "dead", 50, "red")
                    enemy2Damage = 100
                    enemy2Deaths += 1
                    totalenemyDeaths += 1
                    camera.draw(dead)
                    if enemy2.y < 600:
                        enemy2 = uvage.from_image(550, enemy2.y + 150, "enemy2.png")
                    elif enemy2.y > 600:
                        enemy2 = uvage.from_image(550, enemy2.y - 150, "enemy2.png")

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
                    dead = uvage.from_text(enemy3.x, enemy3.y, "dead", 50, "red")
                    enemy3Damage = 50
                    enemy3Deaths += 1
                    totalenemyDeaths += 1
                    camera.draw(dead)
                    if enemy3.y < 600:
                        enemy3 = uvage.from_image(450, enemy3.y + 150, "enemy3.png")
                    elif enemy3.y > 600:
                        enemy3 = uvage.from_image(450, enemy3.y - 150, "enemy3.png")

        '''beat level 1 by killing 4 of enemy 1'''
        if level2 == False and level3 == False:
            if enemy1Deaths >= 4:
                gameplay = False
                beatlevel1 = uvage.from_text(400, 300, "level 1 complete", 100, "green")
                hitEnter = uvage.from_text(400, 400, "hit enter to play level 2", 50, "orange")
                instructions1 = uvage.from_text(400, 450, "press w for weapon 1 and a for weapon 2", 30, "pink")
                instructions2 = uvage.from_text(400, 480, "kill two of each enemy to move on to level 3", 30, "pink")
                camera.draw(instructions1)
                camera.draw(instructions2)
                camera.draw(beatlevel1)
                camera.draw(hitEnter)

                if uvage.is_pressing("return"):  # going to level 2
                    gameplay = True
                    enemy1Deaths = 0
                    level2 = True
                    healthRegen = 35
                    healthDecrease = 700
                    enemy1Damage = 150
                    totalenemyDeaths = 0
                    player = uvage.from_image(25, 250, "player.png")
                    enemy1 = uvage.from_image(700, 250, "enemy1.png")
                    enemy2 = uvage.from_image(550, 250, "enemy2.png")
                    totalHealth = uvage.from_color(0, 550, "red", healthDecrease, 30)
                    camera.draw(enemy2)

        '''beat level 2 by killing 2 of each enemy'''
        if level2 == True:
            if enemy1Deaths >= 2 and enemy2Deaths >= 2:
                gameplay = False
                beatlevel2 = uvage.from_text(400, 300, "level 2 complete", 100, "green")
                hitEnter = uvage.from_text(400, 400, "hit enter to play level 3", 50, "orange")
                instructions1 = uvage.from_text(400, 450, "press w for weapon 1, a for weapon 2, and d for weapon 3",
                                                30, "pink")
                instructions2 = uvage.from_text(400, 480, "kill two of each enemy to win", 30, "pink")
                camera.draw(instructions1)
                camera.draw(instructions2)
                camera.draw(beatlevel2)
                camera.draw(hitEnter)

                if uvage.is_pressing("return"):  # going to level 3
                    gameplay = True
                    enemy1Deaths = 0
                    enemy2Deaths = 0
                    totalenemyDeaths = 0
                    level2 = False
                    level3 = True
                    healthRegen = 35
                    healthDecrease = 700
                    enemy1Damage = 150
                    enemy2Damage = 100
                    player = uvage.from_image(25, 250, "player.png")
                    enemy1 = uvage.from_image(700, 250, "enemy1.png")
                    enemy2 = uvage.from_image(550, 250, "enemy2.png")
                    enemy3 = uvage.from_image(450, 250, "enemy3.png")
                    totalHealth = uvage.from_color(0, 550, "red", healthDecrease, 30)
                    camera.draw(enemy3)

        '''beat level 3 by surviving and killing 2 of each enemy'''
        if level3 == True:
            if enemy3Deaths >= 2 and enemy1Deaths >= 2 and enemy2Deaths >= 2:
                gameplay = False
                beatlevel3 = uvage.from_text(400, 300, "you win!", 100, "green")
                hitEnter = uvage.from_text(400, 400, "hit enter to start over", 50, "orange")
                camera.draw(beatlevel3)
                camera.draw(hitEnter)

                if uvage.is_pressing("return"):  # returns to the beginning of the game
                    gameplay = True
                    enemy1Deaths = 0
                    enemy2Deaths = 0
                    enemy3Deaths = 0
                    totalenemyDeaths = 0
                    level2 = False
                    level3 = False
                    healthRegen = 70
                    healthDecrease = 700
                    enemy1Damage = 150
                    enemy2Damage = 100
                    enemy3Damage = 50
                    player = uvage.from_image(25, 250, "player.png")
                    enemy1 = uvage.from_image(700, 250, "enemy1.png")
                    enemy2 = uvage.from_image(550, 900, "enemy2.png")
                    enemy3 = uvage.from_image(450, 900, "enemy3.png")
                    totalHealth = uvage.from_color(0, 550, "red", healthDecrease, 30)

        camera.draw(displayDeaths)

    camera.display()


uvage.timer_loop(30, tick)

