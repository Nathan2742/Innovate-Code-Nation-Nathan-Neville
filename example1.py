# def add_up(): 
#     num1 = input("What is the first number you'd like to add up? \n") 
#     num2 = input("What is the second number you'd like to add up? \n") 
#     try:
#         print(f"{num1} + {num2} is {(int(num1) + int(num2))}!") 
#     except: 
#         print("\n ERROR: please input only numerical values. \n") 
#         print("**************************** \n") 
#         add_up() 
# add_up() 

# scope is about where somthing is 

from ast import Num
from lzma import FILTER_LZMA2


light= False

def light_switch():
    global light ## this is how we fix the error described below.
    if light:
        print("whoa! its bright in here")
        light = False
    else:
        print("who turned out the lights?")
        light = True

light_switch()
light_switch()

# above this code will give an error as the light variable is globale but also local but as it is global 
# this means it cant update as light is set as a global variable.

def show_num():
    num=13
    print(num)

num = 10

show_num()

# local vaibale is found inside the function

#########

# both lists and tuples are shown as values

# lists are muteable and tuples are immutable

even_nums = [2, 4 ,6, 8, 10] #mutable meaning we can cahnge it 
odd_nums = (1, 3, 5, 7, 9) # immutable meaning we cannot change whats inside it 

even_nums[-1] = "ten"

# odd _nums[-2] = num = "nine"  this throws an error.

###########

# slicenotation ########

my_list = [
    1,2,3,4,5,6,7,8,9
]

print(my_list[-3])
print(my_list[0:5])

# my_list[start:stop] this is an example if we want a slice of the data and where we want to start and stop 

# while True ########

## while game:
## all of game input checks 
## q pressed or esc press : 
############### break

# loop_runs = true 
# while loop_runes:
#print("run the loops")
#do somthing 

# to stop the loop 
#loop_runs stop

# want a different way of while loops to stop and carry on we can use continue and stop
# loop = True
# name = "Nathan"
# while loop:
#     if name != "Nathan":
#         print(hello Nathan)
#         break
#     else:
#         print(f"welcome{name}!")
#         continue

## Activty one

# def user_choice():
#     choice_check = False
#     while choice_check == False:
#         user_input = input('Please enter a number: \n')
#         if user_input.isnumeric():
#             print(f'{user_input} is a number!')
#             user_input = int(user_input)
#             print(type(user_input))
#             choice_check = True
#         else:
#             print(f'{user_input} is not a number!')
            

# user_choice()

def enter_num():
    num = input("Please enter number here..")
    if num.isnumeric():
        num = int(num)
        print(f"{num} is a number! entered as a string and converted to a interger")
    else:
        print("oops this is not a number try again..")
        enter_num()


enter_num()

### Activity two

###### EXAMPLE 
# from random import randint as r

# ghost_chars = [
#     'Peter Venkman', 'Raymond Stantz', 'Egon Spengler',
#     'Winston Zeddemore', 'Dana Barrett', 'Lenny Clotch',
#     'Janine Melnitz', 'Louis Tully', 'Walter Peck',
#     'Joanne Phillips', 'Sammy Kipper', 'George Washington',
#     'Frank Joslin', 'Meryl Campbell', 'John Plisken',
#     'John Conner', 'Kyle Reece', 'Sarah Connor'
# ]
# hscore = 0

# def ghost_game(char_list):
#     p_lives = 3
#     p_score = 0
#     print('You have 3 lives, would you like to begin? Press enter to continue')
#     input()
#     while p_lives > 0:
#         question = r(0, 17)
#         pressed_question = char_list[question]
#         print(f'is {pressed_question} in the Ghostbusters film? [Y/N]\n')
#         user_answer = input()
#         if question <= 8:
#             match user_answer.capitalize():
#                 case 'Y' | "YES":
#                     print(f'{pressed_question} is indeed a charater in the movie!')
#                     p_score += 1
#                 case 'N' | "NO":
#                     print(f'{pressed_question} is not a charater in the movie!')
#                     p_lives -= 1
#         else:
#             match user_answer.capitalize():
#                 case 'Y' | "YES":
#                     print(f'{pressed_question} is not a charater in the movie!')
#                     p_lives -= 1
#                 case 'N' | "NO":
#                     print(f'{pressed_question} is indeed a charater in the movie!')
#                     p_score += 1
#     print('You have run out of lives! GAME OVER!!!!')
#     return p_score

# while True:
#     score = ghost_game(ghost_chars)
#     if score > hscore:
#         print(f'New High Score!! {score} Points!')
#         hscore = score
#     else:
#         print(f'High Score remains at {previous_score} Points!')
#     p_continue = input('Play again? Y | N')
#     match p_continue.capitalize():
#         case 'Y' | 'N':
#             print('Starting a new game')
#         case 'N' | 'NO':
#             print('Have a good day!')
#             break
######## EXAMPLE ^^^^^^

list1 = [
    "action",
    "comedy",
    "fantasy"
]





def start():
    print("Do you like ghostbusters? well we are about to find out!")
    answer = input("Who does Bill murray play ?")
    if answer == "dr peter venkman":
        print("That is correct!! ")
    elif answer == "peter venkman":
        print("That is correct!")
    else:
        print("hhmm that doesnt sound right try again!")
        start()


start()

