import sys
file_circle, file_points = sys.argv[1], sys.argv[2]

with open(file_circle, encoding="utf-8") as f:
    c_lines = f.readlines()

with open(file_points, encoding="utf-8") as f:
    p_lines = f.readlines()

x_center, y_center = map(float, c_lines[0].split(" "))
radius = float(c_lines[1])
r2 = radius ** 2
result = ""
for i in p_lines:
    x_point, y_point = map(float, i.split(" "))
    distance2 = (x_center - x_point) ** 2 + (y_center - y_point) ** 2
    if distance2 == r2:
        result += "0\n"
    elif distance2 < r2:
        result += "1\n"
    else:
        result += "2\n"

print(result)