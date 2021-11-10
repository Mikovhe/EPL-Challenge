import streamlit as st
import pandas as pd
import pickle
from team_news import *



def team_names():
    #ingest the data
    data = pd.read_csv("data/E0.csv")
    teams = {}
    for num,team in enumerate(data.HomeTeam.unique()):
        teams[team]=num


    return teams




def main():

    page = st.sidebar.selectbox("Choose a page",["Team News","Predictions"])

    if page == "Team News":
        html_string = Team_News()
        st.markdown(html_string,unsafe_allow_html=True)

    elif page =="Predictions":
        html_string = game_predictions()
        st.markdown(html_string,unsafe_allow_html=True)

        #teams = pickle.load(open("models/team_names.pkl",'rb'))
        teams = team_names()
        teamlst = list(teams.keys())

        hometeam = st.selectbox("Home Team",teamlst)
        awayteam = st.selectbox("Away Team",teamlst)

        fixture =  pd.DataFrame.from_dict({"HomeTeam":[teams[hometeam]],"AwayTeam":[teams[awayteam]]})

        if st.button("predict"):

            regression_model = pickle.load(open("models/regression_model.pkl",'rb'))
            classification_model = pickle.load(open("models/classification_model.pkl",'rb'))
            play_win =regression_model.predict(fixture)
            result = int(classification_model.predict(play_win))

            if result ==-1:
                st.title("Home Team Wins")
            elif result ==0:
                st.title("Draw")
            else:
                st.title("Away Team Win")

if __name__== "__main__":
    main()