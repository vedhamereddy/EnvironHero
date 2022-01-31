# places window on specific part of screen each time
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 50)

# imports libraries
from pygame import *
from random import *

# variables for setting up the game
TITLE = 'EnvironHero'
WIDTH = 1000
HEIGHT = 700


# initialize pygame and create window
init()
screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption(TITLE)
clock = time.Clock()


# define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
buttonColour = (21, 32, 42)
boldBrown = (219, 161, 104)


# define fonts
menuFont = font.SysFont("verdana", 20)


# states in the game
STATE_MENU = 0
STATE_GAME = 1
STATE_HELP = 2
STATE_QUIT = 3
STATE_TRYAGAIN = 4


# parts in game
PART_ONE = 1
PART_TWO = 2
PART_THREE = 3
PART_FOUR = 4
PART_TWO_INTRO = 5
PART_TWO_OUTRO = 6
PART_THREE_INTRO = 7
PART_THREE_OUTRO = 8
PART_FOUR_INTRO = 9
PART_FOUR_OUTRO = 10
CONCLUSION_INTRO = 11
CONCLUSION = 12
MINI_GAMES_INTRO = 13


# movement key booleans
PRESS_RIGHT = False
PRESS_LEFT = False
PRESS_UP = False
PRESS_DOWN = False


# loading images
playerPic = image.load('Player.png')
playerPic = transform.scale(playerPic, (11520, 192))

GrassBackground = image.load('GrassBackground.png')
GrassBackground = transform.scale(GrassBackground, (192, 192))

dirtBackground = image.load('dirt.png')
dirtBackground = transform.scale(dirtBackground, (189, 189))

bushPic = image.load('Bush.png')
bushPic = transform.scale(bushPic, (96, 96))

GameMenuBack = image.load('Game Menu Background.png')

skyBackground = image.load('partTwoBackground.png')
skyBackground = transform.scale(skyBackground, (1280, 720))

clouds = image.load('clouds.png')
clouds = transform.scale(clouds, (1280, 720))

dustPic = image.load('DustToxin.png')
dustPic = transform.scale(dustPic, (64, 64))

minigameIntroBack = image.load('Mini-Game Intro.png')

partTwoIntroBack = image.load('Part Two Intro.png')
partTwoOutroBack = image.load('Part Two Outro.png')

partThreeIntroBack = image.load('Part Three Intro.png')
partThreeOutroBack = image.load('Part Three Outro.png')

partFourIntroBack = image.load('Part Four Intro.png')
partFourOutroBack = image.load('Part Four Outro.png')

ConclusionBack = image.load('Conclusion.png')

metalsScrapPic = image.load('metals.png')

waterPic = image.load('Water Waves.png')
waterPic = transform.scale(waterPic, (1344, 96))

ShrubPic = image.load('Grass.png')
ShrubPic = transform.scale(ShrubPic, (64, 64))

chickenWalkPic = image.load('ChickenSideWalkLeft.png')
chickenWalkPic = transform.scale(chickenWalkPic, (128, 32))

chickenStandPic = image.load('ChickenIdle.png')
chickenStandPic = transform.scale(chickenStandPic, (128, 32))

toxicSign = image.load('toxic sign.png')

wellPic = image.load('well.png')
waterDrop = image.load('Water Drop.png')

shadowPic = image.load('LargeShadow.png')

bookPic = image.load('book.png')


# loading sounds
music = mixer.Sound('Music.mp3')
MenuSelectSound = mixer.Sound('Menu Select.wav')




# function for efficiently drawing grass blocks using the grass image height and width
def drawGrass(xmultiple, ymultiple):
    screen.blit(GrassBackground, (GrassBackground.get_width() * xmultiple, GrassBackground.get_height() * ymultiple))

# function for efficiently drawing bush pictures using the bush height and width
def drawBush(xmultiple, ymultiple):
    screen.blit(bushPic, (bushPic.get_width() * xmultiple, bushPic.get_width() * ymultiple))


def drawScoreCount(Score):
    score = "Your Score is:  " + str(Score)
    box = draw.rect(screen, WHITE, (0, 0, 200, 50))
    draw.rect(screen, BLACK, box, 5)
    text = menuFont.render(score, 1, BLACK)
    screen.blit(text, Rect(17, 10, 50, 50))


