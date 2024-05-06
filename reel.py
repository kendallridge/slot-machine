"""
Authors: Kendall Ridge & Oliver Ingold
CS-150: Project 4
Date: 5/1/2024
"""

from random import randrange

class Reel:

    # constructor
    def __init__(self,reel_values):
        """
        Defines a slot machine reel. Takes a list of values to initialize the
        reel_values field. Sets the selected_value field to be the first item
        in the reel_values list.
        """
        #set values that are on reel
        self.reel_values = reel_values
        
        #default to first item in list
        self.selected_value = reel_values[0]


    def spin(self):
        """
        Select a random value from the reel_values list and store this as the
        selected_value. Update and return the selected_value field.
        """
        # select random index number
        value = randrange(0,len(self.reel_values))
        # use random index number to select an item from list
        self.selected_value = self.reel_values[value]

        return self.selected_value


    def set_value(self,set_value):
        """
        Allows a value on the reel to be selected manually. Takes one parameter
        containing the value to be selected. If the selected value is not on the
        reel, a value error exception is raised.
        """
        # check if given value is on reel
        if set_value in self.reel_values:
            #set selected_value
            self.selected_value = set_value
        # if not on reel, give user an error
        else:
            raise ValueError("Error, value not in reel.")


    def get_value(self):
        """
        Return the currently selected_value.
        """
        return self.selected_value


    def __str__(self):
        """
        Convert the object's state into a displayable string and return it.
        """
        return str(self.selected_value)


    def __eq__(self,other):
        """
        Compares two reels with each other. 
        Reels are considered equal if the both have the same selected_value.
        """
        # check that you are comparing two reels + check if reels match
        return isinstance(other,Reel) \
        and self.selected_value == other.selected_value
