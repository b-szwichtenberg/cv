def area_ab(a1,a2,b1,b2):
    x=0
    y=1
    area1 = abs(a1[x] - a2[x]) * abs(a1[y] - a2[y])
    area2 = abs(b1[x] - b2[x]) * abs(b1[y] - b2[y])
    x_ab = abs(max(a1[x], b1[x]) - min(a2[x], b2[x]))
    y_ab = abs(max(a1[y], b1[y]) - min(a2[y], b2[y]))
    area_12 = x_ab * y_ab
    return (area1 + area2 - area_12),area_12




a1 = [1,-1] #minimalny punkt
a2 = [4,2] #maksymalny punkt
b1 = [3,-2]
b2 = [5,0]
print(area_ab(a1,a2,b1,b2))