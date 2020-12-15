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