import sys
# sys.stdin=open("./in3.txt", "r")
from collections import deque
str_input = input()

stack_oper = list()
res = ''

for i in str_input:
    if i.isdecimal():
        res += i
    elif i == '(':
        stack_oper.append(i)
    elif i == ')':
        while stack_oper[-1] != '(':
            res += stack_oper.pop()
        stack_oper.pop()
    elif i == '*' or i == '/':
        while stack_oper and (stack_oper[-1] == '*' or stack_oper[-1] == '/'):
            res += stack_oper.pop()
        stack_oper.append(i)
    else:
        while stack_oper and stack_oper[-1]!='(':
                res+=stack_oper.pop()
        stack_oper.append(i)

while stack_oper:
    res += stack_oper.pop()
print(res)


# isdecimal()
# isdigit()
# isnumeric()
# => 주어진 문자열이 숫자로 되어있는지 검사하는 함수
# => return 값은 boolean
# 후위표기식은 우선순위를 정해주는게 중요.

# 우선순위를 리스트에 정하고 푼 코드

# for t in range(1,11):
#     N = int(input())
#     tokens =list(map(str,input().rstrip()))     # 입력받기
#     lst = []        # 빈 리스트 생성
#     stack = []      # 스택 생성
#     prior = {'*':3,'/':3,'+':2,'-':2,'(':1}     # 우선순위 설정
#     for n in range(len(tokens)):    # 토큰의 길이만큼 반복하여
#         if tokens[n].isdigit(): # 만약 숫자이면 바로 lst에 추가
#             lst.append(tokens[n])
#         elif tokens[n] == '(':  # (이면 바로 stack에 추가
#                 stack.append(tokens[n])
#         elif tokens[n] == ')':  # )가 나오면 stack에서 (가 나올때까지 pop처리 및 lst에 추가. 
#             while stack[-1] != '(':
#                 lst.append(stack.pop())
#             stack.pop() # (가 나타나면 pop처리
#         else:   # 그외에 경우 tokens[n]이 stack[-1]의 우선순위와 같거나 보다 작으면 tokens[n]의 우선순위가 더 커질때까지 pop
#             while stack and prior[tokens[n]] <= prior[stack[-1]]:
#                 lst.append(stack.pop()) # pop한것들은 lst에 추가 시켜줌   
#             stack.append(tokens[n]) # 위의 조건이 완료 되면 stack에 추가

#     while len(stack) != 0:  # stack에 남아있는 연산자들 lst에 추가
#         lst.append(stack.pop())