def drawMenu(screen, button, mx, my, state):
    screen.blit(GameMenuBack, (0, 0))

    blockWidth = WIDTH / 7.5
    blockHeight = HEIGHT / 17.5
    blockWCentre = (WIDTH / 2) - 70
    blockHCentre = (HEIGHT / 2) - 90

    rectList = [Rect(blockWCentre, blockHCentre, blockWidth, blockHeight),    # game choice
                Rect(blockWCentre, blockHCentre + 70, blockWidth, blockHeight)]  # quit choice
    stateList = [STATE_GAME, STATE_QUIT]
    titleList = ["Play Game", "Quit Game"]

    for i in range(len(rectList)):
        rect = rectList[i]
        draw.rect(screen, buttonColour, rect)
        text = menuFont.render(titleList[i], 1, boldBrown)
        textWidth, textHeight = menuFont.size(titleList[i])
        useW = (blockWidth - textWidth)/2
        useH = (blockHeight - textHeight)/2
        textRect = Rect(rect[0] + useW, rect[1] + useH, textWidth, textHeight)
        screen.blit(text, textRect)
        if rect.collidepoint(mx, my):
            draw.rect(screen, boldBrown, rect, 4)
            if button == 1:
                MenuSelectSound.play()
                state = stateList[i]
    return state


def drawPartOne(screen):
    # draws grass background using for loop
    multiplesList = [0, 1, 2, 3, 4, 5]
    for xmultiple in multiplesList:
        for ymultiple in multiplesList:
            drawGrass(xmultiple, ymultiple)

    for xmultiple in range(6):
        screen.blit(dirtBackground, (dirtBackground.get_width() * xmultiple, dirtBackground.get_height()))

    for xmultiple in range(10):
        drawBush(xmultiple, 1.3)
        drawBush(xmultiple, 3.4)


def drawMinigameIntro(screen):
    screen.blit(minigameIntroBack, (0, 0))


def drawPartTwoIntro(screen):
    screen.blit(partTwoIntroBack, (0, 0))


def drawPartTwo(screen, backgroundScrollX):
    screen.blit(skyBackground, (backgroundScrollX, 0))
    screen.blit(skyBackground, (backgroundScrollX + 1280, 0))
    screen.blit(clouds, (backgroundScrollX, 0))
    screen.blit(clouds, (backgroundScrollX + 1280, 0))


def drawPartTwoOutro(screen):
    screen.blit(partTwoOutroBack, (0, 0))


def drawPartThreeIntro(screen):
    screen.blit(partThreeIntroBack, (0, 0))


def drawPartThree(screen):
    screen.fill(BLACK)
    # draws grass background using for loop
    multiplesList = [0, 1, 2, 3, 4, 5]
    for xmultiple in multiplesList:
        for ymultiple in multiplesList:
            drawGrass(xmultiple, ymultiple)


def drawPartThreeOutro(screen):
    screen.blit(partThreeOutroBack, (0, 0))


def drawPartFourIntro(screen):
    screen.blit(partFourIntroBack, (0, 0))


def drawPartFour(waterSpriteX):
    # draws grass background using for loop
    multiplesList = [0, 1, 2, 3, 4, 5]
    for xmultiple in multiplesList:
        for ymultiple in multiplesList:
            drawGrass(xmultiple, ymultiple)

    for xmultiple in range(4):
        screen.blit(dirtBackground, (dirtBackground.get_width() * xmultiple, 50))

    # draws water background
    for xmultiple in range(11):
        screen.blit(waterPic, ((32 * 3) * xmultiple, 550, 96, 96), (waterSpriteX, 0, 32 * 3, 32 * 3))
        screen.blit(waterPic, ((32 * 3) * xmultiple, 454, 96, 96), (waterSpriteX, 0, 32 * 3, 32 * 3))

    # outlines water
    draw.rect(screen, BLACK, (0, 450, 1000, 3))
    draw.rect(screen, BLACK, (0, 645, 1000, 3))

    # draws shrubs
    for xmultiple in range(16):
        screen.blit(ShrubPic, (ShrubPic.get_width() * xmultiple, 420))
        screen.blit(ShrubPic, (ShrubPic.get_width() * xmultiple, 615))

    screen.blit(toxicSign, (50, 390))


def drawPartFourOutro(screen):
    screen.blit(partFourOutroBack, (0, 0))


def drawConclusion(screen):
    screen.blit(ConclusionBack, (0, 0))

# player movement variables
playerX = 0
playerY = 0
playerSpriteX = 0
moveRate = 5
spriteSheetMove = 64*3

