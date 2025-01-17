# 아주 간단한 계산기
# 입력 받기(두 개의 자연수 a, b는 1-9의 자연수)
# 나누기 연산에서 소수점 이하 숫자 버림

nums = list(map(int, input().split()))

# input(): 주어진 입력 문자열 받기
# input().split(): 문자열 공백 단위로 쪼갬
# map, int: 각각의 문자열-> 숫자
# list를 하면 [a, b]

a, b = nums # 리스트의 각 원소를 꺼내서 a, b에 저장
print(a+b)
print(a-b)
print(a*b)
print(a//b)
