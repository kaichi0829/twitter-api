import json
import requests
from requests_oauthlib import OAuth1

# APIキーとトークンの設定
API_KEY = 'DN4aq16BV1KjlbOkYz8Is8hEN'
API_SECRET_KEY = 'uN3lZRdk6fBJBVSVSQ5H73qroQgOARHPGQKNgguLnV6ny2UqFG'
ACCESS_TOKEN = '1816077751809630215-jqR6ikbR84com7FMlDOz6ThnhNgg2W'
ACCESS_TOKEN_SECRET = 'pEWG2LSDOk9fuEp2F302MoHpL0Kl6RnCc3gMmSoKffi0c'

# OAuth認証
auth = OAuth1(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# アーカイブデータからツイートIDを抽出する関数
def extract_tweet_ids_from_archive(archive_file_path):
    tweet_ids = []
    with open(archive_file_path, 'r', encoding='utf-8') as file:
        data = file.read()
        data = data.replace('window.YTD.tweets.part0 = ', '')
        tweets_data = json.loads(data)

        for tweet in tweets_data:
            tweet_id = tweet['tweet']['id_str']
            tweet_ids.append(tweet_id)
    return tweet_ids

# ツイートを削除する関数
def delete_tweets(tweet_ids):
    url_delete_tweet = "https://api.twitter.com/1.1/statuses/destroy/"
    for tweet_id in tweet_ids:
        del_response = requests.post(url_delete_tweet + f"{tweet_id}.json", auth=auth)
        if del_response.status_code == 200:
            print(f"Deleted tweet ID: {tweet_id}")
        else:
            print(f"Failed to delete tweet ID: {tweet_id}, Status Code: {del_response.status_code}")

# 実行
archive_file_path = 'tweets-sample.js'  # アーカイブファイルのパスを指定
tweet_ids = extract_tweet_ids_from_archive(archive_file_path)
delete_tweets(tweet_ids)