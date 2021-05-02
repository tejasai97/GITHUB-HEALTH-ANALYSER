# Milestone 4: Deployment


For this Milestone, the major focus of work was on delivering a fully functional and deployable portal using technologies like Flask, nginx with the help of configuration management tools like docker.  


# Deployment methodology and Scripts


## Description


As we need to automate the deployment process a script has been written for the users which when executed on their local system creates web servers automatically and by using the IP address of the portal, the user can get access to the portal and can interact with it to extract the required information. But before running the script the user has to set up and install dependencies involved, the instructions are listed below. After the user has done with the setup he can directly access the portal using its IP address. But the portal is being visualized using Tableau Online and the user should have an account with the Tableau to visit the portal. The credentials for the Tableau account is mentioned below and any user who would like to play around the portal can use them while authenticating.   


### Setup Instructions 

1) Git clone this repository, the link for this repository is [here](https://github.ncsu.edu/sgadipa/csc510-project)


2) Install and setup docker and docker-compose, the steps are mentioned [here](https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-18-04)


### Deployment script to automate the process


The following commands need to be executed to build the dockers and deploy it into the web for usage

3) After cloning the repository traverse to the "backend" folder 


4) Run these following commands
```````
sudo docker-compose build
sudo docker-compose up
```````

### Accessing web portal and credentials required


