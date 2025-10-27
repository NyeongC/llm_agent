from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")  # 환경 변수에서 API 키 가져오기

client = OpenAI(api_key=api_key)  # 오픈AI 클라이언트의 인스턴스 생성

while True:
    user_input = input("사용자: ")

    if user_input == "exit":
        break

    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.9,
        messages=[
            {"role": "system", "content": "너는 사용자를 도와주는 상담사야."},
            {"role": "user", "content": user_input},
        ],
    )
    print("AI: " + response.choices[0].message.content)

'''
사용자: 안녕 난 최철녕이야.
AI: 안녕하세요, 최철녕 씨! 어떻게 도와드릴까요?
사용자: 안녕 내 이름이 뭐라고?
AI: 안녕하세요! 죄송하지만, 대화 중에서는 사용자의 이름을 알 수 없습니다. 하지만 제가 도와드릴 수 있는 다른 것이 있다면 말씀해 주세요!        
사용자:
'''
