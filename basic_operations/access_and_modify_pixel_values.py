import cv2

img = cv2.imread('../image/messi5.jpg')
# access and modify pixel values

px = img[100, 100]  # access
print(px)

blue = img[100, 100, 0]  # specify blue channel
print(blue)

img[100, 100] = [255, 255, 255]  # modify the pixel value
print(img[100, 100])
print('-' * 30)

# better way: using array.item() and array.itemset()

print(img.item(10, 10, 2))
img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))
