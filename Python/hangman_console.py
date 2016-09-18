import random

class HangMan:

    def __init__(self):
        print("Welcome to console-based Hang Man game! We're asking one of the nine HearthStone heroes! (v1.0)")  
        print("-" * 50) # http://stackoverflow.com/questions/9632995/is-there-a-python-library-that-allows-to-easily-print-ascii-art-text
        print("-" * 50)
        self.lives = 3
        print("--> WARNING: You have {} lives at start.".format(self.lives))
        print("-" * 50)
        self.hearthstoneHeroes = ["Shaman", "Rogue", "Priest", "Mage", "Warlock", "Paladin", "Warrior", "Druid", "Hunter"]
        self.randomLetter = random.choice(self.hearthstoneHeroes)

    def ask(self):
        self.x = 1
        #print("DevCopy: '{}'".format(self.randomLetter))
        self.userAnswer = input("Guess the first letter of random chosen word please: ")
        if (self.userAnswer == self.randomLetter[0]):
            print("--> STATUS: You found it! First letter was '{}'. Moving...".format(self.randomLetter[0]))
            print("-" * 50)
            self.askSecond()
        else:
            print("--> STATUS: You didn't find it! Try Again!")
            print("-" * 50)
            self.lives -= 1
            print("--> WARNING: Lives remaining: {}".format(self.lives))
            if (self.lives == 0):
                print("--> GAME OVER: You are out of lives!. Leaving...")
                print("-" * 50)
                return
            else:
                pass
            print("-" * 50)
            self.ask()
    
    def askSecond(self):
        self.userAnswer2 = input("Guess the second letter of random chosen word please: ")
        if (self.userAnswer2 == self.randomLetter[1]):
            print("--> STATUS: You found it! Second letter was '{}'. Moving...".format(self.randomLetter[1]))
            print("-" * 50)
            self.guessLetter()
        else:
            print("--> STATUS: You didn't find it! Try Again!")
            print("-" * 50)
            self.lives -= 1
            print("--> WARNING: Lives remaining: {}".format(self.lives))
            if (self.lives == 0):
                print("--> GAME OVER: You are out of lives!. Leaving...")
                print("-" * 50)
                return
            else:
                pass
            print("-" * 50)
            self.askSecond()
    
    def askThird(self):
        self.userAnswer3 = input("Guess the third letter of random chosen word please: ")
        if (self.userAnswer3 == self.randomLetter[2]):
            print("--> STATUS: You found it! Third letter was '{}'. Moving...".format(self.randomLetter[2]))
            print("-" * 50)
            self.askFourth()
        else:
            print("--> STATUS: You didn't find it! Try Again!")
            print("-" * 50)
            self.lives -= 1
            print("--> WARNING: Lives remaining: {}".format(self.lives))
            if (self.lives == 0):
                print("--> GAME OVER: You are out of lives!. Leaving...")
                print("-" * 50)
                return
            else:
                pass
            print("-" * 50)
            self.askThird()
    
    def askFourth(self):
        self.userAnswer4 = input("Guess the fourth letter of random chosen word please: ")
        if (self.userAnswer4 == self.randomLetter[3]):
            print("--> STATUS: You found it! Fourth letter was '{}'. Moving...".format(self.randomLetter[3]))
            print("-" * 50)
            if (len(self.randomLetter) >= 5):
                self.askFifth()
            else:
                print("It seems it had 4 letters! So you found it! It was : '{}'. Leaving...".format(self.randomLetter))
                return
        else:
            print("--> STATUS: You didn't find it! Try Again!")
            print("-" * 50)
            self.lives -= 1
            print("--> WARNING: Lives remaining: {}".format(self.lives))
            if (self.lives == 0):
                print("--> GAME OVER: You are out of lives!. Leaving...")
                print("-" * 50)
                return
            else:
                pass
            print("-" * 50)
            self.askFourth()
    
    def askFifth(self):
        self.userAnswer5 = input("Guess the fifth letter of random chosen word please: ")
        if (self.userAnswer5 == self.randomLetter[4]):
            print("--> STATUS: You found it! Fifth letter was '{}'. Moving...".format(self.randomLetter[4]))
            print("-" * 50)
            if (len(self.randomLetter) >= 6):
                self.askSixth()
            else:
                print("It seems it had 5 letters! So you found it! It was : '{}'. Leaving...".format(self.randomLetter))
                return
        else:
            print("--> STATUS: You didn't find it! Try Again!")
            print("-" * 50)
            self.lives -= 1
            print("--> WARNING: Lives remaining: {}".format(self.lives))
            if (self.lives == 0):
                print("--> GAME OVER: You are out of lives!. Leaving...")
                print("-" * 50)
                return
            else:
                pass
            print("-" * 50)
            self.askFifth()

    def askSixth(self):
        self.userAnswer6 = input("Guess the sixth letter of random chosen word please: ")
        if (self.userAnswer6 == self.randomLetter[5]):
            print("--> STATUS: You found it! Sixth letter was '{}'. Moving...".format(self.randomLetter[5]))
            print("-" * 50)
            if (len(self.randomLetter) >= 7):
                self.askSeventh()
            else:
                print("It seems it had 6 letters! So you found it! It was : '{}'. Leaving...".format(self.randomLetter))
                return
        else:
            print("--> STATUS: You didn't find it! Try Again!")
            print("-" * 50)
            self.lives -= 1
            print("--> WARNING: Lives remaining: {}".format(self.lives))
            if (self.lives == 0):
                print("--> GAME OVER: You are out of lives!. Leaving...")
                print("-" * 50)
                return
            else:
                pass
            print("-" * 50)
            self.askSixth()
    
    def askSeventh(self):
        self.userAnswer7 = input("Guess the seventh letter of random chosen word please: ")
        if (self.userAnswer7 == self.randomLetter[6]):
            print("--> STATUS: You found it! Seventh letter was '{}'. Moving...".format(self.randomLetter[6]))
            print("-" * 50)
            print("--> GAME OVER: There is no word has over 7 letters!. So you found it! It was : '{}' Leaving...".format(self.randomLetter))
            return
        else:
            print("--> STATUS: You didn't find it! Try Again!")
            print("-" * 50)
            self.lives -= 1
            print("--> WARNING: Lives remaining: {}".format(self.lives))
            if (self.lives == 0):
                print("--> GAME OVER: You are out of lives!. Leaving...")
                print("-" * 50)
                return
            else:
                pass
            print("-" * 50)
            self.askSeventh()

    def guessLetter(self):
        self.userGuess = input("Do you want to guess the HearthStone hero? Give it a try! (Your lives won't be affected ): ")
        print("-" * 50)
        if (self.userGuess == self.randomLetter):
            print("You found it! Conguratulations! Leaving...")
            print("-" * 50)
            return
        else:
            print("I am sorry, you couldn't guess it. Moving to third letter...")
            print("-" * 50)
            self.askThird()          

class Exit:
    def exit(self):
        raise SystemExit
        #goodbye.

HangManGame = HangMan()

if __name__ == '__main__':
    HangManGame.ask()

    #The end
