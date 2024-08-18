from random import randint
from random import shuffle

special_char = [ chr(x) for x in range(33, 48)] + [chr(x) for x in range(58, 65)] + [chr(x) for x in range(91, 97) ]
alphabets_capital = [chr(x) for x in range(65, 91)] 
alphabets_small = [chr(x) for x in range(97, 123)]
numbers = [chr(x) for x in range(48,58)]

default = 2
new_password = ''

def int_inputs():
    password = []
    special_char_len = int(input('Enter the number of special chaarcters required :'))
    alphabets_capital_len = int(input('Enter the capital alphabet required :'))
    alphabets_small_len = int(input('Enter the small alphabet required :'))
    numbers_len = int(input('Enter the number required :'))
    if special_char_len < 1 or alphabets_capital_len < 1 or alphabets_small_len <1 or numbers_len < 1:
        print('please enter the positive numbers only : ')
        if int(input('if you want to take default numbers press 1 ')) == 1:
            special_char_len = alphabets_capital_len = alphabets_small_len = numbers_len = default
        else:int_inputs()
    
    password = [
       [ special_char[randint(0,len(special_char)-1)] for i in range(special_char_len) ] 
     + [ alphabets_capital[randint(0,len(alphabets_capital)-1)] for i in range(alphabets_capital_len) ]
     + [ alphabets_small[randint(0,len(alphabets_small)-1)] for i in range(alphabets_small_len) ] 
     + [ numbers[randint(0,len(numbers)-1)] for i in range(numbers_len) ]
    ]


    return password[0]

password = int_inputs()
shuffle(password)

for i in password:
    new_password+=i
print(new_password)