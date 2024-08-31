import google.generativeai as genai

# APIキーを設定
genai.configure(api_key='AIzaSyC4T29gQ90fv5zuZ-Y2jwQmeVvl-cKGc2Q')

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()

# テキスト入力からレスポンスを生成
response = chat.send_message('現時点での、日本国内で関心がある事象について、意見が割れそうな「はい」か「いいえ」で答えられる質問を一つ考えて。その際、質問は「」で囲ってほしい。')

# レスポンスをgemini.txtにリダイレクトして出力
with open('/opt/twitter-api/post-vote.txt', 'w', encoding='utf-8') as file:
    file.write(response.text)