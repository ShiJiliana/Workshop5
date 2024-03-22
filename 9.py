a, b, c = map(int, input().split())
n1 = max(a, b, c)
n3 = min(a, b, c)
if n1 != a and n3 != a:
    n2 = a
elif n1 != b and n3 != b:
    n2 = b
else: n2 = c
print(n1, n2, n3)