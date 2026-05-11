import random

options = ('rock', 'paper', 'scissor')
player_points = 0
computer_points = 0

num_rounds = int(input('Enter the number of times you have to play (preferably odd): '))

wins = {
    ('rock', 'scissor'): 'you win',
    ('paper', 'rock'): 'you win',
    ('scissor', 'paper'): 'you win',
    ('rock', 'rock'): 'its a draw',
    ('paper', 'paper'): 'its a draw',
    ('scissor', 'scissor'): 'its a draw',
}

for round_num in range(num_rounds):
    while True:
        player = input("Enter your option (rock, paper, or scissor): ").lower()
        if player in options:
            break
        print("Invalid option!")
    
    computer = random.choice(options)
    print(f'Your choice: {player}')
    print(f"Computer's choice: {computer}")
    
    result = wins.get((player, computer), 'you lose')
    print(result)
    
    if 'win' in result:
        player_points += 1
    elif 'lose' in result:
        computer_points += 1

print(f"\nFinal Score - You: {player_points}, Computer: {computer_points}")
if player_points > computer_points:
    print('You won against the computer! :)')
elif player_points < computer_points:
    print('You lost against the computer :(')
else:
    print('Its a draw :o')
