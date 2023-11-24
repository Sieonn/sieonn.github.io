# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     value = []
#     for i in range(N):
#         A = input().split()
#         for j in range(int(A[1])):
#             value.append(A[0])
#     print(value)
    
#     Sten = ""
#     ten = []
#     for l, k in enumerate(value):
#         Sten += k
#         if len(Sten) == 10:
#             ten.append(Sten)
#             Sten = ""
#         elif l == len(value)-1:
#             ten.append(Sten)
#     print(f'#{tc}',*ten, sep= "\n")       
# def solution(s):
#     s = list(s.split())
#     print(s)
#     value = 0
#     for i, v in enumerate(s):
#         if v == "Z":
#             value -= int(s[i-1])
#         else:
#             value += int(v)
#     return value
            

# s = "-1 -2 -3 Z"
# solution(s)

# def solution(my_string):
#     new = ''
#     for i in my_string:
#         if i not in new:
#             new += i
#     return new
# print(solution("people"))

# def solution(sides):
#     sides = sorted(sides)
#     if sides[2]< sides[0] + sides[1]: 
#         return 1
#     else:
#         return 2
# print(solution([199, 72, 222]))

# def solution(sides):
#     sides = sorted(sides)
#     return 2 - int(sides[2]< sides[0] + sides[1])
