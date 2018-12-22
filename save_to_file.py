import random


def saveDetails(name, score):
    '''
    Param: Name, Score
    '''
    playerinfo = open('player_info.txt', 'a')
    player_random_id = random.randint(0, 1000)
    playerinfo.write(f"\n{player_random_id}\t{name}\t{score}")
    return 0
