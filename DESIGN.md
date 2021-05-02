# Problem statement:

Some important issues faced by the companies with respect to the repositories are: Calculating the health, the activity of repositories and to identify the most popular libraries used across these repositories. With this analytics portal, we are providing an approach to screen different repositories belonging to a specific company and analyze the overall performance of individual repositories using visualization techniques. Firstly, it calculates the health of the repositories and displays vital information about it, in an user friendly format. Health can be defined as how well the repository is maintained and it reflects about the activity. Secondly, it provides information regarding the time taken to resolve issues related to the repository. Finally, it provides an approach to find the trends in libraries/packages used for development across a period in an organization.

These problems are significant because we are unable to identify the projects where we need to invest more resources. We need to identify the health and activity of the repository to recognize which project might have better scope in the future. For example, We can obtain a lot of information by tracking the number of forks of a repository. As number of forks indicate the number of developers who are interested in working on these projects, trends regarding this will provide valuable information on what projects are popular in the market right now( for instance,  google material design repository has the highest number of forks and it is also well known that material design is trending UI framework in the market right now. Hence, trends regarding the forks will help the company identify the projects to focus on). We need to identify the response time and different time durations taken to resolve the issues so that we get infer better insights regarding the repository. Identifying the trends in libraries helps us in assessing what new libraries are being used by some teams so that other projects can be benefited from these libraries.

# Solution Description:

For this application, we are working on open source repositories of Google, Facebook, and Microsoft. Firstly, the analytics portal consists of two dashboards. The first dashboard is an interactive one which displays visualizations regarding most popular libraries being used. Upon clicking on these libraries, information regarding which repositories have used it will be displayed. The second dashboard provides more fine-grained information about individual repositories such as health, activity and response time. The health of repositories can be calculated using the parameters such as the number of open pull requests, closed pull request, open issues, and closed issues. The health score can be calculated in the following method:
`````
Total scores = 0.66 * Pull request effectiveness + 0.34 * Issue Effectiveness
Pull request Effectiveness = Pull requests which are open / pull requests which are closed
Issue effectiveness  = scaled ratio of issues closed, and issues opened = 10 * (ratio / (1+ ratio))
`````
Pull requests are given more importance compared to issues since issues may not be an accurate parameter to identify the health. Additionally, we are going to use trends in forks to identify the activity as mentioned in the problem statement. GitHub does not provide insights regarding these information, the activity feature in our portal will help us acquire additional information which is not available in GitHub.

The data related to various repositories of an organization required for calculation of health and activity is retrieved using GitHub REST APIs. The libraries used for various projects can be extracted in the following ways. If the repository is java based, we can get this data either from pom.xml or build.gradle files. If the repository is python based, we can get this information from the requirements.txt file. All this data is stored in a database (Type of the database is yet to be decided). This database is connected to tableau to generate various visualizations. These visualizations can be exported into various formats such as images and pdf.

# Use Cases:

## Use Case: Access statistics regarding popular libraries

### 1 Preconditions

The user must know the organization in which he wants to identify the most popular libraries.

### 2 Main Flow

The user will select the organization [S1]. Portal will provide several visualizations about the top libraries in the organization [S2]. On selecting the library, we get detailed information about it [S3].

### 3 Subflows

[S1] Data related to the organization will be retrieved using a query.

[S2] The portal queries data regarding the libraries and converts this data into various visual formats to analyze.

[S3] The portal queries what repositories have used the selected libraries and shows visualization regarding this data.

