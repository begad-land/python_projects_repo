
import json

x = {
    'movies':
        {
            'x':[1,2,3,4,5],
            'y':[6,7,8,9,10],
        }
}



movie_name = input('insert movie name to watch ')
user_name = input('insert your user name ')
seat_id = input('insert seat id ')


data = [user_name,seat_id]
def write_json(json_dict):
    
    print(json_dict)
    json_obj = json.dumps(json_dict,indent=2)
    with open('text.json', 'w') as f:
        f.write(json_obj)
    
with open('text.json','r') as f:
    json_dict = json.loads(f.read())
 

with open('movies\pending.json','r') as f:
    data_dict = json.loads(f.read())       

movie_list = data_dict['movies'][movie_name] 

data = [user_name,seat_id]

movie_list.append(data)

write_json(json_dict)


