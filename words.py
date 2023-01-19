from pyfiglet import figlet_format

title = figlet_format("Hangman", font = "slant")

phrases = ["PIECE OF CAKE", "SPILL THE BEANS", "WILD GOOSE CHASE", 
"A PENNY FOR YOUR THOUGHTS", "A BLESSING IN DISGUISE", "THIRD TIME'S A CHARM"]
places = ["THE GREAT WALL OF CHINA", "THE WHITE HOUSE", "THE BUCKINGHAM PALACE", 
"GREAT PYRAMID OF GIZA", "STATUE OF LIBERTY", "PUERTO PRINCESA"]
movies = ["THE TEXAS CHAINSAW MASSACRE", "NIGHTMARE ON ELM STREET", "CHUCKY", 
"NIGHT OF THE LIVING DEAD", "EVIL DEAD", "THE THING"]

intro = '''Let's play a game called Hangman, shall we?
The rules are simple:...
You have to guess the word by choosing the correct letters.
You have 10 seconds to choose a letter.
To make this game more interesting, you can only have 5 mistakes... 
or else it's game over for your friend over here.
Game's simple, am I right?
But choose a letter carefully 'cause your friend's life is on the line.
Don't leave your friend................ HANGING'''

hangman = ['''
   +---+
       |
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
       |
      ===''']