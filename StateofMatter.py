Freeze = 0
Evaporate = 100
def stateofmatter(temp):
    if temp > Evaporate:
        X = 'gas'
        return(X)
    elif temp < Freeze:
        X = 'solid'
        return(X)
    elif Freeze < temp < Evaporate:
        X = 'water'
        return(X)




