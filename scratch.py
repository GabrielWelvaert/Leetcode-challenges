import random

#players = input("enter player names separated by spaces: ")
players = "tony gabe stevie julien justin markowski spencer"
players = players.split()
random.shuffle(players)
teams = [[],[]]

for player in players:
    n = random.randint(0, 1)
    if len(teams[n]) < -(-(len(players)//2)):
        teams[n].append(player)
    else:
        teams[1 - n].append(player)

def pretty(team):
    temp = ""
    temp += team[0]
    for i in range(1, len(team)):
        temp += ", " + team[i]
    return temp

print(f"Team 1 is {pretty(teams[0])}")
print(f"Team 2 is {pretty(teams[1])}")