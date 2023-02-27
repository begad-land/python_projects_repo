
class Question:
    def __init__(self,array) -> None:
        self.array=array

    def display_Qs(self):
        score=0
        Q_num=1
        for i in self.array:
            print(f'Q{Q_num}) {i[0]}')
            Q_num+=1
            
            for x in i[1]:
                print(f'{x}\n-----------')
            
            guess=input('pick A/B/C/D ').upper()
            if guess==i[2]:
                print('CORRECT')
                score+=1
            else:
                print(f'INCORRECT\nthe answer is {i[2]}')
                score - 1
            print('----------------------------')
        print(f'score :{score}pts')  
        

             #q1   
q=Question([
            ['whats the coldest planet in our solar system?', ['A. Uranus', 'B. Earth' ,'C. Jupiter', 'D. Mercury'], 'A' ],
            #q2
            ['what is the second most spoken language in the world?',['A. French', 'B. English' ,'C. Hindi', 'D. Mandrin Chinese'], 'D'],
            #q3
            ['what is the name of the second Greek number?',['A. Eth', 'B. Tria' , 'C. Dio' ,'D. Tessera'], 'C'],
            #q4
            ['what is the name of a shape with 7 angles?', ['A. Heptagon' , 'B. Octagon', 'C. pentagon' , 'D. Hexagon'], 'A' ],
            #q5
            ['when a living organism makes more of its own, what is this proccess called?',['A. Reproduction', 'B. Production' , 'C. Increase' , 'D. Reduction' ], 'A' ],
            #q6
            ['what is the name of the species of human beings?',['A. Amphibians', 'B. Homosapiens', 'C. Mammals', 'D.Humans' ], 'B'],
            #q7
            ['in which country is the longest river in the world?',['A. France' , 'B. Egypt', 'C. U.S.A', 'D.Brazil' ], 'B'],
            #q8
            ['which system in the human body controls emotions?',['A.Nervous system', 'B.Digestive system', 'C.Endocrine system', 'D.circulatory system' ], 'C' ]
            ])
q.display_Qs()