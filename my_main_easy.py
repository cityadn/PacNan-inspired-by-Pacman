from turtle import *
from utilities import *
from random import choice
import pygame
from pygame import mixer
import random
from pygame.locals import *
import time
import sys
from point import *

mainClock = pygame.time.Clock()

class runfileEasy():
    def __init__(self):
        # initialises the runfileEasy() class
        pygame.mixer.init(44100, -16, 2, 64)
        # increases the quality of sound effects and music
        pygame.init()
        # initialises pygame

        path = Turtle()
        writer = Turtle()
        turtle.title('PacNan')
        # Uses a turtle to draw the map/maze pattern

        aim = vector(5, 0)
        # This automatically sends the Pac-Man avatar 5 tiles to the right
        pacman = vector(-40, -80)
        # allows the player to move up, down, left and right in the maze

        ghosts = [
            [vector(-180, 160), vector(-5, 0)],
            [vector(-180, -160), vector(0, 5)],
            [vector(100, 160), vector(-5, 0)],
            [vector(100, -160), vector(0, -5)],
            [vector(-10, 40), vector(0, -5)]
        ]
        # creates 4 ghost enemies at 4 different positions
        # the vector variable sends each ghost in different random directions throughout the map
        # 1st vector = Position of Ghost
        # 2nd vector = Direction of Ghost

        state = {'score': 0}
        # Sets the score to zero

        tiles = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 5, 1, 1, 1, 0, 1, 1, 1, 1, 1, 3, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 3, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 4, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 0, 1, 1, 5, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 0, 1, 1, 1, 3, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
            0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 3, 0, 1, 0, 0, 0, 0, 0,
            0, 1, 1, 3, 1, 0, 6, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]
        # Sets a value for each value on the map
        # value 0 = The blocks that make up the maze pattern
        # value 1 = Pac-dots/Collectibles for the Player to obtain
        # value > 1 = Fruits/More points

        def square(x, y):
            "Draw square using path at (x, y)."
            path.hideturtle()
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()

            for count in range(4):
                path.forward(20)
                path.left(90)

            path.end_fill()

        def offset(point):
            "Return offset of point in tiles."
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index

        def valid(point):
            "Return True if point is valid in tiles."
            index = offset(point)

            if tiles[index] == 0:
                return False

            index = offset(point + 19)

            if tiles[index] == 0:
                return False

            return point.x % 20 == 0 or point.y % 20 == 0

        def world():
            Screen().bgcolor('black')
            path.color('green')
            # Sets the color of the background Screen and the blocks that form the maze pattern

            for index in range(len(tiles)):
                tile = tiles[index]
                # sets a value to each tile, first forming the tiles

                if tile > 0:
                    x = (index % 20) * 20 - 200
                    y = 180 - (index // 20) * 20
                    square(x, y)
                    if tile == 1:
                        path.up()
                        path.goto(x + 10, y + 10)
                        path.dot(3, 'white')

                    if tile == 3:
                        path.up()
                        path.goto(x + 10, y + 10)
                        path.dot(8, 'pink')

                    if tile == 4:
                        path.up()
                        path.goto(x + 10, y + 10)
                        path.dot(9, 'red')

                    if tile == 5:
                        path.up()
                        path.goto(x + 10, y + 10)
                        path.dot(9, 'orange')

                    if tile == 6:
                        path.up()
                        path.goto(x + 10, y + 10)
                        path.dot(10, 'lime')

                    # draws a dot and sets its coordinates for each collectible
                    # sets a color to each fruit and collectible, as well as their magnitudes
                    # sets a collectibles color based on what tile value they have

                    update()
                    # updates the screen to display the fruits to the Player
                    # updates the screen to show how many collectibles the player has left, as well as how many they've eaten

            update()
            # updates the screen so that the Player can move

            # r = random.randint(0, 62)
            r = 1
            # chooses a random number between 0 and 62 (including 0 and 62)
            if r == 0:
                mixer.music.load("IndustryBabyBackground1.mp3")
                # loads a song
            elif r == 1:
                mixer.music.load("SevenNationBackground2.mp3")
            elif r == 2:
                mixer.music.load("SweetDreamsBackground3.mp3")
            elif r == 3:
                mixer.music.load("AvengersBackground4.mp3")
            elif r == 4:
                mixer.music.load("GodzillaBackground5.mp3")
            elif r == 5:
                mixer.music.load("SunflowerBackground6.mp3")
            elif r == 6:
                mixer.music.load("ComeAndGetYourLoveBackground7.mp3")
            elif r == 7:
                mixer.music.load("BackInBlackBackground8.mp3")
            elif r == 8:
                mixer.music.load("SmellsLikeTeenSpiritBackground9.mp3")
            elif r == 9:
                mixer.music.load("MandalorianBackground10.mp3")
            elif r == 10:
                mixer.music.load("WeAreTheChampionsBackground11.mp3")
            elif r == 11:
                mixer.music.load("AllStarBackground12.mp3")
            elif r == 12:
                mixer.music.load("BlueBackground13.mp3")
            elif r == 13:
                mixer.music.load("ChainBackground14.mp3")
            elif r == 14:
                mixer.music.load("NeverGonnaGiveYouUpBackground15.mp3")
            elif r == 15:
                mixer.music.load("RasputinBackground16.mp3")
            elif r == 16:
                mixer.music.load("RobberyBackground17.mp3")
            elif r == 17:
                mixer.music.load("HarderBetterFasterStrongerBackground18.mp3")
            elif r == 18:
                mixer.music.load("MegalovaniaBackground19.mp3")
            elif r == 19:
                mixer.music.load("GangstasParadiseBackground20.mp3")
            elif r == 20:
                mixer.music.load("CrabRaveBackground21.mp3")
            elif r == 21:
                mixer.music.load("Spider-ManBackground22.mp3")
            elif r == 22:
                mixer.music.load("DontStopMeNowBackground23.mp3")
            elif r == 23:
                mixer.music.load("BohemianRhapsodyBackground24.mp3")
            elif r == 24:
                mixer.music.load("SuperMarioBrosBackground25.mp3")
            elif r == 25:
                mixer.music.load("StarWarsImperialThemeBackground26.mp3")
            elif r == 26:
                mixer.music.load("InTheEndBackground27.mp3")
            elif r == 27:
                mixer.music.load("NumbBackground28.mp3")
            elif r == 28:
                mixer.music.load("StressedOutBackground29.mp3")
            elif r == 29:
                mixer.music.load("BuildOurMachineBackground30.mp3")
            elif r == 30:
                mixer.music.load("MinecraftSwedenBackground31.mp3")
            elif r == 31:
                mixer.music.load("TakeOnMeBackground32.mp3")
            elif r == 32:
                mixer.music.load("FadedBackground33.mp3")
            elif r == 33:
                mixer.music.load("BegginBackground34.mp3")
            elif r == 34:
                mixer.music.load("ThisIsAmericaBackground35.mp3")
            elif r == 35:
                mixer.music.load("BringMeToLifeBackground36.mp3")
            elif r == 36:
                mixer.music.load("RapGodBackground37.mp3")
            elif r == 37:
                mixer.music.load("XGonGiveItToYaBackground38.mp3")
            elif r == 38:
                mixer.music.load("MonteroBackground39.mp3")
            elif r == 39:
                mixer.music.load("WhereTheHoodAtBackground40.mp3")
            elif r == 40:
                mixer.music.load("ItWasntMeBackground41.mp3")
            elif r == 41:
                mixer.music.load("CelebrateGoodTimesBackground42.mp3")
            elif r == 42:
                mixer.music.load("StarBoyBackground43.mp3")
            elif r == 43:
                mixer.music.load("InDaClubBackground44.mp3")
            elif r == 44:
                mixer.music.load("AstronautInTheOceanBackground45.mp3")
            elif r == 45:
                mixer.music.load("GetLuckyBackground46.mp3")
            elif r == 46:
                mixer.music.load("CountingStarsBackground47.mp3")
            elif r == 47:
                mixer.music.load("DriversLicenseBackground48.mp3")
            elif r == 48:
                mixer.music.load("EyeOfTheTigerBackground49.mp3")
            elif r == 49:
                mixer.music.load("RansomBackground50.mp3")
            elif r == 50:
                mixer.music.load("EverybodyBackground51.mp3")
            elif r == 51:
                mixer.music.load("IWantItThatWayBackground52.mp3")
            elif r == 52:
                mixer.music.load("PrayForMeBackground53.mp3")
            elif r == 53:
                mixer.music.load("AllTheStarsBackground54.mp3")
            elif r == 54:
                mixer.music.load("MinecraftWetHandsBackground55.mp3")
            elif r == 55:
                mixer.music.load("GDFRBackground56.mp3")
            elif r == 56:
                mixer.music.load("ImmortalsBackground57.mp3")
            elif r == 57:
                mixer.music.load("CenturiesBackground58.mp3")
            elif r == 58:
                mixer.music.load("PacManFeverBackground59.mp3")
            elif r == 59:
                mixer.music.load("WakeMeUpBackground60.mp3")
            elif r == 60:
                mixer.music.load("TheNightsBackground61.mp3")
            elif r == 61:
                mixer.music.load("BelieverBackground62.mp3")
            elif r == 62:
                mixer.music.load("RadioactiveBackground63.mp3")
            mixer.music.play(-1)
            # plays the song on a loop/on repeat

        def draw_text(text, font, color, surface, x, y):
            textobj = font.render(text, 1, color)
            # generates the font style
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            surface.blit(textobj, textrect)
            # Allows python to draw text on buttons and title screens

        def gameover():
            flags = DOUBLEBUF
            screen = pygame.display.set_mode((1600, 1300), flags, pygame.RESIZABLE)
            # sets the screen to a length of 1600 pixels and a width of 1300 pixels
            # Utilises the flag constant to increase the frame rate of the game
            font = pygame.font.SysFont("impact", 40)
            # sets the font to 'impact', with a magnitude of 40 pixels
            background = pygame.image.load('JakePeraltaScreaming.jpg')
            screen.blit(background, (1000, 300))
            # sets the background image to coordinates (700, 300)
            draw_text('Game Over!', font, 'red', screen, 1100, 230)
            # draws the words Game Over above the image at coordinates (700, 230)
            pygame.display.update()
            mainClock.tick(60)
            # updates the interface with every interaction every 60 ms
            time.sleep(4)
            # delays the system exit for 4 seconds
            pygame.quit()
            sys.exit()
            # shuts the system and pygame down

        def gamecomplete():
            flags = DOUBLEBUF
            screen = pygame.display.set_mode((1600, 1300), flags, pygame.RESIZABLE)
            # sets the screen to a length of 1600 pixels and a width of 1300 pixels
            # Utilises the flag constant to increase the frame rate of the game
            font = pygame.font.SysFont("impact", 100)
            # sets the font to 'impact', with a magnitude of 100 pixels
            background = pygame.image.load('Ego_vs_PacMan.jpg')
            screen.blit(background, (500, 200))
            # sets the background image to coordinates (500, 200)
            draw_text('Game Complete!', font, 'red', screen, 690, 50)
            # draws the words Game Over above the image at coordinates (690, 50)
            gameCompleteSound = mixer.Sound('Ta-Da.mp3')
            # loads the sound effect
            gameCompleteSound.play()
            # plays the sound effect
            pygame.display.update()
            mainClock.tick(60)
            # updates the interface with every interaction every 60 ms
            time.sleep(4)
            # delays the system exit for 4 seconds
            pygame.quit()
            sys.exit()
            # shuts the system and pygame down

        def move():
            writer.clear()
            writer.write(state['score'])
            clear()
            # writes the word 'score' beside the maze pattern
            # allows the player to view the score to the side of the interface

            if valid(pacman + aim):
                pacman.move(aim)
                # allows the player to move Pac-Man

            index = offset(pacman)
            # calculates the trajectory of where Pac-Man is headed

            if state['score'] == 4770:
                gamecomplete()
                # congratulates the Player after they reach a score of 4770, finishing the level

            if tiles[index] == 1:
                '1 = Pac-dot'
                tiles[index] = 2
                state['score'] += 10
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)
                if state['score'] % 20 == 0:
                    scoreSound = mixer.Sound('pacman_chomp.wav')
                    scoreSound.play()

            if tiles[index] == 3:
                '3 = Cherry'
                tiles[index] = 2
                state['score'] += 100
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)
                fruitSound = mixer.Sound('pacman_eatfruit.wav')
                fruitSound.play()

            if tiles[index] == 4:
                '4 = Stawberry'
                tiles[index] = 2
                state['score'] += 300
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)
                fruitSound = mixer.Sound('pacman_eatfruit.wav')
                fruitSound.play(1)

            if tiles[index] == 5:
                '5 = Orange'
                tiles[index] = 2
                state['score'] += 500
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)
                fruitSound = mixer.Sound('pacman_eatfruit.wav')
                fruitSound.play(2)

            if tiles[index] == 6:
                '6 = Apple'
                tiles[index] = 2
                state['score'] += 700
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)
                fruitSound = mixer.Sound('pacman_eatfruit.wav')
                fruitSound.play(3)

            if tiles[index] == 7:
                '7 = Melon'
                tiles[index] = 2
                state['score'] += 1000
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)
                fruitSound = mixer.Sound('pacman_extrapac.wav')
                fruitSound.play(1)

            if tiles[index] == 8:
                '8 = Galaxian'
                tiles[index] = 2
                state['score'] += 2000
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)
                fruitSound = mixer.Sound('pacman-galaxian.mp3')
                fruitSound.play(1)

            up()
            goto(pacman.x + 10, pacman.y + 10)
            # allows the Player to move Pac-man at a rate of x+10 and y+10
            squareshape()
            # sets the color of the Pac-Man avatar, updating the color every split second
            # sets a magnitude of 20 to the avatar

            for point, course in ghosts:
                if valid(point + course):
                    point.move(course)
                    # allows the ghost enemies to move on their own
                else:
                    options = [
                        vector(5, 0),
                        vector(-5, 0),
                        vector(0, 5),
                        vector(0, -5),
                    ]
                    # these vectors show the ghost enemies where to move and in what direction to move in a random fashion
                    plan = choice(options)
                    # allows the ghost enemies to move on their own
                    course.x = plan.x
                    course.y = plan.y

                up()
                goto(point.x + 10, point.y + 10)
                triangle()
                # sets the color of the ghost enemies, setting the color to red
                # sets a magnitude of 20 to the ghost enemies

            update()
            # updates the screen so that the Player and the ghosts can move

            for point, course in ghosts:
                if abs(pacman - point) < 20:
                    # calcuates the point at which the Player collides with a ghost enemy
                    deathSound = mixer.Sound('pacman_death.wav')
                    # loads sound effect
                    deathSound.play()
                    # plays sound effect when Player dies
                    gameover()
                    # sends the player to a 'gameover' screen when they die

            Screen().ontimer(move, 70)
            # updates the screen so that the Player and the ghosts can move

        def change(x, y):
            "Change pacman aim if valid."
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y

        Screen().setup(420, 420, 550, 125), pygame.RESIZABLE
        # Sets Maze to length 420 and width 420 at coordinates (200, 100)
        Screen().tracer(0, 0)
        # This draws the maze pattern at the fastest possible rate
        writer.hideturtle()
        # takes the turtle tool off the screen
        writer.goto(160, 160)
        # pen goes to coordinates (160, 160)
        writer.color('white')
        # sets pen color to white
        writer.write(state['score'])
        # Writes the word 'score' and the updating value of the score beside the maze pattern
        Screen().listen()
        # Connects the screen to the 'change' subroutine, allowing the Player to move
        hideturtle()
        Screen().onkey(lambda: change(5, 0), 'Right')
        Screen().onkey(lambda: change(-5, 0), 'Left')
        Screen().onkey(lambda: change(0, 5), 'Up')
        Screen().onkey(lambda: change(0, -5), 'Down')
        # Lets the Player click the controls with these keys, moving their avatar
        Screen().onkey(lambda: sys.exit(), 'Escape')
        # Lets the player press the escape button to shut the system down and exit the game

        world()
        move()
        done()
