from random import randint, random


def rand_coord(width: int, height: int):
    return (randint(0, width - 1), randint(0, height - 1))


def rand_spread(chance: float, limit: int):
    n = 0
    while random() < chance and n < limit:
        n += 1
    return n


def rand_chance(chance: float):
    if random() < chance:
        return True
    else:
        return False


def path(start: tuple[int, int], goal: tuple[int, int],
        walls: list[tuple], width: int, height: int, visited: list = []):

    if start in walls:
        return False

    x, y = start
    l = (x - 1, y)
    r = (x + 1, y)
    u = (x, y - 1)
    d = (x, y + 1)

    # Check if goal is next to path
    if start == goal or u == goal or d == goal or l == goal or r == goal:
        return True


    # If (x,y) is a valid node
    if (y >= 0 and y < height) and (x >= 0 and x < width):
        if start in visited:
            return False
        else:
            visited.append(start)

    # Recurse through all adjacent points
        up    = path(u, goal, walls, width, height, visited)
        if up:
            return True

        left  = path(l, goal, walls, width, height, visited)
        if left:
            return True

        down  = path(d, goal, walls, width, height, visited)
        if down:
            return True

        right = path(r, goal, walls, width, height, visited)
        if right:
            return True

    return False

# def dialog_choice(prompt: str, choices: list = ['Yes', 'No'], back = True):
#     low_limit = 1
#     if len(choices) == 0:
#         return -1
#     while True:
#         try:
#             print(prompt)
#             for i, j in enumerate(choices, 1):
#                 print(f'{i} - {j}')
#             if back:
#                 print('0 - back')
#                 low_limit = 0
#             x = int(input('? '))
#             if x not in range(low_limit, len(choices) + 1):
#                 print('Invalid option!')
#                 continue

#             if choices == ['Yes', 'No']:
#                 if x == 1:
#                     return True
#                 if x == 2:
#                     return False
#             else:
#                 return x
#         except ValueError:
#             print('Invalid option!')
#             continue


def dialog_choice(prompt: str, choices: list[str] = ['Yes', 'No'], back = True):
    low_limit = 1
    if len(choices) == 0:
        return -1
    while True:
        try:
            print('')
            print(prompt)

            structured_choices = {j: i for i, j in enumerate(choices, 1)}
            filtered_choices = [i for i in choices if i]

            for i, j in enumerate(filtered_choices, 1):
                print(f'{i} - {j}')
            if back:
                print('0 - back')
                low_limit = 0

            x = int(input('? '))
            if x not in range(low_limit, len(filtered_choices) + 1):
                print('Invalid option!')
                continue

            if choices == ['Yes', 'No']:
                if x == 1:
                    return True
                if x == 2:
                    return False
            else:
                if x == 0:
                    return -1

                choice = filtered_choices[x - 1]
                x = structured_choices[choice]
                return x

        except ValueError:
            print('Invalid option!')
            continue


def dialog_choice_shop(prompt: str, choices: dict[str, int]):
    if len(choices) == 0:
        return -1
    while True:
        try:
            print('')
            print(prompt)
            print('S/N - Name : Cost')
            for i, j in enumerate(choices.keys(), 1):
                print(f'{i} - {j} : {choices[j]}')
            print('0 - back')

            x = int(input('? '))
            if x not in range(0, len(choices) + 1):
                print('Invalid option!')
                continue

            if x == 0:
                return -1

            return list(choices.keys())[x - 1]
        except ValueError:
            print('Invalid option!')
            continue
