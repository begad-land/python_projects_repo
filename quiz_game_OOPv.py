
class Question:

    def __init__(self,q,choices,answer) -> None:
        self.q=q
        self.choices=choices
        self.answer=answer

    def display_Qs(self):
        score=0
        print(self.q)
        for choice in self.choices:
            print(f'{choice}\n------------')
            
        guess=input('pick A/B/C/D ').upper()
        
        if guess==self.answer:
            print('CORRECT')
            score+=1
        else:
            print(f'INCORRECT\nthe answer is : {self.answer}')
        score - 1
        print('---------------------------')
        print(f'Score: {score}pts\n-------')

q1=Question('whats the coldest planet in our solar system?',['A. Uranus ', 'B. Earth' ,'C. Jupiter', 'D. Mercury'], 'A')
q1.display_Qs()

q2=Question('what is the second most spoken language in the world?', ['A. French', 'B. English' ,'C. Hindi', 'D. Mandrin Chinese'], 'D')
q2.display_Qs()

q3=Question('what is the name of the second Greek number?',['A. Eth', 'B. Tria' , 'C. Dio' ,'D. Tessera'], 'C')
q3.display_Qs()

q4=Question('what is the name of a shape with 7 angles?',['A. Heptagon' , 'B. Octagon', 'C. pentagon' , 'D. Hexagon'], 'A')
q4.display_Qs()

q5=Question('when a living organism makes more of its own, what is this proccess called?',['A. Reproduction', 'B. Production' , 'C. Increase' , 'D. Reduction' ], 'A')
q5.display_Qs()

q6=Question('what is the name of the species of human beings?',['A. Amphibians', 'B. Homosapiens', 'C. Mammals', 'D.Humans' ], 'B')
q6.display_Qs()

q7=Question('in which country is the longest river in the world?',['A. France' , 'B. Egypt', 'C. U.S.A', 'D.Brazil' ], 'B')
q7.display_Qs()