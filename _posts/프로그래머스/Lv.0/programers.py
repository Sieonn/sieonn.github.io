# def solution(array, n):
#     sol = []
#     array = sorted(array)
#     for i in array:
#         num = i - n
#         if num < 0:
#             num = num*-1
#         sol.append(num)
#     return array[sol.index(min(sol))]

# print(solution([3, 10, 28], 20))

# def solution(my_string):
#     return my_string.swapcase

# def solution(my_string):
#     sol = ""
#     for i in my_string:
#         if i == i.upper():
#             sol += i.lower()
#         elif i == i.lower():
#             sol += i.upper()
#     return sol
# print(solution("abCdEfghIJ"))

# def solution(numbers):
#     english = { "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
#     sol = ""
#     answer = ""
#     for i in numbers:
#         sol += i
#         if sol in english.keys():
#             answer += str(english[sol])
#             sol = ""
#     return int(answer)

# def solution(numbers):
#     num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#     for i, v in enumerate(num):
#         numbers = numbers.replace(v, str(i))
#     return int(numbers)
# print(solution("onetwothreefourfivesixseveneightnine"))

# def solution(my_string, num1, num2):
#     new_string = [i for i in my_string]
#     new = []
#     for i, v in enumerate(new_string):
#         if i == num1:
#             new.append(my_string[num2])
#         elif i == num2:
#             new.append(my_string[num1])
#         else:
#             new.append(v)
#     return ''.join(new)


# print(solution("I love you", 3, 6))


# def solution(s):
#     ss = sorted(list(s))
#     cnt = []
#     for i in ss:
#         cnt.append(ss.count(i))
#     new = []
#     for j, v in enumerate(cnt):
#         if v == 1:
#             new.append(ss[j])
#     return ''.join(new)
# s = "hello"
# print(solution(s))
# def solution(num, k):
#     for i, v in enumerate(str(num)):
#         if v == str(k):
#             return i+1
#     return -1


# print(solution(29183, 1))


# def solution(quiz):
#     answer = []
#     for i in quiz:
#         new = i.split("=")
#         if eval(new[0]) == int(new[1]):
#             answer.append("O")
#         else:
#             answer.append("X")
#     return answer

# def solution(quiz):
#     answer = []
#     for i in quiz:
#         a = i.split()
#         if a[1] == '-':
#             dab = int(a[0]) - int(a[2])
#             if dab == int(a[-1]):
#                 answer.append("O")
#             else:
#                 answer.append("X")
#         else:
#             dab = int(a[0]) + int(a[2])
#             if dab == int(a[-1]):
#                 answer.append("O")
#             else:
#                 answer.append("X")
#     return answer


# print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))

#
# def solution(my_string):
# new = ""
# for i in my_string:
# if i.isupper():
# new += i.lower()
# else:
# new += i
# return ''.join(sorted(new))
# print(solution("Bcad"))
#
# def solution(array):
# return str(array).count('7')
# print(solution([7, 17, 77]))
# def solution(keyinput, board):
# dist = {"up": [0,1],"down": [0,-1],"left": [-1, 0], "right": [1, 0]}
# start = [0, 0]
#
# for i in keyinput:
# if -(board[0]//2) < start[0] < board[1]//2 and -(board[1]//2) < start[1] < board[1]//2 :
# start[0] += dist[i][0]
# start[1] += dist[i][1]
# return start


# print(solution(["left", "right", "up", "right", "right"],[11,11]))


#
# print(solution(["left", "right", "up", "right", "right"],[11, 11]))

# def solution(score):
# slist = [(x + y)/2 for x, y in score]
# s = sorted(slist, reverse=True)
# val = {}
# for x, y in enumerate(s):
# if y not in val.keys():
# val[y] = x+1
# return [val[i] for i in slist]

# print(key,s)

# n = 1
# for x,y in score:
# key.append(n)
#
# val.append((x+y)/2)
# n += 1
# average = dict(zip(key,val))
# for i in sorted(val, reverse=True):

# return answer
#
# print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))
# def solution(babbling):
# baby = ["aya", "ye", "woo", "ma"]
# count = 0
# for i in babbling:
# for j in baby:
# i = i.replace(j, "1")
# if set(i) == {'1'}:
# count += 1
# return count
#
# return count
#
# print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
#
# def solution(id_pw, db):
# for id, pw  in db:
# if id == id_pw[0]:
# if pw == id_pw[1]:
# return "login"
# else:
# return "wrong"
# return "fail"
#
# print(solution(["programmer01", "15789"], [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))
# def solution(chicken):
# service = 0
# while chicken >= 10:
# rest = chicken % 10
# service += chicken // 10
# chicken = rest + chicken //10
# return service


# def solution(bin1, bin2):
# nums = []
# for i in [bin1, bin2]:
# num = 0
# for j, k in enumerate(i[::-1]):
# if k == "1":
# num += 2**j
# nums.append(num)
# binnum = sum(nums)
# anwser = ''
# while binnum > 0:
# x, y = divmod(binnum, 2)
# binnum = x
# if binnum == 1:
# anwser += str(y)
# else:
# anwser += str(y)
# return anwser[::-1]


#
# print(solution("10", "11"))


# num = 77
# print(bin(num))
# two = "0b1001101"
# print(int(two, 2))
# def solution(before, after):
# for i in before:
# after = after.replace(i,"",1)
# return int(len(after) == 0)
# def solution(A,B):
# for _ in range(len(A)):
# A = A[-1]+ A[:-1]
# if A == B:
# return 1
# n("ollhe", "hello"))
# def solution(A,B):
# for _ in range(len(A)):
# if A == B:
# return 0
# B = B[-1] + B[:-1]
# if A == B:
# return 1
# else:
# return -1
# from collections import deque
#
# def solution(A, B):
# a, b = deque(A), deque(B)
# print(a, b)
# for cnt in range(0, len(A)):
# if a == b:
# return cnt
# a.rotate(1)
# return -1
# print(solution("hello", "ollhe"))
# for i in range(1,0):
# print(i)
# def solution(num, total):
#     return [ (total//num)-1+i for i in range(num)]
# print(solution(3,0))

# def solution(common):
#     if common[1] - common[0] == common[2] - common[1]:
#         w = common[1] - common[0]
#         return common[-1] + w
#     else:
#         w = common[1]//common[0]
#         return common[-1] * w


# print(solution([2, 4, 8]))
T = int(input())
for tc in range(1, T+1):
    S = input()
    b = ""
    for i in S:
        if i.isupper():
            v = bin(ord(i)-65)[2:]
        elif i.islower():
            # v = bin(ord(i))
            v = bin(ord(i)-71)[2:]
        elif i.isdigit():
            v = bin(ord(i)+4)[2:]
        if len(v) != 6:
            v = (6-len(v))*"0" + v
        b += v
    c = ''
    for j in range(0, len(b), 8):
        c += chr(int('0b'+b[j:j+8], 2))
    print(f'#{tc} {c}')

    # print(c)
    # # Stringc += chr(int('0b' + b[j:j+6], 2))
    # Stringc += j
    # if len(Stringc) == 6:
    #     p = int('0b' + Stringc, 2)
    #     print(p)
    #     # Stringd += chr(int('0b' + Stringc, 2))
    #     Stringc = ''
