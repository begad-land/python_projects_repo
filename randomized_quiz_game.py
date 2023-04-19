
import random

questions={
                      'whats the coldest planet in our solar system?':(('A. Uranus', 'B. Earth' ,'C. Jupiter', 'D. Neptune'),'A','its the 7th planet in the solar system'),

                      'what is the second most spoken language in the world?':(('A. French', 'B. English' ,'C. Hindi', 'D. Mandrin Chinese'),'D','its asian'),
                      
                      'what is the most abudnant element in the atmosphere':(('A. Francium(Fr)', 'B. Oxygen(O2)', 'C. Nitrogen(N2)', 'D. Hydrogen(H)' ),'C','its used to put out fires '),

                      'whats the name of the island thats also a continent?':(('A. Australia' , 'B. Austria', 'C.Bora Bora' , 'D. Hawaii'),'A','its knwon for the kangroos'),

                      'the second biggest country in the world?':(('A. Canada', 'B. Russia' , 'C. U.S.A' , 'D. India'),'A','they play a lot of hockey'),

                      'what is the hardest substance on Earth':(('A. Platinum', 'B. Titamnium', 'C. Diamond', 'D. Iron'),'C','its always a rank in video games'),

                      'in which country is the longest river in the world?':(('A. France' , 'B. Egypt', 'C. U.S.A', 'D. Brazil' ),'B','they have a long history'),

                      'which planet has the most moons?': (('A. Jupiter', 'B. Mars', 'C. Mercury', 'D. Saturn'),'D','it has rings around it'),

                      'How many elements are in the periodic table?':(('A. 125', 'B. 118', 'C. 117', 'D. 123'),'B','cant hint for that one'),

                      'What is the country that has the second highest population':(('A. India', 'B. U.S.A', 'C. Indonesia' ,'D. China'), 'A','they are asian'),

                      'What is the biggest organ in the human body':(('A.Liver', 'B. Brain', 'C. Skin', 'D. Lungs'),'C','its the first line of defense in your immune system'),

                      'which planet in our solar system is called the "Red planet" ':(('A.Mercury','B.Venus','C.Earth','D.Jupiter'),'A','it neighbors earth')
                    }
play_again=None

def the_game():

   Qs_displayed=[]

   Q_num=1

   score=0

   while len(Qs_displayed)!=7:
               
      Qs=random.choice(list(questions.items()))

      if Qs[0] in Qs_displayed:
         continue

      Qs_displayed.append(Qs[0])

      print(f'\n{Q_num}) {Qs[0]}\n')
      Q_num+=1  
            

      for i in Qs[1][0]:
         print(f'{i}\n----------------------')

      guess=input('\npick A/B/C/D (insert h for a hint) ').upper()


      if guess=='H':
         print(f'{Qs[1][2]}')
         guess=input('\npick A/B/C/D ').upper()

      if guess==Qs[1][1]:
         print(f'correct!')
         score+=1

      else:
         print(f'wrong the answer is: {Qs[1][1]}')
      print('-------------------------------------------\n') 

   print(f'your score: {score}/{len(Qs_displayed)}')
   

while play_again!='n':
   the_game()
   play_again=input('\nplay again? (y/n) ')
print('hello')