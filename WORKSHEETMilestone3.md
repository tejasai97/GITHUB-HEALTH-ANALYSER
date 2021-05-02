

## Week 1

| Deliverable | Status | Tasks |
| :---: | :---: | :---: |
| **Use case 1 :** **Access statistics regarding popular libraries** [#29](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/29) |
| SubFlow : Retrieving library data(To write a python code to get different libraries of languages like java, javascript,python in a repository)  | Complete | [#30](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/30), [LibraryExtractor](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/server/LibraryExtractor.py) |
| SubFlow : Implement and update database driver module(Write code to insert the data extracted from REST API's into DB using pymongo into Company and Libraries collections) | Complete | [#31](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/31), [DatabaseDriver](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/server/DatabaseDriver.py) |
| SubFlow : Create Visualizations(To generate visualization of most popular libraries used in an organization by querying the database) | Complete | [#32](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/32) |
| SubFlow : Initial Integration with UC1 data(An initial integration of all the components of the project to generate a working system and accomodate UC1 data)  | Incomplete(Moved to Iteration2) |  [#33](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/33) |


## Week 2


| Deliverable | Status | Tasks |
| :---: | :---: | :---: |
| **Use case 1 :** **Access statistics regarding popular libraries** [#29](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/29) |
| SubFlow : Initial Integration with UC1 data (Integrating all the components of the project to generate a working system and accomodate UC1 data) | Complete |  [#33](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/33) |
| **Use case 2 :** **Access information about health and activity of repository** [#34](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/34) |
| SubFlow : Retrieve Health Metrics to calculate score(Writing python code to retrieve data for calculating health of an repository using REST API's like pull/push requests etc) | Complete | [#35](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/35), [Health and Activity](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/server/RepositoryData.py) |
| SubFlow : Updating the Database Driver module(Write a python code to push metrics relating calculation of health of an repository into Repository collection)| Complete |  [#36](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/36), [DatabaseDriver](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/server/DatabaseDriver.py) |
| SubFlow : Creation of Visualizations to analyze health of a repository (Querying the database and creation of visualization in Tableau)  | Complete | [#37](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/37), [Visualization](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/visualization/finalDashboards.twb) |



## Week 3


| Deliverable | Status | Tasks |
| :---: | :---: | :---: |
| **Use case 3 :** **Access information about the response time of repository** [#38](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/38) |
| SubFlow : Retrieval of Repository related data using REST API's(Writing python code to obtain repository related data like forks,commits using REST API's) | Complete | [#39](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/39), [Response Time](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/server/RepositoryData.py) |
| SubFlow : Updating database driver module(Write a python code to push metrics relating repository into Repository collection) | Complete |  [#40](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/40) |
| SubFlow : System end to end integration(Final Integration of all components to create a working portal)   | Complete | [#41](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/41), [Integration](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/backend/server/main.py) |
| SubFlow : Portal navigation and creation of screencast(Integration of all the dashboards and adding actions in Tableau to perform user navigation and creation of screencast which shows the working of portal)  | Complete | [#41](https://dev.azure.com/sgadipa/CSC%20510%20-%20Analytics%20Portal/_workitems/edit/42), [Screencast](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/videos/2019-03-28%20at%2023-11-48.mp4), [Final Visualization](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/visualization/finalDashboards.twb) |


