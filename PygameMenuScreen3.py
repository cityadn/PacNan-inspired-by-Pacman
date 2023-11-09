import pygame
from pygame import mixer
from my_main_easy import runfileEasy
from my_main_medium import runfileMedium
from my_main_hard import runfileHard
import time
from pygame.locals import *
import sys
from tkinter import *

mainClock = pygame.time.Clock()


class menu():
    def __init__(self):
        # initialises the menu() class
        white = (255, 255, 255)
        red = (255, 0, 0)
        darkblue = (0, 0, 51)
        # colors that will be used to replace the word colours

        pygame.init()
        # initialises pygame
        pygame.display.set_caption('Main Menu')
        font = pygame.font.SysFont("Helvetica", 85)
        font2 = pygame.font.SysFont("Helvetica", 160)

        monitor_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        # identifies the length and width of the Player's monitor

        screen = pygame.display.set_mode(monitor_size, HWSURFACE | DOUBLEBUF | RESIZABLE)
        # Sets the screen, allowing the Player to resize the menu screen
        # The doublebuf parameter optimises the frame rate of the menu screen transitions

        def draw_text(text, font, color, surface, x, y):
            textobj = font.render(text, 1, color)
            # generates the font style
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            surface.blit(textobj, textrect)
            # Allows python to draw text on buttons and title screens

        background = pygame.image.load('NeonMaze.jpg')
        # Loads a background image behind each button on the game interface

        def intro():
            # plays an intro sequence before the menu screen is displayed
            introSound = mixer.Sound('pacman_beginning.wav')
            introSound.play()
            background = pygame.image.load('PleaseStandBy (1) (1).jpg')
            screen.blit(background, (0, 0))
            # Sets the background to the coordinates (100, 50)
            pygame.display.update()
            # Updates the screen so that the next transition is executed

        def game():
            # This is the menu screen, where the buttons are situated
            click = False
            running = True
            while running:
                # runs the code below while the screen is displayed, and until a button is clicked
                screen.blit(background, (0, 0))
                # Sets the background to the coordinates (0, 0)
                mx, my = pygame.mouse.get_pos()
                # Identifies the position of the Player's Cursor and its coordinates

                button_1 = pygame.Rect(705, 250, 140, 150)
                button_2 = pygame.Rect(645, 400, 260, 150)
                button_3 = pygame.Rect(705, 550, 130, 120)
                button_4 = pygame.Rect(500, 50, 595, 140)
                # draws a button for 'Play', 'Controls' and 'Quit'

                if button_1.collidepoint((mx, my)):
                    # checks if the Player has clicked the Play Button
                    if click:
                        # The click is set to the boolean value of True
                        difficulty()
                if button_2.collidepoint((mx, my)):
                    # checks if the Player has clicked the Controls Button
                    if click:
                        # The click is set to the boolean value of True
                        about()
                if button_3.collidepoint((mx, my)):
                    # checks if the Player has clicked the Quit Button
                    if click:
                        # The click is set to the boolean value of True
                        quit()
                pygame.draw.rect(screen, darkblue, button_1)
                pygame.draw.rect(screen, darkblue, button_2)
                pygame.draw.rect(screen, darkblue, button_3)
                pygame.draw.rect(screen, darkblue, button_4)
                draw_text('Pac-Block', font2, 'cyan', screen, 500, 20)
                draw_text('Play', font, 'cyan', screen, 705, 250)
                draw_text('Controls', font, 'cyan', screen, 645, 410)
                draw_text('Quit', font, 'cyan', screen, 705, 555)
                # draws a button for 'Play', 'Controls' and 'Quit'

                for event in pygame.event.get():
                    # allows me to utilise built-in-functions from the function pygame.event
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                        # shuts the system and pygame down
                    if event.type == K_ESCAPE:
                        # checks if the Player has clicked the escape button
                        running = False
                        # stops running this specific interface
                    if event.type == MOUSEBUTTONDOWN:
                        # checks if the player has clicked with their cursor
                        if event.button == 1:
                            # changes the binary value of even.button from 0 to 1
                            click = True
                    if event.type == KEYDOWN:
                        # checks if the player has clicked with their cursor
                        if event.key == K_ESCAPE:
                            # checks if the Player has clicked the escape button
                            running = False
                            # stops running this specific interface
                            
                pygame.display.update()
                mainClock.tick(60)
                # updates the interface with every interaction every 60 ms

        def difficulty():
            # This is the screen where the Player chooses their preferred difficulty level
            running = True
            click = False
            while running:
                # This is the menu screen, where the buttons are situated
                screen.blit(background, (0, 0))
                # Sets up the screen at (0, 0)

                mx, my = pygame.mouse.get_pos()
                # Identifies the position of the Player's Cursor and its coordinates

                button_5 = pygame.Rect(705, 250, 155, 150)
                button_6 = pygame.Rect(645, 400, 260, 150)
                button_7 = pygame.Rect(705, 550, 150, 120)
                button_8 = pygame.Rect(500, 50, 595, 140)
                # draws a button for 'Easy', 'Medium', 'Hard'

                if button_5.collidepoint((mx, my)):
                    # checks if the Player has clicked the Easy Button
                    if click:
                        # The click is set to the boolean value of True
                        runfileEasy()
                        # directs the player to the easy level
                if button_6.collidepoint((mx, my)):
                    # checks if the Player has clicked the Medium Button
                    if click:
                        # The click is set to the boolean value of True
                        runfileMedium()
                        # directs the player to the medium level
                if button_7.collidepoint((mx, my)):
                    # checks if the Player has clicked the Hard Button
                    if click:
                        # The click is set to the boolean value of True
                        runfileHard()
                        # directs the player to the hard level
                pygame.draw.rect(screen, 'green', button_5)
                pygame.draw.rect(screen, 'orange', button_6)
                pygame.draw.rect(screen, 'red', button_7)
                pygame.draw.rect(screen, darkblue, button_8)
                draw_text('Pac-Block', font2, 'cyan', screen, 500, 20)
                draw_text('Easy', font, 'cyan', screen, 705, 250)
                draw_text('Medium', font, 'cyan', screen, 645, 410)
                draw_text('Hard', font, 'cyan', screen, 705, 555)
                # draws a button for 'Easy', 'Medium', 'Hard'
                
                for event in pygame.event.get():
                    # allows me to utilise built-in-functions from the function pygame.event
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                        # shuts the system and pygame down
                    if event.type == KEYDOWN:
                        # checks if the player has clicked with their cursor
                        if event.key == K_ESCAPE:
                            # checks if the Player has clicked the escape button
                            running = False
                            # stops running this specific interface
                    if event.type == MOUSEBUTTONDOWN:
                        # checks if the player has clicked with their cursor
                        if event.button == 1:
                            # changes the binary value of even.button from 0 to 1
                            click = True
                pygame.display.update()
                mainClock.tick(60)
                # updates the interface with every interaction every 60 ms

        def about():
            running = True
            while running:
                # runs the code below while the screen is displayed, and until the escape key is clicked
                background = pygame.image.load('AboutScreen.jpg')
                screen.blit(background, (200, 100))
                # Sets the screen to coordinates (0, 0)
                for event in pygame.event.get():
                    # allows me to utilise built-in-functions from the function pygame.event
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                        # shuts the system and pygame down
                    if event.type == KEYDOWN:
                        # checks if the player has clicked with their cursor
                        if event.key == K_ESCAPE:
                            running = False
                            # stops running this specific interface

                pygame.display.update()
                mainClock.tick(60)
                # updates the interface with every interaction every 60 ms

        def quit():
            pygame.quit()
            sys.exit()
            # shuts the system and pygame down

        intro()
        time.sleep(4.2)
        # allows the intro screen to play for 4.2 seconds
        mixer.music.load('ShangChiYourMother.mp3')
        # loads music
        mixer.music.play(-1)
        # loops the song
        game()


menu()
# runs the menu class
