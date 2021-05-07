A, B, C, X, Y = map(int, input().split())

price = A * X + B * Y
min_price = 0
if X <= Y:
    min_price += min(B, C * 2) * (Y - X)
    min_price += C * 2 * X
else:
    min_price += min(A, C * 2) * (X - Y)
    min_price += C * 2 * Y

print(min(price, min_price))
