questions=[
    'whats the coldest planet in our solar system?',
    'what is the second most spoken language in the world?',
    'what is the name of the second Greek number?',
    'what is the name of a shape with 7 angles?',
    'when a living organism makes more of its own, what is this proccess called?',
    'what is the name of the species of human beings?',
    'in which country is the longest river in the world?'
]

choices=[
    ['A. Uranus ', 'B. Earth' ,'C. Jupiter', 'D. Mercury'],

    ['A. French', 'B. English' ,'C. Hindi', 'D. Mandrin Chinese'],

    ['A. Eth', 'B. Tria' , 'C. Dio' ,'D. Tessera'],

    ['A. Heptagon' , 'B. Octagon', 'C. pentagon' , 'D. Hexagon'],

    ['A. Reproduction', 'B. Production' , 'C. Increase' , 'D. Reduction' ],

    ['A. Amphibians', 'B. Homo sapiens', 'C. Mammals', 'D.Humans' ],

    ['A. France' , 'B. Egypt', 'C. U.S.A', 'D.Brazil' ],
    ]
    

answers=['A', 'D', 'C' ,'A', 'A', 'B' , 'B' ]

C_no=0  
Q_no=1
score=0
for question in questions:
    print(f'Q{Q_no}: {question}')
    Q_no+=1

    for choice in choices[C_no]:
        print(choice)
        print('-----')
    
    answer=input('pick A/B/C/D ' ).upper()

    if answer==answers[C_no]:
        print('CORRECT')
        score+=1
    else:
        print('INCORRECT')
        score - 1
        print(f'the answer is : {answers[C_no]}')
    print('---------------------')
    C_no+=1
print('----Result----')
print(f'your score: {score}\nyou got {score} out of {len(choices)} correct')

