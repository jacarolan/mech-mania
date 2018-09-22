# This is Joe's general template

# keep these three import statements
import game_API
import fileinput
import json
from helper_functions import *

# your import statements here

###################################################
########### ONLY EDIT BELOW THIS LINE #############
###################################################

#This should return the relative value of travelling to specified node


###################################################
########### ONLY EDIT ABOVE THIS LINE #############
###################################################

first_line = True # DO NOT REMOVE

# global variables or other functions can go here
def monsterAlive(node, game):
    return game.has_monster(node) and not game.get_monster(node).dead

def get_winning_stance(stance):
    if stance == "Rock":
        return "Paper"
    elif stance == "Paper":
        return "Scissors"
    elif stance == "Scissors":
        return "Rock"



# main player script logic
# DO NOT CHANGE BELOW ----------------------------
for line in fileinput.input():
    if first_line:
        game = game_API.Game(json.loads(line))
        first_line = False
        continue
    game.update(json.loads(line))
# DO NOT CHANGE ABOVE ---------------------------

    # code in this block will be executed each turn of the game

    me = game.get_self()

    opponent = game.get_opponent()

    # Determines destination node
    if me.location == me.destination:

        adjacent_nodes = game.get_adjacent_nodes(me.location)

        maxVal = node_value(me.location)
        destination_node = me.location

        for node in game.get_adjacent_nodes(me.location):

            current_value = node_value(node, game)

            if current_value > maxVal:
                destination_node = node
                maxVal = current_value

    else:

        destination_node = me.destination

    # Determines node on next turn

    nodeAfterMoving = 0
    if me.movement_counter == me.speed + 1:
        nodeAfterMoving = destination_node
    else:
        nodeAfterMoving = me.location

    # Determines best stance, only calls function when dealing with other player
    if monsterAlive(nodeAfterMoving, game):
        if opponent.location == nodeAfterMoving:
            chosen_stance = best_stance_with_monster(me, opponent, game.get_monster(nodeAfterMoving))
        else:
            # if there's a monster at my location, choose the stance that damages that monster
            chosen_stance = get_winning_stance(game.get_monster(me.location).stance)
    else:
        chosen_stance = best_stance_no_monster(me, opponent)

    # submit your decision for the turn (This function should be called exactly once per turn)
    game.submit_decision(destination_node, chosen_stance)