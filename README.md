# PROJECT #1

## Project Description

This project uses Github Actions to lint,test and deploy a django application to dockerhub and github packages.

## Triggers

This project is triggered by:

1. the 'push' event targetted towards the main branch and the 'feature/**' branch , 
2. It can also be triggered manually.

## Jobs

### Linting

Linting - using the matrix startegy the job can be ran on two runners [ubuntu-20.04,ubuntu-22.04] . The job runs on a python:3.9 container. It also contains a service named 'postgres' . This service uses a postgres:latest image. It describes environmental variables e.g POSTGRES_DB which is saved in GHA secrets. It also contains healthchecks for the service

An enviroenmental variable is defined at the job level. This will be used by other services (containers) to create a connection

The job checkouts the code from the repo, caches python packages , installs dependencies and runs python migrations
The linting is done with flake8, test is done with coverage, tests reports are uploaded as artifacts


### Build