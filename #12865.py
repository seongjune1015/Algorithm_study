num, weight = map(int, input().split())
data = {}
for i in range(num) :
    w, v = map(int, input().split())
    if (w in data) and data[w] > v : continue
    else : data[w] = v
