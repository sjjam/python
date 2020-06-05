from lt import lottos

pick = lottos.lotto()
print(pick)

# 1. 만약 4등 한적이 있으면
if pick['4th'] >= 1 :
# 2. 4등 '몇 번' 했습니다.
    print(f'4등 {pick["4th"]} 번 했습니다.')
# 3. 4등 한 적 없으면, 실패 출력
else :
    print("fail")