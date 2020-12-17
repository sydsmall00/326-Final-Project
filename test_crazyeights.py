# Programmers: Dagmawit Asfaw, Aaron Rapaka, Fernando Sierra, Sydney Small

from crazyeights import Game
import pytest

def test_init():
    g = Game()
    assert isinstance(g.suits, list), "The suits attribute should be a list of suits."
    assert len(g.suits) == 4, "There should be 4 suits."
    for suit in g.suits:
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
    assert len(g.computer_hand) == 0, "Computer hand should have no objects."
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
    g.suits = ['Diamond']
    g.computer_hand == [('Club', '7'), ('Spade', '3'), ('Spade', '8'), ('Heart', '9')]
  
    if g.discarded == ('Spade', '4'): #In the instance where the suits match
        assert g.discarded == ('Spade', '3') or ('Spade', '8')
      
    if g.discarded == ('Diamond', '9'): #In the instance where the numbers match
        assert g.discarded == ('Heart', '9')
      
    if g.discarded == ('Club', '8'): #In the instance where an 8 is played
        assert g.discarded == ('Spade', '8')
        assert print("New suit is: Diamond")
      
    if g.suit_change == "Club": #In the instance where the suit is changed by the player
        assert g.discarded == ('Club', '7')
      
    if g.discarded == ('Diamond', '2'): #In the instance where the computer must draw
        assert g.c_draw_count()

        