# Programmers: Dagmawit Asfaw, Aaron Rapaka, Fernando Sierra, Sydney Small

from crazyeights import Game
import pytest

def test_init():
    g = Game()
    assert isinstance(g.suit, list), "The suit attribute should be a list of suit."
    assert len(g.suit) == 4, "There should be 4 suit."
    for suit in g.suit:
        assert isinstance(suit, str), "Each suit should be a string."
    assert isinstance(g.faces, list), "The faces attribute should be a list of faces."
    assert len(g.faces) == 13, "There should be 13 faces."
    for face in g.faces:
        assert isinstance(face, str), "Each face should be a string."
    assert isinstance(g.value, int), "The value attribute should be an integer."
    assert isinstance(g.deck, list), "The deck should be a list."
    for card in g.deck:
        assert isinstance(card, tuple), "The deck should hold cards as tuples."
    assert len(g.deck) == 52, "The deck should hold 52 cards."
    assert len(g.p_hand) == 0, "Player hand should have no objects."
    assert len(g.c_hand) == 0, "Computer hand should have no objects."
    assert len(g.discarded) == 0, "The discard pile should have no objects."
    
def test_card_value():
    g = Game()
    assert g.card_value('8') == 50
    assert g.card_value('K') == 10
    assert g.card_value('J') == 10
    assert g.card_value('Q') == 10
    assert g.card_value('A') == 10
    assert g.card_value('2') == 2
    assert g.card_value('3') == 3
    assert g.card_value('4') == 4
    assert g.card_value('5') == 5
    assert g.card_value('6') == 6
    assert g.card_value('7') == 7
    assert g.card_value('9') == 9
    assert g.card_value('10') == 10
    
def test_computer_options():
    g = Game()
    ################################################################################
    g.suit = ['Diamond']
    g.suit_change = 'Spade'
    g.c_hand = [('Spade', '2'), ('Heart', '9'), 
                 ('Club', '8'), ('Heart', '4')]
    g.deck = [('Spade', 'Q'), ('Diamond', '9')]
    ################################################################################
    #If the numbers match
    g.discarded = ('Diamond', '4')
    g.computer_options()
    assert g.discarded == ('Heart', '4')
    ################################################################################
    #If Suits match 
    g.discarded = ('Spade', '4')
    g.computer_options()
    assert g.discarded == ('Spade', '2')
    ################################################################################
    #If computer discards 8. It should automatically 
    #change the suit, and the number will remain 8
    g.discarded = ('Club', '4')
    g.computer_options()
    assert g.discarded == ('Diamond', '8')
    ################################################################################
    # If Player changes suit to Spade
    g.discarded = ('Heart', '8')
    g.computer_options()
    #Must be drawn from deck, since spade was discarded in previous assertion
    assert g.discarded == ('Spade', 'Q')
    ################################################################################
    # If the computer must draw from deck
    g.discarded = ('Diamond', 'K')
    g.computer_options()
    assert g.discarded == ('Diamond', '9') 

def test_card_dealer():
    g = Game()
    g.card_dealer()
    
    # hands have 7 cards each
    assert len(g.p_hand) == 7
    assert len(g.c_hand) == 7
    
    # check the total deck is 38 (means cards have been added to the hands)
    assert len(g.deck) == 38
    
    # There should be a card in the discard pile
    assert g.discarded is not None
    
    # the deck should be made of cards as tuples
    for card in g.deck:
        assert isinstance(card, tuple)
        
    # last card in deck should be the top of the discard pile
    assert g.deck[0] == g.discarded
