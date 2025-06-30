import pickle
import pandas as pd
import streamlit as st#typr:ignore
import joblib


def app():
    st.markdown(
        '''<h1 style='text-align:center; color: #ffcd19;'><strong>💠 SCORE PREDICTION FOR THE 1st INNING 💠</strong></h1>
            <h3 style='text-align:center; color: #ff01e7;'><strong>  ENTER THE BELOW INFO </strong></h3>
            <hr style="border-top: 3px solid #ffcd19;">
        ''',
        unsafe_allow_html=True
    )

    # Loading the Saved Model
    model = joblib.load('model_new.joblib')

    # Designing WEB APP
    # TEST_DATA = [[180, 2, 18, 70, 1, 1,0,0,0,0,1,0,0, 0,0,0,1,0,0,0,0]]
    # [current_runs,wickets_out, overs_spent, runs_last_5_overs,wickets_last_5_overs, bat,ball]
    TEAMS = [
        'Chennai Super Kings',
        'Delhi Capitals',
        'Kings XI Punjab',
        'Kolkata Knight Riders',
        'Mumbai Indians',
        'Rajasthan Royals',
        'Royal Challengers Bangalore',
        'Sunrisers Hyderabad'
    ]

    # Batting Team & Bowling Team
    col1, col2 = st.columns(2)

    with col1:
        batting_team = st.selectbox('Batting Team At The Moment', TEAMS)
    with col2:
        bowling_team = st.selectbox('Bowling Team At The Moment', TEAMS)

    if bowling_team == batting_team:
        st.error("Bowling and Batting Team Can't Be The Same")
    else:
        # Current Runs
        current_runs = st.number_input(
            'Enter Current Score of Batting Team..',
            min_value=0,  # Setting a minimum value
            step=1        # Ensures only integer input
        )

        # Wickets Out
        wickets_left = st.number_input(
            'Enter Number of Wickets Left For Batting Team..',
            min_value=0,
            step=1
        )

        wickets_out = int(10 - wickets_left)

        # Overs Spent
        over = st.number_input(
            'Current Over of The Match..',
            min_value=0.0,
            step=0.1
        )

        # Runs In Last 5
        run_lst_5 = st.number_input(
            'How Many Runs Batting Team Has Scored In Last 5 Overs ?',
            min_value=0,
            step=1
        )

        # Wickets In Last 5
        wicket_lst_5 = st.number_input(
            'Number of  Wickets Taken By Bowling Team In The Last 5 Overs ?',
            min_value=0,
            step=1
        )

        # Calculate additional features
        # Convert overs like 11.4 to balls bowled
        over_int = int(over)
        over_decimal = over - over_int
        balls_bowled = over_int * 6 + int(round(over_decimal * 10))
        balls_left = 120 - balls_bowled
        crr = current_runs / (balls_bowled / 6) if balls_bowled > 0 else 0

        data = [
            batting_team,   # as string
            bowling_team,   # as string
            int(current_runs),
            int(wickets_out),
            float(over),
            int(run_lst_5),
            int(wicket_lst_5),
            crr,
            balls_left,
            int(wickets_left)
        ]

        st.write('---')

        st.write('Encoded Input Data:', pd.DataFrame([data]))

        # Generating Predictions
        Generate_pred = st.button("Predict Score")

        if Generate_pred:
            pred = model.predict([data])
            st.subheader(
                f'The Predicted Score Will Be Between {int(pred[0])-5} - {int(pred[0])+5}'
            )
