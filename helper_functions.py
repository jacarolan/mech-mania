import random
import game_API


stances = ["Rock", "Paper", "Scissors"]

def node_value(node, game):
    # perhaps this could be the sum of two functions
    # separate monster value and opponent value
    return random.randint(0,10)

#This should return the best stance at our current location
def best_stance_no_monster(me, opponent):
    return stances[random.randint(0,2)]

def best_stance_with_monster(me, opponent, monster):
    return best_stance_no_monster(me, opponent)