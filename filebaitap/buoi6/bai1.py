x, y = map(int, input().split())
ans = lambda x , y : x > y;
if(ans(x, y)):
    print(x)
else:
    print(y)