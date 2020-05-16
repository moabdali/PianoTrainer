import math
from pygame import mixer
from os import system, name
from time import sleep
import sys, pygame, pygame.midi, random
import keysConversion as kc

# Intialize the pygame
pygame.init()
pygame.midi.init()
inp = pygame.midi.Input(1) #NOTE: if you get an error here, change 1 to 0 or 2 or 3 and make sure your piano is on and connected
# open a specific midi device


# create the screen
X = 1900
Y = 1080
screen = pygame.display.set_mode((X, Y))

# Caption and Icon
pygame.display.set_caption("Piano Trainer")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)


pianoFull = pygame.image.load('pianoFull.png')
pfx = 0
pfy = 955

    
random.seed() # random is used to generate a number for the keypress game

def pianoKeys(x,y):
    screen.blit(pianoFull, (x,y) )


white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)
red = (255,0,0)
black = (0,0,0)

  




font = pygame.font.Font('freesansbold.ttf', 60)
asterisk = font.render(
    "*",
    1,
    red)

while True:
    
    
    randomKey = random.randint(21,108) #21 to 108 is used for the keys on piano
    testKey = kc.intToKey(randomKey)
    myText = "("+(str)(testKey)+")"
    text = font.render(myText, True, green, black)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    screen.fill(black)
    screen.blit( text,textRect)
    
    
    while True:
        
        pygame.display.update()
        pianoKeys(0,955) #show piano
        if inp.poll():

            inputRead = (inp.read(1000))
            if (inputRead[0][0][1] == randomKey and inputRead[0][0][2]!=0):
                                #important: inputRead[0][0][2] is required because if the value is 0 it means the game will
                                # receive a button "press" saying that you let go of the button you pressed.  We don't care about
                                # that, we only care about what button was pressed down.  So we must ignore keystrokes that tell
                                # us that the key was released by using that, otherwise we'll get fake inputs
                                #print("SUCCESS")
                                screen.fill(black)
                                pianoKeys(0,955) #show piano
                                successText = font.render("Nice!", True, green, black)
                                textRect3 = successText.get_rect()
                                textRect3.center = (X // 2, Y //4)
                                screen.blit(successText, textRect3)
                                pygame.display.update()
                                sleep(.25)
                                screen.fill(black)
                                break
            else:
                if(inputRead[0][0][2]!=0):

                                if inputRead[0][0][1] > randomKey:
                                    
                                    
                                    stringToShow = "<< You hit "+ (str)(kc.intToKey(inputRead[0][0][1]))
                                    
                                else:
                                    stringToShow = "You hit "+ (str)(kc.intToKey(inputRead[0][0][1]))+">>"

                                    
                                
                                print(inputRead[0][0][1])
                                screen.fill(black)
                                pianoKeys(0,955) #show piano
                                failedText = font.render(stringToShow, True, red, black)
                                textRect2 = failedText.get_rect()
                                textRect2.center = (X // 2, Y // 4)
                                screen.blit(text,textRect)
                                screen.blit(failedText,textRect2)
                                offset = kc.offsetCalculator (inputRead[0][0][1])
                                screen.blit(asterisk, (offset,955))
                                pygame.display.update()
                                sleep(.1)
                                
                                

