import streamlit as st
import pickle
import pandas as pd
import numpy as np
import xgboost
from xgboost import XGBRegressor

# Load the pre-trained model
pipe = pickle.load(open('pipe.pkl','rb'))

# Define the teams and cities for the dropdowns
teams = ['Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa', 
         'England', 'West Indies', 'Afghanistan', 'Pakistan', 'Sri Lanka']

cities = ['Colombo', 'Mirpur', 'Johannesburg', 'Dubai', 'Auckland', 'Cape Town', 
          'London', 'Pallekele', 'Barbados', 'Sydney', 'Mel bourne', 'Durban', 
          'St Lucia', 'Wellington', 'Lauderhill', 'Hamilton', 'Centurion', 
          'Manchester', 'Abu Dhabi', 'Mumbai', 'Nottingham', 'Southampton', 
          'Mount Maunganui', 'Chittagong', 'Kolkata', 'Lahore', 'Delhi', 
          'Nagpur', 'Chandigarh', 'Adelaide', 'Bangalore', 'St Kitts', 
          'Cardiff', 'Christchurch', 'Trinidad']

# Title of the web app
st.title('T20 WORLD CUP SCORE PREDICTOR')

# Layout the input fields into two columns
col1, col2 = st.columns(2)

# Batting and bowling teams selection
with col1:
    batting_team = st.selectbox('Select batting team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

# City selection
city = st.selectbox('Select city', sorted(cities))

# Create additional columns for input fields
col3, col4, col5 = st.columns(3)

# Inputs for current score, overs done, and wickets out
with col3:
    current_score = st.number_input('Current Score', min_value=0)
with col4:
    overs = st.number_input('Overs done (works for over > 5)', min_value=5.0, max_value=20.0, step=0.1)
with col5:
    wickets = st.number_input('Wickets out', min_value=0, max_value=10)

# Input for runs scored in the last 5 overs
last_five = st.number_input('Runs scored in last 5 overs', min_value=0)

# When the "Predict Score" button is pressed
if st.button('Predict Score'):
    # Calculate the number of balls left and wickets left
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets
    crr = current_score / overs

    # Create a DataFrame for the input data
    input_df = pd.DataFrame(
        {'batting_team': [batting_team], 
         'bowling_team': [bowling_team], 
         'city': [city], 
         'current_score': [current_score], 
         'balls_left': [balls_left], 
         'wickets_left': [wickets_left], 
         'crr': [crr], 
         'last_five': [last_five]}
    )
    
    # Make the prediction using the loaded model
    result = pipe.predict(input_df)

    # Display the predicted score
    st.header("Predicted Score - " + str(int(result[0])))
