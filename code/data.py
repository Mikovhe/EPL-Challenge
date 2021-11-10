import pandas as pd
import numpy as np

from datetime import datetime




####################################################
#Helper Functions

def get_teams(team_list):
    teams = {}
    for num,team in enumerate(team_list):
        teams[team]=num

    return teams



def get_home_away(df):


    hometeam,awayteam = [],[]
    teams = get_teams(df.HomeTeam.unique())

    for team in df.HomeTeam:
        hometeam.append(teams[team])


    for team in df.AwayTeam:
        awayteam.append(teams[team])


    return hometeam,awayteam

def final_result(result):
    if result =="H":
        return -1
    elif result =="D":
        return 0
    else:
        return 1









############################################################


def main(cut=360):
    #ingest the data
    data = pd.read_csv("../data/E0.csv")
    

    data.HomeTeam,data.AwayTeam = get_home_away(data)
    data.FTR = data.FTR.apply(final_result)
    data.Date = pd.to_datetime(data.Date)
    data.Time = pd.to_datetime(data.Time)

    data['year'] = data.Date.dt.year 
    data['month'] = data.Date.dt.month 
    data['day'] = data.Date.dt.day
    data['hour'] = data.Time.dt.hour
    data['minute'] = data.Time.dt.minute
    data.drop(["Div","Date","Referee","Time","HTR"],axis=1,inplace=True)


    Y = data.FTR

    X1 = data[["HomeTeam","AwayTeam","year","month","day"]]
    y1 = data.drop(["HomeTeam","AwayTeam","FTR","year","month","day"],axis=1)
    X1_train = X1.iloc[:cut]
    y1_train = y1.iloc[:cut]

    X1_test = X1.iloc[cut:]
    y1_test = y1.iloc[cut:]

    return data,np.array(Y),X1,y1,X1_train,y1_train,X1_test,y1_test



def team_names():
    #ingest the data
    data = pd.read_csv("../data/E0.csv")
    
    teams = get_teams(data.HomeTeam.unique())


    return teams