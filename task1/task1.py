import sys
n, m = int(sys.argv[1]), int(sys.argv[2])
string = ""
if m > n:
    m = n - m % n
point = 1
while 1:
    string += str(point)
    nextPoint = point + m - 1
    if nextPoint > n + 1:
        point = nextPoint % n
    elif nextPoint == n + 1:
        break
    else:
        point += m - 1
        if point == 1:
            break
print(string)