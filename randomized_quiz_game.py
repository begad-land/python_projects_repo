
import random

questions={
                      'whats the coldest planet in our solar system?':(('A. Uranus', 'B. Earth' ,'C. Jupiter', 'D. Neptune'),'A'),

                      'what is the second most spoken language in the world?':(('A. French', 'B. English' ,'C. Hindi', 'D. Mandrin Chinese'),'D'),
                      
                      'what is the most abudnant element in the atmosphere':(('A. Francium(Fr)', 'B. Oxygen(O2)', 'C. Nitrogen(N2)', 'D. Hydrogen(H)' ),'C'),

                      'what is the name of a shape with 7 angles?':(('A. Heptagon' , 'B. Octagon', 'C. pentagon' , 'D. Hexagon'),'A'),

                      'when a living organism makes more of its own, what is this proccess called?':(('A. Reproduction', 'B. Production' , 'C. Increase' , 'D. Reduction'),'A'),

                      'what is the hardest substance on Earth':(('A. Platinum', 'B. Titamnium', 'C. Diamond', 'D. Iron'),'C'),

                      'in which country is the longest river in the world?':(('A. France' , 'B. Egypt', 'C. U.S.A', 'D.Brazil' ),'B'),

                      'which planet has the most moons?': (('A. Jupiter', 'B. Mars', 'C. Mercury', 'D. Saturn'),'D'),

                      'How many elements are in the periodic table?':(('A. 125', 'B. 118', 'C. 117', 'D. 123'),'B'),

                      'What is the country that has the second highest population':(('A. India', 'B. U.S.A', 'C. Indonesia' ,'D. China'), 'A'),

                      'What is the biggest organ in the human body':(('A.Liver', 'B. Brain', 'C. Skin', 'D. Lungs'),'C')
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