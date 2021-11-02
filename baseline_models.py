import pandas as pd

data = pd.read_csv("../data/E0.csv")

teams = {}
for num,team in enumerate(data.HomeTeam.unique()):
    teams[team]=num

hometeam,awayteam = [],[]

for team in data.HomeTeam:
    hometeam.append(teams[team])


for team in data.AwayTeam:
    awayteam.append(teams[team])

data.HomeTeam = hometeam
data.AwayTeam = awayteam


def final_result(result):
    if result =="H":
        return -1
    elif result =="D":
        return 0
    else:
        return 1

data.FTR = data.FTR.apply(final_result)



data.drop(["Div","Date","Referee","Time","HTR"],axis=1,inplace=True)
print(data.head(5))