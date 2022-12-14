import math
w, h, s = map(int,input().split())
print(math.ceil(w/s) * math.ceil(h/s))