After setting up above dependencies the user can access the web portal [here](http://ec2-3-82-251-8.compute-1.amazonaws.com/)


Now the Tableau authentication page pops up and the user can use following credentials to login into the portal and visualize the dashboards. 

```````
Username:  sgadipa@ncsu.edu
Password:  csc510-project
````````


## Procedure involved to automate the deployment


This section gives details on how the deployment was done and what is the technology stack involved also gives the details about the configuration files which need to be created/modified in different components involved in the automation of deployment procedure. 


### Technology Stack 


| Role | Technology involved |
| :---: | :---: |
| Web Framework | Flask application |
| Web Server | Nginx |
| Communication| Web Server Gateway Interface |
| Deployment | Docker |
| Hosting | AWS EC2 |
| Database | MongoDB |
| Visualization | Tableau |


#### Brief Introduction of the Technology stack involved


1) Flask: Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.


2) Nginx: Nginx is a web server which can also be used as a reverse proxy, load balancer, mail proxy, and HTTP cache. 


3) Docker: Docker is used to running software packages called containers. Containers are isolated from each other and bundle their own application, tools, libraries and configuration files; they can communicate with each other through well-defined channels. All containers are run by a single operating system kernel and are thus more lightweight than virtual machines. Containers are created from images that specify their precise contents. Images are often created by combining and modifying standard images downloaded from public repositories.


The pipeline of the above technologies mentioned can be visualized below
![image](https://media.github.ncsu.edu/user/13118/files/508f9580-62e9-11e9-950d-bf6663398e77)


### Description and the background process involved


This section describes the background operations being triggered while executing the deployment script mentioned above


When the command "sudo docker-compose build" is being executed the following happens at the background


-> The docker-compose.yml file which is present [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/docker-compose.yml) will be executed, in the file, it contains the details of two containers which needs to be deployed, one is flask and other is nginx. This file also mentions that flask server is available at port 8080 for communication and thus being exposed. The port number mapping present in nginx server is the mapping from user's request port number to nginx port number. In brief, it implies that user sends an HTTP request to nginx server and further this server communicates with the Flask application at port 8080 and flask gives the desired web page to nginx which is further sent as an HTTP response to the user.


-> Now coming to "Flask" folder and its contents can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/tree/master/backend/flask) 


#### Flask Content Description
All the modules implemented are pushed into the flask application which can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/tree/master/backend/flask/app) 


Additionally, two other modules are being created from Milestone3 for automating the deployment and data ingestion process


  1) Views Module: This module is used to send the desired web-page content to the nginx server when a request is made to the flask application. The content which is being sent is the dashboard which is being deployed in the web using Tableau Online. The codebase for this module can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/flask/app/views.py) 


  2) Scheduler Module: This module is to automate the data ingestion/update process, additional details can be found in the below section.
  The codebase for this module can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/flask/app/schedule.py)


  3) DockerFile: This file contains the required image of the system which needs to be downloaded and packages which need to be installed for setting up this virtual machine, this process is done while executing and building the docker-compose file. The codebase for this can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/flask/Dockerfile)


  4) Configuration File: The configurations required for flask application can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/flask/app.ini) which contains the information about the instance of flask application created and the file to be called while building this container. 


  5) Required Packages: This file contains different packages which needs to be installed while building this container. The file can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/flask/requirements.txt)


  6) Main Program: This is the entry point of the flask application and main function which is being called during the buildup phase. The codebase for this can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/flask/run.py)



-> Now coming to "nginx" folder and its contents can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/tree/master/backend/nginx) 


#### Nginx Content Description


  1) DockerFile: This file contains the required image of the system which needs to be downloaded and packages which need to be installed for setting up this virtual machine, this process is done while executing and building the docker-compose file. The codebase for this can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/nginx/Dockerfile)


  2) Configuration File: The configurations required for flask application can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/nginx/nginx.conf) which contains the information about the port number on which nginx serves and port number of flask application onto which it communicates process HTTP requests.


-> Details about communication between two containers


#### Web Server Gateway Interface


Introduction: The Web Server Gateway Interface is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language.

In this project wsgi acts as a communication channel between two containers, nginx being the web server forwards the requests sent by the users to the web framework which is the flask, and the flask gives the desired content for the request.


# Data Ingest/Update


As part of the deployment task, we also need to automate the data ingestion/update mechanism. For automating this process we use the help of Advanced Python Scheduler library in python. 


## Introduction 

Advanced Python Scheduler (APScheduler) is a Python library that lets you schedule your Python code to be executed later, either just once or periodically. You can add new jobs or remove old ones on the fly as you please. If you store your jobs in a database, they will also survive scheduler restarts and maintain their state. When the scheduler is restarted, it will then run all the jobs it should have run while it was offline 


APScheduler has three built-in scheduling systems you can use:


-> Cron-style scheduling (with optional start/end times)


-> Interval-based execution (runs jobs on even intervals, with optional start/end times)


-> One-off delayed execution (runs jobs once, on a set date/time)


## Usage in the project 


The automation of the data ingestion process is implemented in a separate module called Scheduler and the code base of this module can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/flask/app/schedule.py).


The above file contains a function named schedUpdate() which internally calls all the other cores modules like LibraryExtractor(), DatabaseDriver() which populate the data into the DB and fetches the data using REST API's. Then an instance of BackgroundScheduler() thread is created which has the capability to call any piece of code in a timely manner. Now for this instance created we create a cron job with Interval based execution and interval time of 24 hours also we will pass the schedUpdate() function with it. This implies that this job will call the schedUpdate() function for every 24 hours which in-built calls the other modules which fetch the data using REST API's and update the DB timely. 


Below is a sample code snippet which performs the above mentioned tasks
``````````
sched = BackgroundScheduler(daemon=True)
sched.add_job(schedUpdate,'interval',hours=24)
sched.start()
``````````


# Code Inspection


The code has been modularized according to Object Oriented programming techniques and was modified to handle edge cases. Also previously the organization names were hard-coded. But now the organization names are retrieved from the Database. Also, some of the data retrieved from REST API's were inconsistent and erroneous, so the code has been updated to accommodate that kind of data.


The code structure of the project is given below:

1) Flask: This folder contains all the required configuration files for setting up the flask application and the function to be called when the Flask container gets deployed. This folder can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/tree/master/backend)


2) App: This folder contains the implementation of all the core modules used for retrieving the data from the REST API's and updating the DB. This folder contains the scripts which were used in the implementation of Use Cases. This folder can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/tree/master/backend/flask/app)


3) Nginx: This folder contains all the required configuration files for setting up the nginx web-server and dockerfile to be executed while building this virtual machine. This folder can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/tree/master/backend/nginx)


The master code base can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/tree/master/backend)


# Task Tracking

We have created a worksheet which provides details regarding the work distribution among the teammates for each iteration. It also provides links to the tasks in Azure DevOps.

[WORKSHEET Milestone4](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/WORKSHEETMilestone4.md)
 

# Screencast

We have created a screencast Demonstrating the three use cases, deployment process and also about data ingestion and update. you can look at the video by clicking [here](https://youtu.be/qxOCUz5iKSc).

You can also download the video from [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/videos/2019-03-28%20at%2023-11-48.mp4).
