
class Question:
    def __init__(self,**kwargs) -> None:
        self.kwargs=kwargs
        
    def display_Qs(self):
        C_num=0
        A_num=0
        score=0
        Num_of_Qs=len(self.kwargs['questions'])
        for q in self.kwargs['questions']:
            print(q)

            for x in self.kwargs['choices'][C_num]:
                print(f'{x}\n---------------------------')
            C_num+=1

            guess=input('pick A/B/C/D ').upper()
            if guess==self.kwargs['answers'][A_num]:
                print('CORRECT')
                score+=1     

            else:
                print(f'INCORRECT \nThe correct answer: {self.kwargs["answers"][A_num]}')
                score - 1
            A_num+=1
            print('-----------------------------')
        print(f'Your score: {score}/{Num_of_Qs}pts') 
                
q=Question(questions=(
                      'whats the coldest planet in our solar system?', 
                      'what is the second most spoken language in the world?' ,
                      'what is the most abudnant element in the atmosphere',
                      'what is the name of a shape with 7 angles?',
                      'when a living organism makes more of its own, what is this proccess called?',
                      'what is the hardest substance on Earth',
                      'in which country is the longest river in the world?',
                      'which planet has the most moons?',
                      'How many elements in the periodic table?'
                      ), 
            choices=(
                    ('A. Uranus', 'B. Earth' ,'C. Jupiter', 'D. Mercury'),
                    ('A. French', 'B. English' ,'C. Hindi', 'D. Mandrin Chinese'),
                    ('A.Francium(Fr)', 'B. Oxygen(O2)', 'C. Nitrogen(N2)', 'D.Hydrogen(H)' ), 
                    ('A. Heptagon' , 'B. Octagon', 'C. pentagon' , 'D. Hexagon'),
                    ('A. Reproduction', 'B. Production' , 'C. Increase' , 'D. Reduction'),
                    ('A. Platinum', 'B. Titamnium', 'C. Diamond', 'D. Iron'),
                    ('A. France' , 'B. Egypt', 'C. U.S.A', 'D.Brazil' ),
                    ('A. Jupiter', 'B. Mars', 'C. Mercury', 'D. Saturn'),
                    ('A. 125', 'B. 118', 'C. 117', 'D. 123')
                    ),
            answers=('A', 'D', 'C' ,'A', 'A', 'C' ,'B', 'D', 'B')
            )
q.display_Qs()