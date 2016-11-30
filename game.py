import random


GUESSED_WORDS = []

class Game:

	def __init__(self):
		pass

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
				self.load_random_word()
				return
			elif (choice == 2):
				break
	
	def load_random_word(self):

		dictionary = 'dictionary1.dat'

		try:
			with open(dictionary, 'r') as fp:
				all_words = fp.readlines()
				random_word = all_words[random.randint(0, len(all_words)-1)]
				if (len(random_word) < 4):
					while(True):
						random_word = all_words[random.randint(0, len(all_words)-1)]
						if ((random_word in GUESSED_WORDS) or (len(random_word) < 4)):
							random_word = all_words[random.randint(0, len(all_words)-1)]
							continue
						break

				print (random_word)
		except IOError:
			print ("\nCould not open the file {}\n".format(dictionary))
			return
                # print (len(all_words))
                # print (random.randint(0, len(all_words)-1))
                # print (all_words[61405])
                # return




def main():

	game = Game()
	game.display_menu()
	#game.load_random_word()

if __name__ == "__main__":
	main()	
