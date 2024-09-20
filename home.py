# # a = [1,1,2,3,465,6]
# # b = [1,2,3,4,5,6,7,8,9,10]

# # c = set(a+b)
# # print(c)

# # user_number = int(input('Please enter a prime number: '))

# # if user_number > 1:
# #     for num in range(2, user_number):
# #         if (user_number % num) == 0:
# #             print(f"{user_number} is not a prime number")
# #             break
# #         else:
# #             print(f'{user_number} is a prime number')

# # else:
# #     print(f'{user_number} is not a prime number')


# #      a = b[::len(b)-1]
# #      print(str(a))
    
# # first_and_second()


# # from sympy import * 

# # num1 = isprime(int(input('Enter a prime  number: ')))

# # if num1 is False:
# #     print(f'That is not a prime number')
# # else:
# #     print(f'This is a prime number')    

# # user_number = int(input('Enter a number: '))
# # number = [num for num in range(2,user_number) if user_number % num ==0]

# # def isprime(n):
# #     if user_number > 1:
# #         if len(number) == 0:
# #             print('It is prime')
# #         else:
# #             print('This is not a prime')
# #     else:
# #         print('Nt a prime number')

# # isprime(user_number)
# #first and last
# # b = [1,2,3,4,5,6,7,8,9,10]

# # def first_and_second():
# #     a = b[::len(b)-1]
# #     print(a)

# # first_and_second()
# # fibo

# #fibbonaci

# # fib = [0,1]

# # def fibonnaci(num):
# #     if num < 0:
# #         print('That is not going to work')
# #     elif num < len(fib):
# #         return fib[num]
# #     else:
# #         fib.append(fibonnaci(num-1) + fibonnaci(num-2))
# #         return fib[num]
    

# # print(fibonnaci(1))

# # def rcursive_fibonnaci(num):
# #     if num <= 1:

# #         return num



# # name = input("Please enter your name: ")
# # age = int(input('Please enter you age: '))
# # result = 100- age
# # print(f'{name} will turn a 100 years old in {result} years')


# #Ask user for input number
# # def odd_or_even():

# #     number = int(input('Enter a number :'))
# #     if number % 2 != 0:
# #         print('This is a odd number ')
# #     else:
# #         print('This is even number')

# # def less_than_five():

# #     a = [1,2,3,4,5,6,7,8,9,10]
# #     b = [num for num in a if num < 5]
# #     print(b)

# # less_than_five()

# # def divs():

# #     number = int(input("Please enter a number: "))
# #     nums = list(range(1,number+1))
# #     dividiers = []
# #     for n in nums:
# #         if number % n ==0:
# #             dividiers.append(n)
            
# #     print(dividiers)
# import random


#     # number = int(input('Number please '))
#     # nums = list(range(1, number+1))
#     # divisor = []

#     # for n in nums:
#     #     if number % n == 0:
#     #         divisor.append(n)
        
        
            

#     # print(divisor)

#     a = random.sample(range(1,20),5)
#     b = random.sample(range(1,20),5)
#     print(a)
#     print(b)
#     print(set(a+b))


#     pali = (input('Type a palindrom '))
#     return str(pali[::-1]) 

    # a = random.sample(range(1,20),5)
    # print(a)
    # b =[num for num in a if num % 2 ==0]
    # return b
 #player input
    # player1 = input('Ready player 1: ')
    # player2 = input('Ready player 2: ')

    # #loop to strat the game
    # while True:
    #     if player1.lower() == 'rock':
    #         print('Rock wins')
    #     else:
    #         print('Paper wins')
        

    # """Please pick one:
    #         rock
    #         scissors
    #         paper"""
    
    # while True:
    #     game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    #     player_1 = input('Please choose your weapon ')
    #     player_2 = input('Please choose your weapon ')
    #     p1 = game_dict.get(player_1.lower())
    #     p2 = game_dict.get(player_2.lower())
    #     game_diff = p1 - p2

    #     if game_diff in [-1,2]:
    #         print('Player one wins')
    #         if input('Do you want to play again, y/n\n').lower()== 'yes':
    #             continue
    #         else:
    #             print("Ciao for now")
    #             break

    #     elif game_diff in [-2,1]:
    #         print('Player 2 wins')
    #         if input('Do you want to play again, y/n\n').lower()== 'yes':
    #             continue
    #         else:
    #             print("Ciao for now")
    #             break
    #     else:
    #         print('Draw, hey, please continue')
    #         print('')
# import random
# def divs():
    
#     b = random.sample(range(1,10),1)    Q
#     guess = 0
#     count = 0
#     for num in b:
       
#         while guess != num and guess != 'exit':
#             # guess = input('Please neter a number ')
#             if guess == 'exit':
#                 print('Goodbye')
#                 break
#             guess = int(input('Enter a number'))
#             count += 1 
#             if num > guess:
#                 print('That is too low')
#                 continue
#             elif num < guess:
#                 print('That is too high')
#                 continue
#             elif num  == guess:
#                 print('You got it right')
#                 print(f'You had {count} attempts')
        

# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
# import random
# def r_number():
#     ran_number = random.sample(range(1,11), 5)
#     guess = 0
#     count = 0

#     for num in ran_number:
        
#         while guess != num and guess != 'exit':
#             if guess == 'exit':
#                 print('Have a nice day')
#                 break
            
#             guess = int(input('Please enter a number from 1 to 10: '))
#             count += 1
#             if num < guess :
#                 print('Too high')
#             elif num > guess :
#                 print('too loo') 
#             elif num  == guess :
#                 print(f'Congrats you got the right number')
#                 print(f'You had {count} attempts')
#         break
        

# from sympy import *

# number = isprime(int(input('Please enter a number: ')))
# if number == False:
#     print('This is not a prime number')
# else:
#     print('This is a prime number')

import random
# a = random.sample(range(1,10),5)
# print(a)
# b = a[::len(a)-1]
# print(b)


# def abc():
#     a = [1,2,3,4,5,5,6,4,6]
#     b =[]
#     c = [num for num in a if num in a and not num in b]
#     print(c)

# import random
# from functools import reduce
# def abc():
#     r_s = input('Please type a sentence: ')
#     # reverse_str = reduce(lambda x, y: y +x, r_s)
#     # print(reverse_str)
#     for i in r_s:
#         r_s = i +r_s
#     return r_s


from functools import reduce

def abc():
    user_sentence = input('Type a sentence: ')
    reverse_string = reduce(lambda x,y: y+x, user_sentence)
    