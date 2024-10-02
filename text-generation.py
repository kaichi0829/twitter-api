from dotenv import load_dotenv
import os
import google.generativeai as genai

# .envファイルを読み込む
load_dotenv()

# APIキーを設定
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()

# テキスト入力からレスポンスを生成
response = chat.send_message('日本人が関心を持ちそうなスポーツ、政治、芸能に関するいずれかのニュースについて、意見が割れそうな「はい」か「いいえ」で答えられる質問を1つ考えて。その際、質問は「」で囲ってほしい。')

# レスポンスをgemini.txtにリダイレクトして出力
with open('/opt/twitter-api/post-vote.txt', 'w', encoding='utf-8') as file:
    file.write(response.text)
