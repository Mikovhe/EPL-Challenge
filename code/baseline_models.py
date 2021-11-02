import pandas as pd
import numpy as np
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


Y = data.FTR

X1 = data[["HomeTeam","AwayTeam"]]
y1 = data.drop(["HomeTeam","AwayTeam","FTR"],axis=1)


cut = 360
X1_train = X1.iloc[:cut]
y1_train = y1.iloc[:cut]

X1_test = X1.iloc[cut:]
y1_test = y1.iloc[cut:]




from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_squared_error



LG = LinearRegression()
DT = DecisionTreeRegressor()
RF = RandomForestRegressor(n_estimators=150,max_depth=500,oob_score=True,random_state=0)
sgd = SGDRegressor(max_iter=1000, tol=1e-3)
def train_model(model):
    model.fit(X1_train,y1_train)
    y_predict = pd.DataFrame(model.predict(X1_test),columns=y1.columns)

    mean_square = np.round(mean_squared_error(y1_test,y_predict),2)


    print(mean_square)

train_model(RF)
