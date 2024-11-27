#Triangle Rotation without using built-in functions
import cv2
import numpy as np
#import matplotlib as plt
from matplotlib import pyplot

filename = 'spyderman.png'
image = cv2.imread(filename,cv2.IMREAD_UNCHANGED)
image_array = np.array(image)
print(len(image_array))
print(len(image_array[0]))

def get_rotation(angle):
    angle = np.radians (angle)
    return np.array([
[np.cos(angle), -np.sin(angle), 0],
[np.sin(angle), np.cos(angle), 0],
[0, 0, 1]
])
img_transformed = np.zeros((500,500,3), dtype=np.uint8)
R1= get_rotation(45)
#print(R1)
#print(image_array)
for i,row in enumerate(image_array):
    for j, col in enumerate(row):
        pixel_data = image_array[i, j,:]
        
        input_coords= np.array([i, j,1])
        #print(input_coords)
        i_out, j_out, _ = (R1 @ input_coords).astype(int)
        #print(i_out,j_out)
        img_transformed[i_out+80, j_out,:]= pixel_data
       

pyplot.figure(figsize=(10, 5))
pyplot.subplot(1, 2, 1)
pyplot.imshow(image_array)
pyplot.title("original Grayscale Image")
pyplot.axis("off")

pyplot.subplot(1,2,2)
pyplot.imshow(img_transformed)
pyplot.title("Rotated Image")
pyplot.axis("off")
pyplot.show()
 
cv2.waitKey(0)
cv2.destroyAllWindows()

