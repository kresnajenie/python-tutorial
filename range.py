import random

while True:
    print("9 untuk keluar")
    print("0 untuk batu")
    print("1 untuk kertas")
    print("2 untuk gunting")
    user_input = int(input())
    komputer = random.randint(0,3)
    suit = ["batu", "kertas", "gunting"]
    print(user_input)
    print(f'Komputer pilih {komputer}')
    
    if user_input == 0:
        if komputer == 0:
            print("seri")
            print(f'Komputer pilih {suit[komputer]}')
        elif komputer == 1:
            print("kalah")
            print(f'Komputer pilih {suit[komputer]}')
        elif komputer == 2:
            print("menang")
            print(f'Komputer pilih {suit[komputer]}')
    elif user_input == 1:
        if komputer == 0:
            print("menang")
            print(f'Komputer pilih {suit[komputer]}')
        elif komputer == 1:
            print("seri")
            print(f'Komputer pilih {suit[komputer]}')
        elif komputer == 2:
            print("kalah")
            print(f'Komputer pilih {suit[komputer]}')
    elif user_input == 2:
        print("2223222222")
        if komputer == 0:
            print("kalah")
            print(f'Komputer pilih {suit[komputer]}')
        elif komputer == 1:
            print("menang")
            print(f'Komputer pilih {suit[komputer]}')
        elif komputer == 2:
            print("seri")
            print(f'Komputer pilih {suit[komputer]}')
    elif user_input == 9:
        break


