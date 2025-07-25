import feedparser
import pprint

url = "https://rss.itmedia.co.jp/rss/2.0/itmedia_all.xml"

f = feedparser.parse(url)

pprint.pprint(f)