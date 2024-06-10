from .. import utils

dungeon_sample = [
    ["█", "I", "-", "-", "-", "-", "█", "█"],
    ["█", "█", "█", "-", "T", "-", "-", "█"],
    ["█", "-", "-", "-", "-", "-", "O", "█"],
    ["█", "█", "-", "T", "-", "-", "█", "█"],
    ["█", "█", "█", "-", "-", "█", "█", "█"]
]


class Dungeon:
    def __init__(self, width = 8, height = 5, spawn_chance = 0.2, enemy_types = None) -> None:
        self.width = width
        self.height = height

        check = False
        while not check:
            self.generate_dungeon_layout()
            check = self.verify_dungeon()

        self.player_pos = self.start
        # self.spawn_chance = spawn_chance
        # self.enemy_types = enemy_types


    def generate_dungeon_layout(self):
        self.width -= 1
        self.height -= 1
        self.filled_coords = []

        # Start point
        self.start = utils.rand_coord(self.width, self.height)
        self.filled_coords.append(self.start)

        # Exit
        self.stop = utils.rand_coord(self.width, self.height)
        while self.stop in self.filled_coords:
            self.stop = utils.rand_coord(self.width, self.height)
        self.filled_coords.append(self.stop)

        # Treasure Chests
        self.treasure_no = 1 + utils.rand_spread(0.2, 5)
        self.treasures = []
        for i in range(self.treasure_no):
            coord = utils.rand_coord(self.width, self.height)
            self.treasures.append(coord)
            self.filled_coords.append(coord)

        # Walls
        self.walls = []
        for i in range(self.width + 1):
            for j in range(self.height + 1):
                if i == 0 or j == 0 or i == self.width or j == self.height:
                    chance = 0.7
                else:
                    chance = 0.3

                if (i, j) not in self.filled_coords:
                    wall_chance = utils.rand_spread(chance, self.height/2)
                    for k in range(wall_chance):
                        coord = i, j + k
                        if coord in self.filled_coords or coord[1] > self.height:
                            break
                        else:
                            self.walls.append(coord)
                            self.filled_coords.append(coord)

        self.width += 1
        self.height += 1


    def verify_dungeon(self):
        if not utils.path(self.start, self.stop, self.walls, self.width, self.height, []):
            return False

        for i in self.treasures:
            if not utils.path(self.start, i, self.walls, self.width, self.height, []):
                return False
        else:
            return True


    def display_dungeon(self):
        dungeon_map = [[' ' for _ in range(self.width)] for _ in range(self.height)]

        # Start
        dungeon_map[self.start[1]][self.start[0]] = 'I'

        # Stop
        dungeon_map[self.stop[1]][self.stop[0]] = 'O'

        # Player_pos
        dungeon_map[self.player_pos[1]][self.player_pos[0]] = '*'

        for i in self.treasures:
            dungeon_map[i[1]][i[0]] = 'T'

        for i in self.walls:
            dungeon_map[i[1]][i[0]] = '█'

        for i in dungeon_map:
            print(i)





if __name__ == '__main__':
    pass
