from openai import OpenAI  # 오픈AI 라이브러리를 가져오기
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")  # 환경 변수에서 API 키 가져오기

client = OpenAI(api_key=api_key)  # 오픈AI 클라이언트의 인스턴스 생성

# ①
def get_ai_response(messages):
    response = client.chat.completions.create(
        model="gpt-4o",  # 응답 생성에 사용할 모델 지정
        temperature=0.9,  # 응답 생성에 사용할 temperature 설정
        messages=messages,  # 대화 기록을 입력으로 전달
    )
    return response.choices[0].message.content  # 생성된 응답의 내용 반환

messages = [
    {"role": "system", "content": "너는 사용자를 도와주는 상담사야."},  # 초기 시스템 메시지
]

while True:
    user_input = input("사용자: ")  # 사용자 입력 받기

    if user_input == "exit":  # ② 사용자가 대화를 종료하려는지 확인인
        break
    
    messages.append({"role": "user", "content": user_input})  # 사용자 메시지를 대화 기록에 추가 
    ai_response = get_ai_response(messages)  # 대화 기록을 기반으로 AI 응답 가져오기
    messages.append({"role": "assistant", "content": ai_response})  # AI 응답 대화 기록에 추가하기

    print("AI: " + ai_response)  # AI 응답 출력

'''
사용자: 안녕 난 최철녕이야
AI: 안녕하세요, 최철녕님! 만나서 반갑습니다. 어떻게 도와드릴까요?
사용자: 안녕 내 이름은 뭐게?
AI: 안녕하세요! 방금 전에 본인을 최철녕이라고 소개해 주셨는데, 맞나요? 😊 이름에 대해 다른 힌트를 주시면 더 잘 맞춰볼 수 있을 것 같아요.
사용자: 
'''