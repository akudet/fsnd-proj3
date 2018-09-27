# Logs Analysis
This is the third project of Udacity Full Stack Nanodegree.
In this project we will write a internal reporting tool
that will use information from the database to discover
what kind of articles the readers like.

The program will run from the command line, It will connect
to the database, use SQL queries to analyze the log data, 
and print out the answers to some questions.

The database contains newspaper articles as well as
web server log for the site.It include three tables.

*authors* contains information about the authors of articles
* *name* name of the author
* *bio* biography of the author

*articles* contains information about the article themselves
* *title* tile of the article
* *slug* the slug of the article, the article's path is 
  construct by'/article/' + slug
* *author* id of the author write this article

*log* contains a record each time a reader access the site
* *path* the path that a reader try to access
* *method* HTTP request method
* *status* the HTTP status code that the news site sent to user
* *time* the timestamp when user access the page


Questions that will be report by this program
> 1.What are the most popular three articles of all time?
Which articles have been accessed the most?  Present this information
as a sorted list with the most popular article at the top.

> 2.Who are the most popular article authors of all time?
That is, when you sum up all of the articles each author has written,
which authors get the most page views? Present this as a sorted list
with the most popular author at the top.

> 3.On which days did more than 1% of requests lead to errors?
The log table includes a column status that indicates the HTTP status code
that the news site sent to the user's browser.

## How to run it
What you need
* Vagrant
* VirtualBox
* Git

Assume you have setup vagrant and virtualbox properly.

You can import and login the vm used in this project by the following cmd
```
git clone https://github.com/udacity/fullstack-nanodegree-vm fsnd-vm
cd fsnd-vm/vagrant

vagrant up
vagrant ssh
```

In the vm use the following cmd to download the database file and import it
```
wget https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
unzip newsdata.zip
psql -d news -f newsdata.sql
```

Download this project and import views needed
```
git clone https://github.com/akudet/fsnd-proj3.git
cd fsnd-proj3
psql -d news -f create_view.sql
```

Finally you can run the program by 
```
python2 main.py
```

## Program Design
this project seems pretty straight forward, I write a method for each question
we are interested in. use it to fetch data from database, and write a client
to call this method and properly represent this data in console.