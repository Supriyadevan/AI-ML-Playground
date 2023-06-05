def getmax():
    grades = [9.6,9.2,9.7]
    getmaxscore = max(grades)
    return(getmaxscore)

def getmin():
    grades = [9.6,9.2,9.7]
    getminscore = min(grades)
    return(getminscore)

OptimizedMaxScore = getmax()
OptimizedMinScore = getmin()

print("Max:",OptimizedMaxScore, "Min:",OptimizedMinScore)

