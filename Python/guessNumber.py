import random

mainVar = 1

class guessNumber:
    welcome = "Hello"
    def __init__(self):
        self.welcome = "Bonjour!"
        print("{0}\n".format(self.welcome))
    def main(self):
        while mainVar == 1:
            try:
                answer = input("Guess the number I picked between 0 and 10!\n")
                x = random.randint(0,10)
                if int(answer) == x:
                    print("You guessed it right!, it was {0}\n".format(x))
                else:
                    print("You didn't guess it right.The number was {0}, try again! You won't find it! WHAHAHAHAHA\n".format(x))
            except ValueError:
                print("ERROR: It is not an integer bro! \n")

bt = guessNumber();

if __name__ == '__main__':
    bt.main()
        
