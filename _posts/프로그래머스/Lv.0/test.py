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

# string = "AABBAB"
# string.swapcase()
# print(string)

# from collections import OrderedDict

# # 기본 딕셔너리
# dict_a = {'a': 'apple', 'b': 'banana', 'p': 'pineapple'}
# dict_b = {'b': 'banana', 'a': 'apple', 'p': 'pineapple'}
# dict_a == dict_b
# # True

# OrderedDict
# ordered_a = OrderedDict([('a', 'apple'), ('b', 'banana'), ('p', 'pineapple')])
# ordered_b = OrderedDict([('b', 'banana'), ('a', 'apple'), ('p', 'pineapple')])

# ordered_a == ordered_b
# # False

# def solution(myStr):
#     new = ("a", "b", "c")
#     myStr.split
#     return myStr

# myStr = "baconlettucetomato"
# print(solution(myStr))

# a = ["", "" , ""]
# if a == :
#     print('["EMPTY"]')
# range

# a= []
# a.append()


# def solution(arr):
#     answer = []

#     for i in range(len(arr)):
#         if len(answer) == 0:
#             answer.append(arr[i])
#         else:
#             if answer[-1] == arr[i]:
#                 answer.pop()
#                 i += 1
#             elif answer[-1] != arr[i]:
#                 answer.append(arr[i])
#                 i += 1

#     if len(answer) == 0:
#         return [-1]

#     return answer


# 빈 배열만들기 6
# def solution(arr):
#     stk = []
#     for i in range(len(arr)):
#         if len(stk) == 0:
#             stk.append(arr[i])
#         else:
#             if stk[-1] == arr[i]:
#                 stk.pop()
#                 i += 1
#             else:
#                 stk.append(arr[i])
#                 i += 1
#     if len(stk) == 0:
#         return [-1]
#     return stk
# arr = [0, 1, 1, 1, 0]

# print(solution(arr))7

# def solution(arr):
#     for i in range(len(arr)):
#         if len(arr) < 2**i:
#             return arr + ([0] * (2**i - len(arr)))
#         elif len(arr) == 2 ** i:
#             return arr


# arr = [1, 2, 3, 4, 5, 6]

# print(solution(arr))


# def solution(strArr):
#     new = []
#     zarr = [0] * len(strArr)
#     for i in strArr:
#         zarr[len(i)] += 1

#     return max(zarr)


# strArr = ["a", "bc", "d", "efg", "hi"]

# strArr = ["a", "bc", "d", "efg", "hi"]
# print(solution(strArr))


# def solution(rank, attendance):
#     new = []
#     for i, v in enumerate(attendance):
#         if v:
#             new.append(rank[i])
#     new2 = sorted(new)

#     return rank.index(new2[0]) * 10000 + 100 * rank.index(new2[1]) + rank.index(new2[2])


# rank = [3, 7, 2, 5, 4, 6, 1]
# attendance = [False, True, True, True, True, False, False]
# print(solution(rank, attendance))

# str = "1234"
# sum = 0
# for i in str:
#     sum = sum + int(i)
# print(sum)

# a = "1234"
# print(sum(map(int, a)))

# def eveswitch(str):
#     new = ''
#     for i in range(len(str)):
#         if i % 2 == 0:
#             new += str[i].swapcase()

#         else:
#             new += str[i]

#     return new


# str = 'Divide and conquer algorithm'

# print(eveswitch(str))

# str = "001234"
# print(str[3:])
# def solution(n_str):
#     for i in range(len(n_str)):
#         if n_str[i] != "0":
#             return n_str[i:]
#         else:
#             pass


# n_str = "0010"

# print(solution(n_str)[)
# 이익 = 매매가*(i - 1) - sum(매매가[:i])
# 6- 2 = 4
# 8 - 6 =2
# T = int(input())

# for i in range(T):
#     N = int(input())
#     price = list(map(int, input().split))
#     benefit = 0
#     while len(prince) != 0:
# T = int(int(input()))
# for i in  range(1, T + 1):
#     print("#" * int(input()) )

# # print(solution(n_str))

# test = 0
# for test_case in range(1, 6 + 1):
#     if test_case % 2 == 1:
#         test += test_case

# print(test)
# import math

# a = 5.54
# print(round(a))
# n = list(map(int, input().split()))
# an = sum(n) / 10
# print(n, type(n), sum(n), round(an), an)

# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     # ///////////////////////////////////////////////////////////////////////////////////
#     b, c = map(int, input().split())
#     if b < c:
#         print(f'#{test_case} {"<"}')
#     elif b == c:
#         print(f'#{test_case} {"="}')
#     else:
#         print(f'#{test_case} {">"}')
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     new = []
#     for i in list(map(int, input().split())):
#         new.append(i)
#     print(f'#{test_case} {max(new)}')

# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):

#     new = sort(new)
#     print(f'#{test_case} {new[len(new) // 2 + 1]}')

# N = int(input())
# new = []
# for i in list(map(int, input().split())):
#     new.append(i)
#     nnew = sorted(new)
# print(nnew[N // 2])
# # 3 4 12 13 26 32 43 52 65
# sum = 0
# for i in str(input()):
#     sum += int(i)
# print(sum)
# 20231101
# T = int(input())
# for i in range(1, T+1):
#     date = input()
#     if int(date[4:6]) in [4, 6, 9, 11]:
#         if int(date[6:]) in range(1, 31):
#             print(f'#{i} {date[:4]}{"/"}{date[4:6]}{"/"}{date[6:] }')
#         else:
#             print(f'#{i} {-1}')
#     elif int(date[4:6]) == 2:
#         if int(date[6:]) in range(1, 29):
#             print(f'#{i} {date[:4]}{"/"}{date[4:6]}{"/"}{date[6:] }')
#         else:
#             print(f'#{i} {-1}')
#     elif int(date[4:6]) in [1, 3, 5, 7, 8, 10, 12]:
#         if int(date[6:]) in range(1, 32):
#             print(f'#{i} {date[:4]}{"/"}{date[4:6]}{"/"}{date[6:] }')
#         else:
#             print(f'#{i} {-1}')
#     else:
#         print(f'#{i} {-1}')
# N = input()
# print(' '.join([str(ord(i)-64) for i in N]))

# print(input().upper())

# P, K = map(int, input().split())
# print(P - K + 1)

# print(9//2)

# print("#++++",
#       "+#+++",
#       "++#++",
#       "+++#+",
#       "++++#", end="\n")

# a, b = map(int, input().split())
# print(f'{a + b} {a - b} {a *b} {a // b)
# N = int(input())
# su = []
# for i in range(1, N + 1):
#     if N % i == 0:
#         su.append(str(i))
# print(' '.join(su))

# 가위 : 1 바위 : 2 보 : 3
# A, B = map(int, input().split())
# if (A - B) == -1 or (A-B) == 2:
#     print("B")
# elif (A -B) == 1 or (A - B) == -2:
#     print("A")
# new = []
# for i in range(0, int(input()) + 1):
#     new.append(str(2**i))
# print(' '.join(new))

# new = []
# for i in range(0, int(input())+1):
#     new.append(str(i))
# print(' '.join(reversed(new)))

# 1 1 3 1 2
# 0 2 -2 1
# 10 7 6
# -3 -1
# 3 5 9

# 2 4
# 3 5 8
# 16[2] - (3*1 + 5*1) = 8
# len(N)
# index(max(n))


# T = int(input())
# for i in range(1, T+1):
#     N = list(map(int, input().split()))
# # print(max(N), N.index(max(N)))
#     M = N.index(max(N))
# # O, M = N[:M+1], N[M+1:]
# # print(O, M)
#     A = 0
#     B = 0
#     if max(N) != N[-1] and max(N) != N[0]:
#         O, P = N[:M+1], N[M+1:]
#         A = O[-1]*(len(O)-1) - sum(O[:len(O)-1])
#         B = P[-1]*(len(P)-1) - sum(P[:len(P)-1])
#         print(f'#{i} {A+B}')
#     elif max(N) == N[-1]:
#         print(f'#{i} {N[M]*M - sum(N[:M])}')
#     else:
#         print(F'#{i} {0}')


# T = int(input())
# for i in range(1, T+1):
#     Num = int(input())
#     N = list(map(int, input().split()))
#     M = N.index(max(N))
#     A = 0
#     if M not in [0, Num-1]:
#         O, P = N[:M+1], N[M+1:]
#         if len(P) >= 2:
#             A = O[-1]*(len(O)-1) - sum(O[:len(O)-1])
#             A = A + P[-1]*(len(P)-1) - sum(P[:len(P)-1])
#             print(f'#{i} {A}')
#         elif len(P) < 2:
#             A = O[-1]*(len(O)-1) - sum(O[:len(O)-1])
#             print(f'#{i} {A}')
#     elif max(N) == N[-1]:
#         print(f'#{i} {N[M]*M - sum(N[:M])}')
#     else:
#         print(f'#{i} {0}')
# T = int(input())
# for i in range(1, 1+T):
#     Num = int(input())
#     N = list(map(int, input().split()))
#     new = 0
#     answer = 0

#     for val in N[::-1]:
#         if val >= new:
#             new = val
#         else:
#             answer += new - val
#     print("#", i, " ", answer, sep="")

