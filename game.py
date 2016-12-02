import random


class Game:

	def __init__(self):
		self.current_word = ""
		self.pattern = []

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
				return
			elif (choice == 2):
				break
	
	def load_random_word(self):

		dictionary = 'dictionary.dat'

		try:
			with open(dictionary, 'r') as fp:
				all_words = fp.readlines()
				all_words = [word[:-1] for word in all_words]
				random_word = all_words[random.randint(0, len(all_words)-1)]
				if (len(random_word) < 4):
					while(True):
						random_word = all_words[random.randint(0, len(all_words)-1)]
						if ((self.check_word_in_guessed_words(random_word) == True) or (len(random_word) < 4)):
							random_word = all_words[random.randint(0, len(all_words)-1)]
							continue
						break
				return random_word
		except IOError:
			print ("\nCould not open the file {}\n".format(dictionary))
			return

	def check_word_in_guessed_words(self, random_word):

		guessed_words = 'guessedwords.dat'

		try:
			with open(guessed_words, 'r') as fp:
				all_words = fp.readlines()
				all_words = [word[:-1] for word in all_words]
				if (random_word in all_words):
					return True
				return False
		except IOError:
			print ("\nCould not open the file {}\n".format(guessed_words))
			return
    
	def start_game(self):
    	
    		random_word = self.load_random_word()
    		word_size = len(random_word)
    		
    		print (len(random_word))

    		self.current_word = random_word
    		print(random_word)
    		self.pattern = list(word_size*'_')[:-1]
    		print (len(self.pattern))
    		
    		while(True):
    			print ("\n")
    			self.display_word(self.pattern)
    			letter = raw_input("\nEnter a letter: ")
    			self.check_letter_in_word(letter, random_word)	
    			print ("\n")	

	def check_letter_in_word(self, letter, word):
    		
    		if letter in word:
    			self.replace_letter_in_word(letter, word)


	def replace_letter_in_word(self, letter, word):	
		
		for index in range(0, len(word)):
				if letter == word[index]:
					self.pattern[index] = letter    			



	def display_word(self, pattern):
    		
   			#pattern_size = len(pattern)
   			print (self.pattern)
   			print (''.join(self.pattern))
   			
   			# for i in range(1, pattern_size):
   			# 	underscore += '_'
   			# print (underscore)




def main():

	game = Game()
	game.display_menu()
	

if __name__ == "__main__":
	main()	
