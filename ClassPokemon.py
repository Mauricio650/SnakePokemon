class Pokemon:

    def __init__(self, name, health, level, exp):
        self.name = name
        self.health = health
        self.level = level
        self.exp = exp

    # For know its health in the battle
    def state(self):
        return f"------{self.name}------\n\tHealth : {self.health}" + f"\n\tLevel  : {self.level}\n\t" \
                                                                      f" Exp   : {self.exp}" + "|10"

    def attacks(self, attack_1, damage_a1, attack_2, damage_a2, attack_3, damage_a3):
        self.attacks_dict = {attack_1: damage_a1, attack_2: damage_a2, attack_3: damage_a3}


class Gatemones(Pokemon):
    def __init__(self, name, health, exp, level, lives, gender):
        super().__init__(name, health, level, exp)
        self.lives = lives
        self.gender = gender

    def state(self):
        pokemon_steate = super().state()
        return pokemon_steate + f"\n\tGender : {self.gender}\n\tLives : {self.lives}"


# POKEMONS
charizard = Pokemon("Charizard", 200, 4, 0)  # ENEMY
charizard.attacks("Flamethrower", 25, "Dragon Claw", 20, "Inferno Overdrive", 30)
# -------------------------------------------------
squirtle = Pokemon("Squirtle", 100, 1, 1)  # ENEMY
squirtle.attacks("Water gun", 20, "Tackle", 20, "Bubble beam", 20)
# -------------------------------------------------
player_one = Pokemon("Pikachu", 100, 1, 1)  # PLAYER 1
player_one.attacks("Iron tail", 15, "Volt Tackle", 20, "Thunderbolt", 25)

# GATEMONES

mechas = Gatemones("Mechas", 150, 0, 1, 7, "Female")
mechas.attacks("Cat Claw", 21, "Maullido", 19, "Death to mouse", 30)
# -------------------------------------------------
thor = Gatemones("Thor", 130, 0, 2, 5, "Male")
thor.attacks("Cat Claw", 23, "Maullido", 21, "Death to mouse", 33)

cata = Gatemones("Kata", 300, 777, 20, 1, "Female")
thor.attacks("Cat Claw", 23, "Maullido", 21, "Death to mouse", 33)
