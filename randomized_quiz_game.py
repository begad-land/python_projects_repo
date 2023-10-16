answered_Qs=[]
import random

class PickedSet:
    def __init__(self,random_pick, Q=None, choices=None, answer=None, hint=None) -> None:
      self.random_pick=random_pick
      self.Q=Q
      self.choices=choices
      self.answer=answer
      self.hint=hint

    def picking_set(self):
      self.random_pick = random.choice(list(questions.items()))
      return self.random_pick

    def getting_Q(self):
      self.Q = self.random_pick[0]
      return self.Q 
       
    def getting_choices(self):
       self.choices = self.random_pick[1][0]
       return self.choices
    
    def getting_answer(self):
      self.answer = self.random_pick[1][1]
      return self.answer
    
    def getting_hint(self):
      self.hint = self.random_pick[1][2]
      return self.hint


class Play:
    def __init__(self,questions,score=0) -> None:
      self.questions=questions
      #you are passing the questions var to the random_pick attribute so it can then get its random value in the picking_Q function so if u call the attribute without
      #alone it will give u what u passed to it which is the entire questions var. so you either call the version of the var that the function returns or you call the picking_set func before th display func
      self.pickedset=PickedSet(questions)
      self.score=score



    def display(self):
      
      Q_num=1

      while len(answered_Qs) != 7: 
        self.pickedset.picking_set()

        if self.pickedset.getting_Q() in answered_Qs:
            continue
        
        print(f'{Q_num}) {self.pickedset.getting_Q()}')
        Q_num+=1

        answered_Qs.append(self.pickedset.getting_Q())

        for choice in self.pickedset.getting_choices():
          print(choice)
        
        player_answer=input('Insert A/B/C/D (H for a hint) ').upper()
        print()
        self.correction(player_answer)

    
    def correction(self,player_answer):
        if player_answer=='H':
          print(self.pickedset.getting_hint())
          player_answer=input('Insert A/B/C/D ').upper()

        if player_answer==self.pickedset.getting_answer():
          print(f'correct!')
          self.score +=1

        else:
          print(f'incorrect\nanswer: {self.pickedset.getting_answer()}')
        print('---------------------------------------')  



questions={
                      'whats the coldest planet in our solar system?':(('A. Uranus', 'B. Earth' ,'C. Jupiter', 'D. Neptune'),'A','its the 7th planet in the solar system'),

                      'what is the second most spoken language in the world?':(('A. French', 'B. English' ,'C. Hindi', 'D. Mandrin Chinese'),'D','its asian'),
                      
                      'what is the most abudnant element in the atmosphere':(('A. Francium(Fr)', 'B. Oxygen(O2)', 'C. Nitrogen(N2)', 'D. Hydrogen(H)' ),'C','its used to put out fires '),

                      'whats the name of the island thats also a continent?':(('A. Australia' , 'B. Austria', 'C. Bora Bora' , 'D. Hawaii'),'A','its knwon for the kangroos'),

                      'the second biggest country in the world?':(('A. Canada', 'B. Russia' , 'C. U.S.A' , 'D. India'),'A','they play a lot of hockey'),

                      'what is the hardest substance on Earth':(('A. Platinum', 'B. Titamnium', 'C. Diamond', 'D. Iron'),'C','its always a rank in video games'),

                      'in which country is the longest river in the world?':(('A. France' , 'B. Egypt', 'C. U.S.A', 'D. Brazil' ),'B','they have a long history'),

                      'which planet has the most moons?': (('A. Jupiter', 'B. Mars', 'C. Mercury', 'D. Saturn'),'D','it has rings around it'),

                      'How many elements are in the periodic table?':(('A. 125', 'B. 118', 'C. 117', 'D. 123'),'B','cant hint that one'),

                      'What is the country that has the second highest population':(('A. India', 'B. U.S.A', 'C. Indonesia' ,'D. China'), 'A','they are asian'),

                      'What is the biggest organ in the human body':(('A. Liver', 'B. Brain', 'C. Skin', 'D. Lungs'),'C','its the first line of defense in your immune system'),

                      'which planet in our solar system is called the "Red planet" ':(('A. Mars','B. Venus','C. Earth','D. Jupiter'),'A','it neighbors earth')
            }

play_again=None


#make the play again feature | try to make it a differnt function

play=Play(questions)
play.display()
print(f'score: {play.score}')
print('thanks for playing :)')

