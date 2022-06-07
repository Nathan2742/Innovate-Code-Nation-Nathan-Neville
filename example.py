# import random

# greeting = "Hello world"
# print(greeting)
# print(len(greeting))
# print(greeting[1])

# w_amount =100
# account_num = 12345678

# def cash_withdrawal(amount, accnum):
#     print(f"withdrwing {amount} from account {accnum}")

# cash_withdrawal(w_amount, account_num)
# cash_withdrawal(300, 50449921)
# cash_withdrawal(30, 50449921)



##### Activity 1 


welcome = "Welcome to Code Nation"
print(len(welcome))
welcome = len(welcome)

def string_length():
    if welcome == 22:
        print(f"{welcome} Has an even amount of letters")
    else:
        print(f"{welcome} Has an odd amount of letters")


string_length()

# message_var = 'Welcome to Code Nation'

# def isEven(str1):
#     str_mod = (len(str1) % 2)
#     if str_mod == 0:
#         print(f'{str1} has an even number of letters, {len(str1)}')
#     else:
#         print(f'{str1} has an odd number of letters, {len(str1)}')

# isEven(message_var)

####### Activity 2

alpha = [
    'a','b','c',
    'd','e','f',
    'g','h','i',
    'j','k','l',
    'm','n','o',
    'p','q','r',
    's','t','u',
    'v','w','x',
    'y','z'
]

# def iteration(list_selected):
#     for x in list_selected:
#         print(x)

# def user_selection_list(list_selected):
#     user_input = int(input('Please select a number: '))
#     print(f'Number {user_input} is {list_selected[user_input -1]}')

# iteration(alpha)
# user_selection_list(alpha)

# def get_usernum():
#     usernum = input("please enter a number between 1 and 26!")
#     usernum = int(usernum) - 1
#     print(alpha[usernum].upper())

# get_usernum()


# import random as r
# cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


# def print_board():
#     print(f"|{cells[0]}|{cells[1]}|{cells[2]}|\n")
#     print(f"|{cells[3]}|{cells[4]}|{cells[5]}|\n")
#     print(f"|{cells[6]}|{cells[7]}|{cells[8]}|\n")


# def make_move(p, c):
#     while True:
#         cell = int(input("Pick a cell 0-8\n"))
#         if (cells[cell] == " "):
#             cells[cell] = p
#             break

#     while True:
#         cell = r.randint(0, 8)
#         if (cells[cell] == " "):
#             cells[cell] = c
#             break


# def check_for_three(c):
#     if cells[0] == c and cells[1] == c and cells[2] == c:
#         return True
#     if cells[3] == c and cells[4] == c and cells[5] == c:
#         return True
#     if cells[6] == c and cells[7] == c and cells[8] == c:
#         return True
#     if cells[0] == c and cells[3] == c and cells[6] == c:
#         return True
#     if cells[1] == c and cells[4] == c and cells[7] == c:
#         return True
#     if cells[2] == c and cells[5] == c and cells[8] == c:
#         return True
#     if cells[0] == c and cells[4] == c and cells[8] == c:
#         return True
#     if cells[2] == c and cells[4] == c and cells[6] == c:
#         return True
#     return False


# def game_end_check():
#     if check_for_three("0") or check_for_three("X"):
#         return True
#     else:
#         return False


# def start_game():
#     player = input("Choose 0 or X\n")
#     if player == "0":
#         cpu = "X"
#     else:
#         cpu = "0"
#     print_board()
#     while game_end_check() == False:
#         make_move(player, cpu)
#         print_board()

# start_game()


print (int(5.4))
print (int(54))

# you cant convert a string data type that is not a num value

print(float(54))
print(float("54"))

print(str(54))
print(str(54.0))


print("what is your name ?")
name = input()

if name:
    print(f"hello {name}, how are you ?")
else:
    print("you did not give me your name!")
    

def add_up(): 
    num1 = input("What is the first number you'd like to add up? \n") 
    num2 = input("What is the second number you'd like to add up? \n") 
    try:
        print(f"{num1} + {num2} is {(int(num1) + int(num2))}!") 
    except: 
        print("\n ERROR: please input only numerical values. \n") 
        print("**************************** \n") 
        add_up() 
add_up() 