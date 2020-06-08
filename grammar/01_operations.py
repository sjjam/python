# 01_operations.py
# 논리 연산자
# and, or, not
print("___and___")
print(True and True)
print(True and False)
print(False and False)
print(False and True)

print("___or___")
print(True or True)
print(True or False)
print(False or False)
print(False or True)

print("___not___")
print(not True)
print(not False)
print(not [])

# in, not in
print("___in___")
print('a' in 'apple')
print(1 not in [1,2,3])

# 단축 평가
print('' or 'Text' or 'Text_2')
# 하나가 True가 되면 그 뒤로 연산을 안함 '' > False Text > True여서 Text가 나온다.
print('Text' and '' or 'Text_2')