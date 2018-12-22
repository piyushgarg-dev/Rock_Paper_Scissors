# <--import section-->
'''
This is a Simple Rock Paper Scissor Game Made By Piyush Garg
'''

import rule
from play_game import game_on


# <-Welcome Msg->

print("Welcome To Stone Paper Scissors by Piyush Garg")

# <- name of the current player ->
name = input('Please Enter Your Name: ')

# <- Rules from rules.py->
print(rule.rules)

option = input('Are You Ready? Y/N :  ')

if option.lower() == 'y':
    game_on(name)
else:
    pass
