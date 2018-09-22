# keep these three import statements
import game_API
import fileinput
import json

# your import statements here
import random

first_line = True # DO NOT REMOVE

# global variables or other functions can go here
stances = ["Rock", "Paper", "Scissors"]

##########################################################################################

def node_value(node, game):
    # perhaps this could be the sum of two functions
    # separate monster value and opponent value
    return random.randint(0,10)

#This should return the best stance at our current location
def best_stance_no_monster(me, opponent):
    return stances[random.randint(0,2)]

def best_stance_with_monster(me, opponent, monster):
    return best_stance_no_monster(me, opponent)

##########################################################################################

def monsterWillBeAlive(node, game):
    if not game.has_monster(node):
        return False
    return (not game.get_monster(node).dead) or (game.get_monster(node).respawn_counter == 1)

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

        maxVal = node_value(me.location, game)
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
    if monsterWillBeAlive(nodeAfterMoving, game):
        if opponent.location == nodeAfterMoving:
            chosen_stance = best_stance_with_monster(me, opponent, game.get_monster(nodeAfterMoving))
        else:
            # if there's a monster at my location, choose the stance that damages that monster
            chosen_stance = get_winning_stance(game.get_monster(nodeAfterMoving).stance)
    else:
        chosen_stance = best_stance_no_monster(me, opponent)

    # submit your decision for the turn (This function should be called exactly once per turn)
    game.submit_decision(destination_node, chosen_stance)