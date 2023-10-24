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

# def solution(my_string,m, c):


# def solution(my_string, indices):
#     new = ''
#     for i in range(len(my_string)):
#         if i not in indice:
#                 return new = new + i

#     return new
# my_string = "apporoograpemmemprs"
# indice = [1, 16, 6, 15, 0, 10, 11, 3]

# print(solution(my_string,indice))

# def solution(num_list):
#     a= []
#     b = []
#     for i in range(0, len(num_list)):
#         if i % 2 == 0:
#             a.append(num_list[i])
#         else:
#             b.append(num_list[i])
#     return max(sum(a),sum(b))

# def solution(names):
#     a = []
#     for i, v in range(names):
#         if i % 5 == 0:
#             a.append(v)
#     return a
# names = ["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]
# print(solution(names))4


# def solution(todo_list, finished):
#     a = []
#     for i in range(len(todo_list)):
#         if finished[i] == False:
#             a.append(todo_list[i])
#     return a

# todo_list = ["problemsolving", "practiceguitar", "swim", "studygraph"]
# def solution(arr):
#     idx = 0
#     while True:
#         change = []
#         for i in arr:
#             if i >= 50 and i % 2 == 0:
#                 change.append(int(i / 2))
#             elif i < 50 and i % 2 == 1:
#                 change.append(i * 2 + 1)
#             else:
#                 change.append(i)

#         same = all(a == b for a, b in zip(arr, change))
#         if same:
#             break
#         idx += 1

#         arr = change

#     return idx

# arr = [1, 2, 3, 100, 99, 98]
# print(solution(arr))

# def soultion(num_list):
#     cnt = 0
#     for i in num_list:
#         while i != 1:
#             if i % 2 == 0:
#                 i /= 2
#                 cnt += 1
#             else:
#                 i -= 1
#                 i /= 2
#                 cnt += 1
#     return cnt
# num_list = [12, 4, 15, 1, 14]
# print(soultion(num_list))4

# a = []
# if a:
#     print("참")
# else:
#     print("거짓")

# def solution(myString, pat):
#     return int(pat.lower() in myString.lower())
# myString = "AbCdEfG"
# pat = "aBc"

# print(solution(myString, pat))

# print(int(True))

# def solution(myString, pat):
#     i = myString.rfind(pat)
#     if i != len(myString):
#         return myString[: i+len(pat)]
#     else:
#         return myString


# myString = "AbCdEFG"
# pat = "dE"

# print(solution(myString, pat))

# def solution(strArr):
#     for i in strArr:
#         if "ad" in i:
#             strArr.remove(i)
#     return strArr

# strArr = ["there","are","no","a","ds"]

# print(solution(strArr))
# def solution(my_string):
#     new = my_string.split(" ")
#     return [i for i in new if i != '']

# my_string = " i    lov y"
# print(solution(my_string)) 
            
string = "AABBAB"
string.swapcase()
print(string)