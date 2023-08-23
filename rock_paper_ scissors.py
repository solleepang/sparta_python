import random


def game_result(com_hand, your_hand):
    """ 승패 판정 """
    win_hand = [('가위', '바위'), ('바위', '보'), ('보', '가위')]
    if com_hand == your_hand:
        return 'draw'
    else:
        win = win_hand.count((com_hand, your_hand))
        if win > 0:
            return 'win'
        else:
            return 'lose'


def play_rps():
    """ 가위 바위 보 게임 """
    hand = ['가위', '바위', '보']
    com_hand = random.choice(hand)
    your_hand = input("가위 바위 보? ")
    if your_hand not in hand:
        print("가위 바위 보 모름?")
    else:
        result = game_result(com_hand, your_hand)
        print(f'나: {com_hand} 너: {your_hand} 결과: {result}')
        return result


def start_game():
    """ 추가 도전 과제 - 1: 게임 통계 """
    win, lose, draw = 0, 0, 0

    while True:
        result = play_rps()
        if result == 'draw':
            draw += 1
        elif result == 'lose':
            lose += 1
        elif result == 'win':
            win += 1

        retry = input('다시? ')
        if retry == '다시':
            continue
        else:
            print('싫음 말고.')
            break

    print(f'승:{win} 패:{lose} 비김:{draw}')


start_game()
