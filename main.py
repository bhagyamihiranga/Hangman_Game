import random
import function
import pandas as pd
import socket

host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
db_cursor = function.connection.cursor_object
db_cursor.execute("SELECT (words) FROM words")
result = db_cursor.fetchall()

db_connection = function.connection.db
r_n_d = random.choice(result)
random_name_database = r_n_d[0]

user_name = input('enter your name to begin the game : ')

dif = True
game_attempt = 0
while dif:
    game_difficulty = input('enter difficulty (easy,medium,hard) :')
    if game_difficulty == "easy" : 
    
        game_attempt = 15
        dif = False
    elif game_difficulty == "medium":
        game_attempt = 10
        dif = False
    elif game_difficulty == "hard":
        game_attempt = 5
        dif = False
    else :
        print('enter correct difficulty to continue')
        





random_name_array = []
user_guess_array = []

for i in random_name_database:
  
  random_name_array.append(i)
  
  




    
while game_attempt >= 1:
    
   user_gess_input = input(f'hy,{user_name} guess the name to save the hangman : ')
   print(f'you still have {str(game_attempt)} left')
   
   
   tmp_attemp_status = False
   for count,x in enumerate(user_gess_input,0):
        
        if user_gess_input[count] in random_name_array:
             tmp_attemp_status = True
             
             if user_gess_input[count] in user_guess_array:
                    continue
             else:
                 
                 if function.find_repeats(user_gess_input[count],random_name_array) != 0:
                        for io in range(function.find_repeats(user_gess_input[count],random_name_array)):
                            
                              user_guess_array.append(user_gess_input[count])
                              order_index = {value: index for index, value in enumerate(random_name_array)}
                              user_guess_array = sorted(user_guess_array, key=lambda x: order_index.get(x, len(random_name_array)))
                 else:
                         continue
        else:
            tmp_attemp_status = False
   if tmp_attemp_status == False:
      game_attempt -= 1  
   
   print(f'word be : {user_guess_array}')
   if len(random_name_array) ==  len(user_guess_array):
        
        print(f'you won name is {random_name_database}')
        db_cursor.execute("INSERT INTO logs (ip,level,message) VALUES (%s,%s,%s)",(ip_address,game_difficulty,f"Won Hang Man Game With Remain Attemps {game_attempt} and the name was {random_name_database}"))
        db_connection.commit()
        db_connection.close()
        break
  

if game_attempt == 0:
      print(f'you lose name is {random_name_database}')
      db_cursor.execute("INSERT INTO logs (ip,level,message) VALUES (%s,%s,%s)",(ip_address,game_difficulty,f"Lose Hang Man Game and the name was {random_name_database}"))
      db_connection.commit()
      db_connection.close()

       