# Logs Analysis
This is the third project of Udacity Full Stack Nanodegree. In this project
we write sql query to walk through a millions log records to generate a report
about the data.

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