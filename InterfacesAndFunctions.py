import os
import random
from ClassPokemon import *

interface_ascii = """

                                  ,'
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
                            _                                     
            ___ _ __   __ _| | _____  ___                         
           / __| '_ \ / _` | |/ / _ \/ __|                        
           \__ \ | | | (_| |   <  __/\__ \                        
            |___/_| |_|\__,_|_|\_\___||___/                       \
                                """

game_over = """\
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\
"""

pikachu_draw = """\
       \:.             .:/
        \``._________.''/ 
         \             / 
 .--.--, / .':.   .':. 
/__:  /  | '::' . '::' |
   / /   |`.   ._.   .'|
  / /    |.'         '.|
 /___-_-,|.\  \   /  /.|
      // |''\.;   ;,/ '|
      `==|:=         =:|
         `.          .'
           :-._____.-:
          `''       `''\
"""

squirtle_draw = """\
               _,........__
            ,-'            "`-.
          ,'                   `-.
        ,'                        .
      ,'                           .
      .'\               ,"".       `
     ._.'|             / |  `       .
     |   |            `-.'  ||       `.
     |   |            '-._,'||       | .
     .`.,'             `..,'.'       , |`-.
     l                       .'`.  _/  |   `.
     `-.._'-   ,          _ _'   -" \  .     `
........-.`-...,---------','         `. `....__.
.'        `"-..___      __,'\          \  \     .
\_ .          |   `....'    `.           . \     .
  `.          |              `.          |  .     L
    `.        |`--...________.'.        j   |     |
      `._    .'      |          `.     .|   ,     |
         `--,\       .            `7..' |  ,      |
            ` `      `            /     |  |      |    _,-'...`-.
             \ `.     .          /      |  '      |  ,'          `.
              \  v.__  .        '       .   \    /| /              .
               \/    `"".......`.       \   \  /.''                |
                `        .        `._ ___,j.  `/ .-       ,---.     |
                ,`-.      \         ."     `.  |/        j     `    |
               /    `.     \       /         \ /         |     /    j
              |       `-.   7-.._ .          |"          '         /
              |          `./_    `|          |            .     _,'
              `.           / `----|          |-............`---'
                \          \      |          |
               ,'           )     `.         |
                7____,,..--'      /          |
                                  `---.__,--.'\
                                  """



charizard_draw = """\
                ."-,.__
                 `.     `.  ,
              .--'  .._,'"-' `.
             .    .'         `'
             `.   /          ,'
               `  '--.   ,-"'
                `"`   |  .
                   -. \, |
                    `--Y.'      ___.
                         \     L._, .
               _.,        `.   <  <\                _
             ,' '           `, `.   | \            ( `
          ../, `.            `  |    .\`.           \ \_
         ,' ,..  .           _.,'    ||\l            )  '".
        , ,'   \           ,'.-.`-._,'  |           .  _._`.
      ,' /      \ \        `' ' `--/   | \          / /   ...
    .'  /        \ .         |\__ - _ ,'` `        / /     `.`.
    |  '          ..         `-...-"  |  `-'      / /        . `.
    | /           |L__           |    |          / /          `. `.
   , /            .   .          |    |         / /             ` `
  / /          ,. ,`._ `-_       |    |  _   ,-' /               ` .
 / .           ..`_/. `-_ \_,.  ,'    +-' `-'  _,        ..,-.    \`.
.  '         .-f    ,'   `    '.       \__.---'     _   .'   '     \ .
' /          `.'    l     .' /          \..      ,_|/   `.  ,'`     L`
|'      _.-""` `.    \ _,'  `            \ `.___`.'"`-.  , |   |    | .
||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|
||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||
|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||
||/            _,-------7 '              . |  `-'    l         /    `||
. |          ,' .-   ,' ||               | .-.        `.      .'     ||\
"""

fight_draw = """\
  __ _       _     _   
 / _(_)     | |   | |  
| |_ _  __ _| |__ | |_ 
|  _| |/ _` | '_ \| __|
| | | | (_| | | | | |_ 
|_| |_|\__, |_| |_|\__|
        __/ |          
       |___/\
       """

obstacle_definition = """\
##                  
##  ##   ####  ##  #
                    
  ###    ####    ###
#       #           
    ##  ##   ##  #  
#   ##  ##   ##     
                    
###  #####  ###     
                    
#  #       ######## 
#  ####             
#  #          ##### 
#        # ##       
#  #       #    ### \
"""


