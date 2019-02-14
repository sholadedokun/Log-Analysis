# Introduction
This code generate an analysis of the following activities generated on a web platform:
* The most read Articles
* The most popular Author
* The Day(s) with more that 1% of errors logged.
## Project Name : Website Log Analysis
This project sets up a PostgreSQL database for a news website. The provided Python script logsDb.py uses the psycopg2 library to query the database and produce a report that answers these questions
1. Top Three most Read Articles.
2. Top Three most popular Authors, based on the commulative amount many of times all Author's articles has been read.
3. The Day(s) with more than 1% of errors logged, mostly due to user mistyping/directed to a wrong article URL.

# Database
The database consist of three tables(log, author and articles).Here are brief description of the tables and their columns:
1. Log: This table contains the record of all http request to all the articles, it contains the following columns:
    * Path - The url path, that is requested from the web client.
    * IP - The IP address the web client is connecting with.
    * Method - The HTTP request method  mostly either 'GET' OR 'POST'.
    * Status - The Status code the web-server sends back to the web client.
    * Time - The timestamp when this entry was logged to the database.
    * Id - Primary key to uniquely Identify this entry
2. Author: This table contains the Bio of each Author that has contributed to the news website, it contains the following columns:
    * Name - Full name of the Author.
    * Bio - Brief details about the Author.
    * Id - Primary key to uniquely Identify this entry.
3. Articles: This table contains all the details about each article currently in the database, it contains the following columns:
    * Author - The Id of the Author of the article, this will be a Foreign Key referenced from the author table.
    * Title - The Title of the article.
    * Slug - A unique string that eventually make up the critical part of the article's URL path.
    * Lead - A first few characters of the articles, mostly displayed on a list of articles.
    * Body - The entire body of the article.
    * Time - The timestamp when this entry was logged to the database.
     * Id - Primary key to uniquely Identify this entry.


### Download the database
1. Please click [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) to download the sample database used for this project.
2. Unzip the database and add it to project file.


 
# Installation

## Requirement
### Set up your enviroment
Here are few requirement to run this applicaton in a controlled Virtual enviroment. Please download and install the following application using the link provided.
1. Please click [here]('https://www.vagrantup.com/downloads.html') to choose and download the applicable Vagrant file for your OS. Then install the application.
2. Please click [here]('https://www.virtualbox.org/wiki/Downloads') to choose and download the applicable Virtual Box file for your OS.  Then install the application.
3. Create a new Folder (give it any name) for your new virtual enviroment. 
4. Download/Copy and add this [Vagrant File](https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile) to your virtual enviroment folder. 
5. Move the Project folder to the virtual enviroment folder. It should now contain a vagrant file and the project folder.
6. `CD` into the virtual enviroment folder created and run `vagrant up`, this might take some time to finish running, especially on the first run.
7. Run `vagrant ssh`, then `cd /vagrant` to completly initialize the virtual enviroment and access the local files.
8. Run `ls` to view all the content, notice the vagrant file and project folder are listed.
8. To exit the virtual enviroment run `exit`.
9. To restart the virtual enviroment repeat step 6 and 7 above.

# Import the Database and create the database Views;
1. Start-up the virtual enviroment and `cd` into the project folder - step 6 and 7 from "Set up your enviroment" above.
2. To load the data and create the **news** database, use the command `psql -d news -f newsdata.sql`.
3. This project uses several postgre views, please run `psql -d news -f create_views.sql` the following on your postgre database.

# Run the code.
To Run the program and generate output on the command line, please run `Python logsDB.py`
