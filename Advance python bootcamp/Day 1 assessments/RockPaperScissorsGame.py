import random

# rock = '''      _______
#             ---'   ____)
#                   (_____)
#                   (_____)
#                   (____)
#             ---.__(___)
# '''
# paper = '''

#                  _______
#             ---'    ____)____
#                        ______)
#                       _______)
#                      _______)
#             ---.__________)
# '''
# scissor = '''

#                 _______
#             ---'   ____)____
#                       ______)
#                    __________)
#                   (____)
#             ---.__(___)
# '''
# symbols = {
#     'rock' : rock ,
#     'paper' : paper ,
#     'scissor' : scissor
# }

choices = ('rock','paper','scissor')
while True :
    player = input('Enter your choice : ')
    computer = random.choice(choices)
    print(f'You choice is {player}')
    print(f'Computer choice is {computer}')
    if player == computer :
        print('It\'s a tie')
    elif player == 'rock' and computer == 'scissor' :
        print('You win')
    elif player == 'scissor' and computer == 'paper' :
        print('You win')
    elif player == 'paper' and computer == 'rock' :
        print('You win')
    else:
        print('You lose')
    player = input('Do you want to continue (y/n) : ')
    if player == 'n' :
        break
print('Thank you for playing !')