def PrintDraw(draw):
    return print(draw)


def AutomaticObject(map_objects, num_of_object, map_width, map_height, my_position, obstacle_definition, pos_y, pos_x,
                    map_ob_obl):
    while len(map_objects) < num_of_object:
        object_random = [random.randint(0, map_width - 2), random.randint(0, map_height - 2)]

        if object_random not in map_objects and object_random != my_position and \
                obstacle_definition[object_random[pos_y]][
                    object_random[pos_x]] != "#" and map_objects not in map_ob_obl:
            map_objects.append(object_random)


def MoveAndQuit(direction, new_position, my_position, pos_x, pos_y, map_width, map_height, end_game):
    if direction == "W":
        new_position = [my_position[pos_x], (my_position[pos_y] - 1) % map_height]

    elif direction == "S":
        new_position = [my_position[pos_x], (my_position[pos_y] + 1) % map_height]

    elif direction == "A":
        new_position = [(my_position[pos_x] - 1) % map_width, my_position[pos_y]]

    elif direction == "D":
        new_position = [(my_position[pos_x] + 1) % map_width, my_position[pos_y]]

    elif direction == "Q" or end_game is True:
        end_game = True
    return new_position, end_game


def ChooseAtacksEnemys(pokemon):
    attack_enemy = random.choice(list(pokemon.attacks_dict.keys()))
    player_one.health -= pokemon.attacks_dict[attack_enemy]

    print("\n-----{} HAVE TO USE {}-----".format(pokemon.name, attack_enemy))
    input("---ENTER TO CONTINUE---")
    os.system("cls")


def ChooseAtacksP1(pokemon):
    print(pikachu_draw + "!!!!!PIKA PIKA PIKAAAA!!!!!")
    attack_enemy = input("CHOOSE THE ATTACK:\nA = Iron tail---DAMAGE-{}\nB = Volt Tackle---DAMAGE-{}"
                         "\nC = Thunderbolt---DAMAGE-{}".format(player_one.attacks_dict["Iron tail"],
                                                                player_one.attacks_dict["Volt Tackle"],
                                                                player_one.attacks_dict["Thunderbolt"]))
    os.system("cls")
    if attack_enemy == "A":
        pokemon.health -= player_one.attacks_dict["Iron tail"]
        print("\n-----Pikachu ha usado {}-----".format("Iron tail"))

    elif attack_enemy == "B":
        pokemon.health -= player_one.attacks_dict["Volt Tackle"]
        print("\n-----Pikachu ha usado {}-----".format("Volt Tackle"))
    else:
        pokemon.health -= player_one.attacks_dict["Thunderbolt"]
        print("\n-----Pikachu ha usado {}-----".format("Thunderbolt"))




def ShowOfState(player, pokemon):
    print(player.state())
    print(pokemon.state())


# BATTLES
def battle(victories):
    charizard.health = 200
    squirtle.health = 100

    if player_one.health > 100:
        player_one.health = 100


    os.system("cls")
    print(fight_draw)
    input("!!!---ENTER TO THE BATTLE---!!!")
    os.system("cls")

    while True:
        if victories <= 4:

            print(squirtle_draw + "!!!!!GRRRRRR SQUIRRRRRRRRRR!!!!!")

            ChooseAtacksEnemys(squirtle)

            if player_one.health <= 0:
                print("Suirttle te ha vencido")
                print(game_over)
                exit()

            ShowOfState(player_one, squirtle)
            input("\n---PRESS ENTER----- IS YOUR TURN-----")

            ChooseAtacksP1(squirtle)

            if squirtle.health <= 0:
                input("!!YOU WON!!")
                victories += 1
                player_one.exp += 3
                break

            ShowOfState(player_one, squirtle)
            input("\n---PRESS ENTER----- IS TURN OF SQUIRTTLE-----")

        elif 4 < victories < 7:

            print(charizard_draw + "!!!!!GRRRRRR FLAMEEEEEE!!!!!")

            ChooseAtacksEnemys(charizard)
            ShowOfState(player_one, charizard)

            if player_one.health <= 0:
                print("Charizard te ha vencido")
                print(game_over)
                exit()

            ChooseAtacksP1(charizard)

            if charizard.health <= 0:
                print("\n----YOU WON----")
                input("---PRESS TO CONTINUE---")
                victories += 1
                break

            ShowOfState(player_one, charizard)
            input("\n---PRESS ENTER----- IS TURN OF CHARIZARD-----")

        elif victories > 7:
            pass
    return victories
