create view topArticles
as
    select substring(path, 10) as title, count(*)
    from log
    where status ='200 OK' and path like '%/article/%'
    group by path
    order by count desc;

create view topAuthors
as
    select articles.author, sum(topArticles.count) as SumOfHits
    from articles join topArticles on articles.slug = topArticles.title
    group by articles.author;

create view logsperday
as
    select date_trunc('day', time) as day , count(*) totalHit
    from log
    group by day;

create view errorsPerDay
as
    select date_trunc('day', time) as day , count(*) error_count
    from log
    where status='404 NOT FOUND'
    group by day;