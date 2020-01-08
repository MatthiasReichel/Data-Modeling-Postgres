###### Matthias Reichel |	[Linkedin](https://www.linkedin.com/in/matthiasreichel/) | [Email](mailto:Matthias.K.Reichel@gmail.com)


# Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Architecture](#architecture)
- [Data Model](#data-model)
- [Roadmap](#roadmap)
- [Installation](#installation)
- [Disclaimer](#disclaimer)

___

# Introduction

The goal of the project is to provide an end-to-end solution covering different technology stacks. Ultimately the application
should enable an user to analyze user logs about played songs and details about related artists. The song data used are available on 
<a href="http://millionsongdataset.com/pages/getting-dataset/" target="_blank">Million Song Dataset Webpage</a>. 
The user logs have been generated using the eventsim generator available on <a href="https://github.com/Interana/eventsim" target="_blank">Interana Github</a>.  

# Project Structure

WIP

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

The application is (temporarily) available on Amazon Web Services (AWS). However, the application can be run locally following the steps below:

WIP

# Disclaimer

Originally the project was created as part of the Udacity Nanodegree certificaton. However, to add complexity the scope
of the project was extended adding additional datasources as well as a middle and frontend layer.
Note that the status of the project is tracked via the roadmap.