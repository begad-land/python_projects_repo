questions=[
    'whats 2+2',
    'how many fingers in the human hand'
]

choices=[
    ['A.4 ', 'B.5' ,'C.10', 'D.3'],

    ['A.1 ', 'B.3' ,'C.9', 'D.5']
    ]
answers=['A','D']

C_no=0  
Q_no=1
for question in questions:
    print(f'Q{Q_no}: {question}')
    Q_no+=1

    for choice in choices[C_no]:
        print(choice)
    answer=input('pick A/B/C/D ' ).upper()
    if answer==answers[C_no]:
        print('CORRECT')
    else:
        print('INCORRECT')
        print(f'the answer is : {answers[C_no]}')
    print('---------------------')

    C_no+=1
    

