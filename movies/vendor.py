
#vendor operations
import random as rn
class VendorData:
    def __init__(self, v_id = None, name = None, password = None , data_base = {}) -> None:
        self.v_id = v_id
        self.name = name
        self.password = password
        self.data_base = data_base
        
    def preparing_data(self):        
        with open('movies/v_data.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                data = line.split('-')
                data[2] = data[2].replace('\n' , '')
                self.data_base[data[1]] = [
                                            data[0], data[2] 
                                          ]
        self.check_account()
                
    def log_in(self):
        self.name = input('insert your name ').title()
        self.password = input('insert your password ')
        
        while self.name not in self.data_base:
            print("Couldn't fine the inserted username. Try again")
            self.name = input('insert your name ').title()
            self.password = input('insert your password ')
        
        if self.data_base[self.name][1] == self.password:
            print(f'welcome {self.name}')
                         
    def sign_up(self): 
        self.v_id = f'#v_{rn.randint(10000, 999999)}'
        self.name = input('insert your name ').title() 
        self.password = input('insert your password ')  

        while self.name in self.data_base:
            print(f'\n{self.name} is taken. Try a different one')
            self.name = input('insert your name ').title() 
            self.password = input('insert your password ')  
            
        with open('movies/v_data.txt', 'a') as file :
            file.write(f'\n{self.v_id}-{self.name}-{self.password}')
            
        return True    
         
    def check_account(self):
        ask = input('Do you have an account? (y/n) ').lower()
        
        if ask == 'y':
            self.log_in()
        
        else:
            self.sign_up()



v = VendorData()
v.preparing_data()


            

    
             