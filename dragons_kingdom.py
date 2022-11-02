# this is dragon kingdom game
import random
import time


def displayIntro():
    print('''You are in the lands inhabited by dragons.
In front of you you see two caves. In one of them is a friendly dragon,
who is ready to share his treasures with you. In the second -
a greedy and hungry dragon that will eat you in an instant.''')
    print()


# Code to request from the player, which cave he wants to enter, 1 or 2.
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you enter? (press key 1 or 2)')
        cave = input()

    return cave


def checkCave(chosenCave):
    print('You are approaching a cave...')
    time.sleep(2)
    print('Its darkness makes you tremble with fear...')
    time.sleep(2)
    print('A big dragon jumps out in front of you! He opens his mouth and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('...sharing his treasures with you!')
    else:
        print('... instantly eats you up!')


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Try your luck again? (Yes or no)')
    playAgain = input()
