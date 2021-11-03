import streamlit as st
import pandas as pd
import pickle
import sys
sys.path.append('../')
from team_news import *
from data import team_names

def main():

    page = st.sidebar.selectbox("Choose a page",["Team News","Predictions"])

    if page == "Team News":
        html_string = Team_News()
        st.markdown(html_string,unsafe_allow_html=True)

    elif page =="Predictions":
        html_string = game_predictions()
        st.markdown(html_string,unsafe_allow_html=True)

        teams = team_names()
        teamlst = list(teams.keys())

        hometeam = st.selectbox("Home Team",teamlst)
        awayteam = st.selectbox("Away Team",teamlst)

        fixture =  pd.DataFrame.from_dict({"HomeTeam":[teams[hometeam]],"AwayTeam":[teams[awayteam]]})

        if st.button("predict"):

            regression_model = pickle.load(open("../models/linear_regression.sav",'rb'))
            classification_model = pickle.load(open("../models/svc.sav",'rb'))
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