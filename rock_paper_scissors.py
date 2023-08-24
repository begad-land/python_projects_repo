import random as rd 

computer_choices=[]

options=['Rock','Paper','Scissors']

player_choices=[]

play_again='Y'
round=1
player_score=0
computer_score=0

while play_again=='Y':
    print(f'\n--------ROUND: {round}--------')
    round+=1
    player_choice=input('Enter Rock/Paper/Scissors ').capitalize()
    player_choices.append(player_choice)

    while player_choice not in options:
        player_choices.remove(player_choice)
        player_choice=input('Enter Rock/Paper/Scissors ').capitalize()
        player_choices.append(player_choice)

    computer_choice=rd.choice(options)
    computer_choices.append(computer_choice)

    if player_choice[0]=='R' and computer_choice[0]=='S' or player_choice[0]=='S' and computer_choice[0]=='P' or player_choice[0]=='P' and computer_choice[0]=='R':
        print('YOU WIN!')
        player_score+=1

    elif player_choice[0]==computer_choice[0]:
        print('DRAW')

    else:
        print('YOU LOSE!')
        computer_score+=1

    print(f'the computer picked: {computer_choice}')
    print('--------------------------------------------------')
    play_again=input('play again? (Y/N)').upper()

    if play_again!='Y':
        play_again=='N'

round=1
for player, computer in zip(player_choices,computer_choices):
    print(f'---------------round: {round}---------------\nYou: {player}\nComputer: {computer}')
    round+=1

print(f'----------------\nYour score: {player_score}\nComputer score: {computer_score}')
