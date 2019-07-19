import random

print('')
# Welcome message
print('  <<=========<} Welcome to Nim {>========>>  ')
print('Below are three randomised piles')
print()

# creates the piles at the start, with random amounts
pilea = random.randint(5, 15)
pileb = random.randint(5, 15)
pilec = random.randint(5, 15)


player1 = 1
player2 = -1
currentplayer = -1
whichplayer = 'My dude'

pc = 'Z'
at = 20


def main():
    """
    Runs the display, decrementing and remove code until the piles are empty,
    runs win check to award victory to the player.
    """
    while True:
        while pilea + pileb + pilec != 0:
            display()
            decrementing()
            remove()
        else:
            wincheck()
            print('')
            print('     Thanks for playing')
            break


# used to check that inputs are acceptable or not
# then pass on the information to the next function i.e. what pile and how much to remove
def decrementing():
    """
    This function gets player input for the pile choice (pc) and sets a global variable to be that pile (pile).
    It also gets input on the amount to remove (at)
    :return: pc, at and pile
    """
    global pile
    global pc
    global at
    global a
    global b
    global c

    a = 'A'
    b = 'B'
    c = 'C'
    # Test weather the input is a pile or not.
    # Using while True loops in order to keep the code running and not cause a runtime error that will close the program
    print('')
    players()
    while True:
        print('')
        pc = input('choose which pile to play from (A,B,C): ')
        if pc == a or pc == b or pc == c:
            if pc == a:
                pile = pilea

            elif pc == b:
                pile = pileb

            else:
                pile = pilec
# Used to check weather or not the pile has no tiles in it. If so it will return to the start of the loop.
            if pile == 0:
                print('ERROR; Pile is empty')
                pc
            else:
                break
        else:
            print('ERROR; not a pile')
    # Test weather the input is an acceptable integer.
    # check weather the number chosen is within the range of 1 to the maximum number of the pile
    # if not it gives the
    while True:
        try:
            at = int(input('Choose amount to remove: '))
            if at not in range(1, pile + 1):
                print('ERROR; Cant remove that amount')
            else:
                print('Ok')
                print('Amount was removed')
                break
        except ValueError:
            print('ERROR; Not an integer')

    print()
    return pile
    return at
    return pc


# function used to remove the tiles from the chosen pile
def remove():
    """
    This function takes the global variables of the piles and if that pile was chosen previously
    it removes the chosen amount from it
    """
    global pilea
    global pileb
    global pilec
    global pc
    global at
    # checking if the chosen pile was a, b, c
    # if so how many tiles to be removed and then setting the pile length as that amount
    if pc == 'A':
        pilea = pilea - at
    elif pc == 'B':
        pileb = pileb - at
    else:
        pilec = pilec - at


# function displays the piles and number of tiles. is used anytime the piles must be shown
def display():
    """
    This function takes the global variable of the piles, ones that were created at the beginning, and displays them.
    if the pile size was changed then it displays the new pile amount instead. it also shows the numbers below.
    """
    global pilea
    global pileb
    global pilec
    # this prints out the piles and their tile amounts
    # the amount is determined in the remove function that will change the number in the piles if it is chosen
    print('A:', pilea * '*')
    print('B:', pileb * '*')
    print('C:', pilec * '*')
    print('(', pilea, pileb, pilec, ')')


# players runs a code that will change the value of variable; current player is used in win check.
def players():
    """
    This function changes the player each turn. by multiplying the player variable by -1 each time
    the variable is able to swap between the two values indefinitely.
    :return: currentplayer and whichplayer
    """
    global currentplayer
    global whichplayer
    currentplayer = currentplayer * -1
    if currentplayer == 1:
        whichplayer = 'Player 1'
    else:
        whichplayer = 'Player 2'
    print(whichplayer)
    return currentplayer
    return whichplayer



def wincheck():
    """
    Will check what value the current player is and award the victory to the right player
    """
    if currentplayer == 1:
        print('<===={ Player 1 picked up the last object, player 2 gets the epic victory royale! }====> ')
    else:
        print('<===={ Player 2 picked up the last object, player 1 gets the epic victory royale! }====>')


main()
