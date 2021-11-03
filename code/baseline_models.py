import numpy as np
import pandas as pd
from data import main


############### Models ################################
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import VotingRegressor
from sklearn.svm import SVR
from sklearn.naive_bayes import MultinomialNB


from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split


from sklearn.metrics import mean_squared_error
from sklearn.metrics import classification_report


import pickle
##################### Ingesting the Data ################

data,Y,X1,y1,X1_train,y1_train,X1_test,y1_test = main(cut=300)

##################### Instanciate regression models ###############
LG = LinearRegression()
DT = DecisionTreeRegressor()
RF = RandomForestRegressor(n_estimators=150,max_depth=500,oob_score=True,random_state=0)

VT = VotingRegressor(estimators=[('LG',LG),('RF',RF)])





models = [LG,DT,RF]

################### training the models ####################

def train_model(models,X_train,y_train,X_test,y_test,X,Y):
    diff_final=20
    for model in models:
        model.fit(X_train,y_train)
        y_predict_test = pd.DataFrame(model.predict(X_test),columns=y1.columns)
        y_predict_train = pd.DataFrame(model.predict(X_train),columns=y1.columns)
        mean_square_test = np.round(mean_squared_error(y_test,y_predict_test),2)

        mean_square_train = np.round(mean_squared_error(y_train,y_predict_train),2)


        #print( str(model)+ " train : " + str(mean_square_train) + " test : " + str(mean_square_test))

        diff= np.abs(mean_square_train - mean_square_test)

        if diff < diff_final:
            winner_model = model
            diff_final=diff


    model =  winner_model.fit(X1,y1)

    return model.predict(X1),model




X,regression_model = train_model(models,X1_train,y1_train,X1_test,y1_test,X1,y1)
################ Instantiate classification models ###########################
LR = LogisticRegression()
svc = SVC()
rfc = RandomForestClassifier(n_estimators=500)
knc = KNeighborsClassifier(n_neighbors=3,weights='distance')

class_models = [svc]

Y = list(Y)
X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.25,random_state=0)



for model in class_models:
    model.fit(X_train,y_train)
    ypred = model.predict(X_test)

    print(str(model))
    print(classification_report(y_test,ypred))

modelname = "../models/linear_regression.sav"
pickle.dump(regression_model,open(modelname,'wb'))

playing = {"HomeTeam":[0],"AwayTeam":[1]}
playing = pd.DataFrame.from_dict(playing)

play_win =regression_model.predict(playing)


print(model.predict(play_win))