![usecase1](https://media.github.ncsu.edu/user/10117/files/09332180-307a-11e9-9033-546c381ddfc0)

## Use Case: Access information about health and activity of repository

# 1 Preconditions

The user must know the organization to which the desired repository belongs to.

## 2 Main Flow

The user will select the organization [S1]. Portal will provide a list of all the repositories for that organization and user can select any one of them [S2]. The portal displays details regarding the health and activity of a repository [S3].

### 3 Subflows

[S1] Data related to the organization will be retrieved using a query.

[S2] The portal queries repository specific data based on the user’s selection.

[S3] Portal converts repository specific data into various visual formats.

![usecase2](https://media.github.ncsu.edu/user/10117/files/2cf66780-307a-11e9-973b-0af735f01b8e)

## Use Case: Access information about the response time of repository

### 1 Preconditions

The user must know the organization to which the desired repository belongs to.

### 2 Main Flow

The user will select the organization [S1]. Portal will provide a list of all the repositories for that organization and user can select any one of them [S2]. The portal displays different visualizations of the response time of the selected repository [S3].

### 3 Subflows

[S1] Data related to the organization will be retrieved using a query.

[S2] The portal queries repository specific data based on the user’s selection.

[S3] Portal converts repository specific data into various formats such as time taken to resolve various issues over a period of time and the total average response time.

![usecase3](https://media.github.ncsu.edu/user/10117/files/47304580-307a-11e9-906d-a54d73c597c3)

# Design Sketches

## Sequence Diagram

![sequencediag](https://media.github.ncsu.edu/user/10117/files/a2face80-307a-11e9-958d-17c034807b08)

The above diagram shows object interactions arranged in time sequence. First, the user accesses the portal which displays a list of organizations. Upon selecting a company, details such as the list of repositories and most popular libraries are displayed. If the user selects a library, a list of repositories using it is displayed. If the user selects a repository, details regarding it such as health and activity are displayed.

## Wireframe

A wireframe provides a visual guide that represents the skeletal framework of the application.

### First Dashboard Wireframe

![wireframe-dashboard1](https://media.github.ncsu.edu/user/10117/files/b490a600-307b-11e9-896c-b2e7883f38ce)

As shown in the figure, the left division shows the companies available and the right division shows the most popular libraries for the selected company. The most popular libraries are represented using a packed bubble chart, where the radius of each bubble is proportion the number of repositories using it.

### Second Dashboard Wireframe

![wireframe-dashboard2](https://media.github.ncsu.edu/user/10117/files/734cc600-307c-11e9-8261-213c0d6e8cc0)

As shown in the figure, the screen is divided into four sections. The top left section shows details regarding the health of the repository and other details of parameters used to calculate health. The bottom left section shows details of the repository such as forks, commits, and issues. The top right section displays trends of forks over a period of time. The bottom right section displays details such as trends in response time and average response time.

### Storyboard

A storyboard is a graphic organizer that provides the viewer with a high-level view of a project. a storyboard can help developers quickly get a sense of what work still needs to be completed.

<img width="862" alt="capture1" src="https://media.github.ncsu.edu/user/10117/files/c3795780-307f-11e9-9e6e-8378992450d6">
<img width="864" alt="capture2" src="https://media.github.ncsu.edu/user/10117/files/c96f3880-307f-11e9-9fc4-063c705d674b">

# Architecture Design

![architecturediagram](https://media.github.ncsu.edu/user/10117/files/c7e55500-30ff-11e9-83dd-8e9e54497325)

## Description

For this portal, we are using pipe filter architecture. It consists of a number of components (filters) that transform or filter data, before passing it on via connectors (pipes) to other components. All these components work asynchronously at the same time.

As shown in the above figure, the data is retrieved using GitHub REST APIs and processed by an intermediate server. This processed data is stored in a database. The data from this database is used by dashboards to provide analytics on popular libraries, the health of repositories and trends in the activity of the repositories.

### Architectural Components

**GitHub REST APIs** : GitHub provides a collection of Application programming interfaces which can be used to access several details of repositories such as push, commit, fork and tag details. This details can be retrieved in JSON format, which is used for further processing.

**Intermediate Server** : This Server takes the data about repositories using REST APIs and processes it calculate several details such as the health of the repositories, most popular libraries, and the trends in response time.

**Database** : The Intermediate server writes details regarding the processed data in the database which is used by the analytics portal to generate visualizations.

**Dashboards** : The Dashboards retrieve data from the database and generate visualizations such as most popular libraries, Trends in forks for the selected repository, trends in response time and the health of repository. 

## Constraints

1. The portal cannot update it's database more than once per day.
2. The portal accesses only open source repositories.
3. For analyzing the trends in libraries only java and python repositories are considered.

## Design Pattern

The Analytics portal follows the facade pattern. This pattern provides a facade interface that serves as a front-facing interface masking more complex underlying or structural code.

![design pattern](https://media.github.ncsu.edu/user/13118/files/00198180-315a-11e9-9ec0-19c7caad6740)

When the user interacts with the portal interface, the following subsystems are invoked:

**Repository Trends**: This subsystem gets invoked only when the user tries to access repository specific data. It queries data regarding the trends in the forks of a repository and transforms it into a visual format. 

**Library Trends**: This subsystem gets invoked only when the user tries to access data specific to the libraries used across projects. It queries data regarding the trends in the forks of a repository and transforms it into a visual format. 

**Repository Health**: This subsystem gets invoked only when the user tries to access repository specific data. It queries data regarding the health of a repository and transforms it into a visual format. 

**Database**: This subsystem provides data which is used by other subsystems such as Repository Trends, Library Trends, and Repository which transform this data into several other formats.

**Intermediate Server**: This subsystem retrieves data about different repositories across a company and processes complex transformations of the raw data extracted from REST APIs.  

**GitHub  REST APIs**: This subsystem takes a query from the user and provides various details regarding repositories based on the query in JSON format. 
