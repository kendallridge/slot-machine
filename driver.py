##
#Author: Andrew Scott
#Version: SP24
#Description: Run the slot machine program.
##

from slot_machine import Slot_Machine

def main():
    '''Create a slot machine and play it'''
    INITIAL_CREDITS = 5#Start the game with 10 credits.
    slot = Slot_Machine(INITIAL_CREDITS)#Call the constructor of the slot machine.
    
    #display header at beginning of play
    print("\nLucky 777 Slot Machine\n=======================")
    
    #call play func to start machine
    slot.play()
    
    

#Run the main function if this is called directly by the Python interpreter
if __name__ == "__main__":
    main()