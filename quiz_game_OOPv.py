
import random

class Game:
    def __init__(self,Q,Qs_saved,score) -> None:
        self.Q=Q
        self.Qs_saved=Qs_saved
        self.score=score

    def display_Qs(self):
        print(f'\n{self.Qs_saved}) {self.Q[0]}\n')

        for i in self.Q[1][0]:
            print(f'{i}\n') 

s= {
                      'whats the coldest planet in our solar system?':(('A. Uranus', 'B. Earth' ,'C. Jupiter', 'D. Neptune'),'A'),

                      'what is the second most spoken language in the world?':(('A. French', 'B. English' ,'C. Hindi', 'D. Mandrin Chinese'),'D'),
                      
                      'what is the most abudnant element in the atmosphere':(('A. Francium(Fr)', 'B. Oxygen(O2)', 'C. Nitrogen(N2)', 'D. Hydrogen(H)' ),'C'),

                      'what is the name of a shape with 7 angles?':(('A. Heptagon' , 'B. Octagon', 'C. pentagon' , 'D. Hexagon'),'A'),

                      'when a living organism makes more of its own, what is this proccess called?':(('A. Reproduction', 'B. Production' , 'C. Increase' , 'D. Reduction'),'A'),

                      'what is the hardest substance on Earth':(('A. Platinum', 'B. Titamnium', 'C. Diamond', 'D. Iron'),'C'),

                      'in which country is the longest river in the world?':(('A. France' , 'B. Egypt', 'C. U.S.A', 'D. Brazil' ),'B'),

                      'which planet has the most moons?': (('A. Jupiter', 'B. Mars', 'C. Mercury', 'D. Saturn'),'D'),

                      'How many elements are in the periodic table?':(('A. 125', 'B. 118', 'C. 117', 'D. 123'),'B'),

                      'What is the country that has the second highest population':(('A. India', 'B. U.S.A', 'C. Indonesia' ,'D. China'), 'A'),

                      'What is the biggest organ in the human body':(('A.Liver', 'B. Brain', 'C. Skin', 'D. Lungs'),'C')
                    }

Qs_saved=[]
score=0
while len(Qs_saved) < 7:
    
    randQs=random.choice(list(s.items()))

    if randQs in Qs_saved:
        continue
    
    Qs_saved.append(randQs)

    elements=Game(randQs,len(Qs_saved),score)
    
    elements.display_Qs() 

    guess=input('pick A/B/C/D ').upper()

    if guess==randQs[1][1]:
        print(f'correct')
        score+=1
    else:
        print(f'wrong the correct answer is {randQs[1][1]}')
    
print(f'thanks for playng\nscore:{score}/{len(Qs_saved)}')
