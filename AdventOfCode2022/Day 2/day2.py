file = open('adventofcode.com_2022_day_2_input.txt', 'r')
games = file.readlines()
score = 0
result = ''
# play1 : A - ROCK, B - PAPER, C - SCISSORS
# play2: X - ROCK, Y - PAPER, Z - SCISSORS

def play_points(play):
    if play == 'X':
        return 1
    if play == 'Y':
        return 2
    if play == 'Z':
        return 3
    
def round_points(play1, play2):
    if play1 == 'A': # rock
        if play2 == 'Y': # paper
            return 6
        if play2 == 'Z': # scissors
            return 0
    
    if play1 == 'B': # paper
        if play2 == 'X': # rock
            return 0
        if play2 == 'Z': # scissors
            return 6
        
    if play1 == 'C': # scissors
        if play2 == 'X': # rock
            return 6
        if play2 == 'Y' : #paper
            return 0
    
    return 3

def correct_play(play1, result):
    if result == 'Y':
        if play1 == 'A':
            return 'X'
        if play1 == 'B':
            return 'Y'
        return 'Z'
    if result == 'X':
        if play1 == 'A':
            return 'Z'
        if play1 == 'B':
            return 'X'
        return 'Y'
    if result == 'Z':
        if play1 == 'A':
            return 'Y'
        if play1 == 'B':
            return 'Z'
        return 'X'

for round in games:
    score += play_points( correct_play(round[0], round[2])) + round_points(round[0], correct_play(round[0], round[2]))

print(score)

    