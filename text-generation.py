import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

gemini_pro = genai.GenerativeModel("gemini-2.5-flash")

#prompt = "日本人が関心を持ちそうな直近１週間のニュースについて、意見が割れそうな「はい」か「いいえ」で答えられる質問を1つ考えて。その際、質問は「」で囲ってほしい。質問のテーマは {政治, 経済, スポーツ, エンタメ} の中からランダムに選んで。"

#prompt = "あなたは知識豊富で親切なAIアシスタントです。ユーザーの質問に対し、以下の制約を厳守して回答を生成してください。必ずGoogle Search Toolを有効にし、最新のニュース情報を参照して回答の基盤としてください。質問のテーマは{政治, 経済, スポーツ, エンタメ}の中からランダムに一つ選びます。選ばれたテーマの直近1週間の日本人が関心を持つニュースから、国民の意見が二分しそうな話題を選定します。最終的な出力は、選定した話題に基づき、意見が割れる「はい」か「いいえ」で答えられる質問を一つだけ考案し、それを**「」**で囲って提示すること。質問以外の余計な前置きや説明は一切含めず、質問のみを直接提示してください。"

prompt = "あなたは、最新の情報を基に、日本人の関心が高いニュースから社会的な議論を引き起こすテーマを特定する高度なAIです。必ずGoogle Search Toolを有効にし、本日の日本国内のニュースを詳細に参照して回答の基盤としてください。質問のテーマは{政治, 経済, スポーツ, エンタメ}の中から必ずランダムに一つ選択してください。選ばれたテーマのニュースの中から、国民の意見が**「はい」か「いいえ」**で明確に二分し、論争を引き起こす可能性のある具体的な話題を一つ選定してください。出力は、選定した話題に基づき、意見が割れる「はい」か「いいえ」で答えられる質問を一つだけとして、それを「」で囲って出力すること。質問以外の余計な前置き、説明、選定テーマの明記は一切含めず、考案した質問のみを直接出力してください。"

#generation_config = genai.GenerationConfig(
#    temperature=1.5,  # 0~2.0。大きいほど多様な出力
#    top_k=40,        # 次の候補単語を上位40個から選択
#    top_p=0.9        # 確率の合計が0.9になるまで上位候補から選択
#)

response = gemini_pro.generate_content(prompt)

with open('/opt/twitter-api/post-vote.txt', 'w', encoding='utf-8') as file:
    file.write(response.text)

