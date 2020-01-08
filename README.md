###### Matthias Reichel |	[Linkedin](https://www.linkedin.com/in/matthiasreichel/) | [Email](mailto:Matthias.K.Reichel@gmail.com)


# Data-Modeling-Postgres

The goal of the project is to provide an end-to-end solution applying  technology stacks related to data engineering and API
development. Ultimately the application enables an user to analyze user logs about played songs and details about related artists. The song data used are available on 
<a href="http://millionsongdataset.com/pages/getting-dataset/" target="_blank">Million Song Dataset Webpage</a>. 
The user logs have been generated using the eventsim generator available on <a href="https://github.com/Interana/eventsim" target="_blank">Interana Github</a>.  

# Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Architecture](#architecture)
- [Data Model](#data-model)
- [Roadmap](#roadmap)
- [Installation](#installation)
- [Disclaimer](#disclaimer)

___


# Project Structure

```Data-Modeling-Postgres
    ├── ...
	├──	data						# Contains datasources for project
    ├── src                     	# Source folder contains app
    │   ├── api         			# WIP
    │   ├── batch         			# WIP
    │   └── data                	# Files for ETL 
    │		├── create_tables.py 	# Manage connection and tables        		
	│		├── etl.py        		# Handles ETL process
	│		└── sql_queries.py		# Execute table manipulation and querying
	│
	└── ...
```

# Architecture

The application depends on two different datasources (HDF5 and JSON). Both are are uploaded to an simple storage system (S3). As part of the exercice a postgres
database is set-up and an ETL process implemented. Finally the normalized data are exposed as Rest service which is consumed by an React dashboard.

![alt Image not available](https://raw.githubusercontent.com/MatthiasReichel/Data-Modeling-Postgres/master/img/Architecture.PNG)

# Data Model

WIP


# Roadmap

- [x] Create Postgres server and database
- [x] Design datamodel and create tables
- [x] Implementation ETL Process
- [ ] Create RESTful API for music data consumption
- [ ] Consum data via React dashboard
- [ ] Deploy application on AWS

# Installation

The project can be hosted on different cloud services e.g. Amazon Web Services (AWS). However, to demo the application it can be run locally:


WIP

# Disclaimer

Originally the project was created as part of the Udacity Nanodegree certificaton. However, to add complexity the scope
of the project was extended adding additional datasources as well as a middle and frontend layer.
Note that the status of the project is tracked via the roadmap.