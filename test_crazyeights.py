# Programmers: Dagmawit Asfaw, Aaron Rapaka, Fernando Sierra, Sydney Small

import pytest
from crazyeights import Game

#def test_player_options():
    # test whether the player hand is a list
 #   assert isinstance(self.p_hand, list), "Player hand should be a list."
    # test whether the discard pile is displaying a card
  #  assert len(self.discarded) > 0, "Discard pile has cards to play with."
    # test selected card is either new card or number of card to be discarded
  #  assert isinstance(selected_card, int or str)
    # test if a player plays an 8 that the suit has changed
  #  assert 
    # test if the suit is changed that it is not changed after player turn
  #  assert
    
def test_calculator():
    # instantiate class
    calculator = Game()
    # test if player_points, computer_points, and self.value are integers
  #  assert isinstance(player_points, int)
     #   "Player points of Game should be an integer"
   # assert isinstance(computer_points, int), \
      #  "Computer points of Game should be an integer"
    #assert isinstance(self.value, int), \
       # "self.value attribute of Game instance should be an integer"
    #test calculation of points
    assert calculator('10', '5') == 15
    assert calculator('K', '8') == 60
    assert calculator('Q', '9') == 19
    assert calculator('A', '3') == 13               
    