def drawPlayerWalk(screen, playerX, playerY, playerSpriteX, button, state):
    playerRect = Rect(playerX, playerY, 70, 80)
    screen.blit(playerPic, (playerX-60, playerY-55, 70, 70), (playerSpriteX, 0, 64*3, 64*3))
    return state



# plays game music an infinite number of times while the game is running
music.play(-1)

# variables for part one
button = 0
mx = my = 0

# begins game with state being set to the menu and the game part being set to one
state = STATE_MENU
part = PART_ONE

# variables for part two
skyBackgroundX = 0
playerYChange = 0
obstacleHeight = randint(100, 500)
obstacleX = 1000
obstacleXChange = -10
dustScore = 0

# variables for part three
self = 0  # self counter to draw images on the screen slower than the FPS
score = 0

# variables for part four
waterSpriteX = 0
chickenX = 1010
chickenSpriteX = 0
waterObtained = False
walk = False
chickenScore = 0


# game loop
running = True
while running:
    for e in event.get():  # checks all events that happen
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            mx, my = e.pos # collects mouse coordinates
            button = e.button
        elif e.type == MOUSEMOTION:
            mx, my = e.pos


    # draws menu if state is equal to state menu
    if state == STATE_MENU:
       state = drawMenu(screen, button, mx, my, state)


    # quits game if state is equal to quit
    elif state == STATE_QUIT:
        running = False


    # draws part two intro
    elif state == STATE_GAME and part == PART_TWO_INTRO:
        drawPartTwoIntro(screen)
        for e in event.get():
            if e.type == QUIT:
                running = False
            if e.type == KEYDOWN:
                if e.key == K_RETURN:
                    # reset player X and player Y position for the next mini game
                    playerX = 0
                    playerY = 0
                    # set game part to part two
                    part = PART_TWO


    # draws second part of game
    elif state == STATE_GAME and part == PART_TWO:
        clock.tick(27) # sets mini game FPS to 27
        skyBackgroundX -= 1 # shifts sky background to the left
        playerY += playerYChange # moves player across the Y axis
        drawPartTwo(screen, skyBackgroundX) # uses the part two function to display the scrolling background
        # sets boundaries for player to prevent them from leaving
        if playerY <= 0:
            playerY = 0
        if playerY >= 630:
            playerY = 630
        obstacleX += obstacleXChange # shifts the white walls to the left
        # if obstacle moves off the screen, a point gets added to the score and sets it back to the right of the screen with new dimensions
        if obstacleX <= -90:
            obstacleX = 1000
            dustScore += 1  # add one to the score
            # resets the dust pic from transparent to the original
            dustPic = image.load('DustToxin.png')
            dustPic = transform.scale(dustPic, (64, 64))
            # resets top wall's height for the next time it comes back onto the screen
            obstacleHeight = randint(100, 500)

        # sets top wall's width and height and draws it on screen along with black borders
        obstacleWidth = 90
        topRect = draw.rect(screen, WHITE, (obstacleX, 0, obstacleWidth, obstacleHeight))
        draw.rect(screen, BLACK, topRect, 5) # top wall rect for collision
        # set bottom wall's height, and starting and draws it on screen
        bottomStart = obstacleHeight + 200 # adds 200 to whatever value was randomly generated for the top wall's height
        bottomRect = draw.rect(screen, WHITE, (obstacleX, bottomStart, obstacleWidth, 700))
        draw.rect(screen, BLACK, bottomRect, 5) # bottom wall rect for collision
        playerRect = Rect(playerX, playerY, 50, 50) # player rect for collision

        dustRect = Rect(obstacleX + 10, bottomStart - 130, 64, 64) # dust image collision rect using the png's dimensions
        screen.blit(dustPic, (obstacleX + 10, bottomStart - 130)) # draws dust png between the two walls every time it generates
        drawPlayerWalk(screen, 50, playerY, 7680, button, state) # function to make player walk

        # variables for when collisions occur
        collisionDust = playerRect.colliderect(dustRect)
        collisionTop = playerRect.colliderect(topRect)
        collisionBottom = playerRect.colliderect(bottomRect)

        drawScoreCount(dustScore) # function for drawing the score on screen

        # once the score counts to 10, the game will end the part will change to mini-game outro
        if dustScore == 10:
            part = PART_TWO_OUTRO

        # when player rect and dust rect collide, the dust pic will be redefined as a transparent image to give it the illusion that it disappeared (this resets once it goes off screen)
        if collisionDust:
            dustPic = image.load('transparent.png')

        # when player rect and the bottom or wall rects collide the score gets set to -1 (this is just because once the wall goes off screen it will go back to 0 which happens immediately after)
        elif collisionTop or collisionBottom:
            dustScore = -1


        for e in event.get():
            if e.type == QUIT:
                running = False
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    playerYChange = -9 # if space bar is pressed player will fly up by 9 pixels
                    playerSpriteX = 7680 # set the frame to the one of the player flying
            elif e.type == KEYUP:
                if e.key == K_SPACE:
                    playerYChange = 6.5 # if space is not pressed player will fly down by 6.5 pixels
                    playerSpriteX = 7680 # set the frame to the one of the player flying


    # draws the outro screen of the part two mini game
    elif state == STATE_GAME and part == PART_TWO_OUTRO:
        drawPartTwoOutro(screen)
        for e in event.get():
            if e.type == QUIT:
                running = False
            if e.type == KEYDOWN:
                if e.key == K_RETURN: # if the enter key is pressed the game part will switch to the part three intro
                    part = PART_THREE_INTRO


    # draws the intro screen of the part three mini game
    elif state == STATE_GAME and part == PART_THREE_INTRO:
        drawPartThreeIntro(screen)
        for e in event.get():
            if e.type == QUIT:
                running = False
            if e.type == KEYDOWN:
                if e.key == K_RETURN: # if the enter key is pressed the game part will switch to the part three intro
                    part = PART_THREE


    # draws part three game on screen
    elif state == STATE_GAME and part == PART_THREE:
        self += 1 # counter used to display images slower than the FPS
        xSprite = [0, 88, 176] # splits metal scraps image into three parts and puts the x coordinate for the start of the parts in the list
        xSpriteVal = choice(xSprite) # uses random choice to select one of the three from the list
        xVal = randint(100, 900) # uses random randint to select a random x coordinate for the image to be displayed
        yVal = randint(100, 600) # uses random randint to select a random y coordinate for the image to be displayed

        # once the counter reaches 11 the background and metal scrap images get drawn
        if self > 11:
            drawPartThree(screen)
            drawScoreCount(score) # draws the score of number of images clicked on
            screen.blit(metalsScrapPic, (xVal, yVal, 70, 70), (xSpriteVal, 0, 88, 64)) # displays the image on screen depending on which image and coordinates were selected
            scrapRect = Rect(xVal, yVal, 75, 64) # collision rect for metal scrap image
            self = 0 # resets counter back to 0

        mouseRect = Rect(mx, my, 30, 30) # collision rect for mouse position

        # if the mouse is clicked and the cursor collides with the image, a point gets added to the score
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1 and mouseRect.colliderect(scrapRect):
                score += 1

        # if score reached 20, the part will switch to the part three outro
        if score == 20:
            part = PART_THREE_OUTRO

        clock.tick(10)

    # draws part three outro
    elif state == STATE_GAME and part == PART_THREE_OUTRO:
        drawPartThreeOutro(screen)
        for e in event.get():
            if e.type == QUIT:
                running = False
            if e.type == KEYDOWN:
                if e.key == K_RETURN: # if enter key is pressed, part switches to part four intro
                    part = PART_FOUR_INTRO


    # draws part four intro
    elif state == STATE_GAME and part == PART_FOUR_INTRO:
        drawPartFourIntro(screen)
        for e in event.get():
            if e.type == QUIT:
                running = False
            if e.type == KEYDOWN:
                if e.key == K_RETURN: # if enter key is pressed, part switches to part four
                    # resets player x and y coordinates for next game
                    playerX = 0
                    playerY = 0
                    part = PART_FOUR

    # draws part four of game
    elif state == STATE_GAME and part == PART_FOUR:
        # sets FPS to 14
        clock.tick(14)

        # sets boundaries that the player can't exceed
        if playerY <= 50:
            playerY = 50
        if playerX >= 735:
            playerX = 735
        if playerY >= 390:
            playerY = 390

        #animates the water stream
        drawPartFour(waterSpriteX)
        waterSpriteX += 32 * 3
        if waterSpriteX >= 448 * 3:
            waterSpriteX = 0

        # moves chicken off the screen
        if chickenX >= 250:
            chickenX -= 4

        # chicken animation
        if chickenSpriteX <= 128:
            chickenSpriteX += 64
        elif chickenSpriteX > 128:
            chickenSpriteX = 0
        if chickenX <= 250:
            chickenWalkPic = image.load('transparent.png') # makes original image of chicken walking invisible
            chickenWalkPic = transform.scale(chickenWalkPic, (256, 64))
            screen.blit(chickenStandPic, (chickenX, 360, 32, 32), (0, 0, 32, 32)) # new image of chicken standing can appear in place of chicken walking image
        screen.blit(chickenWalkPic, (chickenX, 360, 32, 32), (chickenSpriteX/2, 0, 32, 32))

        # draws shadow and player
        screen.blit(shadowPic, (playerX + 2, playerY + 55))
        drawPlayerWalk(screen, playerX, playerY, playerSpriteX, button, state)
        # draws the well image and creates a rect for it
        screen.blit(wellPic, (800, 50))
        wellRect = Rect(800, 50, 140, 121)
        # creates a rect for the chicken and player position
        chickenRect = Rect(chickenX, 360, 32, 32)
        playerRect = Rect(playerX, playerY, 70, 80)

        if playerRect.colliderect(wellRect) and waterObtained == False:
            waterObtained = True

        if waterObtained == True:
            screen.blit(waterDrop, (playerX, playerY - 60, 64, 72))

        if waterObtained == True and playerRect.colliderect(chickenRect):
            waterDrop = image.load('transparent.png') # water drop image turns invisible
            chickenStandPic = image.load('transparent.png') # chicken standing image turns invisible
            waterObtained = False
            walk = True

        if walk == True:
            chickenWalkPic = image.load('ChickenSideWalkLeft.png') # resets the chickenWalkPic image to the walk image
            chickenWalkPic = transform.scale(chickenWalkPic, (128, 32))
            # animates and moves the chicken off the screen
            chickenX -= 4
            screen.blit(chickenWalkPic, (chickenX, 360, 32, 32), (chickenSpriteX / 2, 0, 32, 32))

        # once chicken goes off screen, the point increases by one
        if chickenX <= -10:
            chickenScore += 1
            chickenStandPic = image.load('ChickenIdle.png') # the image for the chicken standing gets reset
            chickenStandPic = transform.scale(chickenStandPic, (128, 32))
            waterDrop = image.load('Water Drop.png') # water drop image gets reset
            walk = False
            chickenX = 1010 # places the chicken to the right of the screen

        # uses draw score function to display the score on screen
        drawScoreCount(chickenScore)

        # switches part to part four outro when the score reaches five
        if chickenScore == 5:
            part = PART_FOUR_OUTRO

        # for every button pressed set the character animation frame to the start of that movement sequence
        for e in event.get():
            if e.type == QUIT:
                running = False
            if e.type == KEYDOWN:
                if e.key == K_RIGHT:
                    playerSpriteX = 0
                    PRESS_RIGHT = True
                if e.key == K_UP:
                    playerSpriteX = 384 * 3
                    PRESS_UP = True
                if e.key == K_LEFT:
                    playerSpriteX = 768 * 3
                    PRESS_LEFT = True
                if e.key == K_DOWN:
                    playerSpriteX = 1152 * 3
                    PRESS_DOWN = True
            elif e.type == KEYUP:
                if e.key == K_RIGHT:
                    playerSpriteX = 0
                    PRESS_RIGHT = False
                if e.key == K_UP:
                    playerSpriteX = 384 * 3
                    PRESS_UP = False
                if e.key == K_LEFT:
                    playerSpriteX = 768 * 3
                    PRESS_LEFT = False
                if e.key == K_DOWN:
                    playerSpriteX = 1152 * 3
                    PRESS_DOWN = False
        # update
        if PRESS_RIGHT == True and playerX < WIDTH - 70:
            playerX += moveRate
            if playerSpriteX < 320 * 3:
                playerSpriteX += spriteSheetMove
            else:
                playerSpriteX = 0
        elif PRESS_UP == True and playerY > 0:
            playerY -= moveRate
            if playerSpriteX < 704 * 3 and playerSpriteX >= 384 * 3:
                playerSpriteX += spriteSheetMove
            else:
                playerSpriteX = 384 * 3
        elif PRESS_LEFT == True and playerX > 0:
            playerX -= moveRate
            if playerSpriteX < 1088 * 3 and playerSpriteX >= 768 * 3:
                playerSpriteX += spriteSheetMove
            else:
                playerSpriteX = 768 * 3
        elif PRESS_DOWN == True and playerY < HEIGHT - 80:
            playerY += moveRate
            if playerSpriteX < 1472 * 3 and playerSpriteX >= 1152 * 3:
                playerSpriteX += spriteSheetMove
            else:
                playerSpriteX = 1152 * 3


    # draw part four outro
    elif state == STATE_GAME and part == PART_FOUR_OUTRO:
        drawPartFourOutro(screen)
        for e in event.get():
            if e.type == QUIT:
                running = False
            if e.type == KEYDOWN:
                if e.key == K_RETURN: # when enter key is pressed player x and y is reset and part switches to conclusion
                    playerX = 0
                    playerY = 0
                    part = CONCLUSION

    # draws game conclusion
    elif state == STATE_GAME and part == CONCLUSION:
        drawConclusion(screen)
        for e in event.get():
            if e.type == QUIT:
                running = False
            if e.type == KEYDOWN:
                if e.key == K_RETURN: # if enter key is pressed player x and y coordinates will be reset and game state and part will be brought back to the start
                    playerX = 0
                    playerY = 0
                    state = STATE_MENU
                    part = PART_ONE


    # draws part one
    elif state == STATE_GAME and part == PART_ONE:
        drawPartOne(screen)
        screen.blit(shadowPic, (900, 270))
        screen.blit(bookPic, (900, 250))
        bookRect = Rect(900, 250, 64, 64)
        playerRect = Rect(playerX, playerY, 70, 80)
        screen.blit(shadowPic, (playerX + 2, playerY + 55))
        drawPlayerWalk(screen, playerX, playerY, playerSpriteX, button, state)
        clock.tick(12)

        if playerRect.colliderect(bookRect):
            part = MINI_GAMES_INTRO



        if playerY >= 250:
            playerY = 250
        if playerY <= 150:
            playerY = 150

        for e in event.get():
           if e.type == QUIT:
               running = False
           if e.type == KEYDOWN:
               if e.key == K_RIGHT:
                   playerSpriteX = 0
                   PRESS_RIGHT = True
               if e.key == K_UP:
                   playerSpriteX = 384 * 3
                   PRESS_UP = True
               if e.key == K_LEFT:
                   playerSpriteX = 768 * 3
                   PRESS_LEFT = True
               if e.key == K_DOWN:
                   playerSpriteX = 1152 * 3
                   PRESS_DOWN = True
           elif e.type == KEYUP:
               if e.key == K_RIGHT:
                   playerSpriteX = 0
                   PRESS_RIGHT = False
               if e.key == K_UP:
                   playerSpriteX = 384 * 3
                   PRESS_UP = False
               if e.key == K_LEFT:
                   playerSpriteX = 768 * 3
                   PRESS_LEFT = False
               if e.key == K_DOWN:
                   playerSpriteX = 1152 * 3
                   PRESS_DOWN = False
       # update
        if PRESS_RIGHT == True and playerX < WIDTH - 70:
           playerX += moveRate
           if playerSpriteX < 320 * 3:
               playerSpriteX += spriteSheetMove
           else:
               playerSpriteX = 0
        elif PRESS_UP == True and playerY > 0:
           playerY -= moveRate
           if playerSpriteX < 704 * 3 and playerSpriteX >= 384 * 3:
               playerSpriteX += spriteSheetMove
           else:
               playerSpriteX = 384 * 3
        elif PRESS_LEFT == True and playerX > 0:
           playerX -= moveRate
           if playerSpriteX < 1088 * 3 and playerSpriteX >= 768 * 3:
               playerSpriteX += spriteSheetMove
           else:
               playerSpriteX = 768 * 3
        elif PRESS_DOWN == True and playerY < HEIGHT - 80:
           playerY += moveRate
           if playerSpriteX < 1472 * 3 and playerSpriteX >= 1152 * 3:
               playerSpriteX += spriteSheetMove
           else:
               playerSpriteX = 1152 * 3


    # draws mini game on the screen
    elif state == STATE_GAME and part == MINI_GAMES_INTRO:
        drawMinigameIntro(screen)
        for e in event.get():
            if e.type == QUIT:
                running = False
            if e.type == KEYDOWN:
                if e.key == K_RETURN:  # if enter key is pressed part will switch to part two
                    part = PART_TWO_INTRO

    display.flip()
quit()