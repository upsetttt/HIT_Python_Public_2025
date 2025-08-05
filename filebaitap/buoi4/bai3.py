n, m = map(int, input().split())
a = list(map(int, input().split()))
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
ans = 0;
a = tuple(a)
for x in s1:
    ans += a.count(x)
for x in s2:
    ans -= a.count(x)
print(ans)