# keep these three import statements
import game_API
import fileinput
import json

# your import statements here
import random

first_line = True # DO NOT REMOVE

# global variables or other functions can go here
stances = ["Rock", "Paper", "Scissors"]

def get_winning_stance(stance):
    if stance == "Rock":
        return "Paper"
    elif stance == "Paper":
        return "Scissors"
    elif stance == "Scissors":
        return "Rock"

def valueOfNode(node, game):
    if not game.has_monster(node):
        return 3
    else:
        monster = game.get_monster(node)
        deathEffects = monster.death_effects
        return (deathEffects.rock + deathEffects.scissors + deathEffects.paper +
                deathEffects.health + deathEffects.speed)

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

    if me.location == me.destination: # check if we have moved this turn
        bestNode = 0
        bestValue = 0
        for node in game.get_adjacent_nodes(me.location):
            value = valueOfNode(node, game)
            if value > bestValue:
                bestNode = node
                bestValue = value
        destination_node = bestNode
    else:
        destination_node = me.destination

    if game.has_monster(me.location):
        # if there's a monster at my location, choose the stance that damages that monster
        chosen_stance = get_winning_stance(game.get_monster(me.location).stance)
    else:
        # otherwise, pick a random stance
        chosen_stance = stances[random.randint(0, 2)]

    # submit your decision for the turn (This function should be called exactly once per turn)
    game.submit_decision(destination_node, chosen_stance)