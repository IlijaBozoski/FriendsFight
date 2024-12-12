def readScores():
    usersWithScores=[]
    with open('scores.txt', 'r',encoding='utf-8') as file:
        for line in file:
            usersWithScores.append(line.strip().split(','))
    return usersWithScores
def writeScores(scores):
    # Assume we are storing scores in a file named "scores.txt"
    with open("scores.txt", "w") as file:
        for player, score in scores:
            file.write(f"{player},{score}\n")


def updateScores(player1, score1, player2, score2):
    scores = readScores()
    scores_dict = {item[0]: int(item[1]) for item in scores}
    scores_dict[player1] = scores_dict.get(player1, 0) + score1
    scores_dict[player2] = scores_dict.get(player2, 0) + score2
    updated_scores = [[player, str(score)] for player, score in scores_dict.items()]
    writeScores(updated_scores)
    return updated_scores
def userExists(player1):
    scores = readScores()
    for name, score in scores:
        if name == player1:
            return [name, score]
    return False
def findBulletLevels(score):
    if score <= 300:
        return [0, 0]
    elif score <= 500:
        return [0, 1]
    elif score <= 700:
        return [1, 1]
    elif score <= 900:
        return [1, 2]
    elif score <= 1100:
        return [2, 2]
    elif score <= 1300:
        return [2, 3]
    elif score <= 1500:
        return [3, 3]
    elif score <= 1700:
        return [3, 4]
    elif score <= 1900:
        return [4, 4]
    elif score <= 2100:
        return [4, 5]
    elif score <= 2300:
        return [5, 5]
    elif score <= 2500:
        return [5, 6]
    elif score <= 2700:
        return [6, 6]
    elif score <= 2900:
        return [6, 7]
    elif score <= 3100:
        return [7, 7]
    elif score <= 3300:
        return [7, 8]
    elif score <= 3500:
        return [8, 8]
    elif score <= 3700:
        return [8, 9]
    else:
        return [9, 9]



