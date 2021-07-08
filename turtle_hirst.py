import colorgram

colors = colorgram.extract('hirst-1.jpg', 30)
rgb_colors = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    rgb = (r, g, b)
    rgb_colors.append(rgb)
print(rgb_colors)
