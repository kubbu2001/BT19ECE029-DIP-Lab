# import cv2, numpy, matplotlib
import cv2
import numpy as np
import matplotlib.pyplot as plt

	
# function to obtain histogram of an image
def hist_plot(img):
	
	# empty list to store the count
	# of each intensity value
	count =[]
	
	# empty list to store intensity
	# value
	r = []
	
	# loop to traverse each intensity
	# value
	for k in range(0, 256):
		r.append(k)
		count1 = 0
		
		# loops to traverse each pixel in
		# the image
		for i in range(m):
			for j in range(n):
				if img[i, j]== k:
					count1+= 1
		count.append(count1)
		
	return (r, count)


img = cv2.imread("C:\6th Semester\DIP\LAB DIP\Codes\Tanishk.png", 0)

# To ascertain total numbers of rows and
# columns of the image, size of the image
m, n = img.shape
r1, count1 = hist_plot(img)

# plotting the histogram
plt.stem(r1, count1)
plt.xlabel('intensity value')
plt.ylabel('number of pixels')
plt.title('Histogram of the original image')

# Transformation to obtain stretching
constant = (255-0)/(img.max()-img.min())
img_stretch = img * constant
r, count = hist_plot(img_stretch)

# plotting the histogram
plt.stem(r, count)
plt.xlabel('intensity value')
plt.ylabel('number of pixels')
plt.title('Histogram of the stretched image')

# Storing stretched Image
cv2.imwrite('/Users/mayurdongre/Downloads/Tanishk.jpeg', img_stretch)
