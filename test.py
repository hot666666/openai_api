import openai
import os
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


with open("ex.txt", "r") as f:
    TEXT = f.read()

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "내용에 관한 3가지 질문을 만들어주세요."},
        {"role": "user", "content": TEXT},
    ],
)

print(completion)
print(completion['choices'][0]['message']['content'])


'''
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "1. \ud2b8\ub79c\uc2a4\ud3ec\uba38 \ubaa8\ub378\uc740 \uc5b4\ub5a4 \ud55c\uacc4\ub97c \uadf9\ubcf5\ud558\uae30 \uc704\ud574 \uac1c\ubc1c\ub418\uc5c8\ub098\uc694?\n2. \ud2b8\ub79c\uc2a4\ud3ec\uba38 \ubaa8\ub378\uc740 \uc5b4\ub5a4 \uc790\uc5f0\uc5b4\ucc98\ub9ac \ud0dc\uc2a4\ud06c\uc5d0\uc11c \uc88b\uc740 \uacb0\uacfc\ub97c \ubcf4\uc5ec\uc8fc\ub098\uc694?\n3. \ud2b8\ub79c\uc2a4\ud3ec\uba38 \ubaa8\ub378\uc758 \uc124\uacc4\uc5d0\uc11c \uc5b4\ub5a4 \ud2b9\uc9d5\uc774 \ud559\uc2b5 \uc18d\ub3c4\ub97c \ube60\ub974\uac8c \ud558\uace0 \uc0c8\ub85c\uc6b4 \uc785\ub825\uc5d0 \ub300\ud55c \ucd9c\ub825\uc744 \uc2e4\uc2dc\uac04\uc73c\ub85c \uc0dd\uc131\ud560 \uc218 \uc788\uac8c \ub9cc\ub4e4\uc5b4\uc900 \uac74\uac00\uc694?",
        "role": "assistant"
      }
    }
  ],
  "created": 1678974695,
  "id": "chatcmpl-6uiIx3zwJcudoepjKaKHWSkUKWqDO",
  "model": "gpt-3.5-turbo-0301",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 169,
    "prompt_tokens": 602,
    "total_tokens": 771
  }
}
1. 트랜스포머 모델은 어떤 한계를 극복하기 위해 개발되었나요?
2. 트랜스포머 모델은 어떤 자연어처리 태스크에서 좋은 결과를 보여주나요?
3. 트랜스포머 모델의 설계에서 어떤 특징이 학습 속도를 빠르게 하고 새로운 입력에 대한 출력을 실시간으로 생성할 수 있게 만들어준 건가요?
'''
