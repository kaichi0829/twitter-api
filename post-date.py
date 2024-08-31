import tweepy
import requests
from datetime import datetime

# Consumer Keys
ck = 'DN4aq16BV1KjlbOkYz8Is8hEN' #API KEYが入ります
cs = 'uN3lZRdk6fBJBVSVSQ5H73qroQgOARHPGQKNgguLnV6ny2UqFG' #API KEY SECRETが入ります

# Authentication Tokens
bt = 'AAAAAAAAAAAAAAAAAAAAABEKvAEAAAAA0g%2FWGtj8u%2B%2BTnIfPeHUR0O54ZLM%3DVqqdyoYilbieG2IhcPjOy4uA62cGJUhnxRQcL7dHdhPu7Fo0yR' #Bearer Tokenが入ります
at = '1816077751809630215-jqR6ikbR84com7FMlDOz6ThnhNgg2W' #ACCESS TOKENが入ります
ats = 'pEWG2LSDOk9fuEp2F302MoHpL0Kl6RnCc3gMmSoKffi0c' #ACCESS TOKEN SECRETが入ります

# 認証
client = tweepy.Client(
    bearer_token=bt,
    consumer_key=ck, consumer_secret=cs,
    access_token=at, access_token_secret=ats
)

# 今日の日付を取得
today = datetime.now()
tweet_text = f"今は {today} です！"
client.create_tweet(text=tweet_text)
