## Week 1

| Deliverable | Status | Tasks |
| :---: | :---: | :---: |
| **Refinement and Deployment of UseCases** [#43](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/43) |
| SubFlow : Data cleaning and modification of code base to accommodate edge cases(Modifying the code base in modules to handle edge cases in the data retrieved from REST API's)   | Complete | [#44](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/44),[Codebase](https://github.ncsu.edu/sgadipa/csc510-project/tree/master/backend/flask/app) |
| SubFlow : Initializing and Setting up Flask application(Setting up Flask framework for creating web application)  | Complete | [#45](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/45), [Flask](https://github.ncsu.edu/sgadipa/csc510-project/tree/master/backend/flask) |
| SubFlow : Deployment of Use cases dashboards using Tableau Online(Deployment of the whole portal into the web using Tableau Online)  | Complete | [#46](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/46), [ViewModule](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/flask/app/views.py) |



## Week 2


| Deliverable | Status | Tasks |
| :---: | :---: | :---: |
| **Integration into Flask and automating data ingestion** [#47](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/47) |
| SubFlow : Setting up APScheduler module to automate Data Ingestion/Update(Creating a module to automate the data ingestion process in a timely manner using Advanced Python Scheduler library in python)   | Complete | [#48](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/48), [Scheduler](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/flask/app/schedule.py) |
| SubFlow : Integrating all the modules into Flask application(Consolidating all the modules created and pushing them into flask instance) | Complete | [#49](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/49),[Integration](https://github.ncsu.edu/sgadipa/csc510-project/tree/master/backend/flask/app)  |
| SubFlow : Exploring nginx server and containers to automate deployment(Getting to know about nginx web server and its properties additionally studying on how to create containers using dockers)  | Complete | [#50](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/50),[nginx](https://github.ncsu.edu/sgadipa/csc510-project/tree/master/backend/nginx) |


## Week 3


| Deliverable | Status | Tasks |
| :---: | :---: | :---: |
| **Writing Deployment scripts and System Integration** [#51](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/51) |
| SubFlow : Installing and Creating dockers for Flask and nginx server(Installing docker and creating containers for Flask and nginx servers)  | Complete | [#52](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/52), [Dockercompose](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/docker-compose.yml)|
| SubFlow : Setting up configuration files required for communication of both servers(Creating dockerfile in both servers to inform about the packages and libraries which needs to be installed while building the docker)  | Complete | [#53](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/53), [ConfigFlask](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/flask/Dockerfile),[ConfigNginx](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/nginx/Dockerfile)  |
| SubFlow : Configuring wsgi for communication of 2 severs(Enabling communication between two servers using ports, by Web Server Gateway Interface which forwards web requests from web server to a web application)  | Complete | [#54](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/54),[FlaskWsgi](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/flask/app.ini),[NginxWsgi](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/nginx/nginx.conf) |
| SubFlow : Running the dockers and Creation of Worksheet and screencast(Finally building the dockers and setting them up)  | Complete | [#55](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/55) |

