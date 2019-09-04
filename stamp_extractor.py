import cv2
import matplotlib.pyplot as plt
from skimage import measure, morphology
from skimage.color import label2rgb
from skimage.measure import regionprops

img = cv2.imread('./inputs/in2.jpg', 0)
img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]

blobs = img > img.mean()
blobs_labels = measure.label(blobs, background=1)
image_label_overlay = label2rgb(blobs_labels, image=img)

fig, ax = plt.subplots(figsize=(10, 6))


the_biggest_component = 0
total_area = 0
counter = 0
average = 0.0
for region in regionprops(blobs_labels):
    if (region.area > 10):
        total_area = total_area + region.area
        counter = counter + 1
   
    if (region.area >= 250):
        if (region.area > the_biggest_component):
            the_biggest_component = region.area

average = (total_area/counter)
print("the_biggest_component: " + str(the_biggest_component))
if (the_biggest_component<10500):
    print("Stamp Exists")
else:
    print("no Stamp")   
print("average: " + str(average))

a4_constant = ((average/84.0)*250.0)+100
print("a4_constant: " + str(a4_constant))

b = morphology.remove_small_objects(blobs_labels, a4_constant)

plt.imsave('pre_version.png', b)

img = cv2.imread('pre_version.png', 0)
img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

cv2.imwrite("./out/output.png", img)
