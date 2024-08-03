import streamlit as st
import pandas as pd
import plotly.express as px
from skimage import io
import numpy as np

st.set_page_config(layout="wide")

with st.sidebar:
    st.image("BallTrack.png")
    st.header("🏟️ Match Details",divider="gray")
    bat_team = st.text_input("Batting Team")
    bowl_team = st.text_input("Bowling Team")
    innings = st.radio("Innings",["1","2"],horizontal = True)
    bat_players = st.text_area(f"Enter {bat_team}'s Players")
    bowl_players = st.text_area(f"Enter {bowl_team}'s Players ")
    start = st.toggle("Start App 🚀")

st.header(" :cricket_bat_and_ball: _BallTrack_ _Analyzer_: Every Ball, Every Insight :bar_chart:",divider="gray")


if 'ball_data' not in st.session_state:
    st.session_state.ball_data = pd.DataFrame(columns=["Over", "Ball","Batting Team","Bowling Team","Innings","Batter","Batting Hand","Bowler", "Bowling Style","Bowling Side", "Runs", "Outcome",
    "False Shot", "Pitching Line","line_x","line_y", "Pitching Length","length_x","length_y","Arrival Line","Arrival line_x","Arrival line_y","Shot Type",
    "Shot Connection","Shot Intent","Bat Impact_x","Bat Impact_y", "Wagon Zone","wagon_x","wagon_y","Feet Movement","Extras","Extra Runs","Wicket","Player Dismissed","Dismissed Type","Description"])

col1, col2 = st.columns([1,2])

images = {
    'length': px.imshow(io.imread('Length.png')).update_xaxes(showticklabels=False).update_yaxes(showticklabels=False),
    'line_map': px.imshow(io.imread('line_map.jpg')).update_xaxes(showticklabels=False).update_yaxes(showticklabels=False),
    'bat': px.imshow(io.imread('bat.png')).update_xaxes(showticklabels=False).update_yaxes(showticklabels=False),
    'wagon': px.imshow(io.imread('Wagon.png')).update_xaxes(showticklabels=False).update_yaxes(showticklabels=False)
}


