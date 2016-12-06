import random

class Game:

	def __init__(self):
		self.dictionary = 'dictionary.dat'
		self.guessed_words = 'guessedwords.dat'
		self.gallows = 'gallows.dat'
		self.current_random_word = ""
		self.pattern = []
		self.used_letters = []
		self.next_drawing = 0
		self.new_game = False

	def display_menu(self):

		while(True):
			print ("\n------->Hangman Game<-------\n")
			print ("1. Start Game")
			print ("2. Exit\n")

			choice = input("Enter your choice: ")
			print ("----------------------------")
			
			try:
				choice = int(choice)
			except ValueError:
				print ("\nPlease enter an integer!\n")
				continue

			if (choice not in [1,2]):
				print ("\nPlease enter a valid choice!\n")
				continue
			elif (choice == 1):
				self.start_game()
				if (self.new_game == True):
					continue
				break
			elif (choice == 2):
				break
	
	def load_random_word(self):

		try:
			with open(self.dictionary, 'r') as fp:
				all_words = fp.readlines()
				all_words = [word[:-1] for word in all_words]
				random_word = all_words[random.randint(0, len(all_words)-1)]
				if (len(random_word) < 4):
					while(True):
						random_word = all_words[random.randint(0, len(all_words)-1)]
						if ((self.word_is_in_guessed_words(random_word) == True) or (len(random_word) < 4)):
							continue
						break
				return random_word
		except IOError:
			print ("\nCould not open the file {}\n".format(self.dictionary))
			return

	def word_is_in_guessed_words(self, random_word):

		try:
			with open(self.guessed_words, 'r') as fp:
				all_words = fp.readlines()
				all_words = [word[:-1] for word in all_words]
				if (random_word not in all_words):
					return False
				return True
		except IOError:
			print ("\nCould not open the file {}\n".format(self.guessed_words))
			return 
    
	def start_game(self):
    		
    		random_word = self.load_random_word()
    		print (random_word)
    		random_word = random_word.lower()
    		word_size = len(random_word)
    		self.current_random_word = random_word
    		self.pattern = list(word_size*'_')
    	
    		while(True):
    			print ("\n")
    			self.display_pattern()
    			letter = input("\nEnter a letter: ")
    			letter = letter.lower()
    			if((letter in self.used_letters) or (self.letter_is_in_word(letter) == False)):
    				self.display_gallows()
    				if(self.next_drawing == 49):
    					print ("\nYou lose!\n")
    					self.repeat_game()
    					break
    			elif (self.letter_is_in_word(letter) == True):
    				self.replace_letter_in_word(letter)
    				self.used_letters.append(letter)
    				if (''.join(self.pattern) == self.current_random_word):
    					self.add_word_to_guessed_words()
    					print ("\nYou won!\n")
    					self.repeat_game()
    					break
    			print ("\n")	

	def letter_is_in_word(self, letter):
    		
    		if letter in self.current_random_word:
    			return True
    		return False


	def replace_letter_in_word(self, letter):	
		
		for index in range(0, len(self.current_random_word)):
				if letter == self.current_random_word[index]:
					self.pattern[index] = letter    			

	def display_pattern(self):

			print (' '.join(self.pattern))
   
	def load_and_reverse_gallows(self):

		try:
			with open(self.gallows, 'r') as fp:
				gallows = fp.readlines()
				for line in gallows:

					line = line[:-1]
					mirror_line = list(line[::-1])

					for char in range(0, len(mirror_line)-1):
							if '/' == mirror_line[char]:
								mirror_line[char] = '\\'
							elif('\\' == mirror_line[char]):
								mirror_line[char] = '/'
					yield ''.join(mirror_line)
		except IOError:
			print ("\nCould not open the file {}\n".format(self.gallows))
			return
   	
	def display_gallows(self):

   		gallows_generator = self.load_and_reverse_gallows()
   		self.next_drawing += 7
   		for i in range(0, self.next_drawing):
   			print (next(gallows_generator))
   	
	def add_word_to_guessed_words(self):

   		try:
   			with open(self.guessed_words, 'a') as fp:
   				fp.write(self.current_random_word+'\n')
   		except IOError:
   			print("\nCould not open the file {}\n".format(self.guessedwords))
   			return

	def repeat_game(self):

		new_game = input("New game y/n? ")
		new_game = new_game.lower()
		if (new_game == 'y'):
			self.new_game = True
			self.current_random_word = ""
			self.pattern = []
			self.used_letters = []
			self.next_drawing = 0
		

