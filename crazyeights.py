# Programmers: Dagmawit Asfaw, Aaron Rapaka, Fernando Sierra, Sydney Small

from random import shuffle
            
class Game:
    """ A crazy eights game that can be played between humans and/or computers. 
    
    Attributes:
            suits (str): Suits in a normal card deck.
            faces (str): Each number/rank in a normal card deck.
            value (int): The values that each rank takes in the Crazy Eight's game.
            deck (list): A list of all possible suit, face combinations from a normal card deck.
            name(str): The name of the player
            player_hand: (list): empty list (of where player's 7 cards will be stored).
            computer_hand (list): empty list (of where computer's 7 cards will be stored).
            discard_pile (int): default to 0
            suit_change (str): empty str (of where the new suit in the Crazy Eight's game will be specified.) """
    
    
    def __init__(self, name):
        """ Initializes all attributes pertinent to the game.
        
        Args:
            Name(str)- name of the player
            
        Side Effects:
            Initializes attrributes     
        """
        
    
    def card_dealer(self):
        """ Assigns cards from deck to player and computer hands. Each receive 7 cards.
            Creates the discard pile.
            
           Side Effects:
                shuffles self.deck
                modifies self.player_hand, self.computer_hand, self.discard_pile. 
            """
    
    def card_value(self, card):
        """ Assigns card values according to the Crazy Eight's rules (based on faces).
            All number cards have their number = value,
            Jack, Queen, King, Ace = 10,
            and 8 = 50.
            
        Args:
            card()- 
        
        Returns:


            """
    
    def player_options(self, selected_card):
        """ Determines whether the card selected to add to the discard pile is allowed to be chosen according to Crazy Eight's rules.
            Only a card of the same face or suit can be discarded.
            
        Args:
            selected_card()- the card the player chooses to add to the discard pile.
            
        Returns:
            (boolean)- 
        """
        
        
   
    def player_turn(self):
        """ Allows the player to perform their turn. 
            
            """
        
            
    def computer_options(self):
        """ Determines the card selected is allowed to be chosen according to Crazy Eight's rules.
            Only a card of the same face or suit can be discarded.
            
            """
        
    def computer_turn(self):
        """ Allows the computer to perform its turn. 
        
        Returns:

        """
        
            
    def calculator(self):
        """ Calculates the points as according to the Crazy Eight's rules.
            Adds the values of the cards in player and computer hands,
            whoever's is lowest (0) wins.

            """
          
                
    def start(self):
        """ Starts functions required to play Crazy Eight's program.
        
            """
        



