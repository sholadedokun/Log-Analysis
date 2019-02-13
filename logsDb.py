# "Database code" for the DB Forum.

import psycopg2

Dbase="news"
def get_mostPopularArticles():
  """Return the most Popular Articles from the 'database', most viewed first."""
  """
  
  create view topArticles as select replace(substring(path, 10), '-', ' ') as title, count(*) from log where status ='200 OK' and path like '%/article/%' group by path order by count desc
  
  create view topAuthors as select articles.author, sum(topArticles.count) as SumOfHits  from articles join topArticles on articles.slug = topArticles.title group by articles.author
  
  create view logsperday as select date_trunc('day', time) as day ,  count(*) totalHit from log  group by day;
  create view errorPerDay as select date_trunc('day', time) as day , count(*) error_count from log where status='404 NOT FOUND'  group by day;

  """
  db=psycopg2.connect(database=Dbase)
  cursor=db.cursor()
  cursor.execute("select articles.title, topArticles.count  from articles join topArticles on articles.slug = topArticles.title order by topArticles.count desc limit 3")
  topArticles=cursor.fetchall()
  db.close()
  return topArticles

def get_mostPopularAuthor():
  """Return the most Popular Authors from the 'database', most hits first."""
  db=psycopg2.connect(database=Dbase)
  cursor=db.cursor()
  cursor.execute("select authors.name, topAuthors.sumofhits from authors join topAuthors on authors.id=topAuthors.author order by topAuthors.sumofhits desc limit 3")
  topAuthors=cursor.fetchall()
  db.close()
  return topAuthors
def get_errorDayAbovePercentage(percentValue):
  """Return the most Error days from the 'database', most hits first."""
  db=psycopg2.connect(database=Dbase)
  cursor=db.cursor()
  cursor.execute("select to_char(day, 'FMMonth DD, YYYY'), concat(round(error_percent::DECIMAL, 2), '%%') as percent_error from (select a.day as day, ((b.error_count::float/a.totalHit::float)*100::float) as error_percent from LogsPerDay as a, errorPerDay as b where a.day=b.day) as subQuery  where error_percent >%d order by error_percent desc;" %(percentValue))
  mostErrorDay=cursor.fetchall()
  db.close()
  return mostErrorDay

def outPutResult(result, modifier):
  for data in result:
    print("%s - %s %s" %(data[0], data[1], modifier))

if __name__ == '__main__':
    print("\n\nTop Three Articules of all Times \n")
    outPutResult(get_mostPopularArticles(), 'views')
    print("\n\nTop Three Authors of all Times \n")
    outPutResult(get_mostPopularAuthor(), 'views')
    print("\n\nError Days Above 1%\n\n")
    outPutResult(get_errorDayAbovePercentage(1), 'errors')