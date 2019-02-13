# Introduction
This code generate an analysis of the following activities generated on a web platform:
* The most read Articles
* The most popular Author
* The Day(s) with more that 1% of errors logged.

## Installation
To run this application, please follow the instruction provided in [here](https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/bc938915-0f7e-4550-a48f-82241ab649e3/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91) to setup your machine and download the database source file.
### Create Views
This proect uses several postgre views, please run the following on your postgre database
```
create view topArticles as select substring(path, 10) as title, count(*) from log where status ='200 OK' and path like '%/article/%' group by path order by count desc;

create view topAuthors as select articles.author, sum(topArticles.count) as SumOfHits  from articles join topArticles on articles.slug = topArticles.title group by articles.author;

create view logsperday as select date_trunc('day', time) as day ,  count(*) totalHit from log  group by day;

create view errorsPerDay as select date_trunc('day', time) as day , count(*) error_count from log where status='404 NOT FOUND'  group by day;
```
## Run the code.
`python logsDB.py`
