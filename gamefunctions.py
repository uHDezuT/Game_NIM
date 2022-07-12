from random import randint

_holder = []



def put_stone():
    global _holder
    _holder = []
    for i in range(5):
        _holder.append(randint(1, 20))

def take_from_bunch(position, quantity):

    if quantity > _holder[position - 1]:
        print('Нельзя взять столько камней')
    else:
        if 1 <= position <= len(_holder):
            _holder[position - 1] -= quantity






def get_bunches():
    return _holder

def game_over():
    return sum(_holder) == 0