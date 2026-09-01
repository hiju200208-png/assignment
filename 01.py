image = [
    ["30,60,90", "120,150,180"],
    ["210,180,150", "60,60,60"]
]

all_brightness=[]
brightness_image = []

for row in image:
    row_result = []

    for pixel in row:
        rgb = [int(value) for value in pixel.split(',')]
        pixel_bright = sum(rgb)/3
        row_result.append(pixel_bright)
        all_brightness.append(pixel_bright)

    brightness_image.append(row_result)

threshold= sum(all_brightness) / len(all_brightness)

binary_image = []

for row in brightness_image:
    row_final = []

    for brightness in row:
        if brightness >= threshold:
            row_final.append(1)
        else:
            row_final.append(0)

    binary_image.append(row_final)


for row in binary_image:
    print(row)







