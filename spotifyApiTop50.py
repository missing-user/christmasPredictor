import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os 

# load the credentials from the .env file
load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.environ.get('secretUser'),
                                                           client_secret=os.environ.get('secretKey')))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])





import numpy as np
import pandas as pd
import datetime

# read csv into pandas dataframe
df = pd.read_csv('archive/historicCharts.csv')

# read the date strings into pandas as datetime objects
df["date"] = pd.to_datetime(df["Week"])
df = df.set_index("date")
df.drop(["Week"], axis=1, inplace=True)

# drop other dataframe columns that aren't of interest
df.drop(["Explicit", "Track_Number_on_Album", "Artist_Followers", "Duration_MS", "Track_Number_on_Album", "Link", "Album_Name"], axis=1, inplace=True)

df["Artist"].astype('string')
df["Track"].astype('string')

# convert the Artist_Genres column to lists
df["Artist_Genres"] = df["Artist_Genres"].apply(eval)

df.head()