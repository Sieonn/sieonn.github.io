# # def solution(my_string):
# #     answer = []
# #     for i in range(len(my_string)):
# #         print(i)
# #         answer.append(my_string[i:])
# #     return answer.sort()

# def solution(my_string, is_suffix):
#     anwser = []
#     for i in range(len(my_string)):
#         anwser.append(my_string[i:])
#     print( anwser)
#     if is_suffix in anwser:
#         return 1
#     else:
#         return 0
# # my_string = "ProgrammerS123"
# my_string = "banana"
# is_suffix = "ana"
# n = 11
# print(solution(my_string,is_suffix))
# # if "안" in ["안", "안녕", "으응"]:
# #     print( 1)
# # else:
# #     print(0)

# def solution(my_string, n):
#     return my_string[:n]

# def solution(my_string, s, e):
#     return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
# my_string = "Progra21Sremm3"	
# s = 6
# e = 12
# print(solution(my_string, s, e))

def solution(my_string,m, c):
   return my_string.split[::4]
my_string = "asdfghjlk;zx"
