import sys, pygame, pygame.midi, random
# set up pygame
pygame.init()
pygame.midi.init()
# open a specific midi device
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
                
        }
        return switcher.get(randomKey,"error")
  
random.seed()
inp = pygame.midi.Input(1)

# run the event loop
while True:
        randomKey = random.randint(21,65)
        testKey = intToKey(randomKey)
        print("HIT: ",testKey)      
        while True:
                if inp.poll():
                 # no way to find number of messages in queue
                 # so we just specify a high max value      
                        inputRead = (inp.read(1000))
                        if (inputRead[0][0][1] == randomKey and inputRead[0][0][2]!=0):
                                print ("!!!NICE!!!")
                                break
                        else:
                                if(inputRead[0][0][2]!=0):
                                        print(":( You hit "+ (str)(intToKey(inputRead[0][0][1])))
             # wait 10ms - this is arbitrary, but wait(0) still resulted
             # in 100% cpu utilization
                pygame.time.wait(10)

