
import random as rn
import json
#TODO
#you are viewing the seats and tickets perfectly now group everythin in a composing class and givebthe user the ability 
#to navigate through the program and do diffrent things like: view movies, view bookings in the future you should create 
#the option for the user to remove a booking but thats later bca u got more important shit to do (courses)

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
    def __init__(self,chosen_movie = None ,json_movies = {} , pending = {} , user_name = None, booked = {}, 
                customer_tickets = {}, movie_seats = {}, ) -> None:
        self.chosen_movie = chosen_movie
        self.json_movies = json_movies
        self.pending = pending
        self.customer_data = CustomerData()
        self.user_name = self.customer_data.log_in()
        self.booked = booked
        self.customer_tickets = customer_tickets
        self.movie_seats = movie_seats
        

    def write_in_json(self):
        json_obj = json.dumps(self.pending, indent = 2)

        with open('movies\pending.json' , 'w') as f:
            f.write(json_obj)
            
        
    
    def read_from_json(self):
        with open('movies\movies.json' , 'r') as f:
            self.json_movies = json.loads(f.read())
            
        with open('movies\pending.json' , 'r') as file:
            self.pending = json.loads(file.read())
            
            
        with open('movies/booked.json' , 'r') as file3:
            self.booked = json.loads(file3.read())    

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
        print('movie booked successfully :O')
        self.write_in_json()        
            


    def gather_tickets(self):
        for title, data in self.booked['movies'].items():
            self.movie_seats[title] = [[],[]]
        
        for title, data in self.booked['movies'].items():
            for datum in data:
                if self.user_name == datum[0]:    
                    self.movie_seats[title][0].append(datum[1]) #seats
                    self.movie_seats[title][1].append(datum[2]) #tickets
                    
                                
    def show_tickets(self):
        for title, data in self.movie_seats.items():
            if len(data[0]):
                seats = str(data[0])[1:-1]
                tickets = str(data[1])[1:-1]
                print(f'{title}:\nSeats booked: {seats}\nTickets: {tickets}\n----------------------------------------')


    
    
class Customer:
    def __init__(self) -> None:
        self.c_data = CustomerData()
        self.c_data.preparing_data()
        self.c_booking = CustomerBooking()
        self.c_booking.read_from_json()
        
    def c_ops(self):
       print(f'------------------------------\n1)View movies\n2)View bookings\n3)Log out')
       operation = input('what would you like to do ')
       
       if operation == '1':
               self.c_booking.view_movies()
               self.c_booking.booking_movie()

       elif operation == '2':
               self.c_booking.gather_tickets()
               self.c_booking.show_tickets()
               
       elif operation == '3':
           exit()
           


c = Customer()
while True:
    c.c_ops()
