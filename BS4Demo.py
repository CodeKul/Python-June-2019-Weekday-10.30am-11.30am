from bs4 import BeautifulSoup # pip install beautifulsoup4
import requests # pip install requests
import sys

username = "codekul"
url = "http://www.twitter.com/" + username

response = None

try:
    response = requests.get(url)
except Exception as e:
    print(repr(e))
    sys.exit(1)

if response.status_code != 200:
    print("Non success status code returned "+str(response.status_code))
    sys.exit(1)

soup = BeautifulSoup(response.text, 'html.parser')

if soup.find("div", {"class": "errorpage-topbar"}):
    print("\n\n Error: Invalid username.")
    sys.exit(1)

tweets = soup.find_all("p", {"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})

tweetList = []
for tweet in tweets:
    text = tweet.text.encode('utf-8')
    tweetList.append(text)

for tweetText in tweetList:
    print(tweetText)