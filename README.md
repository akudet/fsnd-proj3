# Logs Analysis
This is the third project of Udacity Full Stack Nanodegree. In this project
we write sql query to walk through a millions log records to generate a report
about the data.

## How to run it
this project use vagrant you cant find it [here](https://github.com/udacity/fullstack-nanodegree-vm).
after set it up, login use `vagrant ssh` and import the data needed by `psql -d news -f newsdata.sql`
I write my own view which is not in the database. before you run the program, use `psql -d news` to
login the database, and run following sql code to import view
```sql
-- view stat of a path
-- only success view (status is 200) and using GET is counted
create view view_stat as
select path, count(*) as view_cnt
from log
where status = '200 OK' and method = 'GET'
group by path
```
after that you can run the program by `python2 main.py`

## Program Design
this project seems pretty straight forward, I write a method for each question
we are interested in. use it to fetch data from database, and write a client
to call this method and properly represent this data in console.