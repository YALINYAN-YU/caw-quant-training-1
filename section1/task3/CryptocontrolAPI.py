import json
import os

from crypto_news_api import CryptoControlAPI

# English (en default)
# Chinese/Mandarin (cn)
# German (de)
# Italian (it)
# Japanese (jp)
# Korean (ko)
# Portuguese (po)
# Russian (ru)
# Spanish (es)

DATA_DIR = './CryptocontrolData'
if not os.path.isdir(DATA_DIR):
    print('Create data folder to store')
    os.mkdir(DATA_DIR)

def save_json(data, filename, save):
    if save:
        filepath = os.path.join(DATA_DIR, filename)
        with open(filepath, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            print ('Data Saved')

with open('../../../api-keys/cryptocontrol-API-Key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

# Connect to the CryptoControl API
api = CryptoControlAPI(key)

# Connect to a self-hosted proxy server (to improve performance) that points to cryptocontrol.io
proxyApi = CryptoControlAPI(key, "http://cryptocontrol_proxy/api/v1/public")


# Get top news
top_news = api.getTopNews(language='cn')
top_news_filename = f'top-news-cn.json'
save_json(top_news, top_news_filename, save=True)

# get latest english news
latest_news = api.getLatestNews('en')
latest_news_filename = f'latest-news-en.json'
save_json(latest_news, latest_news_filename, save=True)

# get top bitcoin news
top_btc_news = api.getTopNewsByCoin("bitcoin")
top_btc_news_filename = f'top-btc-news.json'
save_json(top_btc_news, top_btc_news_filename, save=True)

# get top EOS tweets
eos_tweets = api.getTopTweetsByCoin("eos")
eos_tweets_filename = f'eos-tweets.json'
save_json(eos_tweets, eos_tweets_filename, save=True)

# get top Ripple reddit posts
reddit = api.getLatestRedditPostsByCoin("ripple")
reddit_filename = f'ripple-reddit.json'
save_json(reddit, reddit_filename, save=True)

# get reddit/tweets/articles in a single combined feed for NEO
neo_feed = api.getTopFeedByCoin("neo")
neo_feed_filename = 'neo-feed.json'
save_json(neo_feed, neo_feed_filename, save=True)

# get latest reddit/tweets/articles (seperated) for Litecoin
ltc_latest_feed = api.getLatestItemsByCoin("litecoin")
ltc_file = 'ltc-latest-feed.json'
save_json(ltc_latest_feed, ltc_file, save=True)

# get details (subreddits, twitter handles, description, links) for ethereum
eth_detial = api.getCoinDetails("ethereum")
eth_detial_file = 'eth-detial.json'
save_json(eth_detial, eth_detial_file, save=True)



# Enable the sentiment datapoints
# api.enableSentiment()