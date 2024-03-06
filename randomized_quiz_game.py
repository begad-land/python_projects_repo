
import random
import time
import threading

seconds = 0
done = False

def counter():
    global seconds
    global done
    
    while not done:
        time.sleep(1)
        seconds+=1

threading.Thread(target=counter).start()  

class PickedSet:
    def __init__(self,random_pick, Q=None, choices=None, answer=None, hint=None) -> None:
      self.random_pick=random_pick
      self.Q=Q
      self.choices=choices
      self.answer=answer
      self.hint=hint

    def picking_set(self):
      self.random_pick = random.choice(list(questions.items()))
      self.getting_Q()

    def getting_Q(self):
      self.Q = self.random_pick[0]
      self.getting_choices() 
       
    def getting_choices(self):
       self.choices = self.random_pick[1][0]
       self.getting_answer()
    
    def getting_answer(self):
      self.answer = self.random_pick[1][1]
      self.getting_hint()
    
    def getting_hint(self):
      self.hint = self.random_pick[1][2]


class Play:
    def __init__(self,questions,score=0,answered_Qs=[]) -> None:
      
      self.questions=questions
      self.pickedset=PickedSet(questions)
      self.score=score
      self.answered_Qs=answered_Qs

           
    def checking_Q(self):
         self.pickedset.picking_set()
         
         if self.pickedset.Q in self.answered_Qs:
            return True
         
         self.answered_Qs.append(self.pickedset.Q)

    def checking_round(self):
       if len(self.answered_Qs) == 7:
          self.PLAY_AGAIN()
       
    #prints out the question and the choices. calls checking_Q function to check if the question is repeated, calls the taking answer to store the user's answer and calls the 
    #checking round function after each cycle to check if the round is over
    def display_Question(self):
      Q_num=1

      while True:

        if self.checking_Q()==True:
           continue

        print(f'{Q_num}) {self.pickedset.Q}\n-------------------------------------------------------')
        Q_num+=1

        for choice in self.pickedset.choices:
          print(choice)

        self.taking_answer()

        self.checking_round()

        
    def taking_answer(self):
        player_answer=input('Insert A/B/C/D (H for a hint) ').upper()
        print()
        self.correction(player_answer)


    def correction(self,player_answer):
        
        if player_answer=='H':
          print(self.pickedset.hint)
          player_answer=input('Insert A/B/C/D ').upper()

        if player_answer==self.pickedset.answer:
          print(f'correct!')
          self.score +=1

        else:
            print(f'incorrect\nanswer: {self.pickedset.answer}')  
        print('-------------------------------------------------------\n\n')


    def PLAY_AGAIN(self):
        global done
        done = True
        print(f'score: {self.score} pt(s)\ntime: {seconds} seconds\n-------------------------------------------------------')
        ask=input('would you like to play again? (Y/N) ').upper()
        print('-------------------------------------------------------')
        print()
        if ask=='N':
            print(f'Thanks for playing :)')
            exit()
        self.reset_game()


    def reset_game(self):
          global seconds
          global done
          seconds = 0
          self.answered_Qs.clear()
          self.score=0
          done = False
          threading.Thread(target=counter).start()
          self.display_Question()
           
          



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

play=Play(questions)
play.display_Question()


