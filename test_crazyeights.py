# Programmers: Dagmawit Asfaw, Aaron Rapaka, Fernando Sierra, Sydney Small

from crazyeights import Game
import pytest

def test_init():
    g = Game()
    assert isinstance(g.suits, list), "The suits attribute should be a list of suits."
    assert len(g.suits) == 4, "There should be 4 suits."
    assert isinstance(g.suits[0:], str), "Each suit should be a string."
    assert isinstance(g.faces, list), "The faces attribute should be a list of faces."
    assert len(g.faces) == 13, "There should be 13 faces."
    assert isinstance(g.faces[0:], str), "Each face should be a string."
    assert isinstance(g.value, int), "The value attribute should be an integer."
    assert isinstance(g.deck, list), "The deck should be a list."
    assert isinstance(g.deck[0:], tuple), "The deck should hold cards as tuples."
    for attr in ["suit", "face"]:
        assert hasattr(g.deck[0], attr), "The cards should be a suit, face"
    assert len(g.p_hand) == 0, "Player hand should have no objects."
    assert len(g.computer_hand) == 0, "Computer hand should have no objects."
    assert len(g.discarded) == 0, "The discard pile should have no objects."

def test_card_value():
    g = Game()
    assert g.card_value('1') == 1
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
    assert g.card_value('8') == 8
    assert g.card_value('9') == 9
    assert g.card_value('10') == 10
