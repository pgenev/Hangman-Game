Hangman Game
========================

We're going to implement the game of hangman, that we can play against the computer.

Rules
------------

1. The word should be displayed with "_" in place of each letter.
2. The player should guess a letter.
3. If the letter is in the list of all letters, the letter should be removed from the list, so that the user can not guess it second time.
4. If the letter is in the word, then the corresponding "_" should be replaced with the letter, and we should store how many correct guesses the player has had.
5. If the letter is not in the word (and not already guessed), then next stage of the gallows is drawn.
6. The player should be asked for another letter.
5. The game ends when the last stage of the gallows has been drawn (user looses)  or all the letters in the word have been guessed (the user wins).

Additional notes
------------

A. Use provided "dictionary.dat" and choose a random word from that file. Discard all the words shorter than 4 letters. </br>
B. Optionally the minimum length of the word (>=4) can be provided using command line argument. </br>
C. Use gallows ASCII art from provided file "gallows.dat" to draw each stage of the gallows. Please note that the gallows is mirror image. You have to correct this while drawing the gallows. </br>
D. Store each guessed word in file "guessedwords.dat" and never play with this word again. </br>
E. Use dynamic linked list for the list of letters. </br>
F. Note some words in the dictionary are names therefore starting with capital letters but the game should not be case sensitive. So "A = a", "B = b" etc.


