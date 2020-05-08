import sys, pygame, pygame.midi, random
import tkinter as tk


# set up pygame
pygame.init()
pygame.midi.init()
inp = pygame.midi.Input(1) #NOTE: if you get an error here, change 1 to 0 or 2 or 3 and make sure your piano is on and connected
# open a specific midi device



#function intToKey is used to take a midi value and convert it to an equivalent
#  note.  For example, if the keyboard sends 25 over, it means C sharp of octave 1

def intToKey(randomKey):
        switcher = {
                21:     "A1", 
                22:     "A1 #",
                23:     "B1", 
                24:     "C1", 
                25:     "C1 #",
                26:     "D1", 
                27:     "D1 #",
                28:     "E1", 
                29:     "F1", 
                30:     "F1 #",
                31:     "G1", 
                32:     "G1 #",
                33:     "A2",
                34:     "A2 #",
                35:     "B2", 
                36:     "C2", 
                37:     "C2 #",
                38:     "D2", 
                39:     "D2 #",
                40:     "E2", 
                41:     "F2", 
                42:     "F2 #",
                43:     "G2", 
                44:     "G2 #",
                45:     "A3",
                46:     "A3 #",
                47:     "B3", 
                48:     "C3", 
                49:     "C3 #",
                50:     "D3", 
                51:     "D3 #",
                52:     "E3", 
                53:     "F3", 
                54:     "F3 #",
                55:     "G3", 
                56:     "G3 #",
                57:     "A4",
                58:     "A4 #",
                59:     "B4", 
                60:     "C4", 
                61:     "C4 #",
                62:     "D4", 
                63:     "D4 #",
                64:     "E4", 
                65:     "F4", 
                66:     "F4 #",
                67:     "G4", 
                68:     "G4 #",
                69:     "A5",
                70:     "A5 #",
                71:     "B5", 
                72:     "C5", 
                73:     "C5 #",
                74:     "D5", 
                75:     "D5 #",
                76:     "E5", 
                77:     "F5", 
                78:     "F5 #",
                79:     "G5", 
                80:     "G5 #",
                81:     "A6",
                82:     "A6 #",
                83:     "B6", 
                84:     "C6", 
                85:     "C6 #",
                86:     "D6", 
                87:     "D6 #",
                88:     "E6", 
                89:     "F6", 
                90:     "F6 #",
                91:     "G6", 
                92:     "G6 #",
                93:     "A7",
                94:     "A7 #",
                95:     "B7", 
                96:     "C7", 
                97:     "C7 #",
                98:     "D7", 
                99:     "D7 #",
                100:     "E7", 
                101:     "F7", 
                102:     "F7 #",
                103:     "G7", 
                104:     "G7 #",
                105:     "A8",
                106:     "A8 #",
                107:     "B8", 
                108:     "C8", 
                
                
                
        }
        return switcher.get(randomKey,"error")





wWidth = 4000 # width of the window, used with TK
wHeight = 600
errWidth = 30
errHeight = 2


random.seed() # random is used to generate a number for the keypress game
window = tk.Tk() # main window used to display game
window.wm_attributes("-fullscreen", True)



# run the event loop
while True:

        window.update() #need this to make sure window doesn't disappear
        randomKey = random.randint(21,108) #21 to 108 is used for the keys on piano
        
        testKey = intToKey(randomKey)
        notePic = tk.PhotoImage(file=testKey+".gif") 
        message = tk.Label(
                text= testKey,
                font =  ("Helvetica",90),
                foreground = "green",
                background = "black",
                width = wWidth,
                height = wHeight,
                compound = tk.CENTER,
                image = notePic,
                ).pack()
        #message.pack() #required to show the message in the window
        
        
        while True:
                window.update()
                if inp.poll():
                 # no way to find number of messages in queue
                 # so we just specify a high max value      
                        inputRead = (inp.read(1000))
                        if (inputRead[0][0][1] == randomKey and inputRead[0][0][2]!=0):
                                #important: inputRead[0][0][2] is required because if the value is 0 it means the game will
                                # receive a button "press" saying that you let go of the button you pressed.  We don't care about
                                # that, we only care about what button was pressed down.  So we must ignore keystrokes that tell
                                # us that the key was released by using that, otherwise we'll get fake inputs
                                window.destroy()
                                window = tk.Tk()
                                window.wm_attributes("-fullscreen", True)
                                
                                break
                        else:
                                if(inputRead[0][0][2]!=0):
                                        stringToShow = ":( You hit "+ (str)(intToKey(inputRead[0][0][1]))
                                        message = tk.Label(
                                                text = stringToShow,
                                                foreground = "white",
                                                background = "red",
                                                width = errWidth,
                                                height = errHeight,
                                                font =  ("Helvetica",25))
                                        message.pack()
                                        
             # wait 10ms - this is arbitrary, but wait(0) still resulted
             # in 100% cpu utilization
                pygame.time.wait(10)


