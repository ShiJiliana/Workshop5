n, k, m = map(int, input().split())
if m > k:
    s1 = m - k - 1
    s2 = n - (m - k) - 1
    print(min(s1, s2))
else:
    s1 = k - m - 1
    s2 = n - (k - m) - 1
    print(min(s1, s2))