# CSC510-project

# List of team members


| Name | Unity ID |
| :---: | :---: |
| Siva Ajay Tadepalli | stadepa |
| Subha Sekhar Reddy Pereddy | speredd |
| Sai Teja Gadipally | sgadipa |

Link to DESIGN.md : [DESIGN.md](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/DESIGN.md)


Link to MILESTONE2.md : [MILESTONE2.md](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/MILESTONE2.md)


Link to MILESTONE3.md : [MILESTONE3.md](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/MILESTONE3.md)


Link to MILESTONE4.md : [MILESTONE4.md](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/MILESTONE4.md)

Link to REPORT.md : [REPORT.md](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/REPORT.md)


# Deployment

### Setup Instructions 

1) Git clone this repository, the link for this repository is [here](https://github.ncsu.edu/sgadipa/csc510-project)


2) Install and setup docker and docker-compose, the steps are mentioned [here](https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-18-04)


### Deployment script to automate the process


The following commands needs to be executed to build the dockers and deploy it into the web for usage

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
