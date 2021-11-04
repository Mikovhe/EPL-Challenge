import pandas as pd
import pickle
def team_names():
    #ingest the data
    data = pd.read_csv("../data/E0.csv")
    teams = {}
    for num,team in enumerate(data.HomeTeam.unique()):
        teams[team]=num


    return teams


teams = team_names()

file_path = "../Deploy/team_names.pkl"
pickle.dump(teams,open(file_path,'wb'))
teams = pickle.load(open("../Deploy/team_names.pkl",'rb'))
print(teams)