#importing library's

import cv2 
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure 
import tkinter as tk
from tkinter import filedialog


def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	s = measure.compare_ssim(imageA, imageB)
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = measure.compare_ssim(imageA, imageB)

	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
    

	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")

	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")

	# show the images
    
	plt.show()



def preprocess_image(image_path, display=True):
    raw_image = cv2.imread(image_path)
    bw_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
    bw_image = 255 - bw_image

    if display:
        #cv2.imshow("RGB to Gray", bw_image)
        cv2.waitKey()

    _, threshold_image = cv2.threshold(bw_image, 30, 255, 0)

    if display:
        #cv2.imshow("Threshold", threshold_image)
        cv2.waitKey()

    return threshold_image


def crop(image_path, image_name):
    preprocessed = preprocess_image(image_path)
    #cv2.imshow("preprocess_image", preprocessed)
    cv2.waitKey()
    x , y = 0, 0
    height, width = preprocessed.shape
    top, left, right, bottom = 0, 0, 0, 0
    sum_row=[sum(i) for i in preprocessed]
    for i in range(len(sum_row)):
        if(sum_row[i]!=0):
            top = i
            break
        
    for j in reversed(range(len(sum_row))):
        if(sum_row[j]!=0):
            bottom = j
            break

    sum_col=[sum(x) for x in zip(*preprocessed)]
    for k in range(len(sum_col)):
        if(sum_col[k]!=0):
            left = k
            break
    
    for l in reversed(range(len(sum_col))):
        if(sum_col[l]!=0):
            right = l
            break

    crop_img = preprocessed[y+top:y-(height - bottom), x+left:x-(width - right)]
    cv2.imwrite('images/compare_inputs/'+str(image_name)+'.png',crop_img)
    #cv2.imshow("cropped", crop_img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    return crop_img

#root = tk.Tk()
#root.withdraw()
#file_path1 = filedialog.askopenfilename()

img_path1 = "images/001001_000.png"
img_path2 = "images/001001_000.png"

#input_img1 = cv2.imread("images/001001_000.png")
#file_path2 = filedialog.askopenfilename()
#input_img2 = cv2.imread("images/001001_000.png")

originl_img = crop(img_path1,image_name= "compare1")
contrast_img = crop(img_path2,image_name= "compare2")



#originl_img = cv2.imread("images/compare_inputs/compare1.png")
#contrast_img = cv2.imread("images/compare_inputs/compare2.png")

dim = originl_img.shape

original = cv2.resize(originl_img.copy(), dim )
contrast = cv2.resize(contrast_img.copy(), dim)

fig = plt.figure("Images")
images = ("sample -1", original), ("sample -2", contrast)
# loop over the images
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 3, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")

# show the figure
plt.show()

# compare the images
#compare_images(original, original, "Original vs. Original")
compare_images(original, contrast, "Original vs. Contrast")
#compare_images(original, shopped, "Original vs. Photoshopped")

print("====================================================")
ssim = measure.compare_ssim(original, contrast)
m = mse(original, contrast)
print("Result: ")
print("MSE:: %.2f, Accu :: %.2f" % (m, ssim))





"""
preprocessed = preprocess_image("images/sai.png")
cv2.imshow("preprocess_image", preprocessed)
cv2.waitKey()
x , y = 0, 0
height, width = preprocessed.shape
top, left, right, bottom = 0, 0, 0, 0
sum_row=[sum(i) for i in preprocessed]
for i in range(len(sum_row)):
    if(sum_row[i]!=0):
        top = i
        break
        
for j in reversed(range(len(sum_row))):
    if(sum_row[j]!=0):
        bottom = j
        break

sum_col=[sum(x) for x in zip(*preprocessed)]
for k in range(len(sum_col)):
    if(sum_col[k]!=0):
        left = k
        break
    
for l in reversed(range(len(sum_col))):
    if(sum_col[l]!=0):
        right = l
        break

crop_img = preprocessed[y+top:y-(height - bottom), x+left:x-(width - right)]
cv2.imwrite("images/compare_inputs/ghouri.png",crop_img)
#cv2.imshow("cropped", crop_img)
#cv2.waitKey()
#cv2.destroyAllWindows()

"""