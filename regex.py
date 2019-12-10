import pytesseract
import cv2
import re
from PIL import Image
finaltext=''
dpi=300
image=cv2.imread("a55.png")
b1_crop_img = image[820:1228,260:2207]
b1=cv2.resize(b1_crop_img,(500,400))
b2_crop_img=image[720:1200,2170:4000]
b3_crop_img=image[1426:4400,254:2154]
b4_crop_img=image[1433:2858,2161:4066]
b5_crop_img=image[3067:4391,2172:4005]
b6_crop_img=image[4664:5915,327:2184]
b7_crop_img=image[4630:5897,2191:4023]
b8_crop_img=image[5870:6400,352:3965]
cv2.imwrite('block-8.png',b8_crop_img)
cv2.destroyAllWindows()
blocks=["b1_crop_img"]
print(blocks[0])
for i in range(5,6):
    print('i :'+str(i))
    for j in range(1,9):
        print('j :'+str(j))
        filename='a55q_crop_DPI'
        config = ('-l eng+ara --oem 1 --psm 3')

  # Run tesseract OCR on image
        if j==1:
            text = pytesseract.image_to_string(b1_crop_img, config=config)
            result=re.compile(r"(Center Name)(.*)")
            final=result.search(text)
            print(final.group(1))
            print(final.group(2))
            result=re.compile(r"Center Number.*\d")
            final=result.search(text)
            print(final.group())
        elif j==2:
            text = pytesseract.image_to_string(b2_crop_img, config=config)        
        elif j==3:
            text = pytesseract.image_to_string(b3_crop_img, config=config)
        elif j==4:
            text = pytesseract.image_to_string(b4_crop_img, config=config)
            result=re.compile(r"(First Name).*\n(.*[a-zA-Z])")
            final=result.search(text)
            print(final.group(1))
            print(final.group(2))
            result=re.compile(r"(Second Name).*\n(.*)")
            final=result.search(text)
            print(final.group(1))
            print(final.group(2))
            result=re.compile(r"(Family Name).*\n(.*)")
            final=result.search(text)
            print(final.group(1))
            print(final.group(2))
        elif j==5:
            text = pytesseract.image_to_string(b5_crop_img, config=config)
            result=re.compile(r"(Date Of Birth.*[0-9])")
            final=result.search(text)
            print(final.group())
            result=re.compile(r"(Date Of Expiry)(.*[0-9])")
            final=result.search(text)
            print(final.group())
            result=re.compile(r"(Place Of Birth).[A-Z]*")
            final=result.search(text)
            print(final.group())
            result=re.compile(r"(Place Of Issue).*\n(.*)")
            final=result.search(text)
            print(final.group(1))
            print(final.group(2))

        elif j==6:
            text = pytesseract.image_to_string(b6_crop_img, config=config)
        elif j==7:
            text = pytesseract.image_to_string(b7_crop_img, config=config)
        elif j==8:
            text = pytesseract.image_to_string(b8_crop_img, config=config)

  # Print recognized text
        finaltext=finaltext+text