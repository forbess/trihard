import random

class DiceRolling:
	x = 1
	def __init__(self):
		print("Welcome to dice rolling program.\n")
	def rollDice(self):
		self.x = 1
		while True:
				try:
					while self.x == 1:
						print("STATUS: Rolling dice...")
						self.randNumber = random.randint(1,6)
						print("STATUS: You rolled '{0}'".format(self.randNumber))
						input(" --> Press enter to re-roll.\n")

				except:
					print("\nERROR.RESTARTING...\n")

diceRoll = DiceRolling()

if __name__ == '__main__':
	diceRoll.rollDice()