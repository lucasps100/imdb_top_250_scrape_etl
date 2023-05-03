# imdb_top250

In the 'imdb_top_chart.py' script, BeautifulSoup is used to scrape IMDB's website for their 250 highest rated movies. Then, these titles are sent to themoviedb.org's API to return more information about the movies and their directors and lead actors. This data is then compiled into 3 seperate csv files for SQL databse construction.

In the 'database_construction.py' script, Pandas is used to convert the three csv files into dataframes. 'mysql.connector' is used to create three connected tables outs of these dataframes and input the data. 

Lastly, the 'imdb_clone_views.sql' script creates and presents four different views from our joined tables.

**To run this program,** create a '.env' text file in the provided repository. In this '.env' file, add your themoviedb.org API key (free to get), your mysql server root, your mysql username, and your mysql password as follows:

> API_KEY = "apikey123"

> HOST = "localhost"

> USER = "root"

> PASSWD = "yourpassword"

*Remark:* This program could be simplified in many areas. For example, the step of creating csv files could be skipped. While I may improve this program in the future, it should be noted that the main point of it is to display proficiency with a wide variety of packages.
