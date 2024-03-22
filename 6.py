a, b, c = map(int, input().split())
if a == b and a == c and c == b:
    print(3)
elif a == c and a != b or a == b and a != c or b == c and b != a:
    print(2)
else:
    print(0)