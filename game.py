from gamefunctions import put_stone, get_bunches, take_from_bunch, game_over

put_stone()
user_number = 1
while True:
    print('Текущая позиция')
    print(get_bunches())
    print('Ход игрока №', user_number)
    pos = int(input('Откуда берем? '))
    qua = int(input('Сколько берем? '))
    user_number = 2 if user_number == 1 else 1
    if game_over():
        break

print('Выйграл игрок номер {}'.format(user_number))