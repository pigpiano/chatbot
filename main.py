import streamlit as st
from langchain.chat_models import ChatOpenAI
# llm = ChatOpenAI()

# st.title('인공지능 시인')

# title = st.text_input('시의 주제를 제시해주시요.')
# if st.button('시 작성 요청하기'):
#     with st.spinner('시 작성 중'):
#         result = llm.predict(title + "에 대한 시를 써줘")
#         st.write(result)
    
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI()
st.title('Chatbot잡쉈어?')
st.caption('무엇을 도와드릴까요? :sunglasses:')

# 챗봇 모델 초기화
llm = ChatOpenAI()

# 사용자 입력을 위한 텍스트 입력 상자
user_input = st.text_input("질문을 입력하세요:")

# 사용자가 질문을 입력하면, 챗봇에게 질문 전달하고 응답 받기
if user_input:
    # 챗봇 모델을 사용하여 응답 생성
    response = llm.predict(user_input)

    # 챗봇의 응답을 화면에 표시
    st.text("챗봇의 대답:")
    st.write(response)

