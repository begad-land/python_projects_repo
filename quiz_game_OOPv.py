
class Question:
    def __init__(self,**kwargs) -> None:
        self.kwargs=kwargs

    def display_Qs(self):
        C_num=0
        for q in self.kwargs['questions']:
            print(q)
            for x in self.kwargs['choices'][C_num]:
                print(f'{x}\n---------------------------')
            guess=input('pick A/B/C/D ')
        for answer in self.kwargs['answer']:
            if guess==answer:
                print('CORRECT')


q=Question(questions=[
                      'whats the coldest planet in our solar system?', 
                      'what is the second most spoken language in the world?' ,
                      'what is the most abudnant element in the atmosphere',
                      'what is the name of a shape with 7 angles?',
                      'when a living organism makes more of its own, what is this proccess called?',
                      'what is the name of the species of human beings?',
                      'in which country is the longest river in the world?'], 
            choices=[
                    ['A. Uranus', 'B. Earth' ,'C. Jupiter', 'D. Mercury'],
                    ['A. French', 'B. English' ,'C. Hindi', 'D. Mandrin Chinese'],
                    ['A.Francium(Fr)', 'B. Oxygen(O2)', 'C. Nitrogen(N2)', 'D.Hydrogen(H)' ], 
                    ['A. Heptagon' , 'B. Octagon', 'C. pentagon' , 'D. Hexagon'],
                    ['A. Reproduction', 'B. Production' , 'C. Increase' , 'D. Reduction'],
                    ['A. Amphibians', 'B. Homosapiens', 'C. Mammals', 'D.Humans'],
                    ['A. France' , 'B. Egypt', 'C. U.S.A', 'D.Brazil' ]
                    ],

                    answers=['A', 'D', 'C' ,'A', 'A', 'B' , 'B' ]
                    )
q.display_Qs()