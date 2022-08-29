import random
from shutil import move
import time

rock = 1
paper = 2
scissors = 3

names = {rock: "Rock", paper: "Paper", scissors: "scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}

player_score = 0
computer_score = 0

def start():
    print("Let's play a game of Rock, Paper and Scissors")
    while game():
        pass
    scores()
    
def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()

def move():
    while True:
        print
        player = input ("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: ")
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print("Oops play again I didn't understand. Please choose 1,2 OR 3")


def result(player, computer):
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3...")
    time.sleep(0.5)
    print("Computer threw {0}".format(names[computer]))
    global player_score, computer_score
    if player == computer:
        print("Tie game.")
    else:
        if rules[player] == computer:
            print("Your victory has been assured")
            player_score += 1
        else:
            print("The Computer just beat you!")
            computer_score += 1
        
    
def play_again():
    answer = input("Would you like to play again? (y/n): ")
    if answer in ("y", "Y", "Yes", "Of Course!"):
        return answer
    else:  
        print("Thank you for playing. Try again later.")
                     
def scores():
    global player_score, computer_score
    print("HIGH SCORES")
    print("Player: ",player_score) 
    print("Computer: ", computer_score)
    
if __name__ == "__main__":
    start()
    
