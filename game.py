print('hello world')

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

import uvage
import random
camera = uvage.Camera(500, 500)

player = uvage.from_color(25, 250, "purple", 40, 40) 
playerSpeed = 9

def tick():
    global playerSpeed
    camera.clear("black")
        
    if uvage.is_pressing("right arrow"): 
        player.x += playerSpeed
        if 500 < player.x: 
            player.x -= playerSpeed
    elif uvage.is_pressing("left arrow"): 
        player.x -= playerSpeed 
        if 0 > player.x:
            player.x += playerSpeed


                            
    camera.draw(player)
    camera.display()
 
uvage.timer_loop(30, tick)
