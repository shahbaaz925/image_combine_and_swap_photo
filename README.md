

**README for Code 1 - Combine Two Images**

# Combine Two Images

This Python script combines two images into a single image. It uses the OpenCV library to load, concatenate, and save the images. This can be useful for creating image diptychs, side-by-side comparisons, or other image combinations.

## Prerequisites

Before running the script, make sure you have the OpenCV library installed. You can install it using pip:

```bash
pip install opencv-python
```

## Usage

1. Place the two images you want to combine in the same directory as this script.

2. Modify the script to specify the filenames of the two images you want to combine:

   ```python
   image1 = cv2.imread('image1.jpg')
   image2 = cv2.imread('image2.jpg')
   ```

3. Run the script. It will combine the two images horizontally and save the result as 'combined_image.jpg' in the same directory.

   ```bash
   python combine_images.py
   ```

4. Optionally, you can display the combined image by uncommenting the following lines in the script:

   ```python
   # Display the combined image (optional)
   cv2.imshow('Combined Image', combined_image)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   ```

## Example

Here's an example of how the script can be used:

- Input Image 1: ![Image 1](image1.jpg)
- Input Image 2: ![Image 2](image2.jpg)
- Combined Image: ![Combined Image](combined_image.jpg)

## License

This script is provided under the MIT License. See the [LICENSE](LICENSE) file for details.


**README for Code 2 - Crop and Swap Parts of Two Images**


# Crop and Swap Parts of Two Images

This Python script demonstrates how to crop specific regions from two images and swap those cropped regions. It uses the OpenCV library for image manipulation. This can be useful for creative image editing and compositing.

## Prerequisites

Before running the script, make sure you have the OpenCV library installed. You can install it using pip:

```bash
pip install opencv-python
```

## Usage

1. Place the two images you want to work with in the same directory as this script.

2. Modify the script to specify the filenames of the two images:

   ```python
   image1 = cv2.imread('image1.jpg')
   image2 = cv2.imread('image2.jpg')
   ```

3. Adjust the cropping coordinates in the script to select the regions you want to crop and swap:

   ```python
   crop1 = image1[100:300, 200:400]
   crop2 = image2[150:350, 250:450]
   ```

4. Run the script. It will crop the specified regions from each image, swap them, and save the modified images as 'image1_swapped.jpg' and 'image2_swapped.jpg' in the same directory.

   ```bash
   python crop_and_swap_images.py
   ```

5. Optionally, you can display the modified images by uncommenting the following lines in the script:

   ```python
   # Display the modified images (optional)
   cv2.imshow('Image 1 Swapped', image1)
   cv2.imshow('Image 2 Swapped', image2)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   ```

## Example

Here's an example of how the script can be used:

- Input Image 1: ![Image 1](image1.jpg)
- Input Image 2: ![Image 2](image2.jpg)
- Swapped Image 1: ![Swapped Image 1](image1_swapped.jpg)
- Swapped Image 2: ![Swapped Image 2](image2_swapped.jpg)

## License

This script is provided under the MIT License. See the [LICENSE](LICENSE) file for details.
```

