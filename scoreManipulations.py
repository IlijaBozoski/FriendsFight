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
