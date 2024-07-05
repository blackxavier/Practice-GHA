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

An environmental variable is defined at the job level. This will be used by other services (containers) to create a connection

The job checkouts the code from the repo, caches python packages , installs dependencies and runs python migrations
The linting is done with flake8, test is done with coverage, tests reports are uploaded as artifacts


### Build

Build - This job does not use any strategy , it has a `needs` parameter that makes sure the job does not run until the `Linting` jobs succeeds. It also has a `permissions` parameter that grants the runner write access for github packages . The steps involve checking out the repo, setting up QEMU and Buildx for docker. Logging into dockerhub and ghrc, building an image with the repository root path as a context and pushing the image to both GHCR and dockerhub.

