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
# def solution(keyinput, borad):
#     x, y = 0, 0
#     wx = borad[0]//2
#     wy = borad[1]//2
#     for i in keyinput:
#         if i == "left" and x > -wx:
#             x -= 1
#         elif i == "right" and x < wx:
#             x += 1
#         elif i == "up" and y < wy:
#             y += 1
#         elif i == "down" and y > -wy:
#             y -= 1
#     return [x, y]


# print(solution(["left", "right", "up", "right", "right"], [11, 11]))

# print(solution(["left", "right", "up", "right", "right"],[11, 11]))


# def solution(numbers):
#     max = 0
#     for i, k in enumerate(numbers):
#         for j, l in enumerate(numbers):
#             num = k * l
#             if k * l >= num and i != j:
#                 max = num
#     return max
# def solution(numbers):
#     m = []
#     for i in range(len(numbers)):
#         for j in range(len(numbers)):
#             num = numbers[i] * numbers[j]
#             if i != j:
#                 m.append(num)
#     return max(m)


# print(solution([1, 2, -3, 4, -5]))


# def solution(polynomial):
#     num = polynomial.split(" + ")
#     print(num)
#     x, y = 0, 0
#     sol = []
#     for i in num:
#         if "x" in i:
#             if len(i) != 1:
#                 x += int(i[:-1])
#             else:
#                 x += 1
#         elif i.isdigit():
#             y += int(i)
#     if x > 1:
#         sol.append(str(x)+"x")
#     elif x == 1:
#         sol.append("x")

#     if y != 0:
#         sol.append(str(y))

#     return ' + '.join(sol)


# print(solution("x + 1"))


# def solution(my_string):
#     num = ""
#     sol = []

#     for v, i in enumerate(my_string):
#         if i.isdigit():
#             if my_string[v-1].isdigit() and v != 0:
#                 num = num + i
#                 if v == len(my_string)-1:
#                     sol.append(int(num))
#             else:
#                 num += i
#                 if v == len(my_string)-1:
#                     sol.append(int(num))
#         else:
#             if num != "":
#                 sol.append(int(num))
#                 num = ""
#     if sol == []:
#         return 0
#     # print(sol)
#     return sum(sol)


# print(solution(""))


# def solution(my_string):
#     s = ''.join(i if i.isdigit() else ' ' for i in my_string)
#     print(s, s.split())
#     return sum(int(i) for i in s.split())


# print(solution("aAb1B2cC34oOP"))

# def solution(board):
#     N = len(board)
#     bomb = [[i, j] for i in range(N) for j in range(N) if board[i][j] == 1]
#     if N < 3:
#         if len(bomb) > 0:
#             return 0
#         else:
#             return N*N
#     region = []
#     for x, y in bomb:
#         if x - 1 < 0:
#             xx = 0
#         else:
#             xx = x-1
#         if y - 1 < 0:
#             yy = 0
#         else:
#             yy = y - 1

#         for a in range(xx, x+2):
#             for b in range(yy, y+2):
#                 if [a, b] not in region and a < N and b < N:
#                     region.append([a, b])
#     print(region)
#     if N*N - len(region) > 0:
#         return N*N - len(region)
#     else:
#         return 0

# return answer
# print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
#       0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
# def solution(board):
#     n = len(board)
#     danger = set()
#     for i, row in enumerate(board):
#         for j, k in enumerate(row):
#             if not k:
#                 continue
#             danger.update((i+a, j+b) for a in [-1, 0, 1] for b in [-1, 0, 1])
#     print(danger)
#     return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)


# print(solution([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))


def solution(sides):
    a, b = sorted(sides)
    # 배열 내에 가장 긴 변이 포함된 경우 [3,6]
    count = 0
    num = b - a+1
    while b - a < num <= b:
        count += 1
        num += 1
    num2 = b
    while b < num2+1 < b + a:
        count += 1
        num2 += 1

    return count

    # 주어진 배열의 값이 같은 경우[6,6]
    # 가장 긴변을 구해야하는 경우


print(solution([11, 7]))
