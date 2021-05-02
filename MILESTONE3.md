# Milestone 3: Services

In this milestone, we will start implementing the project with real data, rather than mock data. Our initial focus would be on writing python scripts to mine GitHub repository related data using REST API's. Then the next task would be pushing this data into MongoDB collections. While updating the data into the database, an Intermediate server transforms the data according to our defined schema. Then we query the database and obtain data into Tableau to create an end to end working portal.


In Milestone2 we have created a system which works on mock data, for this milestone we have extracted the real-time data using REST API's and created a portal for analyzing a repository. One additional factor which was added was the implementation of an intermediate server which calculates health of a repository and then updates them into MongoDB collections. 


We have performed the following tasks in this Milestone


1) Writing python scripts to get data from Github REST API's


2) Storing them in JSON format and sending them to an intermediate server


3) Processing of data in the server and conversion of data into the format defined in the schema


4) Python script to send the data processed into MongoDB instance which is hosted on Amazon EC2


5) Integrating MongoDB into Tableau Desktop


6) Applying actions and filters to produce visualizations for user interaction.


# Services Implementation 


## System Design


Here is the basic sketch of our data flow across different components in the system, nothing much has been modified from the previous milestone
![image](https://media.github.ncsu.edu/user/10117/files/6c2b5a80-41d9-11e9-8859-088dd1d1f86f)


### RepositoryData


This module uses GitHub REST API's to get the data related to the repository like forks, commits and other metrics. It also contains the code to update Repository collection in the database. 


The code for implementation of this module can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/server/RepositoryData.py)


### LibraryExtractor


This module contains code to extract libraries used in repositories for different programming languages like Python, Java, and JavaScript. And storage of data into an intermediate server. 


The code for implementation of this module can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/server/LibraryExtractor.py)



### DatabaseDriver


This module contains code to push the data from Intermediate server into MongoDB collection using the pymongo library. 


The code for implementation of this module can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/server/DatabaseDriver.py)


### Tableau


This module creates visualization by connecting to an external database which is hosted on Amazon EC2 instance, before moving data to Tableau the [MongoDB Connector for BI](https://docs.mongodb.com/bi-connector/master/) converts No-SQL data in our database instance to SQL tables. 


Tableau processes the data according to the schema defined here [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/database/schema.drdl)


A pictorial representation of joins across various tables across can be found below ![image](https://media.github.ncsu.edu/user/12731/files/33e60b00-3f92-11e9-88dd-fea54fdb65ec)


The final Dashboard can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/visualization/finalDashboards.twb)

### Real time data


The data extracted and used for implementing this project can be found in this [directory](https://github.ncsu.edu/sgadipa/csc510-project/tree/master/backend/database)

# UseCases


### Use Case 1 Implementation: Access statistics regarding popular libraries


#### Description: 
When the user clicks on a particular organization a visualization(bubble chart) which contains different libraries used across the selected organization will be displayed. The size of the bubble has a major significance, larger the size more the usage and vice versa. 


#### Implementation


The portal loads the data containing different organizations for the user to select from the Organization collection in the database. When a user clicks on any of the organization, the portal triggers another dashboard which contains a bubble chart of various libraries used, this data is populated from the Libraries collection in the database. The bubble size of the library displayed will be according to the usage count in that organization. The libraries can be further drilled down to infer more data. 

![capture3](https://media.github.ncsu.edu/user/10117/files/6f17e900-5275-11e9-8dbd-7285bc67e01d)


#### CodeBase


The code to implement this use case can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/server/LibraryExtractor.py)


#### Data utilized for implementation


The library data for different organizations extracted using REST API's can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/database/mockdata/libraries.json)


### Use Case 2 Implementation: Access information about health and activity of repository


#### Description
When a user clicks on any organization or a library it displays the list of repositories present in that organization which are using the selected library. Then the user can click any one of the repositories and get the health score and activity across a period of time. 


#### Implementation
The portal loads the lists of repositories for that organization by filtering on the attribute, OrgName present in Repository collection. When further drilled down on the repository the portal triggers another dashboard which shows the health score by populating the value from health attribute in the Repository collection. The health of the repository is calculated as follows in the intermediate server


`````
Health score = 0.66 * Pull request effectiveness + 0.34 * Issue Effectiveness
Pull request Effectiveness = Pull requests which are open / pull requests which are closed
Issue effectiveness  = scaled ratio of issues closed, and issues opened = 10 * (ratio / (1+ ratio))
`````


The portal also loads the data regarding the metrics used in the calculation of health score in the form of bar graphs which are obtained from Repository collection. 

![capture6](https://media.github.ncsu.edu/user/10117/files/aab2b300-5275-11e9-9dc7-cb1a1eb9eb85)

The activity of an organization can be found by analyzing the trends in the forks made in the repository, the fork dates of the repository is obtained from the Repository collection and this time series data is converted into a line graph by the portal to visualize and infer about the activity of the repository.


![capture4](https://media.github.ncsu.edu/user/10117/files/8951c700-5275-11e9-8113-3e4a04f22e44)


#### CodeBase


The code to implement this use case can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/server/RepositoryData.py)


#### Data utilized for implementation


The library data for different organizations extracted using REST API's can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/database/mockdata/repository.json)


### Use Case 3 Implementation: Access information about the response time of repository


#### Description
When the user clicks on the repository the portal displays the time taken to respond to an issue created and its trends across a period of time.


#### Implementation
The backend server retrieves issue data using the GitHub REST API. Since the data retrieved is in json format, it is converted into date object using the dateutil library in python.  Response time is calculated by subtracting the closing date from the opened date of the issue and converted into days. This data is stored in MongoDB using database driver. 

The response time for the repository is obtained from the Repository collection and this data is converted into a line graph by the portal to visualize and infer about the average response time of the repository.

![capture5](https://media.github.ncsu.edu/user/10117/files/8951c700-5275-11e9-8241-56346c42a35e)

#### CodeBase


The code to implement this use case can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/server/RepositoryData.py)


#### Data utilized for implementation


The library data for different organizations extracted using REST API's can be found [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/database/mockdata/repository.json)

# Task Tracking

We have created a worksheet which provides details regarding the work distribution among the teammates for each iteration. It also provides links to the tasks in Azure DevOps.

[WORKSHEET Milestone3](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/WORKSHEETMilestone3.md)

# Screencast

We have created a screencast explaining the database schema, data ingestion and the user interaction with the portal. you can look at the video by clicking [here](https://youtu.be/6GM_UdO3ooA).

You can also download the video from [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/videos/2019-03-28%20at%2023-11-48.mp4).




