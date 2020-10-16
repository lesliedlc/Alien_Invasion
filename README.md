Alien Invasion 

- A game created with the Pygame module where a small ship fires bullets at aliens to earn points. 
A score board on the top of the screen keeps track of the ship lifes left, the level, your score, and the high score to beat. 
The ship moves from left to right with the mousepad arrows and shots bullets of three with the spacebar.
Each file creates a class, and the classes are then imported into the main file, alien_invasion. 


EXTRA: 
Definitions

Surface - part of the screen where a game element can be displayed
Event - action a user takes while playing game
Every init method has two parameters, the instance of self and the instance of the Alien invasion game
helper method - indicated by a single leading underscore .... _check
antialiasing makes the edges of the text smoother

Functions

event.get() - returns a list of events that have taken place since the last time the function was called
.bmp files - pygame loads bitmaps by default
get_rect() - access the screens rectangle attributes
super() inherit from sprite which groups elements together and act on all at once
.draw(where to draw it)
floor division // drops remainder
spritecollideany() - two arguments: sprite and group
.font() render text to screen
