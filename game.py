import random


class Game:

	def __init__(self):
		self.current_word = ""
		self.pattern = []
		self.used_letters = []
		self.next_picture = 0

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
    		print (random_word)
    		random_word = random_word.lower()
    		word_size = len(random_word)
    		self.current_word = random_word
    		self.pattern = list(word_size*'_')
    		
    		#print ("random_word length {}".format(len(random_word)))
    		#print(random_word)
    		#print ("pattern length {}".format(len(self.pattern)))
    	
    		while(True):
    			print ("\n")
    			self.display_word()
    			letter = input("\nEnter a letter: ")
    			letter = letter.lower()
    			self.display_gallows()
    			if (self.check_letter_in_word(letter) == True):
    				self.replace_letter_in_word(letter)
    				self.used_letters.append(letter)
    			print ("\n")	

	def check_letter_in_word(self, letter):
    		
    		if letter in self.current_word:
    			return True
    		return False


	def replace_letter_in_word(self, letter):	
		
		for index in range(0, len(self.current_word)):
				if letter == self.current_word[index]:
					self.pattern[index] = letter    			



	def display_word(self):

			print (self.pattern)
			print (' '.join(self.pattern))
   
	def load_and_reverse_gallows(self):

		gallows = 'gallows.dat'

		try:
			with open(gallows, 'r') as fp:
				gallows = fp.readlines()
				for line in gallows:
					line = line[:-1]
					mirror_line = list(line[::-1])

					for char in range(0, len(mirror_line)-1):
							if '/' == mirror_line[char]:
								mirror_line[char] = '\\'
							elif('\\' == mirror_line[char]):
								mirror_line[char] = '/'
					#print ("{}".format(''.join(gallows_miror)))
					yield ''.join(mirror_line)
		except IOError:
			print ("\nCould not open the file {}\n".format(gallows))
			return
   	
	def display_gallows(self):
   		generator = self.load_and_reverse_gallows()
   		self.next_picture += 7
   		print(self.next_picture)
   		for i in range(0, self.next_picture):
   			print (next(generator))
   		
   		#print (','.join(current_line))



def main():

	game = Game()
	game.display_menu()

	

if __name__ == "__main__":
	main()	
