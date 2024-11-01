

#TODO 


import json
import string
import random as rn
class VendorData:
    def __init__(self, v_id = None, name = None, password = None , data_base = {}, vendor_data = {}) -> None:
        self.v_id = v_id
        self.name = name
        self.password = password
        self.data_base = data_base
        self.vendor_data = vendor_data
        self.read_from_json()
     
    def write_in_json(self):
        #converts python dict to data that thats suitable for json
        json_obj1 = json.dumps(self.vendor_data , indent=2)
        with open('movies/vendor.json' , 'w') as file1:
            file1.write(json_obj1) 
            
    def read_from_json(self):
        with open('movies/vendor.json' , 'r') as file1:
            self.vendor_data = json.loads(file1.read()) 
        
  
    def log_in(self):
        self.name = input('insert your name ')
        self.password = input('insert your password ')
        
        while self.name not in self.vendor_data['vendor'] or self.password not in self.vendor_data['vendor'][self.name]:
            print("Wrong username or password. Try again")
            self.name = input('insert your name ')
            self.password = input('insert your password ')
            print('---------------------------------------------')
        
        print(f'welcome {self.name}')
                         
    def sign_up(self): 
        self.v_id = f'#v_{rn.randint(10000, 999999)}'
        self.name = input('insert your name ')
        self.password = input('insert your password ')  

        while self.name in self.vendor_data['vendor']:
            print(f'\n{self.name} is taken. Try a different one')
            self.name = input('insert your name ')
            self.password = input('insert your password ')  
        
        self.vendor_data['vendor'][self.name] = [self.password, self.v_id]
        
        print(f'welcome {self.name}')
        self.write_in_json()
        #with open('movies/v_data.txt', 'a') as file :
            #file.writelines(f'{self.v_id}-{self.name}-{self.password}\n')  
            
    def check_account(self):
        ask = input('Do you have an account? (y/n) ').lower()
        
        if ask == 'y':
            self.log_in()
        
        else:
            self.sign_up()



class VendorOperations:
    def __init__(self, movie_name = None , seats = [] , genre = None , json_movies = {},pending = {}, booked = {} , customer_tickets = {}) -> None:
        self.movie_name = movie_name
        self.seats = seats
        self.genre = genre
        self.json_movies = json_movies
        self.letters = list(string.ascii_uppercase) 
        self.pending = pending
        self.booked = booked
        self.customer_tickets = customer_tickets
        self.read_from_json()
    
        
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
                        
        
    def operation_choices(self):
        print('1)Add movie\n2)List customer bookings and confirm them\n3)Remove movie\n4)List movies\n5)Exit')
        operation = input('what would you like to do? ')
        
        while operation not in ['1','2','3','4','5']:
            print('invalid operation')
            print('1)Add movie\n2)List customer bookings and confirm them\n3)Remove movie\n4)List movies\n5)Exit')
            operation = input('what would you like to do? ')
            
        if operation == '1':
            self.add_movie()
        elif operation == '2':
            self.show_pending_list()
        elif operation == '3':
            self.remove_movie()
        elif operation == '4':
            self.list_movies()          
        elif operation == '5':
            exit()
        
    def list_movies(self):
        print('---------------------available movies--------------------')
        for title , data in self.json_movies['movies'].items():
            print(f'Title: {title}\nGenre: {data[1]}\nSeats: {data[0]}\n---------------------------------')
        #return
            
    
    def add_movie(self):
        random_letter = rn.choice(self.letters)
        self.movie_name = input('insert movie name ').title()
        self.genre = input('insert genre ').title()
        for i in range(1,11):
            self.seats.append(f'{random_letter}{i}')
        
        self.json_movies['movies'][self.movie_name] = [self.seats, self.genre]
        self.pending['movies'][self.movie_name] = [] 
        self.booked['movies'][self.movie_name] = [] 
        self.write_in_json()
            
    def remove_movie(self):
        print('----------------------available movies----------------------')
        for title, content in self.json_movies['movies'].items():
            print(f'Title: {title}\nAvailable seats: {content[0]}\nGenre: {content[1]}\n-----------------------------------------------------------')

        name = input('insert the name of the movie you want to remove ').title()
        
        del self.json_movies['movies'][name]
        del self.json_pending['movies'][name]
        del self.json_booked['movies'][name]
        self.write_in_json()
        print('movie removed')
    
    
    def show_pending_list(self):
        no_items = 0
        for title, data in self.pending['movies'].items():
            if len(data) != 0:
                print(f'{title}: {data}')
                continue
            no_items+=1

        if no_items == len(self.pending['movies']):
            print('All bookings confirmed')
            return
                  
        ask = input('confirm bookings? (y/n) ').lower()
        
        if ask == 'y':
            self.confirm_booking()
        else:
            return


    def confirm_booking(self):
        for title, data in self.pending['movies'].items():
            if len(data) != 0:
                for datum in data:
                    ticket_id = f'{datum[1][0]}_{rn.randint(10,999)}'
                    datum.append(ticket_id)
                    self.booked['movies'][title].append(datum)
        self.remove_seats()
        self.write_in_json()    
        
            
                        
    
class Vendor:
    def __init__(self) -> None:
        self.v_data = VendorData()
        self.vendor_ops = VendorOperations()
        
    def getting_data(self):
        self.v_data.check_account()
    
    def operations(self):
        while True:
            print('---------------------------------')
            self.vendor_ops.operation_choices()
        
        
        
vendor = Vendor()
vendor.getting_data()
vendor.operations()