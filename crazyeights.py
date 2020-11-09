# Programmers: Dagmawit Asfaw, Aaron Rapaka, Fernando Sierra, Sydney Small

from random import shuffle

class Game:
            
""" A Crazy Eights card game that can be played between a human and computer program.
    Objective: Discard your whole hand of cards, so that you have no cards left.
               Players can discard by matching the card @ the top of the discard pile to a suit/face in your hand.
               If you do not have any matching cards, then you must draw a card from the deck.
               If you have an '8', you can change the suit of the card.
               First player to have no cards wins.
    """

    def __init__(self, name):
        """ Initializes all attributes pertinent to the game.

            Attributes:

                suits (str): Suits in a normal card deck of Hearts, Diamonds, Spades, and Clubs.
                faces (str): Each number/rank in a normal card deck with the numbers 1-10 and 
                             "J" for Joker, "K" for King,"Q" for Queen, and "A" for Ace.
                value (int): The values that each rank takes in the Crazy Eight's game with 8s holding
                    a value of 50, Aces, Kings, Queens, and Jokers holding values of 10, and numbers 2-7
                    holding their real values.
                deck (list): A list of all possible suit, face combinations from a normal card deck.
                             For example one possible combination would be[(Heart, Q)].
                name(str): The name of the player.
                player_hand: (list): empty list (of where player's 7 cards will be stored).
                computer_hand (list): empty list (of where computer's 7 cards will be stored).
                discard_pile (int): Cards that the players will discard into a pile throughout the
                                    game with the winner being the first player to discard all of their cards. 
                                    Default to 0.
                suit_change (str): empty str of where the new suit in the Crazy Eight's game will be specified.
                                   The suit is chnaged in cases where a player might play a number, for example an 8,
                                   which allows the player to change the suit for the next turn.
            
            Args:
                Name(str):name of the player to be used throughout the game.
            
        """


    def card_dealer(self):
        """ Assigns cards from deck to player and computer hands. Each receive 7 cards.
            Creates the discard pile.
            
           Side Effects:
                shuffles self.deck
                modifies self.player_hand, self.computer_hand, self.discard_pile. 
                
            """
    
    def card_value(self):
        """ Assigns card values according to the Crazy Eight's rules (based on faces).
            All number cards have their number = value,
            Jack, Queen, King, Ace = 10,
            and 8 = 50.
        
        Returns: values associated with each card in the deck.
            """
    
    def player_options(self, selected_card):
        """ Determines whether the card selected to add to the discard pile is allowed to be chosen according to Crazy Eight's rules.
            Only a card of the same face or suit can be discarded.
            
        Args:
            selected_card(tuple): the card (suit, face) the player chooses to add to the discard pile. 
            
        Returns:
            (boolean): True if player performs a valid action, False if player performs an invalid action.
            
        Raises: error if the action is invalid, allows player to redo turn.
        """
        
        
   
    def player_turn(self):
        """ Allows the player to perform their turn: choose a new card from the discard pile, or enter the number of the card they want to discard.
            Will either append card to player_hand or place a card on top of the discard pile.
            
            Returns: 
                    (str): "You have no more cards!" 
                    (str): "The deck has no more cards!"
                    computer_turn: if the player has completed their turn.
            """
        
            
    def computer_options(self):
        """ Determines the card selected is allowed to be chosen according to Crazy Eight's rules.
            Only a card of the same face or suit can be discarded.
           
        Args:
            selected_card(tuple): the card (suit, face) the player chooses to add to the discard pile. 
            
        Returns:
            (boolean): True if player performs a valid action, False if player performs an invalid action.
            
        Raises: error if the action is invalid, allows player to redo turn. 
            """
        
    def computer_turn(self):
        """ Allows the computer to perform its turn. 
        
        Returns:
        """
        
            
    def calculator(self):
        """ Calculates the points as according to the Crazy Eight's rules.
            Adds the values of the cards in player and computer hands,
            whoever's is lowest (0) wins.
            
            Returns: 
                    winner(str): the winner of the game (whoever has zero or lowest score).
                    player_points(int): # of points the player has @ end of game.
                    computer_points(int): # of points the computer scored @ end of game.
            """
          
                
    def start(self):
        """ Starts functions required to play Crazy Eight's program.
        
            """



