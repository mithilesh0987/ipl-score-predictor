from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import keras
import tensorflow as tf

app = Flask(__name__)

# Load your model and data
ipl = pd.read_csv('/path_to_your_data/ipl_data.csv')
model = keras.models.load_model('/path_to_your_model/ipl_score_predictor.h5')

# Label Encoders
venue_encoder = LabelEncoder()
batting_team_encoder = LabelEncoder()
bowling_team_encoder = LabelEncoder()
striker_encoder = LabelEncoder()
bowler_encoder = LabelEncoder()

# Preprocessing
def preprocess_data():
    df = ipl.drop(['date', 'runs', 'wickets', 'overs', 'runs_last_5', 'wickets_last_5', 'mid', 'striker', 'non-striker'], axis=1)
    X = df.drop(['total'], axis=1)
    X['venue'] = venue_encoder.fit_transform(X['venue'])
    X['bat_team'] = batting_team_encoder.fit_transform(X['bat_team'])
    X['bowl_team'] = bowling_team_encoder.fit_transform(X['bowl_team'])
    X['batsman'] = striker_encoder.fit_transform(X['batsman'])
    X['bowler'] = bowler_encoder.fit_transform(X['bowler'])
    return X

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dropdowns', methods=['GET'])
def dropdowns():
    venues = list(ipl['venue'].unique())
    batting_teams = list(ipl['bat_team'].unique())
    bowling_teams = list(ipl['bowl_team'].unique())
    strikers = list(ipl['batsman'].unique())
    bowlers = list(ipl['bowler'].unique())
    return jsonify({
        'venues': venues,
        'battingTeams': batting_teams,
        'bowlingTeams': bowling_teams,
        'strikers
