T = int(input())
for tc in range(1, T+1):
    N = int(input())
    value = []
    for i in range(N):
        A = input().split()
        for j in range(int(A[1])):
            value.append(A[0])
    print(value)
    
    Sten = ""
    ten = []
    for l, k in enumerate(value):
        Sten += k
        if len(Sten) == 10:
            ten.append(Sten)
            Sten = ""
        elif l == len(value)-1:
            ten.append(Sten)
    print(f'#{tc}',*ten, sep= "\n")       