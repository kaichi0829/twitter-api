from dotenv import load_dotenv
import os
import tweepy
import requests
from datetime import datetime

# .envファイルを読み込む
load_dotenv()

# Consumer Keys
ck = os.getenv('TWITTER_API_KEY') #API KEYが入ります
cs = os.getenv('TWITTER_SECRET_API_KEY') #API KEY SECRETが入ります

# Authentication Tokens
bt = os.getenv('TWITTER_BEARER_TOKEN') #Bearer Tokenが入ります
at = os.getenv('TWITTER_ACCESS_TOKEN') #ACCESS TOKENが入ります
ats = os.getenv('TWITTER_SECRET_ACCESS_TOKEN') #ACCESS TOKEN SECRETが入ります

# 認証
client = tweepy.Client(
    bearer_token=bt,
    consumer_key=ck, consumer_secret=cs,
    access_token=at, access_token_secret=ats
)

with open('/opt/twitter-api/post-vote.txt', 'r', encoding='utf-8') as f:
    content = f.read()  # ファイル全体を文字列として読み込む

print(content)  # 読み込んだ内容を出力

# 投票内容
options = ["はい", "いいえ"]
duration = 24  # 投票の有効期限（時間）

# 投票を投稿
response = client.create_tweet(
    text=content,
    poll_options=options,
    poll_duration_minutes=duration * 60  # 分単位で指定
)

print("投票が投稿されました:", response.data['id'])
