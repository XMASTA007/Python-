import cv2
#Get image location and name
filename = input('Image name?:\n')
img_location = f'D:\Coding_Projects\Python\Learning\Images\{filename}'
#img_location = open(f"./Images/{filename}")

#Read image
img = cv2.imread(img_location)#+filename

#Convert image to grayscale
#gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Invert the Image
Inverted_gray_image = 255 - gray_image

#Blur image by gaussion function
blurred_image = cv2.GaussianBlur(Inverted_gray_image, (21,21), 0)

#Invert blurred image
Inverted_blurred_image = 255 - blurred_image

#Create pencil sketch image
pencil_sketch_img = cv2.divide(gray_image, Inverted_blurred_image, scale=255.0)

#Show Image
cv2.imshow('Original Image', img)
cv2.imshow('New Image', pencil_sketch_img)
cv2.waitKey(0)




