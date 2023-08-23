import random

end_game = False


def check_isdigit(number):
    """ 추가 도전 과제 - 1:  범위 내의 숫자 확인 """
    if not number.isdigit():
        print("Write the NUMBER !!")
        return False
    if int(number) > 100 or int(number) < 1:
        print("Enter a number between 1 and 100.")
    else:
        return True


def ask_end():
    """ 추가 도전 과제 -2: 재시작 확인 """
    end = input("Retry? ")
    if end in ["Yes", "yes", "YES"]:
        return False
    if end in ["No", "NO", "no"]:
        return True
    else:
        print('Yes or No')
        return ask_end()


def start_game():
    """ 숫자 게임"""
    random_number = random.randint(1, 100)
    count = 0

    print("START!")

    while True:
        count += 1
        answer = input()
        if check_isdigit(answer):
            answer = int(answer)
            if answer == random_number:
                print(f'You WIN! score: {count}')
                end = ask_end()
                if end:
                    break
                else:
                    return start_game()
            elif answer > random_number:
                print("Down")
            elif answer < random_number:
                print("UP")
        else:
            continue


while not end_game:
    start = input("start? Yes/Yes ")
    if start in ["Yes", "yes", "YES"]:
        start_game()
        end_game = True
    else:
        print("Say Yes.")
        continue
