import random 

high=100

low=1

num=random.randint(low,high)
guess=None

guesses=0
while guess!=num:
    
    guesses+=1

    guess=int(input('\nguess the random number  ')) 

    if guess > num:
        print(f'\n{guess} is too high')

    elif guess < num:
        print(f'\n{guess} is too low')
    else:
        break
    
print(f'CORRECT\nit took u {guesses} guesses ')