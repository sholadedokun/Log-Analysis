#!/usr/bin/env python3
# "Database code" for the DB Forum.

import psycopg2

Dbase = "news"


def get_mostPopularArticles():
    """
      Return the most Popular Articles from the 'database',
      most viewed first.
    """
    db = psycopg2.connect(database=Dbase)
    cursor = db.cursor()
    cursor.execute(
      """
      SELECT articles.title, topArticles.count
      FROM articles
      JOIN topArticles
      ON articles.slug = topArticles.title
      ORDER BY topArticles.count DESC
      LIMIT 3
      """
    )
    topArticles = cursor.fetchall()
    db.close()
    return topArticles


def get_mostPopularAuthor():
    """
      Return the most Popular Authors from the 'database',
      most hits first.
    """
    db = psycopg2.connect(database=Dbase)
    cursor = db.cursor()
    cursor.execute(
      """
      SELECT authors.name, topAuthors.sumofhits
      FROM authors
      JOIN topAuthors
      ON authors.id=topAuthors.author
      ORDER by topAuthors.sumofhits DESC
      LIMIT 3
      """
      )
    topAuthors = cursor.fetchall()
    db.close()
    return topAuthors


def get_errorDayAbovePercentage(percentValue):
    """
      Return the most Error days from the 'database',
      most hits first.
    """
    db = psycopg2.connect(database=Dbase)
    cursor = db.cursor()
    cursor.execute(
        """
        SELECT
            to_char(day, 'FMMonth DD, YYYY'),
            CONCAT(ROUND(error_percent::DECIMAL, 2), '%%') as percent_error
        FROM (
            SELECT a.day as day,
                (
                     (b.error_count::float/a.totalHit::float)*100::float
                )
            AS error_percent
            FROM LogsPerDay as a, errorsPerDay as b
            WHERE a.day=b.day
        ) AS subQuery
        WHERE error_percent >%d
        ORDER BY error_percent DESC
        LIMIT 3;
        """
        % (percentValue)
    )
    mostErrorDay = cursor.fetchall()
    db.close()
    return mostErrorDay


def outPutResult(result, modifier):
    for data in result:
        print("%s - %s %s" % (data[0], data[1], modifier))


if __name__ == '__main__':
    print("\n\nTop Three Articules of all Times \n")
    outPutResult(get_mostPopularArticles(), 'views')
    print("\n\nTop Three Authors of all Times \n")
    outPutResult(get_mostPopularAuthor(), 'views')
    print("\n\nError Days Above 1%\n\n")
    outPutResult(get_errorDayAbovePercentage(1), 'errors')
