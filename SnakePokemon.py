import readchar
from ClassPokemon import *
from InterfacesAndFunctions import *

#  This function save in a list each row of map for know best the coordinates of obstacles
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

# coordinates, positions, victories etc....
map_width = 20
map_height = 15
num_of_object = 3
num_of_object_live = 2
pos_x = 0
pos_y = 1
my_position = [6, 0]
map_objects = []
map_objects_live = []
victories = 0

# bools for know if the player won or for know if the player was in a battle
end_game = None
flag = bool

# the tail of "snake"
tail_length = 0
tail = []

print(player_one.health)

# for create the main interface and basic instructions [(OS.SYSTEM("CLS")) IS FOR CLEAN THE TERMINAL]
PrintDraw(interface_ascii)

input("\n---YOU ARE ASH KETCHUM YOUR POKEMON IS PIKACHU--- PRESS ENTER TO CONTINUE [You can move with (W,A,S,D)]")
os.system("cls")

# (MAIN LOOP) for know if the player lost
while not end_game:

    # this function is responsible create random generator of health object in the game
    AutomaticObject(map_objects_live, num_of_object_live, map_width, map_height, my_position, obstacle_definition,
                    pos_y, pos_x, map_objects)
    # this function is responsible create random objects in the game
    AutomaticObject(map_objects, num_of_object, map_width, map_height, my_position, obstacle_definition, pos_y, pos_x,
                    map_objects_live)

    # it prints the top part of the map
    print("╔" + "═" * map_width * 2 + "╗")

    # this loop is the responsible to draw the left columns of the map
    for coordinate_y in range(map_height):
        print("║", end="")

        # this loop is the responsible to draw the rows of the map
        for coordinate_x in range(map_width):
            # some variables for indicate what draw in each iteration
            char_to_draw = "  "
            object_in_cell = None
            tail_in_cell = None
            object_live_in_cell = None

            # This loop is for iterate into map_objects for know if is in the same position of coordinates
            for map_object in map_objects:
                if map_object[pos_x] == coordinate_x and map_object[pos_y] == coordinate_y:
                    char_to_draw = " ☼"
                    object_in_cell = map_object

            for map_objects_l in map_objects_live:
                if map_objects_l[pos_x] == coordinate_x and map_objects_l[pos_y] == coordinate_y:
                    char_to_draw = " ±"
                    object_live_in_cell = map_objects_l

            for tail_p in tail:
                if tail_p[pos_x] == coordinate_x and tail_p[pos_y] == coordinate_y:
                    char_to_draw = " ■"
                    tail_in_cell = tail_p

            if my_position[pos_x] == coordinate_x and my_position[pos_y] == coordinate_y:
                char_to_draw = " ■"
                # for know  if the  player is in the same position of an object
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1
                    victories = battle(victories)
                    flag = True
                # for know if the player is in the same position of the tail
                if tail_in_cell:
                    end_game = True

                if object_live_in_cell:
                    map_objects_live.remove(object_live_in_cell)
                    player_one.health += 20

            # the coordinates are the same of obstacles, we have to draw an obstacle
            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = " ░"

            # this "print" is for draw each element in the map
            print("{}".format(char_to_draw), end="")
        # Right columns of map
        print("║")
    # it prints the down part of the map
    print("╚" + "═" * map_width * 2 + "╝", "\nVictories: {} §\n Health {}".format(victories,player_one.health))

    if end_game:
        os.system("cls")
        print(game_over)
        exit()

    # this crazy things is because after battles the map have a bug.
    if flag is not True:  # if not true, all is normal
        direction = readchar.readchar().upper()  # [w = rise][S = down][A = left][D = right] [Q = quit]:")
        new_position = None
    else:
        os.system("cls")  # if is true, we clean the terminal and show the input for the user don't look the bug
        input(" ⚡ ⚡ ⚡ ⚡ ⚡-->   PRESS DOUBLE ENTER TO CONTINUE  <--⚡ ⚡ ⚡ ⚡ ⚡")
        direction = readchar.readchar().upper()  # after clean the terminal, again show the map and all is normal
        new_position = None
        flag = None

    new_position, end_game = MoveAndQuit(direction, new_position, my_position, pos_x, pos_y, map_width, map_height,
                                         end_game)

    if new_position:
        if obstacle_definition[new_position[pos_y]][new_position[pos_x]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position = new_position
    os.system("cls")

print("¡¡SEE YOU AGAIN¡¡")
