# 반복문 종류 2개
# 1. While
n = 0
'''
while n < 3 :
    print(n)
    n += 1

while n < 3 :
    n += 1
    print(n)
print(n)

# 2. for
number = list(range(3, 10, 3)) # range(10) 0~9 / 세번째 인자 3 3개씩 건너 띄기 3,6,9
print(number)

for num in range(10) :
    print(num)

# 2-1. list for
number = ['삼성', '역삼', '선릉', '영등포']
for num in number :
    print(num)

# 2-2. idx로 접근하고 싶어요.
number = ['삼성', '역삼', '선릉', '영등포']
for i in range(len(number)) :
    print(i)
    print(number[i])

# 2-3. enumerate
for idx, i in enumerate(number) :
    print(idx, i)
'''
# 3. dictionary
mask = {
    '삼성' : 100,
    '역삼' : '50개',
    '선릉' : True,
}

for i in mask :
    print(i)
print("*"*30)
# 동작은 위 코드와 동일하나, dict라는걸 표현하기 위함
for i in mask.keys() :
    print(i)
    print(mask[i])
print("*"*30)

for i in mask.values() : # dictionary val로 key 접근은 불가
    print(i)
print("*"*30)

for key, val in mask.items() :
    print(key)
    print(val)
    print(mask[key])
print("*"*30)

for idx, i in enumerate(mask, 3) : # 두번쨰 인자에 있는 수부터 설정 가능
    print(idx, i)