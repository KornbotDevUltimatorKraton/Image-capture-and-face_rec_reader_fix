import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
im = cv2.imread("airport2.jpeg")
im2 = cv2.resize(im, (800,780))
x,y,z = cv.detect_common_objects(im2)
output_img = draw_bbox(im2, x,y,z)
print(y)

object_count = list(set(y))
print("Object in list",list(set(y)))
for x in object_count:
     print("Object",x,y.count(x))
cv2.imshow("Image",output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
