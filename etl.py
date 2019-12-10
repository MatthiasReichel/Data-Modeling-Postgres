import os
import uuid
import glob
import psycopg2
import pandas as pd
from sql_queries import *

"""Execute extract, transfor and load on song details

Ensure that song details fetched from song json, properly processed and inserted in respective song
and artist table
"""
def process_song_file(cur, filepath):
    # Open song file
    df = pd.read_json(filepath, lines=True)

    # Access specific song values (via respective columname)
    song_data_raw = df[['song_id', 'title', 'artist_id', 'year', 'duration']].values

    # Build final list for table insert
    song_data = list([song_data_raw[0,0], song_data_raw[0,1], song_data_raw[0,2], 
                      song_data_raw[0,3], song_data_raw[0,4]])
    cur.execute(song_table_insert, song_data)
    
    # Access specific artist values (viavia respective columname)
    artist_data_raw = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 
                          'artist_longitude']].values

    # Build final list for table insert
    artist_data = list([artist_data_raw[0,0], artist_data_raw[0,1], artist_data_raw[0,2], 
                        artist_data_raw[0,3], artist_data_raw[0,4]])
    cur.execute(artist_table_insert, artist_data)

"""Execute extract, transfor and load on log details

Ensure that log details fetched from log detail json, properly processed and inserted in
time, user and songplay table. Note that the artist id from song and artist table is being matched
to ensure that the played songs being selected

"""
def process_log_file(cur, filepath):
    # Open log file
    df = pd.read_json(filepath, lines=True)

    # Filter by NextSong action
    time_table_raw = df[df.page == 'NextSong']

    # Convert timestamp column to datetime
    timestamp_series = time_table_raw.ts
    datetime_series = pd.to_datetime(timestamp_series, unit='ms') 

    # Extract timedata details and name columns
    timedata = [timestamp_series, datetime_series.dt.hour, datetime_series.dt.day, 
                datetime_series.dt.week, 
                datetime_series.dt.month, datetime_series.dt.year, 
                datetime_series.dt.weekday]
    column_labels = ['start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday']

    # Combine timedata and labels and pack those into dataframe allowing
    labeled_timedata = dict(zip(column_labels, timedata))

    # Create time dataframe allowing to iterate through inserting rows into time time table
    time_df = pd.DataFrame(data=labeled_timedata)
    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
    
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # Insert songplay record 
        songplay_data = list([row.ts, row.userId, songid, row.level, artistid, 
                              row.sessionId, row.location, row.userAgent])
        cur.execute(songplay_table_insert, songplay_data)

"""Receive actual log and song data

Process log and song data based on provided path and respective function
"""
def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))

"""Executed on intitial load ensuring database access and data processing

Establish the connection to database and process song and log data from external datasource
"""
def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()