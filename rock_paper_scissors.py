import random

choices=['rock','paper','scissors']

p_score=0

c_score=0
while True:
    computer=random.choice(choices)
    player=input('pick (rock/ paper / scissors ) ')


    while player not in choices:
        player=input('pick (rock/ paper / scissors ) ')

    if player[0]=='r' and computer[0]=='s' or  player[0]=='p' and computer[0]=='r' or player[0]=='s' and computer[0]=='p':
        print(f'\nthe computer picked {computer} and you picked {player}  \nyou win!')
        p_score+=1
        
    elif player[0]==computer[0]:
        print(f'\nthe computer picked {computer} and you picked {player}  \nits a tie!')

    else:
        print(f'\nthe computer picked {computer} and you picked {player}  \nyou lose!')
        c_score+=1
    if input('play again y/n ') !='y':
        break
    
print(f'\nyour score: {p_score}\nthe computers score: {c_score}')
print('thanks for playing')