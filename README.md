## 1) Discuss the purpose of this database in the context of the startup Sparkify and their analytical goals.** 

Introducing relational database like Postgre allows to standardize the datamodel. Furthermore, the data integrity can be ensured. 
Relational database systems bring also in the needed flexibility as tables can be added (or altered). Furthermore, Power users or
developers can rely on SQL to query details about the user behaviour or songs being played. By relying on Postgre the business users dont need to scan through the JSON files which is not error-prone and extremely time consuming 
Ideally the data in the table could be exposed and a dashboard could be build on top of the database layer allowing business users to slice and dice the music data.

## 2) State and justify your database schema design and ETL pipeline.

The architecture follows the star schema consisting of one fact as well as several dimension tables. Hereby, the fact table contains the
information about songs which have been played (e.g. duration time, location etc,). Hereby, it is important to notice that the fact table also contain
all necessary ids allowing to match it with dimension tables (e.g. user behavior, artist information). By combining and aggregating numbers in those tables business insights can be derived.

## 3) Provide example queries and results for song play analysis.

A typical problem to solve might be to analyse the number of female and male users. By analyzing this aspect it could be derivad which
songs are being preferred by which gender allowing to suggest more suitable tracks depending on the gender of the user. 
The query to run a first analysis might look alike: 

```("""SELECT COUNT(users.gender), songplays.song_id 
FROM songplays JOIN users ON songplays.user_id = users.user_id
WHERE users.gender = 'F' 
GROUP BY songplays.song_id""")```