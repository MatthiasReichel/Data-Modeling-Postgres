# DROP TABLES

songplay_table_drop = ("DROP TABLE IF EXISTS songplays CASCADE")
user_table_drop = ("DROP TABLE IF EXISTS users CASCADE")
song_table_drop = ("DROP TABLE IF EXISTS songs CASCADE")
artist_table_drop = ("DROP TABLE IF EXISTS artists CASCADE")
time_table_drop = ("DROP TABLE IF EXISTS time CASCADE")
test_table_drop = ("DROP TABLE IF EXISTS test CASCADE")


# CREATE FACT TABLE

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY, 
                                start_time BIGINT REFERENCES time (start_time), 
                                user_id VARCHAR REFERENCES users (user_id), 
                                level VARCHAR, 
                                song_id VARCHAR REFERENCES songs (song_id), 
                                artist_id VARCHAR REFERENCES artists (artist_id), 
                                session_id VARCHAR, 
                                location VARCHAR, 
                                user_agent VARCHAR)""")

# CREATE DIMENSION TABLES

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id VARCHAR PRIMARY KEY,
                            first_name VARCHAR, 
                            last_name VARCHAR, 
                            gender VARCHAR, 
                            level VARCHAR)""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time BIGINT PRIMARY KEY,
                            hour INT NOT NULL, 
                            day INT NOT NULL, 
                            week INT NOT NULL, 
                            month INT NOT NULL, 
                            year INT NOT NULL, 
                            weekday INT NOT NULL)""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id VARCHAR PRIMARY KEY,
                            artist_id VARCHAR NOT NULL,
                            song_title VARCHAR,
                            album_title VARCHAR,
                            year INT, 
                            duration FLOAT(20))""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id VARCHAR PRIMARY KEY, 
                            name VARCHAR NOT NULL,
                            latitude DECIMAL(8,5), 
                            longitude DECIMAL(8,5))""")


# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time, 
                            user_id, 
                            song_id,
                            level,
                            artist_id, 
                            session_id, 
                            location, 
                            user_agent) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                            ON CONFLICT DO NOTHING""")

user_table_insert = ("""INSERT INTO users (user_id, 
                        first_name, 
                        last_name, 
                        gender, 
                        level) 
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT DO NOTHING""")

song_table_insert = ("""INSERT INTO songs (song_id,
                        artist_id, 
                        song_title,
                        album_title,
                        year, 
                        duration) 
                        VALUES (%s, %s, %s, %s, %s, %s)
                        ON CONFLICT DO NOTHING""")
 
artist_table_insert = ("""INSERT INTO artists (artist_id, 
                            name,  
                            latitude, 
                            longitude) 
                            VALUES (%s, %s, %s, %s)
                            ON CONFLICT DO NOTHING""")

time_table_insert = ("""INSERT INTO time (start_time, 
                        hour, 
                        day, 
                        week,
                        month, 
                        year, 
                        weekday) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT DO NOTHING""")

# FIND SONGS

song_select = ("""SELECT songs.song_id, artists.artist_id FROM 
                  songs JOIN artists ON songs.artist_id = artists.artist_id
                  WHERE songs.song_title = %s AND artists.name = %s""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [user_table_drop, song_table_drop, artist_table_drop, time_table_drop, songplay_table_drop]