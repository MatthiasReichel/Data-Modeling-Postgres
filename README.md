###### Matthias Reichel |	[linkedin](https://www.linkedin.com/in/matthiasreichel/) | [Email](mailto:Matthias.K.Reichel@gmail.com)


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

The goal of the project is to provide an prototype following an end-to-end approach. Hereby, the application
should e.g. allow a business user to analyze user logs about played music songs. The leveraged technologies are hosted 
on Amazon Web Services (AWS) but can be run locally. The song data used are available on 
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
- [ ] Create RESTful API for data consumption
- [ ] Consum data via React dashboard
- [ ] Deploy application on AWS

# Installation

WIP

# Disclaimer

Originally the project was created as part of the Udacity Nanodegree certificaton. However, to add complexity the scope
of the project was extended adding additional datasources as well as a middle and frontend layer.
Note that the status of the project is tracked via the roadmap.