# Screencast


We have created a screencast demonstrating the implementation and deployment of the whole project. You can look at the video by clicking [here](https://youtu.be/rI17PG77Mu0).

You can also download the video from [here](https://github.ncsu.edu/sgadipa/csc510-project/blob/master/videos/Milestone5Screencast.mov).


# Problem Statement

Some important issues faced by the companies with respect to the repositories are: unable to Calculate the health and activity of repositories and failure to identify the most popular libraries used across these repositories. These problems are significant because we are unable to identify the projects where we need to invest more resources. We need to identify the health and activity of the repository to recognize which project might have better scope in the future. For example, We can obtain a lot of information by tracking the number of forks of a repository. As number of forks indicate the number of developers who are interested in working on these projects, trends regarding this will provide valuable information on what projects are popular in the market right now( for instance,  google material design repository has the highest number of forks and it is also well known that material design is trending UI framework in the market right now. Hence, trends regarding the forks will help the company identify the projects to focus on). We need to identify the response time and different time durations taken to resolve the issues so that we get infer better insights regarding the repository. Identifying the trends in libraries helps us in assessing what new libraries are being used by some teams so that other projects can be benefited from these libraries.

This analytics portal provides an approach to screen different repositories belonging to a specific company and analyzes the overall performance of individual repositories using visualization techniques. Firstly, it provides the trends in libraries/packages used for development across a period in an organization. Secondly, it calculates the health and activity of the repositories and displays vital information about it, in a user-friendly format. Health can be defined as how well the repository is maintained and the number of forks reflects about the activity. Finally, it provides information regarding the time taken to resolve issues related to the repository. 

# Features

we can access the portal using the link [here](http://ec2-3-82-251-8.compute-1.amazonaws.com/). The Landing page of the website looks like this:



   ![LoginPage](https://media.github.ncsu.edu/user/12731/files/eac92680-64ff-11e9-94c1-c4880bdae36d)

   when we click on the "Sign in to Tableau Online" button, we can traverse to the sign in page where we need to enter the credentials to log in to the portal. The login page looks like this


   ![LoginPage2](https://media.github.ncsu.edu/user/12731/files/1ef11700-6501-11e9-83b0-bf1338265450)

We have three main features:

 1)To Access Most popular libraries in an Organization:

   The user will select the organization from the list displayed in the portal. Portal will provide a packed bubble chart representing the top libraries in the organization. On selecting the library, the portal provides more information regarding this library usage in an Organization.
    
   ![capture2](https://media.github.ncsu.edu/user/12731/files/e6ead380-6502-11e9-914c-35f87102be69)
    
    
   we can see in the below picture that when we hover over the bubble, we get details regarding the library such as the Library name, Organization name which is using the library and also the count of the repositories which are using the library.
    
    
   ![Feature1](https://media.github.ncsu.edu/user/12731/files/35e43900-6502-11e9-862d-225c2a61a66e)
   
 2) Access information about health and activity of repository:
     
     On selecting one of the libraries, the second dashboard displays all the repositories which are using the Library:
 
 
    ![capture3](https://media.github.ncsu.edu/user/12731/files/c91e6e00-6504-11e9-90a9-1b0534b01924)
    
 
    The user will select the desired repository to obtain insights. The portal displays details regarding the health and activity of a repository. The portal also provides additional information regarding the activity of a repository.
    
    
    ![capture4](https://media.github.ncsu.edu/user/12731/files/75605480-6505-11e9-89de-93949d02febf)
    
    
    The above picture displays information about health and activity. The health of the repository is shown by the score beside the heart symbol. To calculate the Health we used the formula :
    
     Health score = 0.66 * Pull request effectiveness + 0.34 * Issue Effectiveness
     
     Pull request Effectiveness = Pull requests which are open / pull requests which are closed
     
     Issue effectiveness  = scaled ratio of issues closed, and issues opened = 10 * (ratio / (1+ ratio))
     
     Regarding the Scale Factor of Health: we consider the Health Scores above 700 as good health and repositories with scores between 500 and 700 are considered to be having average health and health scores below 500 are considered to have low or bad health. In the above picture, we can see that the guava repo has good health of 746.
    
    Portal generates line charts regarding the trends in forks of the selected repository. This indicates the activity of the Repository.
    
    
 3) Access information about the response time of repository:
     
     ![capture5](https://media.github.ncsu.edu/user/12731/files/89f11c80-6506-11e9-88d2-f3390987263a)
     
     In the above Picture on the left side, we can see the parameters that are used in calculating the health of the repository. 
     
     Portal converts repository specific data such as time taken to resolve various issues over a period of time into a line chart and displays the total average response time. On the right side of the above picture, we can see a line graph depicting the response time, with X-axis representing the number of issues and Y-axis representing the number of days required to resolve an issue.
     

# Reflection


Given below the list of things which we have learned while developing the project and turned out pretty well 


1) Partitioning the project into milestones and developing it using Agile methodologies. 


2) Dividing the work into tasks and tracking them using software such as Azure DevOps helped us to organize the project in a systematic manner. 


3) Knowledge transfer on different types of databases which are available to store portal-related data. After a lot of screening, we went ahead with MongoDB as it is a NoSQL database. 


4) Discussion about different types of DevOps deployment tools like Ansible,vagrant, and dockers were major learnings from this project. 


If it would have been possible that we went back to the initial stage of the project, here are a few things which we might have changed


1) Developing a UI for our portal using Web technologies like javascript, HTML and etc would have been ideal, as Tableau handled all the visualizations and interaction among dashboards we did not focus much on developing a separate front end page for our portal.


2) We could have used multiple authentication Github tokens to extract a huge amount of data parallelly using REST API's which would have made our job easier and faster. 

3) Since we used MVC Architecture for the application, the division of labor could have been done according to the strengths of each team member. For example, the team member who has expertise in user interface could have worked on the views. This way the team could have worked more efficiently



# Limitations 


This section includes the limitations involved in the project and the scope for future work 


1) The user should manually refresh the web page of the portal to accommodate live data changes. 


2) If any repository data which is been populated in the database, and after a while if that repository has been removed from Github server, there is no module to delete that data in our MongoDB instance. Once populated the data remains persistent.


3) The mathematical formula used to calculate the health of a repository may not be accurate for all repositories, as every repository may not contain pull and push requests. 


4) Any user who wants to interact with the portal should log in into Tableau Online using master user login credentials only.


## Scope for future work

1) The data in the portal is limited to only two organizations, but this can be scalable to accommodate all the organization data given proper resources and time.


2) Presently the portal shows the popular libraries of only a small set of popular programming languages used in that particular organization but this can be scaled to accommodate libraries of all types of programming languages. 


3) The project can be extended in a way that when the user provides the Github link/web-address of a particular repository or organization, the portal can parse the link and generate the visualizations only for that desired repository.