# N = int(input())
# new = []
# # rule = ("3", "6", "9")
# for i in range(1, N+1):
#     i = str(i)
#     clap = i.count('3') + i.count('6') + i.count('9')

#     if clap == 0:
#         print(i, end=' ')
#     else:
#         print("-" * clap, end=' ')

# new = new.replace("3", '-').replace("6", '-').replace("9", '-')
# print(new)

# def solution(order):
#     A = 0
#     B = 0
#     for i in order:
#         A += i.count("americano") + i.count("anything")
#         B += i.count("cafelatte")
#     print(A, B)
#     return 4500*A + 5000*B


# order = ["cafelatte", "americanoice", "hotcafelatte", "anything"]
# print(solution(order))

# def solution(picture, k):
#     new = []
#     new2 = []
#     for i in picture:
#         a = 0
#         while a < k:
#             new.append(i)
#             a += 1
#     new = new
#     for i in new:
#         news = ''
#         for b in i:
#             news += b*k
#         new2.append(news)
#     return new2


# picture = ["x.x", ".x.", "x.x"]
# k = 3
# print(solution(picture, k))
# new = ''
# for i in "abcde":
#     if i < "d":
#         new += 'l'
#     else:
#         new += i
# print(new)

# def solution(n):
#     new = []
#     for i in range(n):
#         news = []
#         for j in range(n):
#             if i == j:
#                 news.append(1)
#             else:
#                 news.append(0)
#         new.append(news)

#     return new


# # d = [1]
# n = 3
# print(solution(6))

# T = int(input())
# for i in (1, T+1):
#     Str = input()
#     new = ''
#     for a in Str:
#         new += a
#         l = len(new)
#         if new == Str[l:l+l]:
#             break
#     print(f'#{i} {len(new)}')


# for i in range(1, case_count + 1):
#     string = input()
#     word = ''
#     for char in string:
#         word += char
#         length = len(word)
#         if word == string[length:length+length]:
#             rest_string = string[length:]
#             rest_string = rest_string.replace(word, '')
#             if len(rest_string) < len(word):
#                 break
#     print('#{} {}'.format(i, len(word)))

# s = input()
# str = ''
# for i in s:
#     str += i
#     l = len(str)
#     if str == s[l:l+l]:
#         news = s[l:].replace(str, "")  # PI-APIAPIAPIAPIA
#         if len(news) == False:
#             # print(news)
#             break
# print(str)

#         if len(news) < len(str):
#             break
# print(l)

# s = input()
# str = ''
# for i in s:
#     str += i
#     l = len(str)
#     if str == s[l:l+l]:
#         print(str)
# T = int(input())
# for i in range(1, T+1):
#     N = int(input())
#     for a in range(1, N+1):
#         new = ''
#         for b in range(1, N+1):
#             if b <= a:
#                 if a == b:
#                     new += "1 "
#                 elif b == 1:
#                     new += "1 "
#                 else:
#                     new += str(a - 1) + " "
#         print(new)
# T = int(input())
# for i in range(1, T+1):
#     N = int(input())
#     print(f'#{i}')
#     for a in range(1, N+1):
#         new = ''
#         for b in range(1, N+1):
#             if b <= a:
#                 if a == b:
#                     new += "1 "
#                 elif b == 1:
#                     new += "1 "
#                 else:
#                     new += str(a - 1) + " "

#         print(new)

# N = [k for k in range(1, int(input())+1)]
# new = []
# new2 = []
# for i in N:
#     new2 += new
#     new.clear()
#     for j in N:
#         if j <= i:
#             if i == j or j == 1:
#                 new.append(1)
#             else:
#                 new.append(new2[j-2] + new2[j-1])
#     new2.clear()
#     print(' '.join(list(map(str, new))))

# print(new)


# (3,2) ==> (2, 1), (2, 2)
# (4,3)==> (3, 2)(3, 3)

# N = [k for k in range(1, int(input())+1)]
# for i in N:
#     new = []
#     for j in N:
#         if j <= i:
#             if i == j or j == 1:
#                 new.append(1)
#             else:
#                 new.append(new2[j-2] + new2[j-1])
#     new2 = []
#     new2 += new
#     print(' '.join(list(map(str, new))))
# T = int(input())
# for q in range(1, 1 + T):
#     N = [k for k in range(int(input()))]
#     print(f'#{q}')
#     for i in N:
#         now = []
#         for j in N:
#             if j <= i:
#                 if i == j or j == 0:
#                     now.append(1)
#                 else:
#                     now.append(save[j-1] + save[j])
#         save = []
#         save += now
#         print(' '.join(list(map(str, now))))


# 내가 통과한 코드

