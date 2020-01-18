###### Matthias Reichel |	[Linkedin](https://www.linkedin.com/in/matthiasreichel/) | [Email](mailto:Matthias.K.Reichel@gmail.com)


# Table of Contents

- [Scope](#scope)
- [Architecture](#architecture)
- [Data Model](#data-model)
- [Roadmap](#roadmap)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Disclaimer](#disclaimer)

___

# Scope

The goal of the project is to provide an end-to-end solution applying technology stacks related to data engineering and API
development. Ultimately the application enables an enduser to analyze user logs about played songs and details about related artists. 
The song data being used are available on <a href="http://millionsongdataset.com/pages/getting-dataset/" target="_blank">Million Song Dataset Webpage</a>. 
The user logs have been generated using the eventsim generator available on <a href="https://github.com/Interana/eventsim" target="_blank">Interana Github</a>.

# Architecture

The application depends on two different datasources (HDF5 and JSON). Both are are uploaded to an simple storage system (S3). As part of the exercice a postgres
database is set-up and an ETL process implemented. Finally the normalized data are exposed as Rest service which is consumed by an React dashboard.

![alt Image not available](https://raw.githubusercontent.com/MatthiasReichel/Data-Modeling-Postgres/master/img/Architecture.PNG)

# Data Model

To normalize the data from the datasource the datamodel follows a star schema resulting in four dimension tables (user, time, artist, song) 
and one fact table (songsplays). Hereby, the songs and artists table containing details about available songs and artists while the 
users and time tables containing information from the user logs. The actual user behaviour is described by the songsplays table representing
details about played songs. The relationship (references) between the entity classes is describend in the image below.
![alt Image not available](https://raw.githubusercontent.com/MatthiasReichel/Data-Modeling-Postgres/master/img/Datamodel.PNG)


# Roadmap

The roadmap tracks status quo of the project:

- [x] Create Postgres server and database
- [x] Design datamodel and create tables
- [x] Implement ETL Process
- [ ] Create RESTful API
- [ ] Consum data via React dashboard
- [ ] Deploy application on AWS

# Project Structure

The project structure shows all files needed to understand and run the application. Note that
the project structure may change as the project evolves (see [roadmap](#roadmap)).

```
├── src   # All app source files 
│   ├── api     # WIP
│   ├── batch   # WIP
│   ├── data    # Source data
│   │   └── log_data    # Json files
│   │   └── song_data   # HDF5 files
│   ├── webapp  # WIP
│   └── etl     #  All ETL related files
│       ├── create_tables.py   # Manage connections and database tables
│       ├── etl.py             # Handles ETL processs
│       └── sql_queries.py     # Execute table manipulation and querying
└── readme.md   # Project description
```

# Installation

For demo purposes the application can be run locally. Therefore, a virtual machine hosting a postgres server
need to be configured. Note that the used Postgres Server Version is 11.2. Afterwards the postgres database 'musicdb' need to be build.
Hereby, ensure that the database is 'UTF-8' encoded. If the database runs on 'WIN1252' you may encounter unicode errors due 
to missing support for specific character sets. More details on the database setup with Anaconda can 
be found <a href="https://medium.com/@FranckPachot/postgresql-and-jupyter-notebook-e7b68cb6427d" target="_blank">here</a>.

To create and execute the ETL pipeline, execute following commands from your terminal:

```
cd ..\Data-Modeling-Postgres\src\data   # Move to the folder with the src files
python create_tables.py                 # Build database and empty tables
python etl.py                           # Execute ETL pipeline and populate tables
```

# Disclaimer

Originally the project was created as part of the Udacity Data Engineering Nanodegree certification. However, to add complexity the scope
of the project was extended adding additional datasources as well as a middle and frontend layer.
Note that the status of the project is tracked via the [roadmap](#roadmap).