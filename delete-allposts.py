import tweepy

# Twitter API認証情報
consumer_key = 'DN4aq16BV1KjlbOkYz8Is8hEN'
consumer_secret = 'uN3lZRdk6fBJBVSVSQ5H73qroQgOARHPGQKNgguLnV6ny2UqFG'
access_token = '1816077751809630215-jqR6ikbR84com7FMlDOz6ThnhNgg2W'
access_token_secret = 'pEWG2LSDOk9fuEp2F302MoHpL0Kl6RnCc3gMmSoKffi0c'

# Twitter APIの認証
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# APIインスタンスの作成
api = tweepy.API(auth)

# 最新の5件のツイートを取得して削除
tweets = api.user_timeline(count=5)
for tweet in tweets:
    print(f"Deleting tweet: {tweet.text}")
    api.destroy_status(tweet.id)
    print("Tweet deleted successfully")

print("Deletion of the 5 most recent tweets completed.")