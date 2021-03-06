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

    game.log(str(opponent))

    if me.location == me.destination: # check if we have moved this turn
        # get all living monsters closest to me
        # monsters = game.nearest_monsters(me.location, 1)

        opponentLocation = opponent.location

        # choose a monster to move to at random
        # monster_to_move_to = monsters[random.randint(0, len(monsters)-1)]
        #
        # # get the set of shortest paths to that monster
        # paths = game.shortest_paths(me.location, monster_to_move_to.location)
        destination_node = opponentLocation

        game.log("Here")

    else:
        destination_node = me.destination
        game.log("Destination:")
        game.log(str(destination_node))

    chosen_stance = stances[random.randint(0, 2)]

    if opponent.stance is None:
        chosen_stance = get_winning_stance(game.get_monster(me.location).stance)
        game.log("Opponent stance is none")
    elif me.location == opponentLocation:
        chosen_stance = get_winning_stance(opponent.stance)
        game.log("heree")
        game.log(str(game.get_opponent().stance))
    elif game.has_monster(me.location):
        # if there's a monster at my location, choose the stance that damages that monster
        chosen_stance = get_winning_stance(game.get_monster(me.location).stance)
    else:
        # otherwise, pick a random stance
        chosen_stance = stances[random.randint(0, 2)]

    if game.get_turn_num() == 1:
        chosen_stance = stances[random.randint(0, 2)]

    # submit your decision for the turn (This function should be called exactly once per turn)
    game.submit_decision(destination_node, chosen_stance)