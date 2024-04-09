

#TODO 
#figure out as way to send ticket ID to user
#create a class that contains all the classes and makes them work togeher in the correct sequental
#fix booked_json problem (the booking get erassed when writing)

import json
import string
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
            file.writelines(f'{self.v_id}-{self.name}-{self.password}\n')  
        return True   
            
    def check_account(self):
        ask = input('Do you have an account? (y/n) ').lower()
        
        if ask == 'y':
            self.log_in()
        
        else:
            self.sign_up()



class VendorOperations:
    def __init__(self, movie_name = None , seats = [] , genre = None , json_movies = {},pending = {}, booked = {}) -> None:
        self.movie_name = movie_name
        self.seats = seats
        self.genre = genre
        self.json_movies = json_movies
        self.letters = list(string.ascii_uppercase) 
        self.pending = pending
        self.booked = booked
        
    
        
    def write_in_json(self):
        #converts python dict to data that thats suitable for json
        json_obj1 = json.dumps(self.json_movies , indent=2)
        with open('movies/movies.json' , 'w') as file1:
            file1.write(json_obj1)
        
        json_obj2 = json.dumps(self.pending , indent=2) 
        with open('movies\pending.json' , 'w') as file2:
            file2.write(json_obj2)
            
        json_obj3 = json.dumps(self.booked , indent = 2)
        with open('movies/booked.json' , 'w') as file3:
            file3.write(json_obj3)
        
            
    def read_from_json(self):
        with open('movies\movies.json' , 'r') as file1:
            self.json_movies = json.loads(file1.read())   
            
        with open('movies\pending.json' , 'r') as file2:
            self.pending = json.loads(file2.read())
            
        with open('movies/booked.json' , 'r') as file3:
            self.booked = json.loads(file3.read())
            
    def remove_seats(self):
        chosen_seats = {}
        for movie, data in self.pending['movies'].items():
            if len(data) != 0:
                for datum in data:
                    chosen_seats[movie] = [datum[1] for datum in data]
            data.clear()
            
        for title, seats in chosen_seats.items():
            for seat in seats:
                self.json_movies['movies'][title][0].remove(seat)
    
        self.write_in_json()
            
         
            
                 
        
    def operation_choices(self):
        print('1)Add movie\n2)Remove movie\n3)List movie bookings\n4)Confirm customer booking\n5)Exit')
        operation = input('what would you like to do? ')
        
        while operation not in ['1','2','3','4']:
            print('invalid operation')
            print('1)Add movie\n2)List customer bookings\n3)Remove movie\n4)Confirm customer booking')
            operation = input('what would you like to do? ')
            
        if operation == '1':
            self.add_movie()
        elif operation == '2':
            self.remove_movie()              
            
    def add_movie(self):
        random_letter = rn.choice(self.letters)
        self.movie_name = input('insert movie name ').title()
        self.genre = input('insert genre ').title()
        for i in range(1,11):
            self.seats.append(f'{random_letter}{i}')
        
        self.json_movies['movies'][self.movie_name] = [self.seats, self.genre]
        self.pending['movies'][self.movie_name] = [] 
        self.write_in_json()
            
    def remove_movie(self):
        print('----------------------available movies----------------------')
        for title, content in self.json_movies['movies'].items():
            print(f'Title: {title}\nAvailable seats: {content[0]}\nGenre: {content[1]}\n-----------------------------------------------------------')

        name = input('insert the name of the movie you want to remove ').title()
        
        del self.json_movies['movies'][name]
        self.write_in_json()
        print('movie removed')
        
    def confirm_booking(self):
        self.booked = self.pending
        self.write_in_json()    
        self.remove_seats()    
    
    
        
        
v = VendorOperations()
v.read_from_json()
v.confirm_booking()

