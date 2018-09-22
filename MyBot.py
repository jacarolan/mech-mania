# This is Joe's general template

# keep these three import statements
import game_API
import fileinput
import json

# your import statements here
import random
import copy
import Math

###################################################
########### ONLY EDIT BELOW THIS LINE #############
###################################################




#This should return the relative value of travelling to specified node
def node_value(node, game):

	return get_value(node, game, 0)


def get_value(node, pastgame, nodes_traversed):

	if nodes_traversed == 7:
		return 0

	game = copy.deepcopy(game)

	adjacent_nodes = game.get_adjacent_nodes()

	me = game.get_self()
	opponent = game.get_opponent()
	
	if room.has_monster(node):
		monster = game.get_monster(node)

		delta_time = monster.respawn_counter-monster.respawn_rate

		fight_time = 0

		if delta_time < 7-player.speed:
			fight_time = Math.ceil(monster.get_health / player.get_damage)

		value = monster_value(node) / (delta_time + fight_time)

		for node in adjacent_nodes:
			value += get_value(node, game, nodes_traversed + 1)

		return value
	else:
		value = 0

		for node in adjacent_nodes:
			value += get_value(node, game, nodes_traversed + 1)

		return value



#This should return the best stance at our current location
def best_stance(destination_node, game):

	return random.randint(0,2)

###################################################
########### ONLY EDIT ABOVE THIS LINE #############
###################################################

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

    if me.location == me.destination:

        adjacent_nodes = game.get_adjacent_nodes(me.location)
        adjacent_nodes.append(me.location)

        maxVal = node_value(adjacent_nodes[0], game)

        destination_node = me.location

        for i in game.get_adjacent_nodes(me.location):

            current_value = node_value(i, game)

            if (current_value > maxVal):
                destination_node = i
                maxVal = current_value

    else:

        destination_node = me.destination

    if opponent.location != me.location:

        chosen_stance = stances[best_stance(destination_node, game)]

    elif game.has_monster(me.location):

        # if there's a monster at my location, choose the stance that damages that monster
        chosen_stance = get_winning_stance(game.get_monster(me.location).stance)

    else:

        # otherwise, pick a random stance
        chosen_stance = stances[random.randint(0, 2)]

    # submit your decision for the turn (This function should be called exactly once per turn)
    game.submit_decision(destination_node, chosen_stance)