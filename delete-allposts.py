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

# 3. ユーザーIDを取得（usernameから）
username = 'X9446833383164'  # 削除したいツイートのユーザー名
user = client.get_user(username=username)
user_id = user.data.id

# 4. ユーザーのツイートを取得
tweet_count = 10  # 取得するツイート数
tweets = client.get_users_tweets(id=user_id, max_results=tweet_count)

# 5. 取得したツイートの表示
for tweet in tweets.data:
    print(f"Tweet ID: {tweet.id} - Tweet Text: {tweet.text}")

# 6. 削除するツイートのIDを指定して削除
tweet_id_to_delete = tweets.data[0].id  # 例として最新ツイートを削除
client.delete_tweet(id=tweet_id_to_delete)
print(f'Tweet with ID {tweet_id_to_delete} has been deleted.')
