import json
import requests
from requests_oauthlib import OAuth1

# APIキーとトークンの設定
API_KEY = 'DN4aq16BV1KjlbOkYz8Is8hEN'
API_SECRET_KEY = 'uN3lZRdk6fBJBVSVSQ5H73qroQgOARHPGQKNgguLnV6ny2UqFG'
ACCESS_TOKEN = '1816077751809630215-jqR6ikbR84com7FMlDOz6ThnhNgg2W'
ACCESS_TOKEN_SECRET = 'pEWG2LSDOk9fuEp2F302MoHpL0Kl6RnCc3gMmSoKffi0c'

# Twitter API認証
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# API接続
api = tweepy.API(auth)

def delete_all_tweets():
    # ツイート取得と削除
    for status in tweepy.Cursor(api.user_timeline).items():
        try:
            api.destroy_status(status.id)
            print(f"Deleted tweet: {status.id}")
        except tweepy.TweepError as e:
            print(f"Failed to delete tweet {status.id}: {e}")
        
        # API制限を回避するための待機
        time.sleep(1)

if __name__ == "__main__":
    delete_all_tweets()
    print("All tweets have been deleted.")