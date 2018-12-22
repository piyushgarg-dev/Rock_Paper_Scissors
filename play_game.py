import random
from save_to_file import saveDetails


def game_on(Player_Name):
    '''
    Param: Player_Name
    Type: String
    Func: Actually Excutes Game On Mode

    '''

    print(f"Welcome {Player_Name}")

    computer_options = ('rock', 'paper', 'scissor')
    human = ''
    choice = 0
    life = 7
    score = 0

    while True:
        human = input('Rock Paper Scissors? : ')
        human = human.lower()
        choice = random.randint(0, 2)
        computer = computer_options[choice]

        # <- Human = Rock ->
        if human == 'r' and computer == 'rock':
            print("It's a drew")
            continue
        if human == 'r' and computer == 'paper':
            print("Computer Wins!!")
            life -= 1
            score -= 1
            if life <= 0:
                break
            else:
                continue
        if human == 'r' and computer == 'scissor':
            print(f'{Player_Name} wons!')
            score += 1
            continue

        # <- Human = Paper ->
        if human == 'p' and computer == 'paper':
            print("It's a drew")
            continue
        if human == 'p' and computer == 'scissor':
            print("Computer Wins!!")
            life -= 1
            score -= 1
            if life <= 0:
                break
            else:
                continue
        if human == 'p' and computer == 'rock':
            print(f'{Player_Name} wons!')
            score += 1

        # <- Human = Scissors ->
        if human == 's' and computer == 'scissor':
            print("It's a drew")
            continue
        if human == 's' and computer == 'rock':
            print("Computer Wins!!")
            life -= 1
            score -= 1
            if life <= 0:
                break
            else:
                continue
        if human == 's' and computer == 'paper':
            print(f'{Player_Name} wons!')
            score += 1
            continue
        if human == 'exit':
            break
    print("\n\n Game Over!")
    print(f"You Scored {score} points")
    saveDetails(Player_Name, score)
