import cv2

# Load two images
image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')

# Ensure both images have the same dimensions
if image1.shape != image2.shape:
    raise ValueError("Both images must have the same dimensions")

# Combine the two images horizontally
combined_image = cv2.hconcat([image1, image2])

# Save the combined image
cv2.imwrite('combined_image.jpg', combined_image)

# Display the combined image (optional)
cv2.imshow('Combined Image', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
