import cv2

# Load two images
image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')

# Crop a region from each image
crop1 = image1[100:300, 200:400]
crop2 = image2[150:350, 250:450]

# Swap the cropped regions
image1[100:300, 200:400] = crop2
image2[150:350, 250:450] = crop1

# Save the modified images
cv2.imwrite('image1_swapped.jpg', image1)
cv2.imwrite('image2_swapped.jpg', image2)

# Display the modified images (optional)
cv2.imshow('Image 1 Swapped', image1)
cv2.imshow('Image 2 Swapped', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
