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

def solution(numbers):
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, v in enumerate(num):
        numbers = numbers.replace(v, str(i))
    return int(numbers)
print(solution("onetwothreefourfivesixseveneightnine"))