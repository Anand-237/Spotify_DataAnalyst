import os
import re 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import mysql.connector
import pandas as pd

# Load Spotify credentials from environment variables
client_id = os.getenv("SPOTIFY_CLIENT_ID", "YOUR_SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET", "YOUR_SPOTIFY_CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
                   client_id=client_id,
                   client_secret=client_secret))


# Load MySQL password from environment variables
mysql_password = os.getenv("MYSQL_PASSWORD", "YOUR_MYSQL_PASSWORD")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=mysql_password,
    database="spotify_db"
)
cursor=conn.cursor()


all_track=[]

song_track=open("trace.txt","r")

for tracks in song_track:
    try:
        track_url=tracks
        match = re.search(r'track/([A-Za-z0-9]+)', track_url)

        if match:
            track_id = match.group(1)
            track = sp.track(track_id)
   

            track_data={
            "Track_Name":track['name'],
            "Artists_Name":track['artists'][0]['name'],
            "Duration":track['duration_ms']/60000,
            "Album_Id":track["album"]["id"],
            'Release Date':track["album"]["release_date"],
            "Playable":track['is_playable'],
            "Disc_Number":track["disc_number"],
            "Track_Type":track["type"]


            }
 
            '''print("Track_Name:",track_data["Track_Name"])
            print("Album_Id:",track_data["Album_Id"])
            print("Artists_Name:",track_data["Artists_Name"])
            print("Duration:",track_data["Duration"])
            print("Release Date:",track_data["Release Date"])
            print("Disc_Number:",track_data["Disc_Number"])
            print("Type:",track_data["Track_Type"])
            print("Is_Playable:",track_data["Playable"])'''

            query="""insert into spotify_entity(Track_Name,Artists_Name,Duration,Album_Id,ReleaseDate,Playable,Disc_Number,Track_Type)
            values(%s,%s,%s,%s,%s,%s,%s,%s)"""
            values=(
                track_data["Track_Name"],
                track_data["Artists_Name"],
                track_data["Duration"],
                track_data["Album_Id"],
                track_data["Release Date"],
                track_data["Playable"],
                track_data["Disc_Number"],
                track_data["Track_Type"],
                
                
            )


            cursor.execute(query,values)
            conn.commit()
            
            '''all_track.append(track_data)
            
            df=pd.DataFrame(all_track)
            print(df)
            df.to_csv("Spotify.csv",index=False)
            df.to_excel("Spotify.xlsx",index=False)'''
       

    except Exception as e :
        print(e)
conn.close()