# T = int(input())
# for i in range(1, T+1):
#     N = [k for k in range(1, int(input())+1)]
#     print(f'#{i}')
#     new = []
#     new2 = []
#     for i in N:
#         new2 += new
#         new.clear()
#         for j in N:
#             if j <= i:
#                 if i == j or j == 1:
#                     new.append(1)
#                 else:
#                     new.append(new2[j-2] + new2[j-1])
#         new2.clear()
#         print(' '.join(list(map(str, new))))
# def solution(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i][j] != arr[j][i]:
#                 return 0
#     return 1


# arr = [[19, 498, 258, 587], [63, 93, 7, 754],
#        [258, 7, 1000, 723], [587, 754, 723, 81]]
# print(solution(arr))


# def solution(board, k):
#     sum = 0
#     for i in range(len(board)):
#         for j in range(len(i)):
#             if i + j <= k:
#                 sum += board[i][j]
#     return sum


# board = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]]
# k = 2
# print(solution(board, k))

# T = int(input())
# for i in range(1, T+1):
#     n, m = map(int, input().split())
#     space = []
#     for _ in range(n):
#         a = list(map(int, input().split()))
#         space.append(a)
#     hap = 0
#     for j in range(n - m-1):  # 012 (1)
#         for k in range(n-m-1):  # 012 (1)()
#             temp = 0
#             # print(j, k)1
#             for l in range(j, j+m):  # (0, 2) /
#                 for o in range(k, k+m):  # (0, 2) (1, 3)/
#                     # (0,0)(0, 1)(1, 0)(1, 1) #(0, 1)(0, 2)(2, 1)(2, 2)
#                     # print(i, k, l, o)
#                     temp += space[l][o]
#                     if temp > hap:
#                         hap = temp
#     print(f'#{i} {hap}')


# T = int(input())
# for test_case in (1, T+1):
#     n, m = map(int, input().split())
#     space = []
#     for i in range(n):
#         v = list(map(int, input().split()))
#         space.append(v)
#     hap = 0
#     for z in range(n-1):
#         for x in range(n-1):
#             temp = 0
#             for a in range(z, z+m):  # (0,)(0, 1)(1, 0)(1, 1)
#                 for b in range(x, x+m):
#                     temp += space[a][b]
#                     if temp > hap:
#                         hap = temp
#     print(f'#{test_case} {hap}')


# 2005파리잡기 해답
# T = int(input())
# for test_case in (1, T+1):
#     n, m = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(n)]

#     max = 0
#     for i in range(n-m+1):
#         for j in range(n-m+1):
#             hap = 0
#             for k in range(m):
#                 for l in range(m):
#                     hap += arr[i+k][j + l]
#                     if hap > max:
#                         max = hap

#     print(f'#{test_case} {max}')
# T = int(input())

# for i in range(1, T+1):
#     for j in list(map(str, input().split())):
#         sum = 0
#         for k in range(len(j)//2):
#             # print(j[k], j[-k-1])
#             if j[k] == j[-k-1]:
#                 sum += 1
#             else:
#                 break
#     print(f'#{i} {int(sum == len(j)//2)}')


# T = int(input())

# for i in range(1, T+1):
#     j = list(map(str, input().split()))
#     sum = 0
#     for l in j:
#         for k in range(len(l)//2):
#             # print(j[k], j[-k-1])
#             if l[k] == l[-k-1]:
#                 sum += 1
#             else:
#                 break
#     print(f'#{i} {int(sum == len(l)//2)}')

# array = [1, 2, 3, 3, 3, 4]


# def solution(array):
#     n = []
#     n2 = 0
#     for i in array:
#         new = array.count(i)
#         n.append(new)
#     n2 = n.index(max(n))
#     if n2 != 0:
#         return array[n2]
#     else:
#         return -1


# array = [1, 2, 3, 3, 3, 4]
# print(solution([1, 1, 2, 2]))


# def solution(array):
#     n = []
#     n2 = 0
#     for i in array:
#         if len(array) == 1:
#             return i
#         elif len(array) != 1:
#             new = array.count(i)
#             n.append(new)
#             n2 = n.index(max(n))
#         if n2 != 0:
#             return array[n2]
#         else:
#             return -1
# def solution(array):
#     n = []
#     if len(array) > 1:
#         for i in array:
#             n.append(array.count(i))

#         if len(set(n)) != 1:
#             new = n.index(max(n))
#             return array[new]
#         else:
#             return -1
#     else:
#         return array[0]


# print(solution([1, 1, 2, 2]))

# def solution(array):
#     while len(array) != 0:
#         for i, a in enumerate(set(array)):
#             array.remove(a)
#         print(array, i)
#         if i == 0:
#             return a
#     return -1


# array = [1, 2, 3, 3, 3, 4]
# print(set(array))
# print(solution(array))

print(round(15//7))
