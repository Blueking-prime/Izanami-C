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

def dialog_choice(prompt, choices: list = ['Yes', 'No']):
    while True:
        try:
            print(prompt)
            for i, j in enumerate(choices, 1):
                print(f'{i} - {j}')
            x = int(input('? '))
            if x not in range(1, len(choices) + 1):
                print('Invalid option!')
                continue

            if choices == ['Yes', 'No']:
                if x == 1:
                    return True
                if x == 2:
                    return False
            else:
                return x
        except ValueError:
            print('Invalid option!')
            continue
