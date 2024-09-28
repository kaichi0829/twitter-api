import tweepy

# 1. 認証情報を設定
api_key = 'DN4aq16BV1KjlbOkYz8Is8hEN'
api_secret_key = 'uN3lZRdk6fBJBVSVSQ5H73qroQgOARHPGQKNgguLnV6ny2UqFG'
access_token = '1816077751809630215-jqR6ikbR84com7FMlDOz6ThnhNgg2W'
access_token_secret = 'pEWG2LSDOk9fuEp2F302MoHpL0Kl6RnCc3gMmSoKffi0c'

# 2. 認証のセットアップ
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# 3. ユーザーのタイムラインからツイートを取得
username = 'X民意'  # 例: 'example_user'
tweet_count = 10  # 取得するツイートの数

try:
    tweets = api.user_timeline(screen_name=username, count=tweet_count)

    # 取得したツイートを表示
    for tweet in tweets:
        print(f"Tweet ID: {tweet.id} - Tweet Text: {tweet.text}")

    # 4. 削除するツイートのIDを指定
    # ここでは、削除したいツイートを指定
    tweet_id_to_delete = tweets[0].id  # 例として最新のツイートを削除

    # 5. ツイートを削除
    api.destroy_status(tweet_id_to_delete)
    print(f'Tweet with ID {tweet_id_to_delete} has been deleted.')

except Exception as e:
    print(f'Error: {e}')