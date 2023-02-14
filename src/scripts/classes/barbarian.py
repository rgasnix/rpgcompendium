from utils.calc_mod import calc_mod
from utils.life_level import life_level
from random import randint

class Barbarian():
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
            "dice": 12,
        }
        
        self.life = 12 + self.modifiers["con"]

    def level_up(self, rollDice):
        self.life += life_level(rollDice, 7, self.lifeDice, self.modifiers["con"])
