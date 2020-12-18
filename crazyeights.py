# Programmers: Dagmawit Asfaw, Aaron Rapaka, Fernando Sierra, Sydney Small

import sys
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
        suits (str): Suits in a normal card deck of Hearts, Diamonds, 
            Spades, and Clubs.
        faces (str): Each number/rank in a normal card deck with the numbers 
            1-10 and "J" for Joker, "K" for King, "Q" for Queen, and "A" for Ace.
        value (int): Empty int, where the values that each rank takes in the 
            Crazy Eight's game with 8s holding a value of 50, 
            Aces, Kings, Queens, and Jokers holding values of 10, 
            and numbers 2-7 holding their real values.
        suit_change (str): empty str of where the new suit in the Crazy Eight's 
            game will be specified. The suit is changed in cases where a player 
            might play a number, for example an 8, which allows the player to 
            change the suit for the next turn.
        deck (list): A list of all possible suits, face combinations from a 
            normal card deck. For example one possible combination would be 
            [(Heart, Q)].
        p_hand: (list): empty list (of where player's 7 cards will be stored).
            c_hand (list): empty list (of where computer's 7 cards will be stored).
        discarded (list): Cards that the players will discard into a pile. 
            It will only consist of one card, the most recently 'popped' card 
            from either player or computer hands. Default to empty str.
        count (int): int defaulted to 0, that keeps track of how many cards are drawn.
        play_options (list): empty list, lists play options of the computer turn.
        
    """
    
    def __init__(self):
        """ Initializes all attributes pertinent to the game.   
            
        """
        self.suit = ['Heart','Diamond','Spade','Club']
        self.faces = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.deck = [(suit,face) for suit in self.suit for face in self.faces]
        self.value = int()
        self.p_hand = []
        self.suit_change = ''
        self.c_hand = []
        self.discarded = []
        self.count= 0 
        self.play_options= []
    
    def card_dealer(self):
        """ Assigns cards from deck to player and computer hands. Each receive 7 cards.
            Creates the discard pile.
            
            Side Effects:
                shuffles self.deck using random method.
                removes cards from the deck.
                adds to self.p_hand, self.c_hand, self.discarded. 
                  
        """ 
    
        random.shuffle(self.deck)
        for card in range(7): 
            self.p_hand.append(self.deck.pop(0))
            self.c_hand.append(self.deck.pop(0))
        discard_card = self.deck[0]
        self.discarded = discard_card
    
    def card_value(self,face):
        """ Assigns card values according to the Crazy Eight's rules (based on faces).
            All number cards have their number = value,
            Jack, Queen, King, Ace = 10,
            and 8 = 50.
        
            Args: 
                face (str): face of the card in the hand
            
            Returns: 
                self.value: value associated with each card in the deck.
        
            Side Effects:
                Changes/gives a value to each face. 
        """
        
        #for face in self.faces:
        if face in ['2','3','4','5','6','7','9','10']:
           self.value = int(face)
        elif face == '8':
            self.value = 50
        elif face in ['J','Q','K','A']:
            self.value = 10
        return self.value

    def player_help(self):
        """ Helps player if they do not know what card to play.
        
            Returns:
                player_turn: to return to the player's actionable turn.
        """
        print(f"\n----You can play a {self.discarded[0]} or a {self.discarded[1]}.----\n")
        return self.player_turn()
    
    def player_options(self, selected_card):
        """ Determines whether the card selected to add to the discard pile is allowed to be chosen 
            as according to Crazy Eight's rules.
            Only a card of the same face or suit can be discarded.
            
            Options:
                    - If the player plays an 8, they are able to change the suit
                    - If the player changes the suit, put down a card that matches
                    - A "normal" turn: The player plays a card in their hand that matches the suit or face.
            
        Args:
            selected_card (str): the card the player chooses to add to the discard pile. 
                                Ex: '3' for the 3rd card in their hand
            
        Returns:
            (boolean): True, if player performs a valid action, 
                       False, if player performs an invalid action.
            
        Side Effects:
            Changes the top card of the discard pile if a discard occurs.
            Changes the suit of the discard pile is an 8 is played.
            Removes cards from player's hand.
            Adds cards to player's hand.
        """
        # If the player plays an '8', change the suit
        if self.p_hand[int(selected_card)-1][1] == '8':
            # tell player what the suit currently is
            print(f"Suit is {self.discarded[0]}.\n")
            # take card from hand and add to discard pile
            self.discarded = self.p_hand[int(selected_card)-1]
            self.p_hand.remove(self.p_hand[int(selected_card)-1])
            # change the suit
            suit_input = input("Please enter a new suit: Heart, Diamond, Spade, Club.\n")
            suit_input = suit_input.capitalize()
            self.suit_change = suit_input
            print(f"New suit is: {self.suit_change}")
            # discard pile is set equal to the suit change, player must put down that suit
            self.discarded = (self.suit_change, '')
            return True
        # if the suit in the selected card equals the suit or face equals the face
        if self.p_hand[int(selected_card)-1][0] == self.discarded[0] or self.p_hand[int(selected_card)-1][1] == self.discarded[1]:
            # add to top of discard pile
            self.discarded = self.p_hand[int(selected_card)-1]
            self.p_hand.remove(self.p_hand[int(selected_card)-1])
            print(f"You played: {self.discarded}\n")
            return True
        else:
            print("You need to match discard pile card suit or rank. Please choose a different card.\n")
            self.player_turn()
            
    def player_turn(self):
        """ Allows the player to perform their turn: choose a new card from the discard pile, 
            enter the number of the card they want to discard, ask for help, or exit the game.
            Will either append card to p_hand or place a card on top of the discard pile.
                
        Side Effects:
            Prints:
                (str): The number of card entered is greater than number of cards in your hand!
                        Please choose a different card.
                (str): "You have no more cards!" 
                (str): "The deck has no more cards!"
                (str): "You chose to stop the game. See you later!"
            May call the player help function.
            Removes card from deck and adds to player's hand.
            Ends the game if no more cards.
            Calls the computer's turn.
            
        """
        selected_card = str()
        print("It's your turn to play!\n")
        # player needs to enter whether they need a new card or which card they want to discard
        while len(self.deck) > 0:
            print(f"Current discard pile is: \n {self.discarded}\n")
            print("Your current hand is:\n")
            for index, card in enumerate(self.p_hand):
                print(f"Card #{index+1}: {card}")
            print("\n")
            selected_card = input("Enter the # of card from your hand to discard\n\
                ----OR----\nEnter 'new' if you need to draw a card\n\
                ----OR----\nEnter 'help' if you need a tip\n\
                ----OR----\nEnter 'exit' if you want to end the game:\n")
            if selected_card.isdigit():
                if len(self.p_hand) < int(selected_card):
                    print("\nThe number of card entered is greater than number of cards in your hand! \nPlease choose a different card.\n")
                    continue
            if selected_card == 'help':
                self.player_help()
                break
            if selected_card == 'exit':
                sys.exit('\nYou chose to stop the game. See you later!\n')
            # if player asks for new card
            if selected_card == 'new':
                # take last card from deck and add to hand
                card = self.deck[-1]
                self.p_hand.append(card)
                self.deck.remove(card)
            else:
                # calls player_options to run through chosen card
                self.player_options(selected_card)
                break
        # if the player has no cards left
        if len(self.p_hand) == 0:
            print("You have no more cards!")
            return self.winner
        # if there are no more cards in the deck
        elif len(self.deck) == 0:
            print("The deck has no more cards!")
            return self.winner
            
    def computer_options(self):
        """ Selects card for the computer to play according to Crazy Eight's rules.
            Only a card of the same face or suit can be discarded. If an 8 is played,
            a new suit can be chosen by the computer for future rounds.
            
            Side Effects:
            Changes the top card of the discard pile if a discard occurs.
            Removes cards from computer's hand.
            Adds cards to computer's hand.
            
            """
        # Top card in the discard pile
        last= self.discarded
        # Sorts computer hand to find only cards that can legally be played.
        # Sorted cards are appended to play_options list
        for card in self.c_hand:
            # If human player discards an 8
            if last[1] == '8':
                # If the computer has another 8 to play
                if card[1] == last[1]:
                    self.play_options.append(card)
                    self.c_hand.remove(card)
                # If the computer has cards of the new suit
                if card[0] == self.suit_change:
                    self.play_options.append(card)
                    self.c_hand.remove(card)
            else:
                # If the computer has cards of the same suit
                if card[0] == last[0]:
                    self.play_options.append(card)
                    self.c_hand.remove(card)
                # If the computer has cards of the same number
                if card[1] == last[1]:
                    self.play_options.append(card)
                    self.c_hand.remove(card)
                    
        if len(self.play_options) > 0:
            discarded_card = random.choice(self.play_options)
            self.play_options.remove(discarded_card)
            # If computer discards an 8
            if discarded_card[1] == '8':
                # New suit is randomly picked
                new_suit=random.choice(self.suit)
                print(f"The computer played a CRAZY EIGHT!! \nNew suit is: {new_suit}")
                self.discarded = (new_suit, str())
            else:
                # Places card in discard pile
                self.discarded = discarded_card
            self.c_hand.extend(self.play_options)    
            del self.play_options[:]
        else:
            self.c_draw_count()

    def c_draw_count(self):
        """ Counts the cards drawn by the computer.
        
            Side Effects:
                Removes card from deck.
                Adds card to deck.
                Updates the count.
        """
        while len(self.play_options) == 0 and len(self.deck) > 0:
            self.c_hand.append(self.deck.pop(0))
            self.count +=1
            self.computer_options()
            break
            
    def computer_turn(self):
        """ Allows the computer to perform its turn by drawing the number of cards necessary,
        and shuffling the discard pile to keep going if there are no more cards.
            
        Side Effects:
            Prints:
                (str): "The computer has no more cards!" 
            Removes card from deck and adds to the computer's hand.
            Ends the game if no more cards -- calling the winner.
            Calls the player's turn.
            
        """
        print("It's the computer's turn to play !")
        while len(self.deck) > 0:
            self.computer_options()
            break
        self.count = 0
        print(f"The computer drew {self.count} card(s).\n")
        if len(self.deck) == 0:
            print("The deck is out of cards.\n")
            return self.winner
        elif len(self.c_hand) == 0:
            print("The computer has no more cards!\n")
            return self.winner
    
    def winner(self):
        """ Calculates the points as according to the Crazy Eight's rules.
            Adds the values of the cards in player and computer hands.
            The player who reaches 0 cards first wins,
            then their points are added.
            
        Side Effects:
            Prints:
                p_points (int): # of points the player has @ end of game.
                c_points (int): # of points the computer scored @ end of game.
            Changes point values.
            
        """
        #Assign player and computer points to empty integers.
        p_points = int()
        c_points = int()
    
        #Update player points and computer points according to each cards value.
        for face in self.p_hand:
            p_points += self.card_value(face[1])
        for face in self.c_hand:
            c_points += self.card_value(face[1])
    
        #if the player gets down to 0 cards, the player wins.
        if len(self.p_hand) == 0: 
            print("You win since you reached 0 points! :)")
            print(f"The computer still had {c_points} points and {len(self.c_hand)} cards left.")
            
        # if the computer gets down to 0, the computer wins.
        elif len(self.c_hand) == 0:
            print("The computer wins since it reached 0 points. :(")
            print(f"You still had {p_points} points and {len(self.p_hand)} cards left.")

def main():
    
    print("------------------------------*Game*------------------------------")
    game = Game()
    player_name = input("Please enter your player name: \n")
    print("------------------------------------------------------------")
    print(f"\nWelcome, {player_name}!\n")
    
    game.card_dealer()
    while len(game.p_hand) and len(game.c_hand) > 0:
        game.player_turn()
        game.computer_turn()
        if len(game.deck) or len(game.p_hand) or len(game.c_hand) == 0:
            game.winner()
            
if __name__ == "__main__":
    main()
  
    
    # python3 crazyeights.py