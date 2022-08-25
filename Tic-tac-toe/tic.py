board = [
    ["-","-","-"],
    ["-","-","-"] , 
    ["-","-","-"] 
]
def showboard(board):
    for row in board:
        for character in row:
            print(character+ " ",end="")
        print()
showboard(board)

def quitgame(user_input):
    if user_input == "q":
        print("Thanks for playing")
        return True
    else: return False

while True:
    user_input = input("Choose a position between 1 and 9 or \"q\" to quit: ")
    if quitgame(user_input): break
    