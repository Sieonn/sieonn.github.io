#1945
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = [2, 3, 5, 7, 11]
    count = [0]*5
    d = 0
    while d < 5:
        if N % numbers[d] == 0:
            N = N // numbers[d]
            count[d] += 1
        else:
            d += 1
    print(f'#{tc}',*count)