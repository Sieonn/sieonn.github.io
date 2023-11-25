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

def solution(my_string):
    sol = ""
    for i in my_string:
        if i == i.upper():
            sol += i.lower()
        elif i == i.lower():
            sol += i.upper()
    return sol
print(solution("abCdEfghIJ"))