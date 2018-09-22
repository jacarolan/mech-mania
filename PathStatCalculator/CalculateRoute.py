import json
import math
#route as a list

data = {}

with open('Map.json') as data_file:
    data = json.load(data_file)

def findMonster(node):
    for i in range(len(data["Monsters"])):
        if data["Monsters"][i]["Location"] == node:
            return (True, i)

    return (False, 0)


def routeCalculator(route):
    dHealth = 0
    dRock = 1
    dScissors = 1
    dPaper = 1
    dSpeed = 0
    time = 0


    for node in route:

       if findMonster(node)[0]:
            index = findMonster(node)[1]

            monsterState = data["Monsters"][index]["Stance"]
            myDamage = 0

            if monsterState == "Rock":
                myDamage = dPaper
            if monsterState == "Paper":
                myDamage = dScissors
            if monsterState == "Scissors":
                myDamage = dRock

            monsterHealth = data["Monsters"][index]["Health"]
            monstTime = math.ceil(monsterHealth // myDamage)
            if (monstTime < 7):
                time += 7
            else:
                time += monstTime


            dHealth += data["Monsters"][index]["Death Effects"]["Health"] - data["Monsters"][index]["Attack"] * monstTime
            dRock += data["Monsters"][index]["Death Effects"]["Rock"]
            dScissors += data["Monsters"][index]["Death Effects"]["Scissors"]
            dPaper += data["Monsters"][index]["Death Effects"]["Paper"]
            dSpeed += data["Monsters"][index]["Death Effects"]["Speed"]
       else:
           time += 7 - dSpeed

    return {"Health": dHealth, "Rock": dRock, "Scissors": dScissors, "Paper": dPaper, "Speed": dSpeed, "Time": time}


print(routeCalculator([0, 10, 9, 8, 14, 19, 23, 24])) # good route
print(routeCalculator([0, 10, 11, 12, 22, 21]))
print(routeCalculator([0, 1, 3, 2, 4, 13, 20, 21])) # good route
print(routeCalculator([0, 1, 3, 2, 4, 5, 6, 7, 8])) # really bad
print(routeCalculator([0, 10, 9, 8, 7, 6, 5, 4]))
print(routeCalculator([0, 1, 3, 2, 4, 13, 20, 19, 23, 24])) # good stats, bad health
print(routeCalculator([0, 10, 9, 8, 14, 19, 23, 24, 19, 14, 8, 9, 10, 16, 15, 18, 17])) # very cool, Kanye!