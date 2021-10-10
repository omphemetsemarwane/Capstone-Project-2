#This code creates a simple game using Pygame
#Pygame (a collection of modules in one package) was installed for the code to work
#To do so:
# 1) open the command line interface on your computer,
# 2) cd to the directory that this task is located in,
# 3) follow the instructions here: https://www.pygame.org/wiki/GettingStarted
# 4) if you need help using pip, see here: https://projects.raspberrypi.org/en/projects/using-pip-on-windows

#(import pygame) Imports a game library that lets you use specific functions in your program.
# (import random) Import to generate random numbers.
import pygame
import random

# pygame module is initialized to get everything started
pygame.init()

#The width(1200) and height(800) of the screen are set.
screen_width = 1200
screen_height = 800


#This creates the screen and gives it the width and height specified as a 2 item sequence.
screen = pygame.display.set_mode((screen_width, screen_height))

#This creates the player, 3 enemies and prize characters and gives it the images found in this folder
# I created my own character image for enemy_3(I downloaded the image from Google).
#Images from this folder are assigned to each character.
player = pygame.image.load("image.png")
enemy1 = pygame.image.load("enemy.png")
enemy2 = pygame.image.load("monster.jpg")
enemy3 = pygame.image.load("alien.jpg")
prize = pygame.image.load("prize.jpg")

#The get() method is used to get the height and width of the character's images, this enables boundary detection.
#This helps to make sure the image stays within screen boundaries or know when the image is off the screen

player_height = player.get_height()
player_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

#The X and Y values for player's position were set
playerXposition = 100
playerYposition = 50

#The X and Y values for enemies's positions are set
enemy_1X = 800
enemy_1Y = 10
enemy_2X = 60
enemy_2Y = 800
enemy_3X = 500
enemy_3Y = 35

#The X and Y values for prize character position are set
prize_X = 800
prize_Y = 600

#The Boolean values for the up and down keys, left and right keys are set.
keyUp = False
keyDown = False
keyLeft = False
keyRight = False

#The game loop is created.
# This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting).
# In Python the int 1 has the boolean value of 'true', numbers greater than 0 also do.
# Zero(0) on the other hand has a boolean value of false.
# You can test this out with the bool(...) function to see what boolean value types have.

while 1:

    screen.fill(0)  #Clears the screen.

#This draws the player image to the screen at specified X and Y postions

    screen.blit(player, (playerXposition, playerYposition))
    screen.blit(enemy1, (enemy_1X, enemy_1Y))
    screen.blit(enemy2, (enemy_2X, enemy_2Y))
    screen.blit(enemy3, (enemy_3X, enemy_3Y))
    screen.blit(prize, (prize_X, prize_Y))

#This updates the screen.
    pygame.display.flip()

    #This for loop, loops through events in the game.
    for event in pygame.event.get():

        #This checks if the user quits the program, then if so it exits the program.
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        #This checks if the user press a key down.
        if event.type == pygame.KEYDOWN:

            #This test if the key pressed is the one we want (up, down, left or right key).
            #The previously assigned Boolean values are set to true.
            if event.key == pygame.K_UP: #pygame.K_UP represents a keyboard key constant.
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True

        #This checks if the key is up(i.e. not pressed by the user).
        if event.type == pygame.KEYUP:

            # Testing if the key released is what we want (up, down, left or right keys)
            #This set the Boolean values back to False.

            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False

#After events are checked for in the for loop above and values are set,
#check key pressed values and move player accordingly.

#The coordinate system of the game window(screen) is that the top left corner is (0, 0).
#This means that if you want the player to move down you will have to increase the y position.

    if keyUp == True:
        if playerYposition > 0:  #This ensure's that the user does not move the player above the window.
            playerYposition -= 1
    if keyDown == True:
        if playerYposition < screen_height - player_height:  #This ensures's that the user does not move the player below the window
            playerYposition += 1
    if keyLeft == True:
        if playerXposition > 0:  #This ensure's that the user does not move the player beyond the left side of the screen.
            playerXposition -= 1
    if keyRight == True:
        if playerXposition < screen_width - player_width:  #This ensure's that the user does not move the player beyond the right side of the screen.
            playerXposition += 1

#This checks for collision of the enemy with the player.
#To do this we need bounding boxes around the images of the player and enemy.
#We then need to test if these boxes intersect. If they do then there is a collision.

    #This creates bounding boxes for all character images.
    #This will help enable actions to occur when the player collides with an enemy or the prize.

    playerBox = pygame.Rect(player.get_rect())
    enemy_1Box = pygame.Rect(enemy1.get_rect())
    enemy_2Box = pygame.Rect(enemy2.get_rect())
    enemy_3Box = pygame.Rect(enemy3.get_rect())
    prizeBox = pygame.Rect(prize.get_rect())

#This updates the playerBox position to the player's X and Y positions,
# in effect making the box stay around the player image.

    playerBox.top = playerXposition
    playerBox.left = playerYposition
    enemy_1Box.top = enemy_1X
    enemy_1Box.left = enemy_1Y
    enemy_2Box.top = enemy_2X
    enemy_2Box.left = enemy_2Y
    enemy_3Box.top = enemy_3X
    enemy_3Box.left = enemy_3Y
    prizeBox.top = prize_X
    prizeBox.left = prize_Y

    #This tests collision of the player box with enemy boxes.
    if playerBox.colliderect(enemy_1Box) or playerBox.colliderect(enemy_2Box) or playerBox.colliderect(enemy_3Box):
        #Display losing status to the user.
        print("You lose")

        #Quit's the game and exit window.
        pygame.quit()
        exit(0)

    if playerBox.colliderect(prizeBox):
        #Display the winning status to the user.
        print("You win")

        #Quit's the game and exit the window.
        pygame.quit()
        exit(0)

    #If the prize exits the window before the user reaches it(prize), the user lose the game.
    if prize_Y < 0 - prize_width:
        #Display losing status to the user.
        print("You lose")

        #Quit's the game and exit the window.
        pygame.quit()
        exit(0)

    #This makes the enemy and prize characters to approach the player.
    enemy_1X -= 0.15
    enemy_3Y += 0.3
    enemy_2Y -= 0.1
    prize_Y -= 0.15
