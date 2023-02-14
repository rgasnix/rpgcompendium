from utils.calc_mod import calc_mod
from utils.life_level import life_level
from random import randint

class Bard():
    def __init__(self, strength, dexterity, constituiton, intelligence, wisdom, charisma):
        self.attributes = {
            "str": strength,
            "dex": dexterity,
            "con": constituiton,
            "int": intelligence,
            "wis": wisdom,
            "cha": charisma,
        }
        self.modifiers = {
            "str": calc_mod(strength),
            "dex": calc_mod(dexterity),
            "con": calc_mod(constituiton),
            "int": calc_mod(intelligence),
            "wis": calc_mod(wisdom),
            "cha": calc_mod(charisma),
        }
        self.lifeDice = {
            "quantity": 1,
            "dice": 8,
        }
        self.life = 8 + self.modifiers["con"]

        def level_up(self, rollDice):
         self.life += life_level(rollDice, 8, self.lifeDice, self.modifiers["con"])
