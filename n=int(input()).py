n=int(input())
for i in range(0,n):
    n=n+1
    i=0
    if n>1:
        print(n,i+1,i+122,i+22)
    else:
        print(n)
        if n>2:
            mid=0
            for mid in range(0,n):
                n=n+1//2
                mid=n//2
            mid=mid+n/2
            print(n,n//2)