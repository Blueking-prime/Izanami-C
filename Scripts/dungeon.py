from random import randint, random

dungeon_sample = [
    ["█", "I", "-", "-", "-", "-", "█", "█"],
    ["█", "█", "█", "-", "T", "-", "-", "█"],
    ["█", "-", "-", "-", "-", "-", "O", "█"],
    ["█", "█", "-", "T", "-", "-", "█", "█"],
    ["█", "█", "█", "-", "-", "█", "█", "█"]
]


def rand_coord(width: int, height: int):
    return (randint(0, width - 1), randint(0, height - 1))


def rand_spread(chance: float, limit: int):
    n = 0
    while random() < chance and n < limit:
        n += 1
    return n


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


def generate_dungeon_layout(width: int, height: int):
    width -= 1
    height -= 1
    filled_coords = []

    # Start point
    start = rand_coord(width, height)
    filled_coords.append(start)

    # Exit
    stop = rand_coord(width, height)
    while stop in filled_coords:
        stop = rand_coord(width, height)
    filled_coords.append(stop)

    # Treasure Chests
    treasure_no = 1 + rand_spread(0.2, 5)
    treasures = []
    for i in range(treasure_no):
        coord = rand_coord(width, height)
        treasures.append(coord)
        filled_coords.append(coord)

    # Walls
    walls = []
    for i in range(width + 1):
        for j in range(height + 1):
            if i == 0 or j == 0 or i == width or j == height:
                chance = 0.7
            else:
                chance = 0.3

            if (i, j) not in filled_coords:
                wall_chance = rand_spread(chance, height/2)
                for k in range(wall_chance):
                    coord = i, j + k
                    if coord in filled_coords or coord[1] > height:
                        break
                    else:
                        walls.append(coord)
                        filled_coords.append(coord)

    return {'start': start,
            'stop': stop,
            'dimensions': (width + 1, height + 1),
            'treasures': treasures,
            'walls': walls,
            'filled_coords': filled_coords}

def verify_dungeon(dungeon: dict):
    if not path(dungeon.get('start'), dungeon.get('stop'),
                dungeon.get('walls'), dungeon.get('dimensions')[0],
                dungeon.get('dimensions')[1], []):
        return False

    for i in dungeon.get('treasures'):
        if not path(dungeon.get('start'), i, dungeon.get('walls'),
                    dungeon.get('dimensions')[0], dungeon.get('dimensions')[1], []):
            return False
    else:
        return True


def display_dungeon(dungeon: dict):
    dungeon_map = [['-' for _ in range(dungeon.get('dimensions')[0])]
                   for _ in range(dungeon.get('dimensions')[1])]

    # Start
    dungeon_map[dungeon.get('start')[1]][dungeon.get('start')[0]] = 'I'

    # Stop
    dungeon_map[dungeon.get('stop')[1]][dungeon.get('stop')[0]] = 'O'

    for i in dungeon.get('treasures'):
        dungeon_map[i[1]][i[0]] = 'T'

    for i in dungeon.get('walls'):
        dungeon_map[i[1]][i[0]] = '█'

    for i in dungeon_map:
        print(i)

def create_dungeon(width = 8, height = 5, dungeon: dict | None = None):
    if dungeon:
        display_dungeon(dungeon)
    else:
        check = False
        while not check:
            dungeon = generate_dungeon_layout(width, height)
            check = verify_dungeon(dungeon)
        display_dungeon(dungeon)




if __name__ == '__main__':
    create_dungeon()
