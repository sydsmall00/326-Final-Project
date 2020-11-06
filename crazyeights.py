# Programmers: Dag Asfaw, Aaron Rapaka, Fernando Sierra, Sydney Small

from random import shuffle
            
class Game:
    
    def __init__(self, name):
        """ Initializes all attributes pertinent to the game.
            
            Attributes:
                suits (str): Suits in a normal card deck.
                faces (str): Each number/rank in a normal card deck.
                value (int): The values that each rank takes in the Crazy Eight's game.
                deck (list): A list of all possible suit, face combinations from a normal card deck.
                player_hand: (list): empty list (of where player's 7 cards will be stored).
                computer_hand (list): empty list (of where computer's 7 cards will be stored).
                discard_pile (int): default to 0
                suit_change (str): empty str (of where the new suit in the Crazy Eight's game will be specified.)
            """
        self.suits = ['Heart','Diamond','Spade','Club']
        self.faces = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.value = [2, 3, 4, 5, 6, 7, 50, 9, 10, 10, 10, 10, 10]
        self.deck = [(suit,face) for suit in self.suits for face in self.faces]
        self.player_hand = []
        self.computer_hand = []
        self.discard_pile = 0
        self.suit_change = ''
    
    def card_dealer(self):
        """ Assigns cards from deck to player and computer hands. Each receive 7 cards.
            Creates the discard pile.
            """
        shuffle(self.deck)
        for card in range(7):
            self.player_hand.append(self.deck.pop())
            self.computer_hand.append(self.deck.pop())
        self.discard_pile = self.deck.pop()
    
    def card_value(self, card):
        """ Assigns card values according to the Crazy Eight's rules (based on faces).
            All number cards have their number = value,
            Jack, Queen, King, Ace = 10,
            and 8 = 50.
            """
        return self.value[self.faces.index(card[1])]
    
    def player_options(self, selected_card):
        """ Determines whether the card selected to add to the discard pile is allowed to be chosen according to Crazy Eight's rules.
            Only a card of the same face or suit can be discarded.
            """
        # If the user does not input a number, return 0
        if selected_card.isdigit() is False:
            return False
        # If the user inputs a number greater than the amount in their hand, return 0
        if len(self.player_hand) < int(selected_card):
            print("The number of card entered is greater than number of cards in your hand! Please choose a different card.")
            return False
        # If the player plays an '8', change the suit
        if self.player_hand[int(selected_card)-1][1] == '8':
            self.discard_pile = self.player_hand.pop(int(selected_card)-1)
            self.suit_change= ''
            while self.suit_change not in ['Heart','Diamond','Spade','Club']:
                self.suit_change = input("Please enter a new suit: Heart, Diamond, Spade, Club.")
            print(f"New suit is: {self.suit_change}")
            return True
        # If the suit change is not empty
        if self.suit_change != '':
            # if the suit in the selected card equals the suit
            if self.player_hand[int(selected_card)-1][0] == self.suit_change:
                # add to top of discard pile
                self.discard_pile = self.player_hand.pop(int(selected_card)-1)
                self.suit_change = ''
                return True
            else:
                print("You need to match the changed suit. Please choose a different card.")
                return False
        # If suit change is empty
        if self.suit_change == '':
            # if the suit in the selected card equals the suit or face equals the face
            if self.player_hand[int(selected_card)-1][0] == self.discard_pile[0] or self.player_hand[int(selected_card)-1][1] == self.discard_pile[1]:
                # add to top of discard pile
                self.discard_pile = self.player_hand.pop(int(selected_card)-1)
                return True
            else:
                print("You need to match discard pile card suit or rank. Please choose a different card.")
                return False
   
    def player_turn(self):
        """ Allows the player to perform their turn. 
            
            """
        selected_card = ''
        discarded = 0
        print("It's your turn!")
        while discarded == 0 and len(self.deck) > 0:
            print("Your cards: ", self.player_hand)
            print("Discard pile: ", self.discard_pile)
            selected_card = input("Please enter 'new card' if you need another card, or enter the number of card you want to discard.")
            if selected_card == 'new card':
                self.player_hand.append(self.deck.pop())
            else:
                discarded = self.player_options(selected_card)
        if len(self.player_hand) == 0:
            print("You have no more cards!")
            return
        elif len(self.deck) == 0:
            print("There are no more cards in the deck!")
            return
        else:
            self.computer_turn()
            
    def computer_options(self):
        """ Determines the card selected is allowed to be chosen according to Crazy Eight's rules.
            Only a card of the same face or suit can be discarded.
            
            """
        
    def computer_turn(self):
        """ Allows the computer to perform its turn. 
        
            """
        discarded = 0
        print("It's the computer's turn!")
        count = 0
        while discarded == 0 and len(self.deck) > 0:
            print("Computer's faces: ", self.computer_hand)
            print("Discard pile: ", self.discard_pile)
            discarded = self.computer_options()
            if discarded == 0:
                self.computer_hand.append(self.deck.pop())
                count +=1
        print(f"The computer drew {count} cards")
        if len(self.computer_hand) == 0:
            print("The computer has no more cards!")
            return
        elif len(self.deck) == 0:
            print("There are no more cards in the deck.")
            return
        else:
            self.player_turn()
            
    def calculator(self):
        """ Calculates the points as according to the Crazy Eight's rules.
            Adds the values of the cards in player and computer hands,
            whoever's is lowest (0) wins.

            """
        player_points = 0
        computer_points = 0
        for card in self.player_hand:
            player_points += self.card_value(card)
        for card in self.computer_hand:
            computer_points += self.card_value(card)
        
        print(f"You totaled {player_points}.")
        print(f"The computer had {computer_points}.")
        if player_points < computer_points:
            print("You win! :)")
        else:
            print("The computer won. :(")   
                
    def start(self):
        """ Starts functions required to play Crazy Eight's program.
        
            """
        self.card_dealer()
        self.player_turn()
        self.calculator()



