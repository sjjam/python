import random

# 1. 로또번호 추첨하는데 5번 반복해서
for i in range(5) :
    print(sorted(random.sample(range(1, 46), 6)))
print("*"*30)
lotto = [sorted(random.sample(range(1, 46), 6)) for i in range(5)]
print(lotto)

# 2. 음식점 이름, 전화번호인 딕셔너리
food = {
    'a' : '111',
    'b' : '222',
    'c' : '333',
    'd' : '444',
    'e' : '555'
}
# 2-1. 그중에서 무작위 음식점 하나 뽑아서
pick = random.choice(list(food.keys()))
# 2-2. 가게이름이랑 전화번호 출력
print('가게이름 :', pick)
print('전화번호 :', food[pick])

# f-string
print(f'가게이름 : {pick}, 전화번호 : {food[pick]}')