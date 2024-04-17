
import random as rn
import json
#TODO
#you need to go into the bboo


class CustomerData:
    def __init__(self ,c_id = None, name = None, email= None, phone_number = None, password = None, database = {} ) -> None:
        self.c_id = c_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.database = database
    
    
    def sign_up(self):
        self.c_id = f'#v_{rn.randint(10000, 999999)}'
        self._extracted_from_sign_up_10()
        while self.name in self.database:
            print(f'\n{self.name} is taken. Try a different one')
            self._extracted_from_sign_up_10() 
        return self.name
    
    
    
    def log_in(self):
        self.name = input('insert yout user name ')
        self.password = input('insert your password ')

        while self.name not in self.database or self.password != self.database[self.name][1] :
            print("-----------------------------------------------\nWrong username or password. Try again")
            self.name = input('insert your name ')
            self.password = input('insert your password ')

        print(f'welcome {self.name}')   
        return self.name   
    
    # TODO Rename this here and in `sign_up` #
    def _extracted_from_sign_up_10(self):
        self.name = input('insert your name ')
        self.email = input('insert your email ')
        self.phone_number = input('insert your phone number ')
        self.password = input('insert password ') 

    
    def preparing_data(self):        
        with open('movies/c_data.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                data = line.split('-')
                data[2] = data[2].replace('\n' , '')
                self.database[data[1]] = [
                                            data[0], data[2] 
                                          ]



class CustomerBooking():
    def __init__(self,chosen_movie = None ,json_movies = {} , pending = {} , user_name = None, customer_tickets = {}) -> None:
        self.chosen_movie = chosen_movie
        self.json_movies = json_movies
        self.pending = pending
        self.customer_tickets = customer_tickets
        self.customer_data = CustomerData()
        self.user_name = self.customer_data.log_in()
        

    def write_in_json(self):
        json_obj = json.dumps(self.pending, indent = 2)

        with open('movies\pending.json' , 'w') as f:
            f.write(json_obj)
            
        
    
    def read_from_json(self):
        with open('movies\movies.json' , 'r') as f:
            self.json_movies = json.loads(f.read())
            
        with open('movies\pending.json' , 'r') as file:
            self.pending = json.loads(file.read())
            

    def view_movies(self):
        print('---------------------available movies--------------------')
        for title , data in self.json_movies['movies'].items():
            print(f'Title: {title}\nGenre: {data[1]}\nSeats: {data[0]}\n---------------------------------')

            
    def booking_movie(self):
        
        choice = input('insert movie name ').title()
        chosen_movie = self.json_movies['movies'][choice]
        
      
        
        print(f'Title: {choice}\nGenre: {chosen_movie[1]}\nSeats: {chosen_movie[0]}\n-----------------------------------')
        
        seat = input('insert the seat that you want ').title()
        seats = self.json_movies['movies'][choice][0]
        seat_and_username = [self.user_name, seat]
        
        pending_list = self.pending['movies'][choice]
        pending_list.append(seat_and_username)
        self.write_in_json()
        
            

c1 = CustomerData()
c1.preparing_data()

c2 = CustomerBooking()
c2.read_from_json()
c2.view_movies()
c2.booking_movie()



