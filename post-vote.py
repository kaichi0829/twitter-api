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

with open('/opt/twitter-api/post-vote.txt', 'r', encoding='utf-8') as f:
    content = f.read()  # ファイル全体を文字列として読み込む

print(content)  # 読み込んだ内容を出力

# 投票内容
poll_question = "あなたはどのプログラミング言語が好きですか？"
options = ["はい", "いいえ"]
duration = 24  # 投票の有効期限（時間）

# 投票を投稿
response = client.create_tweet(
    text=content,
    poll_options=options,
    poll_duration_minutes=duration * 60  # 分単位で指定
)

print("投票が投稿されました:", response.data['id'])
