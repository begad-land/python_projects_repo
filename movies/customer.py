
import random as rn

class CustomerData:
    def __init__(self ,c_id = None, name = None, email= None, phone_number = None, password = None, database = {}) -> None:
        self.c_id = c_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.database = database
        
        
    
    def preparing_data(self):        
        with open('movies/c_data.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                data = line.split('-')
                data[2] = data[2].replace('\n' , '')
                self.database[data[1]] = [
                                            data[0], data[2] 
                                          ]

    def log_in(self):
        self.name = input('insert yout user name ')
        self.password = input('insert your password ')
        
        while self.name not in self.database:
            print("Couldn't fine the inserted username. Try again")
            self.name = input('insert your name ').title()
            self.password = input('insert your password ')
        
        if self.data_base[self.name][1] == self.password:
            print(f'welcome {self.name}')
        
        
    def sign_up(self):
        self.c_id = f'#v_{rn.randint(10000, 999999)}'
        self.name = input('insert your name ')
        self.email = input('insert your email ')
        self.phone_number = input('insert your phone number ')
        self.password = input('insert password ')
        
        while self.name in self.database:
            print(f'\n{self.name} is taken. Try a different one')
            self.name = input('insert your name ').title() 
            self.password = input('insert your password ')
        
        with open('movies/c_data.txt', 'a') as file :
            file.writelines(f'{self.c_id}-{self.name}-{self.password}-{self.email}-{self.phone_number}\n')  
        return True 

c = CustomerData()
c.sign_up()