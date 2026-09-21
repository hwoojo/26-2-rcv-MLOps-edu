import datetime  # 시간을 다루는 패키지

print(datetime.datetime.now())  # 지금 시간이 나온다

import random  # 난수 출력 패키지

for i in range(0, 5):
    print(random.randint(1, 30))  # 1에서 30 사이 난수

basket = ["사과", "복숭아", "레몬", "블루베리"]

print(random.choice(basket))  # 이런 식으로 랜덤으로 하나 고르기 가능

import requests  # 웹 사이트에 접근 할 수 있는 외부 라이브러리


def get_example():
    response = requests.get("https://google.com")

    print(f"Status code: {response.status_code}")
    print(response.text)


get_example()
