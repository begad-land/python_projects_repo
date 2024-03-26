
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
        
        while self.name not in self.database or self.password != self.database[self.name][1] :
            print("-----------------------------------------------\nWrong username or password. Try again")
            self.name = input('insert your name ')
            self.password = input('insert your password ')
        
        print(f'welcome {self.name}')
        
        
    def sign_up(self):
        self.c_id = f'#v_{rn.randint(10000, 999999)}'
        self.name = input('insert your name ')
        self.email = input('insert your email ')
        self.phone_number = input('insert your phone number ')
        self.password = input('insert password ')
        
        while self.name in self.database:
            print(f'\n{self.name} is taken. Try a different one')
            self.name = input('insert your name ')
            self.email = input('insert your email ')
            self.phone_number = input('insert your phone number ')
            self.password = input('insert password ')
        
        with open('movies/c_data.txt', 'a') as file :
            file.writelines(f'{self.c_id}-{self.name}-{self.password}-{self.email}-{self.phone_number}\n')  
        return True 


class CustomerBooking():
    def __init__(self,chosen_movie = None ,movies = {}) -> None:
        self.chosen_movie = chosen_movie
        self.movies = movies

    def get_movies(self):
        with open('movies/movies.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                data = line.split('-')
                data[2] = data[2].replace('\n' , '')
                self.movies[data[0]] = [
                                        data[1] , data[2]
                                        
                                       ] 

    def view_movies(self):
        print('---------------------available movies--------------------')
        for title , data in self.movies.items():
            print(f'Title: {title}\nGenre: {data[0]}\nSeats: {data[1]}\n----------------------------------------------')

c = CustomerBooking()
c.get_movies()
c.view_movies()
