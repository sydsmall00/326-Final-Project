# Programmers: Dagmawit Asfaw, Aaron Rapaka, Fernando Sierra, Sydney Small

import random
from random import shuffle

class Game:
            
    """ A Crazy Eights card game that can be played between a human and computer program.
    Objective: Discard your whole hand of cards, so that you have no cards left.
            Players can discard by matching the card @ the top of the discard pile to a suit/face in your hand.
            If you do not have any matching cards, then you must draw a card from the deck.
            If you have an '8', you can change the suit of the card.
            First player to have no cards left wins.
            
    Attributes:
        suits (str): Suits in a normal card deck of Hearts, Diamonds, Spades, and Clubs.
        faces (str): Empty string where each number/rank in a normal card deck with the numbers 1-10 and 
            "J" for Joker, "K" for King,"Q" for Queen, and "A" for Ace.
        value (str): Empty string where the values that each rank takes in the Crazy Eight's game with 8s holding
            a value of 50, Aces, Kings, Queens, and Jokers holding values of 10, and numbers 2-7
            holding their real values.
        deck (list): A list of all possible suit, face combinations from a normal card deck.
            For example one possible combination would be[(Heart, Q)].
        p_hand: (list): empty list (of where player's 7 cards will be stored).
        computer_hand (list): empty list (of where computer's 7 cards will be stored).
        discarded (list): Cards that the players will discard into a pile. 
            It will only consist of one card, the most recently 'popped' card from either player or computer hands.
            Default to empty str.
        suit_change (str): empty str of where the new suit in the Crazy Eight's game will be specified.
            The suit is chnaged in cases where a player might play a number, for example an 8,
            which allows the player to change the suit for the next turn.
            
    """

    def __init__(self):
        """ Initializes all attributes pertinent to the game.   
            
        """
        self.suits = ['Heart','Diamond','Spade','Club']
        self.faces = ''
        self.value = ''
        self.deck = [(suit,face) for suit in self.suits for face in self.faces]
        self.p_hand = []
        self.computer_hand = []
        self.discarded = []
        self.suit_change = ''
    
    def card_value(self):
        """ Assigns card values according to the Crazy Eight's rules (based on faces).
            All number cards have their number = value,
            Jack, Queen, King, Ace = 10,
            and 8 = 50.
        
        Returns: values associated with each card in the deck.
        
        """

        #Assign faces to values
        if self.faces == '2':
            self.value = self.faces 
        if self.faces == '3':
            self.value = self.faces
        if self.faces == '4':
            self.value = self.faces
        if self.faces == '5':
            self.value = self.faces
        if self.faces == '6':
            self.value = self.faces
        if self.faces == '7':
            self.value = self.faces
        if self.faces == '8':
            self.value = '50'
        if self.faces == '9':
            self.value = self.faces
        if self.faces == '10':
            self.value = '10'
        if self.faces == 'A':
            self.value = '10' 
        if self.faces == 'K':
            self.value = '10' 
        if self.faces == 'Q':
            self.value = '10' 
        if self.faces == 'J':
            self.value = '10'    
    
    def card_dealer(self):
        """ Assigns cards from deck to player and computer hands. Each receive 7 cards.
            Creates the discard pile.
            
        Side Effects:
            shuffles self.deck
            modifies self.p_hand, self.computer_hand, self.discarded. 
                  
        """
        new_card=shuffle(self.deck)
        for card in new_card:
            if len(self.p_hand) <= 7:
                self.p_hand.append(card.pop())
                self.computer_hand.append(card.pop())
        self.discarded = self.deck.pop()
        
    def player_options(self, selected_card):
        """ Determines whether the card selected to add to the discard pile is allowed to be chosen 
            as according to Crazy Eight's rules.
            Only a card of the same face or suit can be discarded.
            Options:
                    - If the player didn't input a number
                    - If the player inputted a number larger than they have in their hand (doesn't exist)
                    - If the player plays an 8, they are able to change the suit
                    - If the player changes the suit, put down a card that matches
                    - A "normal" turn: The player plays a card in their hand that matches the suit or face.
            
        Args:
            selected_card(str): the card the player chooses to add to the discard pile. 
                                Ex: '3' for the 3rd card in their hand
            
        Returns:
            (boolean): True if player performs a valid action, 
                       False if player performs an invalid action.
            
        Side Effects:
            Changes the top card of the discard pile if a discard occurs.
            Removes cards from player's hand.
            Adds cards to player's hand.
        """
       # If there is no suit change needed, allow regular discard (of suit or face)
        if self.suit_change == '':
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
        if self.suit_change != '':
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
            print("The number of card entered is greater than number of cards in your hand! \n Please choose a different card.")
            return False
   
    def player_turn(self):
        """ Allows the player to perform their turn: choose a new card from the discard pile, 
            or enter the number of the card they want to discard.
            Will either append card to p_hand or place a card on top of the discard pile.
            
        Returns: 
            (str): "You have no more cards!" 
            (str): "The deck has no more cards!"
            computer_turn: if the player has completed their turn.
            
        Side Effects:
            Removes card from deck and adds to player's hand.
            Ends the game if no more cards.
            Calls the computer's turn.
            
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
        if len(self.p_hand) == 0:
            print("You have no more cards!")
        # if there are no more cards in the deck
        if len(self.deck) == 0:
            print("The deck has no more cards!")
        else:
            # once player turn is finished, call computer turn
            self.computer_turn()
            
    def computer_options(self):
        """ Selects card for the computer to play according to Crazy Eight's rules.
            Only a card of the same face or suit can be discarded. If an 8 is played,
            a new suit can be chosen by the computer for future rounds.
            
            Parameters:
                last(tuple): Top card of the discard pile
                play_options(list): Options for the computer to choose from
                discarded_card(tuple): Card that is discarded by the computer
            
            Side Effects:
            Changes the top card of the discard pile if a discard occurs.
            Removes cards from computer's hand.
            Adds cards to computer's hand.
            
            """
        #Top card in the discard pile
        last= self.discarded[-1]
        #A list of cards that the computer can legally discard
        play_options=[]
        
        #Sorts computer hand to find only cards that can legally be played.
        #Sorted cards are appended to play_options list
        for card in self.computer_hand:
            #If human player discards an 8
            if last[1] == '8':
                #If the computer has another 8 to play
                if card[1] == last[1]:
                    play_options.append(card)
                #If the computer has cards of the new suit
                if card[0] == self.suit_change:
                    play_options.append(card)
            else:
                #If the computer has cards of the same suit
                if card[0] == last[0]:
                    play_options.append(card)
                #If the computer has cards of the same number
                if card[1] == last[1]:
                    play_options.append(card)
                    
        #Deletes any possible repeating cards
        play_options=list(dict.fromkeys(play_options))
        #Randomly selects a card to discard from play_options
        discarded_card = random.choice(play_options)

        #Places card in discard pile
        self.discarded.append(discarded_card)

        #If computer discards an 8
        if discarded_card[1] == '8':
            #New suit picked
            new_suit=random.choice(self.suits)
            print(f"New suit is: {new_suit}")
        
    def computer_turn(self):
        """ Allows the computer to perform its turn by drawing the number of cards necessary,
        and shuffling the discard pile to keep going if there are no more cards.
 
        Returns:
            (str): "The computer has no more cards!" 
            calculator(): If the computer has run out of cards
            player_turn: if the computer has finished its turn
            
        Side Effects:
            Removes card from deck and adds to the computer's hand.
            Ends the game if no more cards -- calling the calculator.
            Calls the player's turn.
            
        """
        discard = 0
        print("It's the computer's turn!")
        count = 0
        while len(self.deck) > 0:
            #print("Computer's faces: ", self.computer_hand)
            print("Discard pile: ", self.discarded)
            self.computer_options()
            if discard == 0:
                self.computer_hand.append(self.deck.pop())
                count +=1
            self.computer_options()
        print(f"The computer drew {count} cards")
        if len(self.computer_hand) == 0:
            print("The computer has no more cards!")
            return self.calculator()
        else:
            self.player_turn()
            
    def calculator(self):
        """ Calculates the points as according to the Crazy Eight's rules.
            Adds the values of the cards in player and computer hands,
            whoever's is lowest (0) wins.
            
        Returns: 
            winner(str): the winner of the game (whoever has zero or lowest score).
            player_points(int): # of points the player has @ end of game.
            computer_points(int): # of points the computer scored @ end of game.
            
        Side Effects:
            Changes point values.
            
        """
        #Assign player and computer points to empty integers.
        player_points = int()
        computer_points = int()
        
        #Update player points and computer points according to each cards value.
        for card in self.p_hand:
            player_points += self.card_value()
        for card in self.computer_hand:
            computer_points += self.card_value()
            
        #if the player gets down to a score of 0 first, the player wins.
        if player_points == 0:
            print("You win! :)")
            print(f"You totaled {player_points} points.")
            print(f"The computer totaled {computer_points} points.")
            
        #if the computer gets down to a score of 0 first, the computer wins.
        elif computer_points == 0:
            print("The computer wins. :(")
            print(f"You totaled {player_points} points.")
            print(f"The computer totaled {computer_points} points.")  
                    
    def start(self):
        """ Starts functions required to play Crazy Eight's program.
        
        """
        player_name = input("Please enter your player name.")
        print(f"Welcome, {player_name}!")
        self.card_dealer()
        self.player_turn()
        self.calculator()
    
# Call class and function to start
import crazyeights
Game()

