points = [(1,1), (2,2), (2.5,1)]
print(points[2][0])
y=0
x=0

    #point -> neue Variable für jeden Listeneintrag
for point in points:
    print(point[1])
    y = y+point[1]
    x = x+point[0]

print(x,y)

avg_x = x / len(points)
avg_y = y / len(points)

print(avg_x,avg_y)

w_enumerator = 0
w_denominator = 0

for point in points:
    w_enumerator += (point[0]-avg_x)*(point[1]-avg_y) # Du tuesch das setze. aso bi jedem loop durchlauf wird de alt wert ersetzt. Du wotsch glaub "w_enumerator +=" anstatt "w_enumerator =", (das addiert nach jedem durchlauf de neui wert zum alte wert vo w_enumerator dezue)

print(w_enumerator)

for point in points:
    w_denominator += (point[0]-avg_x)**2

print(w_denominator)

w1 = w_enumerator/w_denominator
print(w1)

w0 = 0


w0 = avg_y - w1 * avg_x

print(w0)