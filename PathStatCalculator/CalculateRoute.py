import json
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
            myState = ""

            if monsterState == "Rock":
                myState = "Paper"
            if monsterState == "Paper":
                myState = "Scissors"
            if monsterState == "Scissors":
                myState = "Rock"
                
            monsterHealth = data["Monsters"][index]["Health"]
            monstTime = monsterHealth // dRock
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


print(routeCalculator([0, 1, 3, 2, 4, 13, 20, 21]))
