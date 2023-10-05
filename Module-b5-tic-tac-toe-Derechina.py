print("Крестики-нолики")

screen = list(range(1, 10))


def draw_board(screen):
    print("-" * 13)
    for i in range(3):
        print("|", screen[0 + i * 3], "|", screen[1 + i * 3], "|", screen[2 + i * 3], "|")
        print("-" * 13)


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Введите номер ячейки от 1 до 9 для " + player_token + ": ")
        try:
            player_answer = int(player_answer)
        except Exception as player_answer:
            print("Некорректный ввод. Вы уверены, что ввели число?", player_answer)
            continue
        if 1 <= player_answer <= 9:
            if str(screen[player_answer - 1]) not in "XO":
                screen[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win():
    victories = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in victories:
        if screen[each[0]] == screen[each[1]] == screen[each[2]]:
            return screen[each[0]]
    return False


def main(screen):
    counter = 0
    win = False
    while not win:
        draw_board(screen)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win()
            if tmp:
                print(tmp, "выиграл!")
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(screen)


main(screen)

input("Нажмите Enter для выхода!")
