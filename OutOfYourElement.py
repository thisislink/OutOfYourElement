''' Title: Out of Your Element
Story Written By: Daphne Link
Programmer: Daphne Link
Artist: Daphne Link
'''

#Global Variables
#Possible directions to move player
moveLeft = "left"
moveRight = "right"
moveUp = "up"
moveDown = "down"
moveExit = "exit"
#Elements needed to collect per level
levelOneElements = 1

def gameMenu():
    #Title Screen
    print "Welcome to..."
    gameTitle = '''\
******  *    *   *****    ******  *****    *   *  ******  *    *  ******
*    *  *    *     *      *    *  *         * *   *    *  *    *  *    *
*    *  *    *     *      *    *  ***        *    *    *  *    *  *****
*    *  *    *     *      *    *  *          *    *    *  *    *  *   *
******  ******     *      ******  *          *    ******  ******  *    *

                             ------------
                            | ???        |
                            | Element    |
                            | ******  *  |
                            | *       *  |
                            | ****    *  |
                            | *       *  |
                            | ******  *  |
                            |    V 1.0   |    
                             ------------

'''
    print gameTitle
    #Game Rules Function
    '''Player will press enter to Accept Mission and begin play after reading the rules'''
    def gameRules():
        print '''\nYou've been selected to do a secret mission to stop a government underground
medical lab from developing a serum that turns humans into zombies.
\nFind elements scattered in the lab rooms and exit the lab without getting caught by secret agents.'''
        print "\nControls: You can type up, down, left, right, and exit to navigate the lab"
        playerReady = raw_input("\nPress Enter to Accept Your Mission ")

    #Check for correct key presses from menu screen   
    ''' If player presses Enter proceed to level otherwise
    If player presses any other key, do not proceed '''
    playerInput = 'R'
    playerReady = raw_input("Type the letter R to read the rules: ")
    while playerReady != playerInput:
        playerReady = raw_input("Type the letter R to read the rules: ")
    if playerReady == playerInput:
        gameRules()

#Text Graphics Map Functions
#Beginning of game map
def startMap():
    print "\n-------x-"
#Moved left from beginning of game
def movedFromStartMap():
    print "\n------x--"
#Entered room with Na (Sodium-11)
def movedNaRoom():
    print "\n----Na (Sodium-11)----"

#Functions to check if player moved in directions they shouldn't
def fromStartCheck(movePlayer):
    if movePlayer != moveLeft:
        #Check if player moves any direction other than left
        while movePlayer != moveRight or movePlayer != moveUp or movePlayer != moveDown:
            movePlayer = raw_input("Wrong direction!\nEnter a direction. You can move left: ")
            if movePlayer == moveLeft:
                break
    print "You are still in the hallway."

def upExitCheck(movePlayer, elementsFound):
    if movePlayer != moveUp:
        while movePlayer == moveExit and elementsFound != levelOneElements or movePlayer != moveExit and elementsFound != levelOneElements:
            print "You have not yet collected all the elements in this level, you cannot exit!"
            break
        while movePlayer != moveDown or movePlayer != moveLeft or movePlayer != moveRight:
            movePlayer = raw_input("Wrong direction!\nEnter a direction. You can move up or exit: ")
            if movePlayer == moveUp:
                break
    movedNaRoom()
    collectElement = raw_input('''You have entered a room. The Element Na (Sodium-11) is in this room.
\nPress Enter to collect the element and leave the room.''')
    elementsFound = 1

def endGame(movePlayer):
    if movePlayer != moveExit:
        while movePlayer == moveUp or movePlayer == moveDown or movePlayer == moveLeft or movePlayer != moveRight:
            movePlayer = raw_input('''You already collected Na (Sodium-11). Get out now!\nEnter a direction. You can exit: ''')
            if movePlayer == moveExit:
                break
    gameOver = raw_input("\nCongratulations you found all the elements and escaped the lab!\nPress Enter to Quit.")
        
#Start game once player has pressed enter
def startGame():
    gameMenu()
    #Show current map location
    startMap()
    print "\nYou are in the hallway."
    #Get player input for direction
    movePlayer = raw_input("Enter a direction. You can move left: ")
    #Move player based on what they type and check if player moved in directions other than left
    fromStartCheck(movePlayer)
    #Show current map location
    movedFromStartMap()
    #Get player input for direction
    movePlayer = raw_input("Enter a direction. You can move up or exit: ")
    #Move player based on what they type and check if player moved in directions other than up or exit
    #Initialize elements found to 0
    elementsFound = 0
    upExitCheck(movePlayer, elementsFound)
    #Once upExitCheck checks out, increment elementsFound by 1
    elementsFound = 1
    #Map after finding element
    movedFromStartMap()
    print "You are in the hallway again."
    movePlayer = raw_input("Enter a direction. You can now exit: ")
    endGame(movePlayer)
    
startGame()
