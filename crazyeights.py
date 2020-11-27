# Programmers: Dagmawit Asfaw, Aaron Rapaka, Fernando Sierra, Sydney Small

from random import shuffle

class Game:
            
    """ A Crazy Eights card game that can be played between a human and computer program.
    Objective: Discard your whole hand of cards, so that you have no cards left.
            Players can discard by matching the card @ the top of the discard pile to a suit/face in your hand.
            If you do not have any matching cards, then you must draw a card from the deck.
            If you have an '8', you can change the suit of the card.
            First player to have no cards wins.
            
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
        p_hand: (list): empty list (of where player's 7 cards will be stored).
        computer_hand (list): empty list (of where computer's 7 cards will be stored).
        discarded (tuple): Cards that the players will discard into a pile. 
            It will only consist of one card, the most recently 'popped' card from either player or computer hands.
            Default to empty str.
        suit_change (str): empty str of where the new suit in the Crazy Eight's game will be specified.
            The suit is chnaged in cases where a player might play a number, for example an 8,
            which allows the player to change the suit for the next turn.
    """

    def __init__(self, name):
        """ Initializes all attributes pertinent to the game.
        
        Args:
            Name(str):name of the player to be used throughout the game.   
        """
        
    def card_dealer(self):
        """ Assigns cards from deck to player and computer hands. Each receive 7 cards.
            Creates the discard pile.
            
        Side Effects:
            shuffles self.deck
            modifies self.p_hand, self.computer_hand, self.discarded.       
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
            Options:
                    - If the player didn't input a number
                    - If the player inputted a number larger than they have in their hand (doesn't exist)
                    - If the player plays an 8, they are able to change the suit
                    - If the player changes the suit, put down a card that matches
                    - A "normal" turn: The player plays a card in their hand that matches the suit or face.
            
        Args:
            selected_card(str): the card the player chooses to add to the discard pile. 
                                ex: 3 for 3rd card
            
        Returns:
            (boolean): True if player performs a valid action, False if player performs an invalid action.
            
        Side Effects:
            May change the top card of the discard pile.
        """
       # If there is no suit change needed, allow regular discard (of suit or face)
        if self.suit_change is '':
            # if the suit in the selected card equals the suit or face equals the face
            if self.p_hand[int(selected_card)-1][0] == self.discarded[0] or self.p_hand[int(selected_card)-1][1] == self.discarded[1]:
                # add to top of discard pile
                self.discarded.append(self.p_hand.pop(int(selected_card)-1))
                print(f"You drew: {self.p_hand[int(selected_card)-1]}")
                return True
            else:
                print("You need to match discard pile card suit or rank. Please choose a different card.")
                return False
        # If the player plays an '8', change the suit
        if self.p_hand[int(selected_card)-1][1] == '8':
            self.discarded = self.p_hand.pop(int(selected_card)-1)
            self.suit_change= ''
            print(f"Suit is {self.discarded}.")
            print("What do you want to do?")
            while self.suit_change not in ['Heart','Diamond','Spade','Club']:
                self.suit_change = input("Please enter a new suit: Heart, Diamond, Spade, Club.")
            print(f"New suit is: {self.suit_change}")
            return True
        # If the suit is changed
        if self.suit_change is not '':
            # if the suit in the selected card equals the suit
            if self.p_hand[int(selected_card)-1][0] == self.suit_change:
                # add to top of discard pile
                self.discarded.append(self.p_hand.pop(int(selected_card)-1))
                # reset suit change
                self.suit_change = ''
                return True
            else:
                print("You need to match the changed suit. Please choose a different card to discard.")
                return False
        # If the user does not input a number, return false
        if selected_card.isdigit() is False:
            return False
        # If the user inputs a number greater than the amount in their hand, return 0
        if len(self.p_hand) < int(selected_card):
            print("The number of card entered is greater than number of cards in your hand! Please choose a different card.")
            return False
   
    def player_turn(self):
        """ Allows the player to perform their turn: choose a new card from the discard pile, 
            or enter the number of the card they want to discard.
            Will either append card to p_hand or place a card on top of the discard pile.
            
        Returns: 
            (str): "You have no more cards!" 
            (str): "The deck has no more cards!"
            computer_turn: if the player has completed their turn.
        """
        print("It's your turn to play!")
        # player needs to enter whether need a new card or which card they want to discard
        selected_card = input("Enter 'new' if you need to draw from the discard pile. \n OR \n Enter the # of card from your hand to discard.")
        # as long as there are cards in the deck
        while len(self.deck) > 0:
            print(f"Current discard pile is: \n {self.discarded}")
            print(f"Your current hand is: \n {self.p_hand}")
            # if player asks for new card
            if selected_card == 'new':
                # take card from deck and add to hand
                self.p_hand.append(self.deck.pop())
            else:
                # calls player_options to run through chosen card
                self.player_options(selected_card)
        # if the player has no cards left
        if len(self.p_hand) is 0:
            print("You have no more cards!")
        # if there are no more cards in the deck
        if len(self.deck) is 0:
            print("The deck has no more cards!")
        else:
            # once player turn is finished, call computer turn
            self.computer_turn()
            
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
        """ Allows the player to perform their turn: choose a new card from the discard pile, or enter the number of the card they want to discard.
            Will either append card to p_hand or place a card on top of the discard pile.
        
        Returns:
            (str): "You have no more cards!" 
            (str): "The deck has no more cards!"
            player_turn: if the computer has finished its turn
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



