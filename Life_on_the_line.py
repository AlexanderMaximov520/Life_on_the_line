import time
import random
check_point = ""
while check_point != "Выход":
    print("Введите длину мира --> ", end="")
    length = int(input())
    print(length)
    empty_world, new_world, random_world = ["_" for j in range(length)], list(), ["0", "_"]
    print("Введите число поколений --> ", end="")
    generations = int(input())
    print(generations)
    print("Хотите ли вы сгенерировать случайный мир?")
    word = input()
    print(word)
    if word == "Да":
        world = [random.choice(random_world) for k in range(length)]
        print("Создан случайный мир:")
    else:
        print("Создайте свой мир:")
        world = list(input())
    print(*world)
    for g in range(generations - 1):
        if world == empty_world:
            print("Не осталось живых клеток.")
            break
        for i in range(len(world)):
            if len(world) - 1 == i:
                if world[0] == world[i - 1]:
                    new_world.append("_")
                else:
                    new_world.append("0")
            elif world[i + 1] == world[i - 1]:
                new_world.append("_")
            else:
                new_world.append("0")
        world, new_world = new_world, []
        time.sleep(0.5)
        print(*world)
    print("""Введите "Выход" для закрытия программы. Если вы хотите продолжить, введите пустую строку.""")
    check_point = input()
