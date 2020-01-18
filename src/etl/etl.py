import os
import glob
import psycopg2
import pandas as pd
import h5py
from sql_queries import *

def process_song_file(cur, filepath):
    """Execute ETL process on song data inserting data into a song and artist table
    
    Parameters: 
        cur (object) - database cursor
        filepath (object) - path to song data on S3
    Returns: 
        None
    """       
    # Read content in h5 file
    file = h5py.File(filepath, 'r')

    # Access groups and receive data via key following the hierarchy in h5 file 
    group_metadata = file['metadata']
    group_analysis = file['analysis']
    group_musicbrainz = file['musicbrainz']
    
    data_metadata_songs = group_metadata['songs'].value
    data_analysis_songs = group_analysis['songs'].value
    data_musicbrainz_songs = group_musicbrainz['songs'].value
    
    # Decode binary data format and flatten dataset for insert 
    artist_data = list([data_metadata_songs[0][4].decode('utf-8'), data_metadata_songs[0][9].decode('utf-8'),
                        data_metadata_songs[0][5].item(), data_metadata_songs[0][7].item()])
    
    song_data = list([data_metadata_songs[0][17].decode('utf-8'), data_metadata_songs[0][4].decode('utf-8'), 
                      data_metadata_songs[0][18].decode('utf-8'), data_metadata_songs[0][14].decode('utf-8'),
                      data_musicbrainz_songs[0][1].item(), data_analysis_songs[0][3].item()])

    # Fill artist and song table
    cur.execute(artist_table_insert, artist_data)
    cur.execute(song_table_insert, song_data)

def process_log_file(cur, filepath):
    """
    Extract data in log files from datasource and manage the transformation of the data
    
    Parameters: 
        cur (object) - database cursor
        filepath (object) - path to song log data on S3
    Returns: 
        None
    """    
    # Read content in json file and filter by NextSong
    file = pd.read_json(filepath, lines=True)
    data = file[file.page == 'NextSong']
    
    # Transform time, user, songplays data and insert them to respective tables
    transform_time_data(data, cur)
    transform_user_data(data, cur)
    transform_songplay_data(data, cur) 

def transform_time_data(data, cur):
    """
    Transform and load log data containing time related details
    about played songs into time table
    
    Parameters: 
        data (object) - pd dataframe containing log data
    Returns: 
        None
    """

    # Convert timestamp column to datetime (in ms)
    timestamp_series = data.ts
    datetime_series = pd.to_datetime(timestamp_series, unit='ms') 

    # Extract timedata details and name columns
    timedata = [timestamp_series, datetime_series.dt.hour, datetime_series.dt.day, 
                datetime_series.dt.week, 
                datetime_series.dt.month, datetime_series.dt.year, 
                datetime_series.dt.weekday]
    column_labels = ['start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday']

    # Combine timedata and labels
    labeled_timedata = dict(zip(column_labels, timedata))

    # Iterate through dataframe and insert each row in time table
    time_df = pd.DataFrame(data=labeled_timedata)
    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

def transform_user_data(data, cur):
    """
    Transform and load log data containing user details into user table
    
    Parameters: 
        data (object) - pd dataframe containing log data
    Returns: 
        None
    """
    # Remove user duplicates and create user dataframe
    user_df = data[['userId', 'firstName', 'lastName', 'gender', 'level']].drop_duplicates('userId')

    # Insert user records in user table
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

def transform_songplay_data(data, cur):
    """
    Transform and load log data about played songs to songplays table
    
    Parameters: 
        data (object) - pd dataframe containing log data
    Returns: 
        None
    """
    # Get played songs based on user logs and artist- and song ids
    for i, row in data.iterrows():
        # Get songid and artistid from song and artist tables
        # indicating the played songs is available in song datasource
        cur.execute(song_select, (row.song, row.artist))
        results = cur.fetchone()
        
        # Mark played songs as with None when these are not available in own datasource
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None
   
        # Insert played songs into songplay table
        songplay_data = ([row.ts, row.userId, songid, row.level, artistid, 
                              row.sessionId, row.location, row.userAgent])
        cur.execute(songplay_table_insert, songplay_data)

def process_data(cur, conn, filepath, func, filetyp):
    """ 
    Establish the connection to database and process song and log data from external datasource
    
    Parameters: 
        cur (object) - database cursor
        conn (object) - database connection details
        filepath (string) - path to song or log data
        func (function) - process song or log file function
        filetyp (string) - filetyp of datasource (.h5 or .json)
    Returns: 
        None
    """ 
    # Get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, filetyp))
        for f in files :
            all_files.append(os.path.abspath(f))

    # Get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # Apply processing function on respective file 
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))

def main():
    """
    Establish the connection to database and process song and log data from external datasource
    
    Parameters: 
        None
    Returns: 
        None
    """ 
    conn = psycopg2.connect("host=localhost dbname=musicdb")
    cur = conn.cursor()
    process_data(cur, conn, filepath='../data/song_data', func=process_song_file, filetyp='*.h5')
    process_data(cur, conn, filepath='../data/log_data', func=process_log_file, filetyp='*.json')

if __name__ == "__main__":
    main()