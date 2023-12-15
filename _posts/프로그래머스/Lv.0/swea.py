# 1945
# T = int(input())
# for tc in range(1, T+1):
# N = int(input())
# numbers = [2, 3, 5, 7, 11]
# count = [0]*5
# d = 0
# while d < 5:
# if N % numbers[d] == 0:
# N = N // numbers[d]
# count[d] += 1
# else:
# d += 1
# print(f'#{tc}',*count)

# T = int(input())
# for tc in range(1, T+1):
# answer = 0
# now = 0
# for i in range(int(input())):
# speed = list(map(int,input().split()))
# if speed[0] == 1:
# now = now + speed[1]
# answer += now
# elif speed[0] == 2:
# now = now - speed[1]
# if now < 0:
# now = 0
# else:
# answer += now
# elif speed[0] == 0:
# answer += now
# print(f'#{tc}', answer)


# T = int(input())
# for tc in range(1, 1+T):
#     N = int(input())
#     count = 1
#     Nlist = [0 for _ in range(10)]
#     while len(Nlist) == 10:
#         for i in str(N*count):
#             Nlist[int(i)] = 1
#         if sum(Nlist) == 10:
#             print(f'#{tc} {count*N}')
#             break
#         else:
#             count += 1
