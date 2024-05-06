"""
Authors: Kendall Ridge & Oliver Ingold
CS-150: Project 4
Date: 5/1/2024
"""

from reel import Reel

class Slot_Machine:

    # constuctor
    def __init__(self,credits):
        """
        Constructor has one parameter that specifies the initial credits 
        to put in the machine and is assigned to the credits field.
        """
        # create reel #1
        self.reel1 = Reel(['Mellon','Cherry','Orange','Grape','Bells','Lemon',\
                           'Lu7cky','Cherry','Orange','Grape','Lemon'])
        # create reel #2
        self.reel2 = Reel(['Mellon','Cherry','Orange','Grape','Bells','Lemon',\
                           'Mellon','Lu7cky','Grape','Orange','Lemon'])
        # create reel #3
        self.reel3 = Reel(['Mellon','Cherry','Orange','Grape','Bells','Lemon',\
                           'Mellon','Cherry','Lu7cky','Bells','Grape'])
        # default credit amount received as parameter
        self.credits = credits
        # bank is set to zero as default
        self.bank = 0


    def play(self):
        """
        Present a menu of options, then take user input and use this to select
        the appropriate method to call.

        Options: 
        (1) Spin, 
        (2) View Prizes, 
        (3) Show Bank, 
        (4) Add Credits, 
        (0) Exit
        """
        menu_selection = None # default

        # loops until user exits by entering 0
        while menu_selection != '0':
            # user selects menu option
            menu_selection = input("\nOptions:\
                                   \n1: Spin, 2: View Prizes, 3: Show Bank, " +\
                                   "4: Add Credits, 0: Exit\
                                   \nEnter Choice: ")
            
            # call appropriate function from user selection
            if menu_selection == '1':
                self.spin()
            elif menu_selection == '2':
                print(self.display_win_table())
            elif menu_selection == '3':
                print(self.display_bank())
            elif menu_selection == '4':
                self.add_credits()
            # if user exits, refund any remaining credits to bank 
            # and reset credits to 0
            elif menu_selection == '0':
                self.bank += self.credits
                self.credits = 0
            # if user inputs number outside of menu options, give error
            else:
                print("Invalid input, try again.")

        # display end bank amount
        print(self.display_bank())
        print("Bye!")


    def spin(self):
        """
        Simulate 'pulling the level' on the slot machine to make 
        all three reels spin to a random value. 
        Calling the function decrements the number of credits by 1.
        If no credits remain, dislay error message. Once all reels have spun, 
        display the current state of the reels via the display method.
        """
        # checks that there are credits in machine
        if self.credits > 0:
            # decrement credits for each spin
            self.credits -= 1
            
            # spin each reel
            self.reel1.spin()
            self.reel2.spin()
            self.reel3.spin()
            
            # determine if a prize was won
            prize = self.get_wins()
            
            # display reels, machine info, and prize
            print(self.__str__())
            print("Win:",prize)

            # add prize to player's bank
            self.bank += prize
        
        # if no credits in machine, prompt user to add more
        else:
            print("No credits. Please add credits.")


    def get_wins(self):
        """
        Get the randomly selected values of reel one, two, and three 
        and use this to determine if a win occured. 
        Wins are calculated based on given table. 
        """
        # get values for all reels
        reel1 = self.reel1.get_value()
        reel2 = self.reel2.get_value()
        reel3 = self.reel3.get_value()

        # default to initialize
        prize = 0

        # sets a prize amount for reel 1 that can be multiplied if theres a win
        if reel1 == "Cherry":
            prize = 1
        elif reel1 == "Lemon":
            prize = 2
        elif reel1 == "Grape":
            prize == 3
        elif reel1 == "Orange":
            prize = 4
        elif reel1 == "Melon":
            prize = 5
        elif reel1 == "Bells":
            prize = 6
        elif reel1 == "Lu7cky":
            prize = 7

        # if doubles win, multiply prize for matching icon by 2
        if reel1 == reel2:
            prize *= 2
        # if triples win, multiply prize for matching icon by 3
        elif reel1 == reel2 and reel2 == reel3:
            prize *= 3
        # if no double or triple match, no win. set prize to 0
        else:
            prize = 0

        return prize


    def display_win_table(self):
        """
        Displays a table of wins on the screen.
        """
        # list of reel icons
        value_list = ['Cherry', 'Lemon', 'Grape', 'Orange',\
                      'Mellon', 'Bells', 'Lu7cky']
        
        # table header that rest of table is concantated with
        win_table = "\n===============PRIZES===============\n"

        # win multipliers
        doubles_reward = 2
        triples_reward = 3

        # create doubles win section
        win_table += "\nDoubles:\n" + "-"*51 + "\n"
        for i in value_list:
            doubles_line = i + "\t:\t" + i + "\t:\t-\t=\t" \
                                + str(doubles_reward) + "\n"
            win_table += doubles_line
            doubles_reward += 2

        # create triples win section
        win_table += "\nTriples:\n" + "-"*51 + "\n"
        for i in value_list:
            triples_line = i + "\t:\t" + i + "\t:\t" + i + "\t=\t" +\
                           str(triples_reward) + "\n"
            win_table += triples_line
            triples_reward += 3

        return win_table


    def add_credits(self):
        """
        Prompts the user to enter the number of credits to add (int) and 
        adds this to the number of credit stored in the object's credit field. 
        The method should handle input errors with an error message and 
        repeatedly re-prompt the user for input until a valid response is given.
        """
        success = False # default to start while loop

        while not success:
            # prompt user for credits num and add to credits attribute
            try:
                credit_input = int(input("How many credits? "))
                self.credits += credit_input
                #set to true to end while loop
                success = True
            # give error if non-int was given (cannot add to credits)
            except ValueError:       
                print("Error: Enter a Whole Number between 0 and 2.")
        
        return self.credits


    def display_bank(self):
        """
        Display on screen the credits and bank.
        """
        # format machine info
        display_bank = "Credits: " + str(self.credits) + "\nBank: " +\
                       str(self.bank)
        
        return display_bank


    def __str__(self):
        """
        Return the values of each of the three reels and follow that with the 
        number of credits and value in the bank. Returns a printable string.
        """
        # format reels values after spin, 
        # call display_bank func to show machine stats
        string = " "*9 + "\nREELS\n" + "="*23 +\
        f"\n[{str(self.reel1)}]:[{str(self.reel2)}]:[{str(self.reel3)}]\n" +\
        "="*23 + "\n" + self.display_bank()
        
        return string
