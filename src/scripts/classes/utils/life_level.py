from random import randint

def life_level(rollDice, defaultValue, lifeDice, con):
    value = 0
    if rollDice:
        for i in range(1, lifeDice["quantity"]+1):
            value += randint(1, lifeDice["dice"]) + con
        return value
    else:
        return defaultValue + con