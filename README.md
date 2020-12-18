# 326-Final-Project

### **Files**:

**crazyeights.py**: Main program that runs the crazy eights game. The user plays the game with this script.
          
**test_crazyeights.py**: Script that tests crazy eights program functions/methods.
      
### **Command Line Instructions:**
Use "python3 crazyeights.py" for Mac
             **OR**
"python crazyeights.py" for Windows.

### **Crazy Eights Instructions:**
The game will ask you to input your **player name**.

Then, it will lay out your hand of cards, as well as the card at the top of the discard pile.

You must match either the **suit** or **face** of the card on top of the discard pile.

Or, if you have an **'8'**, you can change the suit to be your liking at any time. 
You must put down a card that matches the suit you changed to.

To run the program and complete these actions, you either input into the terminal:

         the number of the card in your hand that you want to discard,
         
         "new" if you need a new card (e.g. if you have no cards that match),
         
                  ex: input "3" if you want to discard the 3rd card in your hand
                  
         "help" if you do not know what to do (it will give you a hint!),
         
         or "exit" if you no longer want to play.
         
You will play until the deck, the compupter, or you run out of cards. The aim of the game is to 
strategically put down cards in your hand that amtch either the suit or the face of the card on 
top of the discard pile. You want to get rid of your cards in as little turns as possible.

To win, you must get rid of your cards before the computer does.

### **Annotated Bibliography**

**gofish.py**:

We used this script as an inspiration for our script. It was useful to gain a general understanding 
of how a card game should be laid out and structured in a python program. We did not take anything 
specific from the script, rather we split our program up similarly. We decided to have "turn" methods 
and set similar conditions to "while the deck still has cards in it, perform these actions".

**cards.py**

While we decided to initialize our cards/deck differently than this script, it was helpful to realize 
that we needed suit, value, and face attributes to create the deck of cards. The shuffle and pop methods 
used in this script came in handy for our program, especially when creating the deck, as well as taking 
cards from the computer and player hands and adding to the discard pile.

**test_cards.py**

This script was useful in creating our test script. This script exemplifies the "assert", "hasattr", 
"isinstance", and "len" methods that are helpful in creating our test functions that deal with cards 
as well.

**https://www.w3schools.com/python/python_ref_functions.asp**

This dictionary of all python's built-in functions was very useful in writing our script. It was very 
useful to refer to when a function was needed in order to perform the goals of our script. We referred 
to this for the "enumerate()", "hasattr()", "input()", "int()", "isinstance()", "len()", "list()", 
"range()" in order to confirm previously used functions were suitable, as well as discovering new functions 
we used for the first time in our program.

**https://docs.python.org/3/library/stdtypes.html**

This python library was also very useful to refer to. Like the w3schools dictionary, this library lists out 
built-in types to python. We had to branch out and find new functions in order to accomplish the program's 
goals, so this reference was key. 

          Ex:

          isdigit(): allowed us to determine whether the player input a number that represents the selected_card
          
          capitalize(): allowed us to make sure there is no error and break in the program if the player does not 
          capitalize the first letter of the suit when changing it. 
          
          extend(): allowed us to have the computer add cards (based on the play_options method the to the end of 
          the current list (computer_hand).
          
**https://www.tutorialsteacher.com/python/random-module**

This website described all of the functions that are imported by the random module. We needed to use the random 
module in order to accomplish goals of our program.

          Ex:

          random.shuffle(): allowed us to shuffle the deck of cards we created to make sure that the cards 
          were not added to the player and computer's hands in order. Simulates a real card shuffle.
          
          random.choice(): allowed us to have the computer run through its turn by itself. Specifically, the 
          random choice allowed the computer to randomly choose a card and randomly choose a suit.

**https://www.tutorialsteacher.com/python/sys-module**

This website also helped us create a safe exit of the program. In our script, the player can input "exit" if 
they want to stop playing the game at any time.

          Ex:
          
          sys.exit(): allowed us to safely exit the program and return to the command line, where the player can 
          fully restart the crazy eights game.

**https://towardsdatascience.com/python-the-boolean-confusion-f7fc5288f0ce**

This website helped us made sure that the number of discarded cards in our test function of card_dealer was not 
empty. 

            Ex:

            The "is not None" was used to make sure the number of discarded cards had value.

**https://www.programiz.com/python-programming/del**
This webste showed how us how to delete all items in a list at once, which was necessary to reset a list in our program.
            Ex:
            del my_list[:]:
                Clears the list of computer's playable options in computer_options(), so 
                that it can be reset for the next turn.
