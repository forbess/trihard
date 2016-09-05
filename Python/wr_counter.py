from tkinter import *

root = Tk()
root.title('Winrate Counter')
root.minsize(width=160, height=140)
root.maxsize(width=160, height=140)

value = IntVar()
value.set(0)
value2 = IntVar()
value2.set(0)


winrate = IntVar()
winrate.set(0)

winr = IntVar()
winr.set(0)

#Functions
def increase_value(*args):
    valueOne = value.get() + 1
    value.set(valueOne)
    calc = int((value.get() / (value.get() + value2.get()) * 100))
    winr.set(calc)
    
def decrease_value(*args):
    valueTwo = value2.get() + 1
    value2.set(valueTwo)
    calc = int((value.get() / (value.get() + value2.get()) * 100))
    winr.set(calc)

def reset_value(*args):
    value.set(0)
    value2.set(0)
    calc = int(0)
    winr.set(calc)

def save_value(*args):
    pass

def quit():
    root.quit()

#Buttons
winrateButton = Button(root, text=" Won\t↑", command = increase_value, bg='green', fg='white')
loseButton = Button(root, text=" Lost\t↓", command=decrease_value ,bg='red', fg='white')
resetButton = Button(root, text="Reset\tØ", command=reset_value, bg='blue', fg='white')
exitButton = Button(root, text="Quit\t✗", command=quit, bg='firebrick', fg='white')
# saveButton = Button(root, text="Save ✓ ", command=save_value, bg='purple', fg='white')

#Labels
valueLabel = Label(root, textvariable=value)
value2Label = Label(root, textvariable=value2)
winrateLabel = Label(root, textvariable=winr)
wrCountLabel = Label(root, text ='~Winrate (%) :')
WinCountLabel = Label(root, text='Win Count :')
LoseCountLabel = Label(root, text='Lose Count :')

#Grids
valueLabel.grid(row=1, column=2)
WinCountLabel.grid(row=1, column=1)
LoseCountLabel.grid(row=2, column=1)
value2Label.grid(row=2, column=2)
wrCountLabel.grid(row=3, column=1)
winrateLabel.grid(row=3, column=2)
loseButton.grid(row=4, column=2)
winrateButton.grid(row=4, column=1)
resetButton.grid(row=5, column=1)
exitButton.grid(row=5, column=2)
# saveButton.grid(row=5, column=1)

root.mainloop()

