#!/usr/bin/env python3
# 
# A buggy web service in need of a database.

from flask import Flask, request, redirect, url_for

from logsDb import get_mostPopularAuthor, get_mostPopularArticles, get_mostErrorDay

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Log Analysis</title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
    </style>
  </head>
  <body>
    <h1>Most Popular Three Articles of All times</h1>
      <!-- Top Articules will go here -->
      <ul>
      %s
      </ul>
    <br>
    <h1>Most Popular Three Auhors  of All times</h1>
      <!-- Top Author will go here -->
      <ul>
      %s
      </ul>
    <br>
    <h1>Days with more than 1% of the errors</h1>
      <!-- Error Days will go here -->
      <ul>
      %s
      </ul>    
  </body>
</html>
'''

# HTML template for an individual comment
LISTS = '''\
    <div class=post><em class=date>%s</em> - %s Views</div>
'''


@app.route('/', methods=['GET'])
def main():
  '''Main page of the forum.'''
  articles = "".join(LISTS % (date, text) for text, date in get_mostPopularArticles())
  author = "".join(LISTS % (date, text) for text, date in get_mostPopularAuthor())
  errorDays = "".join(LISTS % (date, text) for text, date in get_mostErrorDay())
  html = HTML_WRAP % articles, author, errorDays 
  return html

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)

