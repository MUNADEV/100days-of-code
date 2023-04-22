import colorgram

colors = colorgram.extract('image.jpg', 30)

print("\nRGB Format")

rgb_colors = [f"{color.rgb[0]}, {color.rgb[1]}, {color.rgb[2]}" for color in colors]
print(", ".join(rgb_colors))

print("\nHexadecimal Format")

rgb_colors = ["#{:02x}{:02x}{:02x}".format(color.rgb[0], color.rgb[1], color.rgb[2]) for color in colors]
print(", ".join(rgb_colors))
