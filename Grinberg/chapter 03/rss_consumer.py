import feedparser
from flask import Flask


app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}


@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    content = ""
    for x in range(0, 9):
        content += """
        <b>{0}</b><br/>
             <i>{1}</i><br/>
             <p>{2}</p><br/>""".format(feed['entries'][x].get("title"),
                                       feed['entries'][x].get("published"),
                                       feed['entries'][x].get("summary"))

    return """<html>
        <body>
            <h1> Headlines </h1>""" + content + """</body>
    </html>"""


if __name__ == "__main__":
    app.run(port=5000, debug=True)
