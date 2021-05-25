def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def solution(w,h):
    g = gcd(w, h)
    # return w * h - (g * ( (w//g) + (h//g) - 1 ))
    return w * h - (w + h - g)

if __name__ == "__main__":
    w, h = 8, 12
    print(solution(w, h))