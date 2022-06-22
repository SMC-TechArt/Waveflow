import time, keyboard

counter = 0
speed = .1
direction = "right"
letter = "."
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
spaces = []
spacelength = 2
exp = 0
gap = ""
for i in range (41 - spacelength):
    gap += " "

### Style functions normal/exponental
def spacemaker():
    spacestring = ""
    for x in range(spacelength):
        spacestring += " "
        spaces.append(spacestring)
def expmaker():
    spacestring = ""
    for x in range(spacelength):
        for y in range(x):
            spacestring += " "
        spaces.append(spacestring)
spacemaker()

print("""

    _    _                                ____   __
   F L  J J     ___ _  _    _   ____     F ___J  LJ    ____      _    _
  J J .. L L   F __` LJ |  | L F __ J   J |___:  FJ   F __ J    FJ .. L]
  | |/  \| |  | |--| |J J  F L| _____J  | _____|J  L | |--| |  | |/  \| |
  F   /\   J  F L__J JJ\ \/ /FF L___--. F |____JJ  L F L__J J  F   /\   J
 J___//\\___LJ\____,__L\\__//J\______/FJ__F     J__LJ\______/FJ\__//\\__/L
 |___/  \___| J____,__F \__/  J______F |__|     |__| J______F  \__/  \__/


                    Push enter to start your journey.

""")
keyboard.wait("enter")

while 1:

    ### Toggles exponential spaces
    if keyboard.is_pressed("ctrl"):
        if exp == 0:
            exp = 1
            expmaker()
        else:
            exp = 0
            spacemaker()


    ### Changes width
    if keyboard.is_pressed("right"):
        if spacelength < 40:
            spacelength += 1
            spaces = []
            if exp == 0:
                spacemaker()
            else:
                expmaker()
            gap = ""
            for i in range (41 - spacelength):
                gap += " "
    if keyboard.is_pressed("left"):
        if spacelength > 2:
            spacelength -= 1
            spaces = []
            if exp == 0:
                spacemaker()
            else:
                expmaker()
            gap = ""
            for i in range (40 - spacelength):
                gap += " "

    # Changes letter
    for i in alphabet:
        if keyboard.is_pressed(i):
            letter = i

    # Controls speed
    if keyboard.is_pressed("down") & (speed < 1):
        speed = speed + .05
    if keyboard.is_pressed("up") & (speed >= .04):
        speed = speed - .05

    # Pause
    if keyboard.is_pressed("space"):
        keyboard.wait("space")
        time.sleep(.2)

    # Exit
    if keyboard.is_pressed("backspace"):
        exit()

    # Changes direction on edge
    if (direction == "right") & (counter < (len(spaces) - 1)):
        counter = counter + 1
    else:
        direction = "left"
    if (direction == "left") & (counter > 0):
        counter = counter - 1
    else:
        direction = "right"

    ###print(exp)
    print(gap + spaces[counter] + letter)
    time.sleep(speed)