if start:
    with col1:
        c1,c2 = st.columns(2)
        with c1:
            with st.container(border=True):
                over_no = st.number_input("Over No.",min_value = 1)
                batter = st.selectbox("Batter",[name.strip() for name in bat_players.split(",")])
                bat_hand = st.radio("Batting Hand",["RHB","LHB"],horizontal = True)
                runs = st.number_input("Runs Off Bat", min_value=0)
                extras = st.selectbox("Extras",["None","Wide","Legbyes","Byes","No ball","Penalty"])
                false_shot = st.radio("False Shot", ["No", "Yes"],horizontal = True)
        with c2:
            with st.container(border=True):
                ball_no = st.number_input("Ball No.",min_value = 1,max_value = 6)
                bowler = st.selectbox("Bowler",[name.strip() for name in bowl_players.split(",")])
                bowling_style = st.selectbox("Bowling Style", ["Right-arm Fast","Right-arm Medium", "Left-arm Fast","Left-arm Medium", "Right-arm Legspin","Right-arm Offspin","Left-arm Chinaman","Left-arm Orthodox"])
                outcome = st.selectbox("Outcome",["Dot", "Single", "Double", "Triple", "Four", "Six","Extras"])
                extra_runs = st.number_input("Extra Runs",min_value=0)
                bowl_side = st.radio("Bowling Side",["Around","Over"],horizontal = True)

        with st.container(border=True):
            Wicket = st.radio("Wicket", ["No", "Yes"],horizontal = True)
            player_options = ["None"] + [name.strip() for name in bat_players.split(",")]
            player_out = st.selectbox("Player Dismissed",player_options)
            out_type = st.selectbox("Dismissed Type",["None","Bowled","Caught","LBW","Run Out","Stumped","Hit Wicket","Retire Out","Timed Out"
            ,"Handled Ball","Obstructed Field"])


    with col2:
        with st.container(border=True):
            tab1, tab2, tab3, tab4 = st.tabs(["Pitching Length Zone", "Arrival Line Zone","Bat Impact Points", "Wagon Wheel"])
            with tab1:
                C1,C2 = st.columns(2)
                with C1:
                    line = st.selectbox("Line", ["Wide Off Stump", "Outside Off Stump", "On Stumps", "Down Leg", "Wide Leg"])
                    Length_X_axis = st.number_input("X-axis", min_value=0)
                with C2:
                    length = st.selectbox("Length", ["Full Toss", "Yorker", "Full", "Good", "Back of Length", "Short"])
                    Length_Y_axis = st.number_input("Y-axis", min_value=0)
                Length_Y_axis = 1250 - Length_Y_axis
                st.write(images['length'])
            

            with tab2:
                C3,C4 = st.columns(2)
                with C3:
                    arr_line =  st.selectbox("Arrival Line", ["Wide Off Stump", "Outside Off Stump", "On Stumps", "Down Leg", "Wide Leg"])
                    Line_X_axis = st.number_input("X_axis", min_value=0)
                with C4:
                    shot_type = st.selectbox("Shot Type", ["None","FF def","BF def","Steer","Cover Drive", "Straight Drive", "Pull Shot ", "Square Cut", "Flick","Push"
                    ,"Worked","Leg Glance","On Drive","Off Drive","Square Drive","Late Cut","Upper Cut","Hook Shot","Sweep Shot","Reverse Sweep"
                    ,"Switch Hit","Paddle Sweep","Paddle Scoop","Slog Sweep","Slog","Inside Out","Glance"])
                    Line_Y_axis = st.number_input("Y_axis", min_value=0)
                Line_Y_axis = 500 - Line_Y_axis
                st.write(images['line_map'])
                

            with tab3:
                C7,C8 = st.columns(2)
                with C7:
                    shot_con = st.selectbox("Shot Connection",["None","Middle","Mistime","Leading Edge","Inside Edge", "Outside Edge", "Top Edge", "Bottom Edge", "Beaten","Glove"])
                    con_X_axis = st.number_input("X-Axis ", min_value=0)
                with C8:
                    shot_intent = st.selectbox("Shot Intent",["None","Attack","Defense","Rotate","Leave"])
                    con_Y_axis = st.number_input("Y-Axis ", min_value=0)
                con_Y_axis = 500 - con_Y_axis
                st.write(images['bat'])
                

            with tab4:
                C5,C6 = st.columns(2)
                with C5:
                    wagon = st.selectbox("Wagon",["None","Fine Leg", "Square Leg", "Mid Wicket", "Long On", "Long Off", "Covers", "Point", "Third Man"])
                    Wagon_X_axis = st.number_input("X-Axis", min_value=0)
                with C6:
                    feet_mov = st.selectbox("Feet Movement",["None","Front Foot","Back Foot","Charged Down","Walked Across","Created Room"])
                    Wagon_Y_axis = st.number_input("Y-Axis", min_value=0)
                Wagon_Y_axis = 1250 - Wagon_Y_axis
                st.write(images['wagon'])
    

        with st.container(border=True):
            p1, p2 = st.columns([1,2])
            with p2:
                desc = st.text_input("Description")

            with p1:
                if st.button("Add Ball Data 📝"):
                    new_data = pd.DataFrame({"Over": [over_no],"Ball": [ball_no],"Batting Team":[bat_team],"Bowling Team":[bowl_team],"Innings":[innings],
                    "Batter": [batter],"Batting Hand":[bat_hand],"Bowler":[bowler],"Bowling Style": [bowling_style],"Bowling Side":[bowl_side],"Runs": [runs],
                    "Outcome": [outcome],"False Shot": [false_shot],"Pitching Line": [line],"Pitching Length": [length],"length_x":[Length_X_axis],"length_y":[Length_Y_axis],
                    "Arrival Line":[arr_line],"Arrival line_x":[Line_X_axis],"Arrival line_y":[Line_Y_axis],"Shot Type":[shot_type],"Shot Connection":[shot_con],"Shot Intent":[shot_intent],
                    "Bat Impact_x":[con_X_axis],"Bat Impact_y":[con_Y_axis],"Wagon Zone": [wagon],"wagon_x":[Wagon_X_axis],"wagon_y":[Wagon_Y_axis],"Feet Movement":[feet_mov],
                    "Extras":[extras],"Extra Runs":[extra_runs],"Wicket":[Wicket],"Player Dismissed":[player_out],"Dismissed Type":[out_type],"Description":[desc if desc else None]})

                    st.session_state.ball_data = pd.concat([st.session_state.ball_data, new_data], ignore_index=True)


    st.divider()

    st.write(st.session_state.ball_data)

    @st.cache_data
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df(st.session_state.ball_data)

    st.download_button(label="Download Data ⬇️",data=csv,file_name='match_data.csv',mime='text/csv')

st.markdown("---")
st.markdown("<h4 style='font-size: 18px;'>🛠️ App Developed By:</h4>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 16px;'>"
            "<a href='https://www.linkedin.com/in/saiprasad-kagne/' target='_blank'>👨‍💻 Saiprasad Kagne</a> | "
            "<a href='https://www.linkedin.com/in/aakansha-sonawane-b5baa62ab/' target='_blank'>👩‍💻 Aakansha Sonawane</a>"
            "</p>", unsafe_allow_html=True)

